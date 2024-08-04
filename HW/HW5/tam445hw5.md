1. $\nabla \mathbf{v}=\mathbf{I}$

$$
\begin{align}
\nabla \mathbf{v}=\frac{ \partial x_{i} }{ \partial x_{j} } \underline{e}_{i}\otimes \underline{e}_{j} \\
\mathbf{I} = \delta_{ij}\underline{e}_{i}\otimes \underline{e}_{j} \\
\mathbf{I}\mathbf{u} = (\delta_{ij}\underline{e}_{i}\otimes \underline{e}_{j})\mathbf{u} \\
(\mathbf{I}\mathbf{u})_{i}=\mathbf{I}_{ij}u_{j} \\
(\delta_{ij}\underline{e}_{i}\otimes \underline{e}_{j})\mathbf{u}=\delta_{ij}(\underline{e}_{j}\cdot \mathbf{u})\underline{e}_{i} \\
=\delta_{ij}u_{j}\underline{e}_{i}
\end{align}
$$

$$
\begin{align}
\mathbf{I}_{ij}u_{j}=\delta_{ij}u_{j} \\
\end{align}
$$

2. $\nabla v=\frac{\mathbf{x}}{x}$

$$
\begin{align}
v(\mathbf{x})=(x_{i}x_{i})^{1/2} \\
\frac{ \partial (x_{j}x_{j})^{1/2} }{ \partial x_{i} } =\frac{1}{2}(x_{j}x_{j})^{-1/2}\left( \frac{ \partial x_{j} }{ \partial x_{i} } x_{j} +\frac{ \partial x_{j} }{ \partial x_{i} } x_{j}\right) \\
=\frac{1}{2}(x_{j}x_{j})^{-1/2}\left( 2\frac{ \partial x_j }{ \partial x_{i} } x_{j} \right) \\
=\frac{\delta_{ij}x_{j}}{(x_{j}x_{j})^{1/2}} \\
=\frac{x_{i}}{(x_{j}x_{j})^{1/2}} \\
=\frac{\mathbf{x}}{x}
\end{align}
$$

$\text{div}(\mathbf{v})=3$

$$
\begin{align}
\text{div}(\mathbf{v})=\text{tr}(\nabla \mathbf{v}) \\
=\text{tr}(\mathbf{I}) \\
=3
\end{align}
$$

$\text{div}\left( \frac{\mathbf{v}}{v} \right)=\frac{2}{x}$

$$
\begin{align}
\phi=\frac{1}{v} =\frac{1}{(v_{i}v_{i})^{1/2}}
\end{align}
$$

$$
\begin{align}
\text{div}(\phi \mathbf{v})=\phi \ \text{div}(\mathbf{v})+\mathbf{v}\cdot \nabla \phi \\
=\frac{1}{v}\text{tr}(\nabla \mathbf{v})+\mathbf{v}\cdot \left( \nabla \frac{1}{v} \right)
\end{align}
$$

$$
\begin{align}
\nabla \frac{1}{v} \\
=\nabla (x_{i}x_{i})^{-1/2} \\
= \frac{ \partial (x_{j}x_{j})^{-1/2} }{ \partial x_{i} }  \\
=-\frac{1}{2}(x_{j}x_{j})^{-3/2}(\delta_{ij}x_{j}+\delta_{ij}x_{j}) \\
=-\frac{2\delta_{ij}x_{j}}{2(x_{j}x_{j})^{3/2}} \\
=-\frac{x_{i}}{(x_{j}x_{j})^{3/2}} \\
=-\frac{\mathbf{x}}{x^3} \\
\end{align}
$$
$$
\begin{align}
\lvert \mathbf{x} \rvert =(\mathbf{x}\cdot \mathbf{x})^{1/2} \\
=x \\
=v
\end{align}
$$
$$
\begin{align}
\mathbf{x}\cdot\left( -\frac{\mathbf{x}}{x^3} \right) \\
=\frac{1}{x^3}(\mathbf{x}\cdot \mathbf{x}) \\
=-\frac{1}{x^3}(x^2) \\
=-\frac{1}{x}
\end{align}
$$

$$
\begin{align}
\frac{1}{v}\text{tr}(\mathbf{I}) =\frac{3}{x}\\
\end{align}
$$$$
\begin{align}
\frac{3}{x}+\mathbf{x}\cdot\left( -\frac{\mathbf{x}}{x^3} \right) \\
=\frac{2}{x}
\end{align}
$$

$$
\text{div}(\mathbf{v}\otimes \mathbf{v})=4x
$$
$$
\begin{align}
\text{div}(\mathbf{v}\otimes \mathbf{v})=\mathbf{v}(\text{div}(\mathbf{v}))+(\nabla \mathbf{v})\mathbf{v}
\end{align}
$$

$$
\begin{align} \\
\mathbf{v}(\text{div}(\mathbf{v}))+(\nabla \mathbf{v})\mathbf{v} =
3\mathbf{v}+I\mathbf{v} \\
=4\mathbf{v} \\
=4\mathbf{x}
\end{align}
$$

$$
\text{curl}(\mathbf{v})=\mathbf{0}
$$
$$
\begin{align}
\text{curl}(\mathbf{v})=\epsilon_{kji}\frac{ \partial v_{i} }{ \partial x_{j} } e_{k}
\end{align}
$$

Using Eqn (\ref{eq:21}), Eqn (\ref{43}) is simplified as follows:

$$
\begin{align}
=\epsilon_{kji}\frac{ \partial v_{i} }{ \partial x_{j} } e_{k} \\
=\epsilon_{kji}\delta_{ij}e_{k} \\
=\epsilon_{kii}e_{k} \\
=\mathbf{0}
\end{align}
$$

$\text{curl}\left( \frac{\mathbf{v}}{v} \right)=\mathbf{0}$

Setting $\phi=\frac{1}{v}$, using the identity of the curl of a scalar field multiplied by a vector field, and using the result of Eqn (\ref{eq:x}):
$$
\begin{align}
\frac{1}{v}=\phi \\
=\underbrace{ \cancel{ \phi \ \text{curl}(\mathbf{v}) } }_{ 0 }+\nabla \phi \times \mathbf{v}
\end{align}
$$

Substituting Eqn (\ref{eq:31}) into Eqn (\ref{eq:x}):

$$
\begin{align}
=-\left( \frac{1}{x^3} \right)\underbrace{ \cancel{ \mathbf{x}\times \mathbf{x} } }_{ 0 } \\
=\mathbf{0}
\end{align}
$$

$\text{div}(\text{curl}(\mathbf{v}))=0$

$\text{curl}(\nabla \phi)=\mathbf{0}$

$$
\nabla \phi+\text{curl}(\mathbf{v})=\mathbf{0}
$$

$\Delta \phi=0$

$\text{div}(\mathbf{v})$

$$
\begin{align}
\text{div}(\text{curl}(\mathbf{v}))=\text{div}\left( \epsilon_{kji}\frac{ \partial v_{i} }{ \partial x_{j} } \underline{e}_{k} \right) \\
\end{align}
$$
Setting $\mathbf{\gamma}(\mathbf{v})=\underline{e}_{k}$ and $\varepsilon(\mathbf{v})=\epsilon_{kji}\frac{ \partial v_{i} }{ \partial x_{j} }$ and using the identity of divergence of the curl of a vector:

$$
\begin{align}
=\epsilon \  \text{div}(\mathbf{\gamma})+\mathbf{\gamma}\cdot \nabla\varepsilon \\
\underbrace{ \cancel{ \varepsilon \ \text{tr}(\nabla \underline{e}_{k}) } }_{ 0 }+\underbrace{ \cancel{ \underline{e}_{k} \cdot \frac{ \partial \varepsilon}{ \partial x_{i} }e_\underline{i} } }_{ 0 }
\end{align}
$$
$$
\underbrace{ \cancel{ \varepsilon \ \text{tr}(\nabla \underline{e}_{k}) } }_{ 0 }+\underbrace{ \cancel{ \underline{e}_{k}\cdot \frac{ \partial \varepsilon }{ \partial x_{i} } \underline{e}_{i} } }_{ 0 }
$$


$$
\begin{align}
\text{curl}(\nabla \phi)=\mathbf{0} \\
\text{curl}\left( \frac{ \partial \phi }{ \partial x_{i} } \underline{e}_{i} \right) \\
=\nabla \times\left( \frac{ \partial \phi }{ \partial x_{i} } \underline{e}_{i} \right) \\
=\underbrace{ \cancel{ \nabla \frac{ \partial \phi }{ \partial x_{i} } \times \underline{e}_{i} } }_{ 0 }+\underbrace{ \cancel{ \frac{ \partial \phi }{ \partial x_{i} } \text{curl}(\underline{e}_{i}) } }_{ 0 }
\end{align}
$$


We begin by calculating $\nabla \phi$:
$$
\begin{align}
\phi=\frac{c_{j}x_{j}}{(x_{k}x_{k})^{3/2}} \\
\nabla \phi=\frac{ \partial (c_{j}x_{j}(x_{k}x_{k})^{-3/2}) }{ \partial x_{i} } \underline{e}_{k} \\
=c_{j}\frac{ \partial x_{j} }{ \partial x_{i} } (x_{k}x_{k})^{-3/2}\underline{e}_{k}+ -\frac{3}{2}c_{j}x_{j}(x_{k}x_{k})^{-5/2}\left( 2\frac{ \partial x_{k} }{ \partial x_{i} } x_{k} \right)\underline{e}_{k} \\
=\frac{c_{i}}{(x_{k}x_{k})^{3/2}}\underline{e}_{i}-\frac{3c_{j}x_{j}x_{i}}{(x_{k}x_{k})^{5/2}}\underline{e}_{i}
\end{align}
$$

Calculating $\mathbf{v}$ in indicial notation:

$$
\begin{align}
\mathbf{v}(\mathbf{x})=\frac{\mathbf{c}\times \mathbf{v}}{x^3} \\
=\frac{\epsilon_{ijk}c_{j}x_{k}}{(x_{s}x_{s})^{3/2}}\underline{e}_{i}
\end{align}
$$

Calculating $\text{curl}(\mathbf{v})$:

$$
\begin{align}
\nabla \times \mathbf{v}=\epsilon_{lnm}\frac{ \partial (\epsilon_{ijk}c_{j}x_{k}(x_{s}x_{s})^{-3/2}) }{ \partial x_{n} } \delta_{\mathrm{im}}\underline{e}_{l} \\
\end{align}
$$

Taking the partial derivative of Eqn (\ref{eq:x}) using the product rule for the first term:

$$
\begin{align}
=\epsilon_{lnm}\epsilon_{ijk}c_{j}\delta_{kn}(x_{s}x_{s})^{-3/2}\delta_{im}\underline{e}_{l} \\
\epsilon_{lni}\epsilon_{jni}c_{j}(x_{s}x_{s})^{-3/2}\underline{e}_{l} \\
=2\delta_{lj}c_{j}(x_{s}x_{s})^{-3/2}\underline{e}_{l} \\
=\frac{2c_{l}}{(x_{s}x_{s})^{3/2}}
\end{align}
$$

Taking the partial derivative of Eqn (\ref{eq:x}) using the product rule for the first term:

$$
\begin{align}
 -\frac{3}{2} \epsilon_{lnm}\epsilon_{ijk}c_{j}x_{k}(x_{s}x_{s})^{-5/2}(2\delta_{sn}x_{s})\delta_{im}e_{l} \\
=-\frac{3}{2}\epsilon_{lni}\epsilon_{ijk}c_{j}x_{k}(x_{s}x_{s})^{-5/2}2x_{n}e_{l} \\
=-3\epsilon_{lni}\epsilon_{jki}c_{j}x_{k}x_{n}(x_{s}x_{s})^{-5/2}\underline{e}_{l} \\
(\delta_{lj}\delta_{nk}-\delta_{lk}\delta_{nj})(-3c_{j}x_{k}x_{n}(x_{s}x_{s})^{-5/2})\underline{e}_{l} \\
=\delta_{lj}\delta_{nk}(-3c_{j}x_{k}x_{n}(x_{s}x_{s})^{-5/2})\underline{e}_{l}-\delta_{lk}\delta_{nj}(-3c_{j}x_{k}x_{n}(x_{s}x_{s})^{-5/2})\underline{e}_{l} \\
=-3c_{l}x_{k}x_{k}(x_{s}x_{s})^{-5/2}e_{l}+3c_{n}x_{l}x_{n}(x_{s}x_{s})^{-5/2}\underline{e}_{l} \\
=-\frac{3c_{l}}{(x_{s}x_{s})^{3/2}}\underline{e}_{l}+\frac{3c_{n}x_{n}x_{l}}{(x_{s}x_{s})^{5/2}}\underline{e}_{l}+\frac{2c_{l}}{(x_{s}x_{s})^{3/2}}\underline{e}_{l} \\
=-\frac{c_{l}}{(x_{s}x_{s})^{3/2}}\underline{e}_{l}+\frac{3c_{n}x_{n}x_{l}}{(x_{s}x_{s})^{5/2}}\underline{e}_{l}
\end{align}
$$

$$
\begin{align}
\nabla \phi+\text{curl}(\mathbf{v})=\mathbf{0} \\
=
\frac{c_{i}}{(x_{k}x_{k})^{3/2}}\underline{e}_{i}-\frac{3c_{j}x_{j}x_{i}}{(x_{k}x_{k})^{5/2}}\underline{e}_{i}-\frac{c_{l}}{(x_{s}x_{s})^{3/2}}\underline{e}_{l}+\frac{3c_{n}x_{n}x_{l}}{(x_{s}x_{s})^{5/2}}\underline{e}_{l} \\
=0
\end{align}
$$

$$
\begin{align}
\Delta \phi=0 \\
\phi(\mathbf{x})=\frac{\mathbf{c}\cdot \mathbf{x}}{x^3} \\
\nabla \phi=\left( \frac{c_{i}}{(x_{k}x_{k})^{3/2}}-\frac{3c_{j}x_{j}x_{i}}{(x_{k}x_{k})^{5/2}} \right)\underline{e}_{i} \\
\nabla(\nabla \phi)=\nabla\left( \frac{c_{i}}{(x_{k}x_{k})^{3/2}}\right)-\nabla\left( \frac{3c_{j}x_{j}x_{i}}{(x_{k}x_{k})^{5/2}}  \right) \\
=\nabla(c_{i}(x_{k}x_{k})^{-3/2})-\nabla(3c_{j}x_{j}x_{i}(x_{k}x_{k})^{-5/2}) \\
\frac{ \partial c_{i}(x_{k}x_{k})^{-3/2} }{ \partial x_{j} } -\frac{ \partial (3c_{j}x_{j}x_{i}(x_{k}x_{k})^{-5/2}) }{ \partial x_{j} }  \\
=-\frac{3}{2}c_{i}(x_{k}x_{k})^{-5/2}(2\delta_{kj}x_{k})-3c_{j}(3)x_{i}(x_{k}x_{k})^{-5/2} \\
=-3c_{i}(x_{k}x_{k})^{-5/2}x_{j}=\frac{9c_{j}x_{i}}{(x_{k}x_{k})^{5/2}}+\frac{3c_{j}x_{i}}{(x_{k}x_{k})^{5/2}} \\
-\frac{3c_{i}x_{j}}{(x_{k}x_{k})^{5/2}}=3c_{j}x_{j}x_{i}\left( -\frac{5}{2} \right)(x_{k}x_{k})^{-7/2}(2\delta_{kj}x_{k}) \\
=-3c_{i}x_{j} \\
(x_{k}x_{k})^{5/2}=-\frac{15c_{j}(x_{j}x_{j})x_{i}}{(x_{k}x_{k})^{7/2}} \\
=\frac{-3c_{i}x_{j}}{(x_{k}x_{k})^{5/2}}+\frac{3c_{j}x_{i}}{(x_{k}x_{k})^{5/2}}
\end{align}
$$

The index $i=j$ when applying the trace function upon a tensor, so the following holds true:

$$
\begin{align}
\text{tr}\left( \frac{-3c_{i}x_{j}}{(x_{k}x_{k})^{5/2}}+\frac{3c_{j}x_{i}}{(x_{k}x_{k})^{5/2}} \right) \\
=0
\end{align}
$$


$$
\begin{align}
\text{div}(\mathbf{v})=0 \\
\text{div}(\epsilon_{ijk}c_{j}x_{k}(x_{s}x_{s})^{-3/2})\underline{e}_{i} \\
=tr(\nabla \mathbf{v}) \\
=\frac{ \partial \epsilon_{ijk}c_{j}x_{k}(x_{s}x_{s}^{-3/2}) }{ \partial x_{j} } \underline{e}_{i}\otimes \underline{e}_{j} \\
=\epsilon_{ijk}c_{j}\delta_{kj}(x_{s}x_{s})^{-3/2}+\epsilon_{ijk}c_{j}x_{k}\left( -\frac{3}{2} \right)(x_{s}x_{s})^{5/2}(2\delta_{sj}x_{s}) \\
=\underbrace{ \cancel{ \epsilon_{ikk}c_{j}(x_{s}x_{s})^{-3/2} } }_{ 0 }-\frac{3\epsilon_{ijk}c_{j}x_{k}x_{j}}{(x_{s}x_{s})^{5/2}}\underline{e}_{i}\otimes \underline{e}_{j} \\
\end{align}
$$

Taking the trace of Eqn (\ref{eq:x}):

$$
\begin{align}
\text{tr}(\nabla \mathbf{v})=-\frac{3\epsilon_{ijk}c_{j}x_{k}x_{j}}{(x_{s}x_{s})^{5/2}}\delta_{ij} \\
=-\frac{3\epsilon_{iik}c_{j}x_{j}x_{k}}{(x_{s}x_{s})^{5/2}} \\
=0
\end{align}
$$
