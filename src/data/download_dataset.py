"""
Script tải siêu tốc toàn bộ Dataset chuỗi lạnh xoài từ Recherche Data Gouv:
DOI: 10.57745/F9UJGQ
Hỗ trợ Multi-threading (ThreadPoolExecutor) để tải 562 files chỉ trong vài chục giây.
"""

import os
import sys
import json
import urllib.request
import ssl
from concurrent.futures import ThreadPoolExecutor, as_completed

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ssl_context = ssl._create_unverified_context()

DATASET_DOI = "doi:10.57745/F9UJGQ"
BASE_URL = "https://entrepot.recherche.data.gouv.fr"
TARGET_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "raw"))

os.makedirs(TARGET_DIR, exist_ok=True)


def download_single_file(f_item):
    df_info = f_item["dataFile"]
    f_id = df_info["id"]
    f_name = df_info["filename"]
    expected_size = df_info["filesize"]
    dir_label = f_item.get("directoryLabel", "")

    dest_folder = os.path.join(TARGET_DIR, dir_label)
    os.makedirs(dest_folder, exist_ok=True)
    dest_path = os.path.join(dest_folder, f_name)

    # Đã tải đủ dung lượng thì bỏ qua
    if os.path.exists(dest_path) and os.path.getsize(dest_path) == expected_size:
        return True, f_name, 0

    file_url = f"{BASE_URL}/api/access/datafile/{f_id}"
    req = urllib.request.Request(file_url, headers={"User-Agent": "Mozilla/5.0"})

    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30, context=ssl_context) as f_resp:
                content = f_resp.read()
                with open(dest_path, "wb") as out_f:
                    out_f.write(content)
            return True, f_name, len(content)
        except Exception as e:
            if attempt == 2:
                return False, f_name, str(e)
    return False, f_name, "Max retries exceeded"


def main():
    print(f"--> Đang kết nối tới Recherche Data Gouv để lấy danh mục 562 files...")
    meta_url = f"{BASE_URL}/api/datasets/:persistentId/?persistentId={DATASET_DOI}"
    req = urllib.request.Request(meta_url, headers={"User-Agent": "Mozilla/5.0"})

    with urllib.request.urlopen(req, context=ssl_context) as resp:
        data = json.loads(resp.read().decode())
        files = data["data"]["latestVersion"]["files"]

    total_files = len(files)
    print(f"--> Đã lấy xong metadata! Bắt đầu tải đa luồng ({total_files} files) với 20 workers...")

    completed = 0
    errors = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        future_to_file = {executor.submit(download_single_file, f): f["dataFile"]["filename"] for f in files}

        for future in as_completed(future_to_file):
            success, filename, res = future.result()
            completed += 1
            if success:
                sys.stdout.write(f"\r    Tiến độ: [{completed}/{total_files}] ({completed/total_files*100:.1f}%) | Vừa xong: {filename[:30]}")
                sys.stdout.flush()
            else:
                errors.append((filename, res))

    print(f"\n\n TẢI HOÀN TẤT: {completed - len(errors)}/{total_files} files thành công!")
    if errors:
        print(f" Có {len(errors)} file gặp lỗi: {errors[:5]}")
    else:
        print(f" Toàn bộ dữ liệu đã được lưu trữ hoàn chỉnh tại: {TARGET_DIR}")


if __name__ == "__main__":
    main()
