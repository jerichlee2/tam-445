
How do I convert the vector field
$$
\begin{align}\mathbf{x}(\mathbf{a})=
\begin{bmatrix}
a_{x} \\
a_{z}-(a_{z}-r)\left( 1-\cos\left( \frac{a_{y}}{r} \right) \right) \\
(a_{z}+r)\sin\left( \frac{a_{y}}{r} \right)
\end{bmatrix}
\end{align}
$$
into a matrix?

perhaps...

$$
\begin{align}
\begin{bmatrix}
a & b & c \\
d  & e & f \\
g & h & i
\end{bmatrix}\begin{bmatrix}
a_{x} \\
a_{y} \\
a_{z}
\end{bmatrix}=\begin{bmatrix}
a_{x} \\
a_{z}-(a_{z}-r)\left( 1-\cos\left( \frac{a_{y}}{r} \right) \right) \\
(a_{z}+r)\sin\left( \frac{a_{y}}{r} \right)
\end{bmatrix}
\end{align}
$$
, where $$
A = \begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{bmatrix}
$$
Then I could find the determinant of $A$ and:

- If $\det(A)=1$ then the magnitude is constant
- If $\det(A) = -1$ then mag is constant and the direction is flipped
- else the mag changes

Hmm.. we need more equations...

I guess what I'm trying to ask is can we extract some information solely from $\mathbf{x}(\mathbf{a})$ that tells us something about how it transforms the domain? 
