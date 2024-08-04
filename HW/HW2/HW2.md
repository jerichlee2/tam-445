2/3/24

![[Pasted image 20240203141854.png]]


$$
e_{i}\otimes e_{j}
$$

To show that the above is a basis of all second order tensors, we must prove that they are a set of linearly independent vectors that span the vector space of Lin(V)

how do we do?

perhaps we can show that the dimension of the null space is zero

$$
e_{i}\otimes e_{j}=
\begin{bmatrix}
e_{1}e_{1} & e_{1}e_{2} & e_{1}e_{3}\\
e_{2}e_{3} & e_{2}e_{2} & e_{2}e_{3} \\
e_{3}e_{1} & e_{3}e_{2 }& e_{3}e_{3}
\end{bmatrix}


$$

Let $e_{i}$ be defined as a set of basis vectors in $\mathbb{R}^3$. 

$$
e_{i}=\{e_{1}, e_{2}, e_{3}\}
$$

Let T be a tensor in $\text{Lin}(V)$, such that 

$$
T\underline{u}=\alpha_{i}\cdot T\underline{e}_{i}
$$
where 

$$
\underline{u}=\alpha_{i}\underline{e}_{i}
$$

Therefore:
$$
T\underline{u}=\alpha_{1}\underline{e}_{1}+\alpha_{2}\underline{e}_{2}+\alpha_{3}\underline{e}_{3}
$$

Each component can be obtained as:

$$
\alpha_{i}=T\underline{u}\cdot \underline{e}_{i}
$$

Because $\underline{u}$ can be represented as $\underline{u}=u_{j}\underline{e}_{j}$,

$$
\begin{align*}
\alpha_{i}&=T(u_{j}\underline{e}_{j})\cdot \underline{e}_{i}\\[10pt]
&=u_{j}T\underline{e}_{j}\cdot \underline{e}_{i}\\[10pt]
&=u_{j}T_{ij}
\end{align*}

$$

To prove that $e_{i}\otimes e_{j}$ forms a basis for $\text{Lin}(V)$, we need to show that 

$$
((T_{ij}e_{i}\otimes e_{j})\underline{u})_{i} = T_{ij}u_{j})
$$


The list of tensors in $e_{i}\otimes e_{j}$ is linearly independent from each other, (i.e, neither tensor can be represented as a combination of the other). The dimension of $\text{Lin}(V)$is defined to be 9. Thus the set of all tensors in $e_{i}\otimes e_{j}$ is a basis of $\text{Lin}(V)$. 

$\text{Lin}(V)$ is defined as the set of all second-order tensors with dimension 9, the span must have a length of 9, which corresponds to each tensor of $e_{i}\otimes e_{j}$. Each tensor cannot be represented as a combination of another tensor, i.e—which means that the length of this set is at a maximum. This proves that the set of nine tensors forms a basis for $\text{Lin}(V)$. 


we can use the result of LADR about proving that the length of two sets of bases in a span is equal, but apply this to the span of tensor spaces