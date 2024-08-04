
1.

$\mathbf{S}(\mathbf{u\otimes v})=(\mathbf{Su})\otimes \mathbf{v}$

According to the definition of the tensor product, the left hand side can be multiplied by the following:
$$
\begin{align*}
\mathbf{S}(\mathbf{u}\otimes \mathbf{v}) \mathbf{w}&=\mathbf{S(\mathbf{v}\cdot \mathbf{w})\mathbf{u}}\\[10pt]
&=(\mathbf{v}\cdot \mathbf{w})\mathbf{S}\mathbf{u}\tag{1}
\end{align*}
$$
Multiplying by $\mathbf{w}$ on the right hand side:

$$
\begin{align*}
(\mathbf{S}\mathbf{u}\otimes \mathbf{v})\mathbf{w}&=(\mathbf{v}\cdot \mathbf{w})(\mathbf{S}\mathbf{u})\tag{2}
\end{align*}
$$

Equation 1 and Equation 2 are equal after being both multiplied by $\mathbf{w}$. Q.E.D.


$(\mathbf{u}\otimes \mathbf{v})\mathbf{S}=\mathbf{u}\otimes(\mathbf{S^T}\mathbf{v})$

Taking the transpose of both sides then multiplying by $\mathbf{w}$ yields:

$$
\begin{align*}
((\mathbf{u}\otimes \mathbf{v})\mathbf{S})^T\mathbf{w}&=\mathbf{S}^T(\mathbf{v}\otimes \mathbf{u})\cdot \mathbf{w}\\[10pt]
&=\mathbf{S}^T(\mathbf{u}\cdot \mathbf{w})\mathbf{v}
\end{align*}
$$

Right hand side:

$$
\begin{align*}
(\mathbf{u}\otimes (\mathbf{S}^T\mathbf{v}))^T&=((\mathbf{S}^T\mathbf{v})\otimes \mathbf{u})\mathbf{\mathbf{w}}=(\mathbf{u}\cdot \mathbf{w})\mathbf{S}^T\mathbf{v}\\[10pt]
&=\mathbf{S}^T(\mathbf{u}\cdot \mathbf{w})\mathbf{v}
\end{align*}
$$

The LHS and RHS are equal, Q.E.D.


$(\mathbf{a}\otimes \mathbf{b})(\mathbf{c}\otimes \mathbf{d})=(\mathbf{b}\cdot \mathbf{c})\mathbf{a}\otimes \mathbf{d}$

Using the identity below:

$$
\mathbf{S}(\mathbf{u\otimes v})=(\mathbf{Su})\otimes \mathbf{v}
$$

$$
\begin{align*}
(\mathbf{a}\otimes \mathbf{b})(\mathbf{c}\otimes \mathbf{d})&=(\mathbf{b}\cdot \mathbf{c})\mathbf{a}\otimes \mathbf{d}\\[10pt]
\end{align*}
$$
Multiplying both sides by $\mathbf{w}$:

$$
\begin{align*}
(((\mathbf{b}\cdot \mathbf{c})\mathbf{a})\otimes \mathbf{d})\mathbf{w}&=(\mathbf{d}\cdot \mathbf{w})((\mathbf{b}\cdot \mathbf{c})\mathbf{a})
\end{align*}
$$
Multiplying the RHS by $\mathbf{w}$:

$$
((\mathbf{b}\cdot \mathbf{c})\mathbf{a}\otimes \mathbf{d})\mathbf{w}=(\mathbf{d}\cdot \mathbf{w})((\mathbf{b}\cdot \mathbf{c})\mathbf{a})
$$

The LHS and RHS are equal, Q.E.D.


$\mathbf{R}\cdot(\mathbf{S}\mathbf{T})=(\mathbf{S}^T\mathbf{R})\cdot \mathbf{T}=(\mathbf{R}\mathbf{T}^T)\cdot \mathbf{S}$

By the definition of the transpose:

$$
\mathbf{S}\mathbf{u}\cdot \mathbf{v}=\mathbf{u}\cdot \mathbf{S}^T\mathbf{v}
$$
Taking the transpose of each term:

$$
\begin{align*}
(\mathbf{R}\cdot(\mathbf{S}\mathbf{T}))^T&=((\mathbf{S}^T\mathbf{R})\cdot \mathbf{T})^T=((\mathbf{R}\mathbf{T}^T)\cdot \mathbf{S})^T\\[10pt]
\implies \text{tr}(\mathbf{R}(\mathbf{S}\mathbf{T})^T)&=\text{tr}(\mathbf{S}^T\mathbf{R}\mathbf{T}^T)=\text{tr}((\mathbf{R}\mathbf{T}^T)\mathbf{S}^T)\\[10pt]\implies
\text{tr}(\mathbf{R}\mathbf{T^T}\mathbf{S^T})&=\text{tr}(\mathbf{R}\mathbf{T^T}\mathbf{S^T})=\text{tr}(\mathbf{R}\mathbf{T^T}\mathbf{S^T})\tag{1}
\end{align*}
$$

Equation 1 is all equal. Q.E.D.

$\mathbf{S}\cdot(\mathbf{u}\otimes \mathbf{v})=\mathbf{u}\cdot \mathbf{S}\mathbf{v}$

Taking the trace of the LHS:

$$
\begin{align*}
\mathbf{S}\cdot(\mathbf{u}\otimes \mathbf{v})&=\text{tr}(\mathbf{S}(\mathbf{v}\otimes \mathbf{u}))\\[10pt]
&=\text{tr}((\mathbf{v}\otimes \mathbf{u})\mathbf{S})=\text{tr}(\mathbf{S\mathbf{v}}\otimes \mathbf{u})\\[10pt]
&=\mathbf{S}\mathbf{v}\cdot \mathbf{u}
\end{align*}
$$

Dot products are commutative, so the LHS is equal to the S: 

$$
\mathbf{u}\cdot \mathbf{S}\mathbf{v}=\mathbf{S}\mathbf{v}\cdot \mathbf{u}
$$

Q.E.D.


$(\mathbf{a}\otimes \mathbf{b})\cdot(\mathbf{c}\otimes \mathbf{d})=(\mathbf{a}\cdot \mathbf{c})(\mathbf{b}\cdot \mathbf{d})$

Taking the trace of the LHS:

$$
\begin{align*}
(\mathbf{a}\otimes \mathbf{b})\cdot(\mathbf{c}\otimes \mathbf{d})&=\text{tr}((\mathbf{a}\otimes \mathbf{b})(\mathbf{d}\otimes \mathbf{c})\\[10pt]
&=\text{tr}((\mathbf{b}\cdot \mathbf{d})\mathbf{a}\otimes \mathbf{c})\\[10pt]
&=(\mathbf{b}\cdot \mathbf{d})\mathbf{a}\cdot \mathbf{c}=(\mathbf{b}\cdot \mathbf{d})(\mathbf{a}\cdot \mathbf{c})
\end{align*}
$$
The LHS is equal to the RHS. Q.E.D

2.

$(\mathbf{u}\times \mathbf{v})\times \mathbf{w}=(\mathbf{u}\cdot \mathbf{w})\mathbf{v}-(\mathbf{v}\cdot \mathbf{w})\mathbf{u}$

$\mathbf{u}\times(\mathbf{v}\times \mathbf{w})=(\mathbf{u}\cdot \mathbf{w})\mathbf{v}-(\mathbf{u}\cdot \mathbf{v})\mathbf{w}$

$\text{det}\mathbf{S}=\frac{\mathbf{S}\mathbf{u}\cdot(\mathbf{S}\mathbf{v}\times \mathbf{S}\mathbf{w})}{\mathbf{u}\cdot(\mathbf{v}\times \mathbf{w})}$

3.



$$

$(u\times v)\times w$

$$
\frac{Su\cdot(Sv\times Sw)}{u\cdot(v\times w)}
$$

$$
e_{1}\otimes e_{1}



3.

$$
\Lambda=\begin{bmatrix}
-0.5 & -0.5 & 0.707 \\
0.707 & -0.707 & 0 \\
0.5 & 0.5 & 0.707
\end{bmatrix}
$$

$$
\mathbf{v}=
\begin{bmatrix}
1 \\
2 \\
-1
\end{bmatrix}\cdot
\begin{bmatrix}
e_{1} & e_{2} & e_{3}
\end{bmatrix}
=\begin{bmatrix}
-2.207 \\
-0.707 \\
0.793
\end{bmatrix}\cdot
\begin{bmatrix}
e_{1}' & e_{2}' & e_{3}'
\end{bmatrix}
$$

$$
\mathbf{T}=
\begin{bmatrix}
-0.5 & -1 & -0.707 \\
0.707 & -1.414 & 0 \\
0.5 & 1 & -0.707
\end{bmatrix}\cdot \begin{bmatrix}
e_{1}' & 0 & 0 \\
0 & e_{2}' & 0 \\
0 & 0 & e_{3}'
\end{bmatrix}=\begin{bmatrix}
1 & 0 & 0 \\
0 & -2 & 0 \\
0 & 0 & -1
\end{bmatrix}
$$

$$
n = \begin{bmatrix}
\frac{1}{\sqrt{ 6 }} \\
\frac{1}{\sqrt{ 6 }} \\
\frac{2}{\sqrt{ 6 }}
\end{bmatrix}
$$

$$
\mathbf{W}=
\begin{bmatrix}
0 & -\frac{2}{\sqrt{ 6 }} & \frac{1}{\sqrt{ 6 }} \\
\frac{2}{\sqrt{ 6 }} & 0 & \frac-{1}{\sqrt{ 6 }} \\
\frac-{1}{\sqrt{ 6 }} & \frac{1}{\sqrt{ 6 }} & 0
\end{bmatrix}
$$

$$
\mathbf{I}= \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

$$
\mathbf{R} = \mathbf{I}+(\sin(\theta))\mathbf{W}+(1+\cos(\theta))\mathbf{W}^2
$$
$$
\mathbf{R}=\begin{bmatrix}
0.88 & -0.38 & 0.24 \\
0.43 & 0.88 & -.159 \\
-0.159 & 0.24 & 0.955
\end{bmatrix}
$$

$$
\mathbf{R}\mathbf{n}=\begin{bmatrix}
0.40 \\
0.40 \\
0.81
\end{bmatrix}
$$