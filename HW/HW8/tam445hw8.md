
$$
\begin{align}
\mathbf{a}_{s}=\frac{ \partial \mathbf{v}_{s} }{ \partial t } + \text{grad}\mathbf{v}_{s}\mathbf{v}_{s}(\mathbf{x}, t) \\
= \begin{bmatrix}
-ce^{-ct+x_{3}}\cos(\omega t)-\omega e^{-ct+x_{3}}\sin(\omega t) \\
-ce^{-ct+x_{3}}\sin(\omega t)+\omega e^{-ct+x_{3}}\cos(\omega t) \\
0
\end{bmatrix}+\begin{bmatrix}
0 & 0 & c^{-ct+x_{3}}\cos(\omega t) \\
0 & 0 & e^{-ct+x_{3}}\sin(\omega t) \\
0 & 0 & 0
\end{bmatrix}\begin{bmatrix}
e^{x_{3}-ct}\cos(\omega t) \\
e^{x_{3}-ct}\sin(\omega t) \\
c
\end{bmatrix}
\end{align}
$$

Computing $\mathbf{a}_{s}\cdot \mathbf{v_{s}}$ where:

$$
\mathbf{v}_{s}=\begin{bmatrix}
e^{x_{3}-ct}\cos(\omega t) \\
e^{x_{3}-ct}\sin(\omega t) \\
c
\end{bmatrix}
$$

$$
\mathbf{a}_{s}\cdot \mathbf{v}_{s}=0
$$




$$
\begin{align}
\mathbf{a}_{s}= \begin{bmatrix}
-\omega e^{-ct+x_{3}}\sin(\omega t) \\
\omega e^{-ct+x_{3}}\cos(\omega t) \\
0
\end{bmatrix}
\end{align}

$$

$$
\begin{align}
D(\mathbf{x}, t)=\frac{1}{2}(\text{grad}\mathbf{v}_{s}+\text{grad}\mathbf{v}_{s}^{\text{T}}) \\
= \begin{bmatrix}
0 & 0 & \frac{1}{2}e^{-ct+x_{3}}\cos(\omega t) \\
0 & 0 & \frac{1}{2}e^{-ct+x_{3}}\sin(\omega t) \\
\frac{1}{2}e^{-ct+x_{3}}\cos(\omega t) & \frac{1}{2}e^{-ct+x_{3}}\sin(\omega t) & 0
\end{bmatrix}\begin{bmatrix}
\frac{1}{2} \\
0 \\
\frac{1}{2} \\
\end{bmatrix}  \\
= \begin{bmatrix}
\frac{1}{4}e^{-ct}\cos(\omega t) \\
\frac{1}{4}e^{-ct}\sin(\omega t) \\
\frac{1}{4}e^{-ct}\cos(\omega t)
\end{bmatrix} \\
\end{align}
$$
Taking the dot product to obtain the scalar value:

$$
\begin{align}
D\cdot \mathbf{\text{dir}}= \frac{1}{2}e^{-ct+x_{3}}\cos(\omega t)
\end{align}
$$

Integrating the third component of $\mathbf{v}_{s}$:
$$
\begin{align}
x_{3}=c(t+1)+X_{3} \\
\end{align}
$$

Substituting the above into $\mathbf{v}_{s}$:

$$
\begin{align}
\mathbf{v}_{s}=\begin{bmatrix}
e^{ct+c-ct+X_{3}}\cos(\omega t) \\
e^{ct+c-ct+X_{3}}\sin(\omega t) \\
c
\end{bmatrix} \\
= \begin{bmatrix}
e^{X_{3}+c}\cos(\omega t) \\
e^{X_{3}+c}\sin(\omega t) \\
c
\end{bmatrix}
\end{align}
$$

Integrating the components of $\mathbf{v}_{s}$:

$$
\begin{align}
\mathbf{x}=\begin{bmatrix}
e^{X_{3}+c}\sin(\omega t) \\
e^{X_{3}+c}\cos(\omega t) \\
c(t+1)
\end{bmatrix}
\end{align}
$$


$$
\begin{align}
\lambda_{3}\to n=v_{3} \\
\lvert N \rvert = \lvert T\mathbf{n}\cdot \mathbf{n} \rvert \leq \lvert T\mathbf{v}_{3}\cdot v_{3} \rvert \\
= \lvert \lambda \mathbf{v}_{3}\cdot \mathbf{v}_{3} \rvert \\
\implies \parallel T \mathbf{n} \cdot \mathbf{n}\parallel \leq \lvert \lambda_{3} \rvert 
\end{align}
$$

$$
\begin{align}
\lvert T \mathbf{n}\cdot \mathbf{n} \rvert =  \\
\lvert T(k_{1}\mathbf{v}_{1}+k_{2}\mathbf{v}_{2}+k_{3}\mathbf{v}_{3})\cdot(k_{1}\mathbf{v}_{1}+k_{2}\mathbf{v}_{2}+k_{3}\mathbf{v}_{3})\rvert   \\
= \lvert k_{1}T\mathbf{v}_{1}+k_{2}T\mathbf{v}_{2}+k_{3}Tv_{3} \cdot k_{1}T\mathbf{v}_{1}+k_{2}T\mathbf{v}_{2}+k_{3}Tv_{3}\rvert  \\
= \lvert \lambda k_{1}\mathbf{v_{1}} + \lambda_{2}k_{2}\mathbf{v_{2}}+\lambda_{3}k_{3}\mathbf{v_{3}} \cdot \lambda_{1}k_{1}\mathbf{v_{1}} + \lambda_{2}k_{2}\mathbf{v_{2}}+\lambda_{3}k_{3}\mathbf{v_{3}}\rvert \\
= \lvert \lambda_{1}k_{1}^2+\lambda_{2}k_{2}^2+\lambda_{3}k_{3}^2 \rvert 
\end{align}
$$

$$
\begin{align}
\lambda_{1}\cos^2\theta_{1}+\lambda_{2}\cos^2\theta_{2}+\lambda_{3}\cos^2\theta_{3} \leq \lvert \lambda_{3}|(\cos^2\theta_{1}+\cos^2\theta_{2}+\cos^2\theta_{3}) \leq \lvert \lambda_{3} \rvert 
\end{align}
$$$$
\begin{align}
\frac{ \partial x }{ \partial t }  \\
\int_{0}^{\infty}  \, dx 
\end{align}
$$