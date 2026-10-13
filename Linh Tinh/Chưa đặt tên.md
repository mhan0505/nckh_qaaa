
---

# PHẦN IV — MULTIVARIABLE CALCULUS



---

# PHẦN V — LINEAR REGRESSION

# EX9 — Xây dựng model

## 1. Nhắc lại kiến thức

Với một observation:

x=(x1,…,xd)x=(x_1,\ldots,x_d)

Linear Regression giả định:

f(x)=w0+w1x1+⋯+wdxd\boxed{ f(x)=w_0+w_1x_1+\cdots+w_dx_d }

Ta thêm:

x0=1x_0=1

thì:

f(x)=∑j=0dwjxj\boxed{ f(x)=\sum_{j=0}^{d}w_jx_j }

hay:

f(x)=wTx\boxed{ f(x)=w^Tx }

---

## 2. Đề bài

Giả sử có dữ liệu lịch sử giá nhà:

x(i)=(x1(i),...,xd(i))x^{(i)}=(x_1^{(i)},...,x_d^{(i)})

và giá thực tế:

y(i)y^{(i)}

Hãy xây dựng mô hình dự đoán giá.

---

## 3. Cách giải

Prediction:

y^(i)=w0+∑j=1dwjxj(i)\boxed{ \hat y^{(i)} = w_0+ \sum_{j=1}^dw_jx_j^{(i)} }

Hay:

y^(i)=wTx(i)\boxed{ \hat y^{(i)}=w^Tx^{(i)} }

---

# EX10 — Loss Function

## 1. Nhắc lại kiến thức

Prediction:

y^i=f(xi)\hat y_i=f(x_i)

Sai số:

y^i−yi\hat y_i-y_i

Linear Regression thường dùng squared error:

(y^i−yi)2(\hat y_i-y_i)^2

Loss trung bình:

J(w)=1n∑i=1n(y^i−yi)2\boxed{ J(w) = \frac1n \sum_{i=1}^n (\hat y_i-y_i)^2 }

Đây là **Mean Squared Error — MSE**.

---

## 2. Đề bài

Với:

y^i=w0+w1xi\hat y_i=w_0+w_1x_i

hãy viết loss function.

---

## 3. Cách giải

J(w0,w1)=1n∑i=1n(w0+w1xi−yi)2\boxed{ J(w_0,w_1) = \frac1n \sum_{i=1}^n (w_0+w_1x_i-y_i)^2 }

Mục tiêu:

min⁡w0,w1J(w0,w1)\boxed{ \min_{w_0,w_1}J(w_0,w_1) }

---

# EX11 — Gradient của Linear Regression

## 1. Nhắc lại

Gradient cho biết hướng tăng nhanh nhất của hàm.

Nếu:

J=J(w0,w1)J=J(w_0,w_1)

thì:

∇J=(∂J∂w0∂J∂w1)\nabla J = \begin{pmatrix} \frac{\partial J}{\partial w_0}\\ \frac{\partial J}{\partial w_1} \end{pmatrix}

---

## 2. Đề bài

Cho:

J(w0,w1)=1n∑i=1n(w0+w1xi−yi)2J(w_0,w_1) = \frac1n \sum_{i=1}^n (w_0+w_1x_i-y_i)^2

Tính:

∂J∂w0\frac{\partial J}{\partial w_0}

và

∂J∂w1\frac{\partial J}{\partial w_1}

---

## 3. Cách giải

Đặt:

y^i=w0+w1xi\hat y_i=w_0+w_1x_i

Khi đó:

∂J∂w0=2n∑i=1n(y^i−yi)\boxed{ \frac{\partial J}{\partial w_0} = \frac2n \sum_{i=1}^n (\hat y_i-y_i) }

và:

∂J∂w1=2n∑i=1nxi(y^i−yi)\boxed{ \frac{\partial J}{\partial w_1} = \frac2n \sum_{i=1}^n x_i(\hat y_i-y_i) }

---

# EX12 — Gradient Descent

## 1. Nhắc lại kiến thức

Ta muốn:

w∗=arg⁡min⁡wJ(w)w^*=\arg\min_wJ(w)

Gradient chỉ hướng **tăng nhanh nhất**.

Muốn đi xuống:

−∇J(w)-\nabla J(w)

Do đó:

w(t+1)=w(t)−η∇J(w(t))\boxed{ w^{(t+1)} = w^{(t)} - \eta\nabla J(w^{(t)}) }

Trong đó:

- ww: weights
    
- J(w)J(w): loss
    
- ∇J\nabla J: gradient
    
- η\eta: learning rate
    

---

## 2. Đề bài nên luyện

Cho:

J(w)=w2J(w)=w^2

và:

w0=4,η=0.1w_0=4,\qquad \eta=0.1

Thực hiện một bước Gradient Descent.

---

## 3. Cách giải

Gradient:

∇J(w)=2w\nabla J(w)=2w

Tại w=4w=4:

∇J(4)=8\nabla J(4)=8

Cập nhật:

wnew=4−0.1(8)w_{\text{new}} = 4-0.1(8) wnew=3.2\boxed{w_{\text{new}}=3.2}

---

# PHẦN VI — CLOSED-FORM LINEAR REGRESSION

Đây là phần **rất đáng chú ý** vì bạn vừa chụp ảnh thầy viết trực tiếp trên bảng.

# EX13 — Normal Equation

## 1. Nhắc lại kiến thức

Ta có:

X∈Rn×(d+1)X\in\mathbb R^{n\times(d+1)} w∈Rd+1w\in\mathbb R^{d+1} y∈Rny\in\mathbb R^n

Prediction:

y^=Xw\boxed{\hat y=Xw}

Mục tiêu:

min⁡w∥Xw−y∥2\boxed{ \min_w\|Xw-y\|^2 }

---

## 2. Đề bài

Cho:

X=(1x1(1)⋯xd(1)⋮⋮⋮1x1(n)⋯xd(n))X= \begin{pmatrix} 1&x_1^{(1)}&\cdots&x_d^{(1)}\\ \vdots&\vdots&&\vdots\\ 1&x_1^{(n)}&\cdots&x_d^{(n)} \end{pmatrix}

và:

y=(y1⋮yn)y= \begin{pmatrix} y_1\\ \vdots\\ y_n \end{pmatrix}

Tìm ww tối ưu.

---

## 3. Cách giải

Loss:

J(w)=∥Xw−y∥2J(w)=\|Xw-y\|^2

Lấy gradient:

∇J(w)=2XT(Xw−y)\nabla J(w) = 2X^T(Xw-y)

Tại optimum:

∇J(w)=0\nabla J(w)=0

nên:

XT(Xw−y)=0X^T(Xw-y)=0 XTXw=XTyX^TXw=X^Ty

Nếu XTXX^TX khả nghịch:

w∗=(XTX)−1XTy\boxed{ w^*=(X^TX)^{-1}X^Ty }

Đây là:

Normal Equation\boxed{\text{Normal Equation}}

hay:

Closed-form solution\boxed{\text{Closed-form solution}}

---

# EX14 — Ý nghĩa hình học của Linear Regression

Đây là phần thầy viết:

Xw−y⊥XXw-y\perp X

Cách hiểu:

Các vector XwXw tạo thành **column space của XX**.

Ta muốn tìm điểm:

XwXw

gần yy nhất.

Nói cách khác:

Xw=projection⁡Col(X)(y)\boxed{ Xw=\operatorname{projection}_{Col(X)}(y) }

Sai số:

Xw−yXw-y

phải vuông góc với column space.

Do đó:

XT(Xw−y)=0X^T(Xw-y)=0

và lại quay về:

XTXw=XTyX^TXw=X^Ty

### Đây là lý do hình học phía sau Normal Equation.

Không nhất thiết phải chứng minh sâu nếu đề thi chỉ yêu cầu tính, nhưng **phải hiểu logic này**.

---

# PHẦN VII — R2R^2

## 1. Nhắc lại kiến thức

Có hai loại variation:

### Tổng biến thiên của dữ liệu

SStot=∑i(yi−yˉ)2SS_{tot} = \sum_i(y_i-\bar y)^2

### Sai số còn lại của model

SSres=∑i(yi−y^i)2SS_{res} = \sum_i(y_i-\hat y_i)^2

Do đó:

R2=1−SSresSStot\boxed{ R^2 = 1-\frac{SS_{res}}{SS_{tot}} }

---

## 2. Đề bài

Cho:

y=(2,4,6)y=(2,4,6)

và:

y^=(2,5,5)\hat y=(2,5,5)

Tính R2R^2.

---

## 3. Cách giải

Mean:

yˉ=4\bar y=4

Total variation:

SStot=(2−4)2+(4−4)2+(6−4)2SS_{tot} = (2-4)^2+(4-4)^2+(6-4)^2 =4+0+4=8=4+0+4=8

Residual:

SSres=(2−2)2+(4−5)2+(6−5)2SS_{res} = (2-2)^2+(4-5)^2+(6-5)^2 =0+1+1=2=0+1+1=2

Do đó:

R2=1−28R^2 = 1-\frac28 R2=0.75\boxed{R^2=0.75}

---

# PHẦN VIII — NHỮNG BÀI MÌNH KHUYẾN NGHỊ BỔ SUNG

Dựa trên toàn bộ ghi chép của bạn, nếu muốn biến nó thành **một bộ đề ôn có khả năng bao phủ cao**, mình sẽ bổ sung các dạng sau.

## Probability

### P1 — Conditional probability cơ bản

P(A∣B)P(A|B)

### P2 — Bayes

Đúng dạng unfair coin.

### P3 — Total probability

P(B)=∑iP(B∣Ai)P(Ai)P(B)=\sum_iP(B|A_i)P(A_i)

### P4 — Independence

Cho:

P(A),P(B)P(A),P(B)

kiểm tra A,BA,B có độc lập không.

### P5 — Expectation

Tính:

E[X]E[X]

từ bảng phân phối.

### P6 — Variance

Var(X)=E[X2]−E[X]2Var(X)=E[X^2]-E[X]^2

### P7 — Linearity of expectation

E[∑Xi]E[\sum X_i]

### P8 — Variance of independent sum

Var(∑Xi)Var(\sum X_i)

### P9 — Counting

Dice / cards / combinations.

### P10 — Sum of random variables

Đặc biệt:

∑Bernoulli(p)→Binomial(n,p)\sum Bernoulli(p) \rightarrow Binomial(n,p)

---

# Calculus

### C1 — Partial derivative

### C2 — Gradient

∇f\nabla f

### C3 — Jacobian

JFJ_F

### C4 — Directional derivative

Ví dụ:

Dvf(x)=∇f(x)TvD_vf(x)=\nabla f(x)^Tv

Đây là một dạng mình **khuyên bổ sung**, vì nó nối rất tự nhiên gradient với ý nghĩa "hướng thay đổi".

---

# Linear Regression

### LR1 — Viết model

f(x)=wTxf(x)=w^Tx

### LR2 — Prediction

y^=Xw\hat y=Xw

### LR3 — MSE

J(w)=1n∥Xw−y∥2J(w)=\frac1n\|Xw-y\|^2

### LR4 — Derivative

∇J(w)\nabla J(w)

### LR5 — Gradient descent

wt+1=wt−η∇J(wt)w_{t+1}=w_t-\eta\nabla J(w_t)

### LR6 — Normal equation

w∗=(XTX)−1XTyw^*=(X^TX)^{-1}X^Ty

### LR7 — Geometry

Xw−y⊥Col(X)Xw-y\perp Col(X)

### LR8 — R2R^2

R2=1−SSresSStotR^2=1-\frac{SS_{res}}{SS_{tot}}

---

# Cuối cùng: thứ tự bạn nên học để ôn

**Đừng học theo thứ tự ảnh chụp.** Hãy học theo dependency:

```text
                    ┌───────────────┐
                    │ Random Variable│
                    └───────┬───────┘
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
             E[X], Var[X]       Conditional Probability
                                       │
                              ┌────────┴────────┐
                              ▼                 ▼
                            Bayes         Total Probability
                              │
                              ▼
                         Independence
                              │
                              ▼
                       Sum of X_i
                              │
                              ▼
                    ───────────────────
                         CALCULUS
                    ───────────────────
                              │
                     Partial derivative
                              │
                       ┌──────┴──────┐
                       ▼             ▼
                    Gradient      Jacobian
                       │
                       ▼
                 Linear Regression
                       │
            ┌──────────┼───────────┐
            ▼          ▼           ▼
         Model       Loss       Prediction
            │          │
            └────┬─────┘
                 ▼
              Gradient
                 │
                 ▼
         Gradient Descent
                 │
                 │
        ┌────────┴────────┐
        ▼                 ▼
  Closed Form          Iterative
 Normal Equation    Gradient Descent
        │
        ▼
       R²
```

**Điểm quan trọng nhất:** bộ ghi chép của bạn hiện đã đủ để thấy thầy không chỉ kiểm tra "nhớ công thức". Các câu được chọn để kiểm tra 4 năng lực:

1. **Nhận dạng loại bài** — Uniform? Bernoulli? Bayes? Jacobian?
    
2. **Thiết lập đúng mathematical object** — P(A∣B)P(A|B), JFJ_F, XwXw, J(w)J(w).
    
3. **Biến đổi toán học** — từ loss → gradient → normal equation.
    
4. **Hiểu ý nghĩa** — projection, gradient direction, conditional probability.
    

Nếu ôn để thi, mình sẽ ưu tiên **làm được từng dạng trên giấy mà không nhìn công thức**, rồi mới học thêm phần lý thuyết. Đây là cách kiểm tra xem bạn thực sự "biết" hay chỉ nhận ra công thức khi nhìn thấy nó.