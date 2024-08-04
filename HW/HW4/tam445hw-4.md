
$$
\begin{bmatrix}
-5 & 2 & 4 \\
2 & -8 & 2 \\
4 & 2 & -5
\end{bmatrix}
$$

$$
\alpha I+\beta m \otimes m = \alpha \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix} + \beta \begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix}
$$



$$
\beta m \otimes  m=\beta \begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix}
$$

$$
(\alpha+\beta -\lambda)((\alpha+\beta-\lambda)^2-\beta^2)-\beta(\beta(\alpha+\beta-\lambda)-\beta^2)+\beta(\beta^2-\beta(\alpha+\beta-\lambda))
$$

$$
(a+b-c)((a+b-c)^2-b^2)-b\cdot(b\cdot(a+b-c)-b^2)+b\cdot(b^2-b\cdot(a+b-c))
$$


$$
-c^3+9c^2-20c+12=0
$$

$$
\begin{bmatrix}
3 & \sqrt{ 3 } & 0 \\
\sqrt{ 3 } & 5 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

$$
\begin{bmatrix}
2 & \sqrt{ 3 } & 0 \\
\sqrt{ 3 } & 4 & 0 \\
0 & 0 & 0
\end{bmatrix}
$$

$$
\begin{bmatrix}
1 & \sqrt{ 3 } & 0 \\
\sqrt{ 3 } & 3 & 0 \\
0 & 0 & -1
\end{bmatrix}
$$

$$
\begin{bmatrix}
0 \\
0 \\
1
\end{bmatrix}\otimes \begin{bmatrix}
0 \\
0 \\
1
\end{bmatrix}
$$

$$
\begin{bmatrix}
-\sqrt{ 3 } \\
1 \\
0
\end{bmatrix}\otimes \begin{bmatrix}
-\sqrt{ 3 } \\
1 \\
0
\end{bmatrix}
$$

$$
\begin{bmatrix}
0 & 0 & 1
\end{bmatrix}
$$

$$
\begin{bmatrix}
0 & 0 & 1
\end{bmatrix}
$$

$$
\begin{bmatrix}
-\sqrt{ 3 } & 1 & 0
\end{bmatrix}
$$
$$
\begin{bmatrix}
\frac{\sqrt{ 3 }}{3} & 1 & 0
\end{bmatrix}
$$

$$
\begin{bmatrix}
\frac{\sqrt{ 6 }}{4}+\frac{3\sqrt{ 2 }}{4} & -\frac{\sqrt{ 6 }}{4}+\frac{3\sqrt{ 2 }}{4} & 0 \\
-\frac{\sqrt{ 6 }}{4}+\frac{3\sqrt{ 2 }}{4} & \frac{\sqrt{ 2 }}{4}+\frac{3\sqrt{ 6 }}{4} & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

$$
\begin{bmatrix}
\sqrt{ 3 } & 1 & 0 \\
0 & 2 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

$$
\mathbf{A} = \alpha \mathbf{I}+\beta \mathbf{m}\otimes \mathbf{m}
$$

$$
\mathbf{B}=\mathbf{m}\otimes \mathbf{n}+\mathbf{n}\otimes \mathbf{m}
$$

$$
\mathbf{T}=\mathbf{R}\mathbf{U}=\mathbf{V}\mathbf{R}
$$
where $\mathbf{U},\mathbf{V} \in \text{Psym}$ and $\mathbf{R}\in \text{Orth}$, or a tensor $\mathbf{T}$ whose components are given by

$$
\begin{bmatrix}
\sqrt{ 3 } & 1 & 0 \\
0 & 2 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

Write down the eigenvectors and eigenvalues of $\mathbf{U}$ and $\mathbf{V}$, and describe in words the geometric interpretation of the above decompositions.

1. Due to the following result from the definition of eigenvectors and eigenvalues:
$$
Ax=\lambda x
$$
$A$ can act upon an arbitrary vector, namely $m$ as shown below:

$$
\begin{align*}
Am&=(\alpha I+\beta m\otimes m)m\\[10pt]
&=\alpha Im+\beta(m\otimes m)m\\[10pt]
&=\alpha m+\beta(m\cdot m)m\\[10pt]
&=\alpha m+\beta m\\[10pt]
&=(\alpha+\beta)m\\[10pt]
Am&=(\alpha+\beta)m
\end{align*}
$$

We know that there must be three eigenvalues because the dimension of the tensor $A$ is $3$. We can use the property than eigenvectors are mutually orthogonal to each other to determine the other eigenvectors of $A$. A prospective vector is $n$, which is orthogonal to $m$:

$$
\begin{align*}
An&=(\alpha I+\beta m\otimes m)n\\[10pt]
&=(\alpha In+\beta(m\otimes m)n)\\[10pt]
&=(\alpha n+\beta(m\cdot n)m)\\[10pt]
&=\alpha n\\[10pt]
An&=\alpha n
\end{align*}
$$

If $m$ and $n$ are both orthogonal to each other, then a vector $l=m\times n$ is also mutually orthogonal to $m$ and $n$, and lives in the space of the third eigenvector of $A$.:

$$
\begin{align*}
Al&=(\alpha I+\beta m\otimes m)\\[10pt]
&=\alpha l+\beta(m\otimes m)l\\[10pt]
&=\alpha l+\underbrace{ \cancel{ \beta(m\cdot l)mC } }_{ 0 }\\[10pt]
Al&=\alpha l
\end{align*}
$$



The spectral decomposition of a tensor $\in \text{Psym}$ is defined as the following:

$$
S=\sum_{i=1}^3 \lambda_{i}\underline{u}_{i}\otimes \underline{u}_{i}
$$

Therefore, the tensor $A$ can be written in terms of the eigenvalues and eigenvectors as:

$$
\lambda_{1}=\alpha+\beta,\ \lambda_{2}=\alpha,\ \lambda_{3}=\alpha
$$
$$
v_{1}=m,\ v_{2}=n, \ v_{3}=m\times n
$$

$$
\begin{align*}
A&=(\alpha+\beta)m\otimes m+\alpha n\otimes n+\alpha(m\times n)\otimes (m\times n)\\[10pt]
&=\alpha m\otimes m+\beta m\otimes m+\alpha n\otimes n+\alpha(m\times n)\otimes (m\times n)\\[10pt]
A&=\alpha(m\otimes m+n\otimes n+(m\times n)\otimes (m\times n))+\beta(m\otimes m)
\end{align*}
$$
$$
B=m\otimes n+n\otimes m
$$

Applying the operation of tensor $B$ upon the given unit vector $m$:
$$
\begin{align*}
Bm &=(m\otimes n+n\otimes m)m)\\[10pt]
&=(m\otimes n)m+(n\otimes m)m\\[10pt]
&=\underbrace{ \cancel{ (n\cdot m)m }C }_{ 0 }+\underbrace{ (m\cdot m) }_{ 1 }n\\[10pt]
Bm&=n
\end{align*}
$$
Applying the operation of tensor $B$ upon the given unit vector $n$:
$$
\begin{align*}
Bn&=(m\otimes n+n\otimes m)n)\\[10pt]
&=(m\otimes n)n+(n\otimes m)n\\[10pt]
&=(n\cdot n)m+(m\cdot n)n\\[10pt]
Bn&=m
\end{align*}
$$Applying the operation of tensor $B$ upon the unit vector $m\times n$:

$$
\begin{align*}
B(m\times n)&=(m\otimes n+n\otimes m)(m\times n)\\[10pt]
&=(m\otimes n)(m\times n)+(n\otimes m)(m\times n)\\[10pt]
&=(n\cdot(m\times n))m+(m\cdot(m\times n))n=0
\end{align*}
$$

The following lists the eigenvalues and eigenvectors of the tensor $B$:

$$
\lambda_{1}=1,\ \lambda_{2}=1,\ \lambda_{3}=0
$$

$$
v_{1}=n, \ v_{2}=m,\ v_{3}=0
$$

$$
\begin{align*}
B&=\sum_{i=1}^3 \lambda_{i}\underline{u}_{i}\otimes u_{i}\\[10pt]
&=n\otimes n+m\otimes m\\[10pt]
\end{align*}
$$

$T^TT$ is found by multiplying the tensor $T$ by its transpose:

$$
\begin{align*}
T^TT&=\begin{bmatrix}
\sqrt{ 3 } & 0 & 0 \\
1 & 2 & 0 \\
0 & 0 & 1
\end{bmatrix}\begin{bmatrix}
\sqrt{ 3 } & 1 & 0 \\
0 & 2 & 0 \\
0 & 0 & 1
\end{bmatrix}\\[10pt]
&=\begin{bmatrix}
3 & \sqrt{ 3 } & 0 \\
\sqrt{ 3 } & 5 & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{align*}
$$

To determine the eigenvalues and the eigenvalues pairs of symmetric tensor $T^TT$, the $\lambda$ values of $\text{det}(T-\lambda I)=0$ are found.

$$
\begin{align*}
\text{det}(T-\lambda I)&=0\\[10pt]
&=\text{det}\begin{bmatrix}
3-\lambda & \sqrt{ 3 } & 0 \\
\sqrt{ 3 } & 5-\lambda & 0 \\
0 & 0 & 1-\lambda
\end{bmatrix}\\[10pt]
&=(3-\lambda)(5-\lambda)(1-\lambda)-\sqrt{ 3 }(\sqrt{ 3 }(1-\lambda))\\[10pt]
&=-\lambda^3+9\lambda^2-20\lambda+12=0
\end{align*}
$$

Solving the polynomial equation, the following eigenvalues are determined:

$$
\lambda_{1}=1,\ \lambda_{2}=2,\ \lambda_{3}=6
$$

The procedure that follows involves determining the eigenvectors for each eigenvalue. 

Substituting $\lambda_{1}$ into $T-\lambda I$:

$$
\begin{align*}
\begin{bmatrix}
2 & \sqrt{ 3 } & 0 \\
\sqrt{ 3 } & 4 & 0 \\
0 & 0 & 0
\end{bmatrix}\begin{bmatrix}
v_{1,1} \\
v_{2,1} \\
v_{3,1}
\end{bmatrix}&=\begin{bmatrix}
0 \\
0 \\
0
\end{bmatrix}
\end{align*}
$$

The nullspace of $T-\lambda_{1}I$ is the space of which the eigenvector that corresponds to eigenvalue $\lambda_{1}$ lives in:

$$
\begin{align*}
2v_{1,1}+\sqrt{ 3 }v_{1,2}&=0\\[10pt]
\sqrt{ 3 }v_{1,1}+4v_{1,2}&=0
\end{align*}
$$

Setting our free variable equal to $v_{3}$, we get the following solution for eigenvalue $\lambda_{1}=1$:

$$
v_{1}=v_{1,3}\begin{bmatrix}
0 \\
0 \\
1
\end{bmatrix}
$$

This procedure is repeated for the remaining two eigenvalues, $\lambda_2$, and $\lambda_{3}$.

For $\lambda_{2}=2$:

$$
\begin{bmatrix}
1 & \sqrt{ 3 } & 0 \\
\sqrt{ 3 } & 3 & 0 \\
0 & 0 & -1
\end{bmatrix}\begin{bmatrix}
v_{2,1} \\
v_{2,2} \\
v_{2,3}
\end{bmatrix}=\begin{bmatrix}
0 \\
0 \\
0
\end{bmatrix}
$$

Computing the nullspace of the system above and setting the free variable equal to $v_{2,2}$:

$$
\begin{align*}
v_{2,1}+\sqrt{ 3 }v_{2,2}&=0\\[10pt]
\sqrt{ 3 }v_{2,1}+3v_{2,2}&=0\\[10pt]
-v_{2,3}&=0\\[10pt]
\bar{v}_{2}&=\begin{bmatrix}
-\sqrt{ 3}v_{2,2} \\
v_{2,2} \\
0
\end{bmatrix}\\[10pt]
&=
v_{2,2}\begin{bmatrix}
-\sqrt{ 3 } \\
1 \\
0
\end{bmatrix}
\end{align*}
$$


Substituting $\lambda_{3}$ into $\text{det}(T-\lambda I)$:

$$
\begin{align*}
\begin{bmatrix}
-3 & \sqrt{ 3 } & 0 \\
\sqrt{ 3 } & -1 & 0 \\
0 & 0 & -5
\end{bmatrix}\begin{bmatrix}
v_{3,1} \\
v_{3,2} \\
v_{3,3}
\end{bmatrix}&=
\begin{bmatrix}
0 \\
0 \\
0
\end{bmatrix}
\end{align*}
$$

Computing the nullspace of the above system and setting the free variable equal to $v_{3,2}$:

$$
\begin{align*}
-3v_{3,1}+\sqrt{ 3 }v_{3,2}&=0\\[10pt]
\sqrt{ 3 }v_{3,1}-v_{3,2}&=0\\[10pt]
-5v_{3,3}&=0
\end{align*}
$$
Solving for the nullspace:
$$
\begin{align*}
\bar{v}_{3}&=\begin{bmatrix}
\frac{\sqrt{ 3 }}{3} \\
1 \\
0
\end{bmatrix}
\end{align*}
$$

The eigenvalue and eigenvector pairs are shown below:

$$
\left( [1,\begin{bmatrix}
0 \\
0 \\
1
\end{bmatrix}], [2,\begin{bmatrix}
-\sqrt{ 3 } \\
1 \\
0
\end{bmatrix}],
\left[ 6,\begin{bmatrix}
\frac{\sqrt{ 3 }}{3} \\
0 \\
1
\end{bmatrix} \right] \right)
$$

Our next goal is to determine the polar decomposition $T=RU=VR$, where $U,V\in \text{Psym}$ and $R\in \text{Orth}$. 

$U$ is determined by the definition of the square root theorem, where $\underline{u}_{i}$ are normalized eigenvectors and $\lambda_{i}$ are the eigenvalues that were found in earlier steps:

$$
\begin{align*}
U&=\sum_{i=1}^3 \sqrt{ \lambda_{i} }\underline{u}_{i}\otimes u_{i}\\[10pt]
&=\sqrt{ 1 }\begin{bmatrix}
0 \\
0 \\
1 \\
\end{bmatrix}\otimes 
\begin{bmatrix}
0 \\
0 \\
1
\end{bmatrix}+\sqrt{ 2 }\begin{bmatrix}
-\sqrt{ 3 } \\
1 \\
0
\end{bmatrix}\otimes \begin{bmatrix}
-\sqrt{ 3 } \\
1 \\
0
\end{bmatrix}+\sqrt{ 6 }\begin{bmatrix}
\frac{\sqrt{ 3 }}{3} \\
1 \\
0
\end{bmatrix}\otimes 
\begin{bmatrix}
\frac{\sqrt{ 3 }}{3} \\
1 \\
0
\end{bmatrix}\\[10pt]
&=\begin{bmatrix}
0 & 0 & 0 \\
0 & 0 & 0  \\
0 & 0 & 1
\end{bmatrix}+\sqrt{ 2 }\begin{bmatrix}
3 & -\sqrt{ 3 } & 0 \\
-\sqrt{ 3 } & 1 & 0 \\
0 & 0 & 0
\end{bmatrix}+\sqrt{ 6 }\begin{bmatrix}
\frac{1}{3} & \frac{\sqrt{ 3 }}{3} & 0 \\
\frac{\sqrt{ 3 }}{3} & 1 & 0 \\
0 & 0 & 0
\end{bmatrix}\\[10pt]
U&=\begin{bmatrix}
\frac{\sqrt{ 6 }}{4}+\frac{3\sqrt{ 2 }}{4} & -\frac{\sqrt{ 6 }}{4}+\frac{3\sqrt{ 2 }}{4} & 0 \\
-\frac{\sqrt{ 6 }}{4}+\frac{3\sqrt{ 2 }}{4} & \frac{\sqrt{ 2 }}{4}+\frac{3\sqrt{ 6 }}{4} & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{align*}
$$

Finding $R$ is straightforward using:

$$
R=TU^{-1}
$$

The inverse of $U$ can be found using the following:

$$
\begin{align*}
U^{-1}&=\frac{1}{\text{det}(U)}\text{adj}(U)\\[10pt]
&=\begin{bmatrix}
\frac{\sqrt{ 6 }}{24}+\frac{3\sqrt{ 2 }}{8} & -\frac{\sqrt{ 6 }}{8}+\frac{\sqrt{ 2 }}{8} & 0 \\
-\frac{\sqrt{ 6 }}{8}+\frac{\sqrt{ 2 }}{8} & \frac{\sqrt{ 2 }}{8}+\frac{\sqrt{ 6 }}{8} & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{align*}
$$

Computing $R$:

$$
\begin{align*}
R&=TU^{-1}\\[10pt]
&= \begin{bmatrix}
\sqrt{ 3 } & 1 & 0 \\
0 & 2 & 0 \\
0 & 0 & 1
\end{bmatrix}\begin{bmatrix}
\frac{\sqrt{ 6 }}{24}+\frac{3\sqrt{ 2 }}{8} & -\frac{\sqrt{ 6 }}{8}+\frac{\sqrt{ 2 }}{8} & 0 \\
-\frac{\sqrt{ 6 }}{8}+\frac{\sqrt{ 2 }}{8} & \frac{\sqrt{ 2 }}{8}+\frac{\sqrt{ 6 }}{8} & 0 \\
0 & 0 & 1
\end{bmatrix}\\[10pt]
R&=\begin{bmatrix}
\frac{\sqrt{ 2 }}{4}+\frac{\sqrt{ 6 }}{4} & -\frac{\sqrt{ 2 }}{4}+\frac{\sqrt{ 6 }}{4} & 0 \\
-\frac{\sqrt{ 6 }}{4}+\frac{\sqrt{ 2 }}{4} & \frac{\sqrt{ 2 }}{4}+\frac{\sqrt{ 6 }}{4} & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{align*}
$$

Using the definition $V=RUR^T$:

$$
\begin{align*}
V&=RUR^T\\[10pt]
&=\begin{bmatrix}
\frac{\sqrt{ 2 }}{4}+\frac{\sqrt{ 6 }}{4} & -\frac{\sqrt{ 2 }}{4}+\frac{\sqrt{ 6 }}{4} & 0 \\
-\frac{\sqrt{ 6 }}{4}+\frac{\sqrt{ 2 }}{4} & \frac{\sqrt{ 2 }}{4}+\frac{\sqrt{ 6 }}{4} & 0 \\
0 & 0 & 1
\end{bmatrix}\begin{bmatrix}
\frac{\sqrt{ 6 }}{4}+\frac{3\sqrt{ 2 }}{4} & -\frac{\sqrt{ 6 }}{4}+\frac{3\sqrt{ 2 }}{4} & 0 \\
-\frac{\sqrt{ 6 }}{4}+\frac{3\sqrt{ 2 }}{4} & \frac{\sqrt{ 2 }}{4}+\frac{3\sqrt{ 6 }}{4} & 0 \\
0 & 0 & 1
\end{bmatrix}\begin{bmatrix}
\frac{\sqrt{ 2 }}{4}+\frac{\sqrt{ 6 }}{4} & -\frac{\sqrt{ 6 }}{4}+\frac{\sqrt{ 2 }}{4} & 0 \\
-\frac{\sqrt{ 2 }}{4}+\frac{\sqrt{ 6 }}{4} & \frac{\sqrt{ 2 }}{4}+\frac{\sqrt{ 6 }}{4} & 0 \\
0 & 0 & 1
\end{bmatrix}\\[10pt]
V&=\begin{bmatrix}
\frac{\sqrt{ 2 }}{2}+\frac{\sqrt{ 6 }}{2} & -\frac{\sqrt{ 2 }}{2}+\frac{\sqrt{ 6 }}{2} & 0 \\
-\frac{\sqrt{ 2 }}{2}+\frac{\sqrt{ 6 }}{2} & \frac{\sqrt{ 2 }}{2}+\frac{\sqrt{ 6 }}{2} & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{align*}
$$

The tensor $T$ can be decomposed into the the polar decomposition $T=RU$ and $T=VR$ as the following:

Right Polar Decomposition:

$$
\begin{align*}
T&=RU\\[10pt]
&=\begin{bmatrix}
\frac{\sqrt{ 2 }}{4}+\frac{\sqrt{ 6 }}{4} & -\frac{\sqrt{ 2 }}{4}+\frac{\sqrt{ 6 }}{4} & 0 \\
-\frac{\sqrt{ 6 }}{4}+\frac{\sqrt{ 2 }}{4} & \frac{\sqrt{ 2 }}{4}+\frac{\sqrt{ 6 }}{4} & 0 \\
0 & 0 & 1
\end{bmatrix}\begin{bmatrix}
\frac{\sqrt{ 6 }}{4}+\frac{3\sqrt{ 2 }}{4} & -\frac{\sqrt{ 6 }}{4}+\frac{3\sqrt{ 2 }}{4} & 0 \\
-\frac{\sqrt{ 6 }}{4}+\frac{3\sqrt{ 2 }}{4} & \frac{\sqrt{ 2 }}{4}+\frac{3\sqrt{ 6 }}{4} & 0 \\
0 & 0 & 1
\end{bmatrix}\\[10pt]
&=\begin{bmatrix}
\sqrt{ 3 } & 1 & 0 \\
0 & 2 & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{align*}
$$

Left Polar Decomposition:


$$
\begin{align*}
T&=VR\\[10pt]
&=\begin{bmatrix}
\frac{\sqrt{ 2 }}{2}+\frac{\sqrt{ 6 }}{2} & -\frac{\sqrt{ 2 }}{2}+\frac{\sqrt{ 6 }}{2} & 0 \\
-\frac{\sqrt{ 2 }}{2}+\frac{\sqrt{ 6 }}{2} & \frac{\sqrt{ 2 }}{2}+\frac{\sqrt{ 6 }}{2} & 0 \\
0 & 0 & 1
\end{bmatrix}\begin{bmatrix}
\frac{\sqrt{ 2 }}{4}+\frac{\sqrt{ 6 }}{4} & -\frac{\sqrt{ 2 }}{4}+\frac{\sqrt{ 6 }}{4} & 0 \\
-\frac{\sqrt{ 6 }}{4}+\frac{\sqrt{ 2 }}{4} & \frac{\sqrt{ 2 }}{4}+\frac{\sqrt{ 6 }}{4} & 0 \\
0 & 0 & 1
\end{bmatrix}\\[10pt]
&=
\begin{bmatrix}
\sqrt{ 3 } & 1 & 0 \\
0 & 2 & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{align*}
$$


The geometric interpretation of the polar decomposition of tensor $T$ consists of a rotation and a dilation, where $R$ is a rotation matrix, taking a unit square and operating upon the square as a rigid body rotation without deformation. The tensors $U$ and $V$ perform stretch operations upon a unit square. 