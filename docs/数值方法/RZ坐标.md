# 尾场加速，兼考虑PIC的RZ坐标测试对比









RZ坐标方法是一种**准三维 PIC**。电磁场、电荷和电流定义在 \(r\!-\!z\) 网格上，用有限个傅里叶模描述方位角 \(\phi\) 的变化。宏粒子保留三维位置和动量，在重建出的局部电磁场中运动。这让同一次计算既能解析线偏振激光的光学振荡，也能描述近轴对称的等离子体尾场。论文的主要算法贡献，是让**每个保留的模都独立满足离散电荷连续性方程**。

## 1.  \(r\!-\!z\) 网格的基本考虑

把电磁场投影到随 \(\phi\) 旋转的圆柱基底 \((\hat{\mathbf e}_r,\hat{\mathbf e}_\phi,\hat{\mathbf e}_z)\)。对每个分量，以及标量 \(\rho\)，分别做方位角傅里叶展开。以下采用标准双边傅里叶系数约定


$$
F(r,\phi,z,t) =F_0(r,z,t)+2\operatorname{Re} \sum_{m=1}^{m_{\max}}F_m(r,z,t)e^{im\phi}
$$


这里 \(F_m\) 是定义在二维网格上的复数。它的实部和虚部共同编码该模的余弦和正弦分量。于是，保留到 \(m_{\max}\) 时，每个场分量需要 \(1+2m_{\max}\) 个实值二维数组。或者固定时间 $t$ ，显示地写出 $\sin ,\;\cos $ 项


$$
\boxed{ F(r,\phi,z) = F_0(r,z) + \sum_{m=1}^{m_{\max}} \left[ A_m(r,z)\cos(m\phi) + B_m(r,z)\sin(m\phi) \right]}
$$


这里，\(F_0,A_m,B_m\) 都是**定义在 \(r\!-\!z\) 平面上的实函数**。按照 \(e^{+im\phi}\) 的约定，它们与复系数的关系是


$$
A_m=2\operatorname{Re}F_m,\qquad B_m=-2\operatorname{Im}F_m
$$


例如只保留到 \(m_{\max}=2\)，逐项写开就是


$$
\begin{aligned} F(r,\phi,z) ={}&F_0(r,z)\\ &+A_1(r,z)\cos\phi+B_1(r,z)\sin\phi\\ &+A_2(r,z)\cos2\phi+B_2(r,z)\sin2\phi. \end{aligned}
$$


这样 RZ 的表示就很直观：**在每个 \((r,z)\) 网格点，只存五个实数，就能得到这一圈上任意 \(\phi\) 处的值。** \(F_0\) 给出圆周平均值，\(m=1\) 项绕一圈振荡一次，\(m=2\) 项绕一圈振荡两次。恢复时间依赖时，只需把这些二维系数写回 \(F_0(r,z,t)\)、\(A_m(r,z,t)\)、\(B_m(r,z,t)\)。**随时间推进的是系数，角向基函数 \(\cos(m\phi)\)、\(\sin(m\phi)\) 始终固定。**

可以说，借助基函数，使得取定 $r,z$ 坐标之后，任意标量场或向量场的分量对 $\phi$ 的依赖通过少数几个基函数的系数来表征。具体精度取决于取得的阶数 $m$ 。

对于保存和推进的数据量：设 3D PIC 任意横截面网格划分为 $N_x \times N_y =64 \times 64$ ，而相应 RZ PIC 的划分为 $N_r =32$ ，角向阶数如果取 $M$ ，则包含了 $2M+1$ 个系数的推进和保存，于是横向切片数据量为 $(2M+1)N_r$ ，若仅仅论及数据量相等，可以取得阶数 $M \sim 64$ 。 

### 1.1 RZ 坐标解析注入激光

#### 1.1.1 **线偏振光取 $m=1$** 

以沿 \(+z\) 传播、沿 \(x\) 线偏振的入射激光为例。设其横向场是 \(\mathbf E_\perp=A(r,z,t)\hat{\mathbf x}\)，其中 \(A\) 的横向分布是圆对称的。由于


$$
\hat{\mathbf x} =\cos\phi\,\hat{\mathbf e}_r-\sin\phi\,\hat{\mathbf e}_\phi, \qquad E_r=A\cos\phi,\qquad E_\phi=-A\sin\phi
$$


这两个圆柱分量恰好都由 **\(m=1\)** 表示。沿 \(y\) 线偏振同样属于 \(m=1\)，只是方位角因子变成 \(E_r=A\sin\phi,\ E_\phi=A\cos\phi\)。

#### 1.1.2 **圆偏振光取 $m=1$** 

固定一个时刻。对沿 \(+z\) 传播的理想圆斑圆偏振光，横向电场可写成


$$
\mathbf E_\perp =A(r,z)\big[\cos\psi\,\hat{\mathbf x} +\sin\psi\,\hat{\mathbf y}\big]
$$


其中 \(\psi\) 是该时刻的载波相位。投影到随 \(\phi\) 转动的圆柱基底，得到


$$
\begin{aligned} E_r &= A\cos(\psi-\phi) =A\big(\cos\psi\cos\phi+\sin\psi\sin\phi\big),\\ E_\phi &= A\sin(\psi-\phi) =A\big(\sin\psi\cos\phi-\cos\psi\sin\phi\big) \end{aligned}
$$


两式的角向基函数都是 **\(\cos\phi,\sin\phi\)**，所以这两个横向场分量属于 **\(m=1\)**。不过平方相加后，


$$
E_r^2+E_\phi^2=A^2(r,z)
$$


方位角依赖恰好消掉了，所以强度是 \(m=0\)。

#### 1.1.3 **LG激光天然配合于RZ坐标**

对居中、沿 \(z\) 传播的 Laguerre–Gaussian（LG）光束，RZ 特别方便。 LG 的径向节点由 \(r\) 网格解析，涡旋相位 \(e^{i\ell\phi}\) 则直接对应角向 Fourier 模。不过要分清 LG 包络的涡旋阶数 \(\ell\) 和 WarpX 圆柱场分量的模数 \(m\)。偏振会让两者相差一阶。 [LASY 0.7.0 documentation](https://lasydoc.readthedocs.io/en/latest/api/profiles/transverse/laguerre_gaussian_profile.html?utm_source=chatgpt.com)

**为什么偏振会改变所需的 \(m\)？**

在注入平面，把 LG 的复横向场写成


$$
\widetilde{\mathbf E}_\perp =u_{p\ell}(r)\,e^{i\ell\phi}\,\mathbf e_{\rm pol}
$$


其中 \(p\) 是径向阶数。增加 \(p\) 会增加径向节点，因此可能需要更细的 \(\Delta r\)，但不会增加所需的角向模数。

对于圆偏振，明确采用 \(\mathbf e_\sigma=(\hat{\mathbf x}+i\sigma\hat{\mathbf y})/\sqrt2\)，其中 \(\sigma=\pm1\)。换到圆柱基底后，


$$
\mathbf e_\sigma =e^{i\sigma\phi}\, \frac{\hat{\mathbf r}+i\sigma\hat{\boldsymbol\phi}}{\sqrt2}
$$


于是 \(E_r,E_\phi\) 的角向因子变成 \(e^{i(\ell+\sigma)\phi}\) ；偏振会给角向阶数带来 \(\pm1\) 的移位，这个正负号由圆偏振的手性 \(\sigma\) 决定。**在线偏振下**，可把偏振分解成两个相反的圆偏振分量，因此一般同时出现 \(\ell+1\) 和 \(\ell-1\)。

|                  入射光束                   | 横向圆柱场所需的非负 \(m\) |
| :-----------------------------------------: | :------------------------: |
|  普通圆斑高斯，\(\ell=0\)，线偏振或圆偏振   |          \(m=1\)           |
|        \(\mathrm{LG}_{p,1}\)，线偏振        |         \(m=0,2\)          |
| \(\mathrm{LG}_{p,1}\)，圆偏振 \(\sigma=+1\) |          \(m=2\)           |
| \(\mathrm{LG}_{p,1}\)，圆偏振 \(\sigma=-1\) |          \(m=0\)           |

最后一行恰补充了刚才的问题：普通圆偏振高斯束需要 \(m=1\)，但带有适当涡旋相位的圆偏振 LG 束，可以让圆柱场只剩 \(m=0\)。这是因为涡旋相位恰好抵消了偏振矢量换基带来的角向相位。总之， $m=\ell +\sigma$ 。

**实际怎么注入？**

- **低阶 LG，沿用WarpX现有的解析天线**：用 `parse_field_function` 写出注入平面上的实电场即可。例如焦平面上的 \(\mathrm{LG}_{0,+1}\) 标量包络正比于 \((x+iy)e^{-(x^2+y^2)/w_0^2}\)，可用多项式写法避开轴上方位角未定义的问题。 [warpx.readthedocs.io](https://warpx.readthedocs.io/en/latest/usage/parameters.html?utm_source=chatgpt.com)
- **更高阶、离焦注入或多个 LG 模叠加**：可以用 LASY 的 `LaguerreGaussianTransverseProfile` 生成包络，再通过 WarpX 的 `from_file` 天线读取。

![LG](C:\Users\zsxl0\Desktop\LG.png)

然而事实上，无论是WarpX解析天线、还是LASY通过脚本注入，在WarpX的RZ运行读取时，仍是先转化为 $X,Y$ 坐标。从这个意义上，LG激光适合于RZ坐标只是内部推进的事，并非注入时候非常方便。



## 2. 一个 PIC 时间步如何推进RZ

### 2.1 Maxwell方程在角向分模

沿用前面的约定，对每个**圆柱分量**和标量做展开


$$
F(r,\phi,z,t)=\sum_{m=-M}^{M}F_m(r,z,t)e^{im\phi}
$$


代入 Maxwell 方程后，角向微分成为


$$
\partial_\phi F\ \longrightarrow\ imF_m
$$


柱坐标下的旋度，对 \(\mathbf F=F_r\hat{\mathbf r}+F_\phi\hat{\boldsymbol\phi}+F_z\hat{\mathbf z}\)


$$
\boxed{ \begin{aligned} (\nabla\times\mathbf F)_r &=\frac1r\partial_\phi F_z-\partial_zF_\phi,\\[3pt] (\nabla\times\mathbf F)_\phi &=\partial_zF_r-\partial_rF_z,\\[3pt] (\nabla\times\mathbf F)_z &=\partial_rF_\phi+\frac{F_\phi}{r}-\frac1r\partial_\phi F_r \end{aligned} }
$$


各项前面的系数：只有 \(1\)、\(-1\) 和 \(\pm1/r\)，都不含 \(\phi\) ，因此说：旋度算符的系数只依赖 \(r\) 。RZ求解已经假设若三个圆柱分量都含同一个角向因子 \(e^{im\phi}\) ，那么 \(\partial_r,\partial_z\) 只作用于模系数，\(\partial_\phi\) 则带来一个 \(im\)。例如，令 \(G=(\nabla\times\mathbf F)_z\) ，先把 \(F_\phi,F_r\) 的完整傅里叶展开代入


$$
\begin{aligned} G &=\frac1r\partial_r(rF_\phi)-\frac1r\partial_\phi F_r\\ &=\frac1r\partial_r\left(r\sum_m F_{\phi,m}e^{im\phi}\right) -\frac1r\partial_\phi\left(\sum_m F_{r,m}e^{im\phi}\right)\\ &=\sum_m e^{im\phi} \left[ \frac1r\partial_r(rF_{\phi,m})-\frac{im}{r}F_{r,m} \right] \end{aligned}
$$


现在把最后一行和 \(G=\sum_m G_m e^{im\phi}\) 逐项对照，就得到


$$
\boxed{ G_m=\big[(\nabla\times\mathbf F)_z\big]_m =\frac1r\partial_r(rF_{\phi,m})-\frac{im}{r}F_{r,m} }
$$


所以有三个不同的量：总旋度是 \(\sum_m G_m e^{im\phi}\)，第 \(m\) 模对总旋度的贡献是 \(G_m e^{im\phi}\)，第 \(m\) 模的系数是 \(G_m\)。上一条右边写的是第二个量。

“**第 \(m\) 模进去，第 \(m\) 模出来**”现在可以直接从框里的式子看出：求 \(G_m\) 时只用了 \(F_{\phi,m}\) 和 \(F_{r,m}\)。例如，求 \(G_2\) 时，\(F_{r,1}\) 不会出现在右边。这就是旋度算符**不混合不同角向模**的具体含义。

旋度输入是第 \(m\) 模，输出仍是第 \(m\) 模。 这就解释了为什么 Maxwell 方程可以在 \(r\!-\!z\) 网格上逐模 \(m\) 推进。对任意矢量 \(\mathbf F_m=(F_{r,m},F_{\phi,m},F_{z,m})\)，先定义该模的旋度


$$
\mathcal C_m\mathbf F_m= \begin{pmatrix} \displaystyle \frac{im}{r}F_{z,m}-\partial_zF_{\phi,m}\\[4pt] \displaystyle \partial_zF_{r,m}-\partial_rF_{z,m}\\[4pt] \displaystyle \frac1r\partial_r(rF_{\phi,m})-\frac{im}{r}F_{r,m} \end{pmatrix}
$$


这样，六个 Maxwell 演化方程就浓缩成两行。用 SI 单位写


$$
\boxed{ \partial_t\mathbf B_m=-\mathcal C_m\mathbf E_m,\qquad \partial_t\mathbf E_m=c^2\mathcal C_m\mathbf B_m-\frac{\mathbf J_m}{\varepsilon_0} }
$$

### 2.2 Yee网格交错

设径向节点为 \(r_i=i\Delta r\)，纵向节点为 \(z_j=j\Delta z\)。按 Davidson 的布置，用这些位置表示一组 Yee 网格

|    分量    |   径向位置    |   纵向位置    |
| :--------: | :-----------: | :-----------: |
|  \(E_r\)   |    \(r_i\)    |    \(z_j\)    |
| \(E_\phi\) | \(r_{i+1/2}\) |    \(z_j\)    |
|  \(E_z\)   | \(r_{i+1/2}\) | \(z_{j+1/2}\) |
|  \(B_r\)   | \(r_{i+1/2}\) | \(z_{j+1/2}\) |
| \(B_\phi\) |    \(r_i\)    | \(z_{j+1/2}\) |
|  \(B_z\)   |    \(r_i\)    |    \(z_j\)    |

**交错的用处是，旋度里的每一项都自然落在被更新分量的位置上。** 例如更新 \(B_{z,m}\) 时，\(E_{r,m}\) 已经和它共点，而 \(E_{\phi,m}\) 在径向左右两侧各有一个值。因此对 \(i\ge1\)


$$
\begin{aligned} B_{z,m,i,j}^{n+1/2} ={}&B_{z,m,i,j}^{n-1/2}\\ &-\frac{\Delta t}{r_i\Delta r} \left[ r_{i+1/2}E_{\phi,m,i+1/2,j}^{n} -r_{i-1/2}E_{\phi,m,i-1/2,j}^{n} \right]\\ &+\Delta t\,\frac{im}{r_i}E_{r,m,i,j}^{n}
\end{aligned}
$$


上式可以直接对照连续方程。第二行对 **\(rE_\phi\)** 做差再除以 \(r_i\Delta r\)，第三行则在本地取 \(E_r\) 乘以 \(im/r_i\)。角向已经用 Fourier 模处理，因此这里没有 \(\Delta\phi\)，也无需在相邻角度之间做有限差分。 具体哪几个分量正好落在 \(r=0\)，取决于径向交错的原点。论文也指出，其他 RZ 实现的轴线布局可以不同。

### 2.3 时间上的Leapfrog推进

电场放在整数时刻 \(t^n\)，磁场和用于更新电场的电流放在半整数时刻。把空间差分后的旋度记作 \(\mathcal C_m^h\)，一步就是


$$
\begin{aligned} \mathbf B_m^{n+1/2} &=\mathbf B_m^{n-1/2}-\Delta t\,\mathcal C_m^h\mathbf E_m^n,\\[2pt] \mathbf E_m^{n+1} &=\mathbf E_m^n+\Delta t \left(c^2\mathcal C_m^h\mathbf B_m^{n+1/2} -\frac{\mathbf J_m^{n+1/2}}{\varepsilon_0}\right) \end{aligned}
$$


第一行用整数时刻的 \(E\)，把 \(B\) 从前半步推进到后半步。第二行用同一半步的 \(B\) 和 \(J\)，把 \(E\) 推进一个整步。\(m>0\) 的系数可以用复数写，程序也可以分开存其实部和虚部。比如 \(imF_m=im(a+ib)=-mb+ima\)，所以 **\(im\) 在数组里体现为实部和虚部之间的交叉更新**。 [escholarship.org](https://escholarship.org/content/qt98q8g2m6/qt98q8g2m6_noSplash_785b08288f7b5555841da271aa47f446.pdf?utm_source=chatgpt.com)

**模数–时间步**相连属性。\(m\) 越高，近轴格点上的 \(m/r\) 耦合越强，显式 Yee 的稳定时间步可能越小。因此做 \(m=1,5,11\) 的收敛对照时，用能满足最高模 CFL 的统一时间步，才能把时间离散误差和模截断误差分开。 

### 2.4 轴上处理

上面的 \(B_z\) 差分式只写给 \(r_i>0\)。Davidson 在轴上按场的正则性分别处理

- \(\rho,E_z,B_z\) 在轴上只有 \(m=0\) 可以非零。
- \(E_r,E_\phi,B_r,B_\phi\) 在轴上只有 \(m=1\) 可以非零。有限的笛卡尔横向场投影到旋转的圆柱基底，正好产生这一阶角依赖。

**例一，轴上的 \(B_{z,0}\)。** 用法拉第环路积分，取半径 \(a=\Delta r/2\) 的小圆


$$
\pi a^2\,\partial_t B_{z,0} \ \simeq\ -2\pi a\,E_{\phi,0}(a)
$$


除以面积得到 Davidson 的轴上更新所用的系数


$$
\partial_t B_{z,0}(0) \simeq -\frac{4}{\Delta r}E_{\phi,0}(\Delta r/2)
$$


直观上，\(E_{\phi,0}\) 近轴正比于 \(r\)，所以圆周环量和圆盘面积都按 \(r^2\) 缩小，两者之比在轴上仍然有限。

**例二，轴上的 \(E_{r,1}\)。** 安培方程含有 \(iB_{z,1}/r\)。虽然 \(B_{z,1}(0)=0\)，比值仍可有限，因为


$$
\lim_{r\to0}\frac{B_{z,1}(r)}{r} =\partial_rB_{z,1}(0)
$$


在 Davidson 的网格上，可以用第一径向节点处的 \(B_{z,1}(\Delta r)/\Delta r\) 离散这个极限。仅把轴上的 \(B_{z,1}\) 设为零还不够，更新式需要它的径向斜率。 这正是轴线上最容易误读的地方。

### 2.5 完整PIC循环中各个模态如何相互影响

一个时间步可以这样读：

1. **场到粒子。** 在粒子的 \((r_p,z_p)\) 处插值各模，再用粒子的 \(\phi_p\) 重建局部总场，并转成笛卡尔分量。
2. **推进粒子。** 用总场计算洛伦兹力。Davidson 的 OSIRIS 实现用三维笛卡尔位置和动量推进宏粒子。
3. **粒子到场。** 根据粒子在 \(t^n\) 和 \(t^{n+1}\) 的位置变化，把电流沉积到各个模。下一次电场更新使用这些 \(\mathbf J_m^{n+1/2}\)。

所以，**给定电流后，Maxwell 更新逐模独立；自洽 PIC 里，粒子使各模耦合。** 粒子感受到叠加后的总场，一条被 \(m=1\) 激光改变的轨迹，可以在重新沉积时贡献 \(m=0\) 的尾场电流，也可以贡献更高模。计算实际能保留哪些反馈，由所选的 \(m_{\max}\) 决定。

#### 2.5.1 对电流的细致处理

因为粒子就算只绕轴转动、\(r_p,z_p\) 一点没变，**它的 \(m>0\) 电荷系数仍会变**。单个粒子的角向沉积权重含有 \(e^{-im\phi_p}\)。因此，逐模离散连续性方程必须包括方位向电流


$$
\frac{\rho_m^{n+1}-\rho_m^n}{\Delta t} + D_{rz}^h\mathbf J_{rz,m}^{n+1/2} + \frac{im}{r}J_{\phi,m}^{n+1/2}=0
$$


Davidson 的做法是，以已有的 \(m=0\) 守恒轨迹沉积为基础，为 \(r,z\) 电流加入角相位，然后对 \(m>0\) **用这条离散连续性方程求出 \(J_{\phi,m}\)**，补上端点电荷变化和 \(r,z\) 电流散度之间的差额。\(m=0\) 的方位向散度为零，继续沿用轴对称的守恒沉积。

这和 Yee 场推进是配套的。如果离散旋度与散度满足 \(D^h\mathcal C_m^h=0\)，对电场更新取散度，就有


$$
\left(D^h\mathbf E_m-\frac{\rho_m}{\varepsilon_0}\right)^{n+1} = \left(D^h\mathbf E_m-\frac{\rho_m}{\varepsilon_0}\right)^{n}
$$


**也就是说，初始化时满足 Gauss 定律，并且电流沉积满足同一个离散连续性方程，推进就会逐模保持 Gauss 定律。** 这就是 Davidson 的沉积推导为什么与 Yee 网格、轴线处理同样重要。术语上可以把 **RZ** 理解为场的空间表示，把 **Yee** 理解为场的差分与交错推进，而 **电荷守恒沉积**负责让三维粒子轨迹产生与该场推进相容的电流。

### 2.6 其他事项

#### 2.6.1 CFL

准圆柱 RZ 把电磁场展开成角向傅里叶模。对第 \(m\) 模，柱坐标旋度中的角向导数变成


$$
\frac{1}{r}\frac{\partial}{\partial\theta} \;\longrightarrow\; \frac{im}{r}
$$


因此，同一个 \(m\) 在不同半径对应不同的弧长周期


$$
\ell_\theta(r)=\frac{2\pi r}{m}
$$


**越靠近轴，固定 \(m\) 对应的角向尺度越短。** 例如 m11 算例，同一个 \(m=11\) 在 \(r=2\lambda_0\) 处对应约 \(1.14\lambda_0\) 的角向周期，而在第一圈网格中心 \(r=\Delta r/2\) 处，对应约 \(0.013\lambda_0\)。即使只关心 \(r\sim 2\lambda_0\) 处的靶面纹理，靠轴网格仍参与场推进，并可能限制整个盒子共用的时间步。

从离散稳定性看，显式 Yee 推进要求最高频的离散电磁本征模满足 \(\omega_{\max}\Delta t\lesssim 2\)。用靠轴尺度 \(r\sim\Delta r/2\) 估计，角向项给出 \(\omega_{\max}\sim cm/(\Delta r/2)\)，所以在高模数下有


$$
\boxed{\Delta t_{\rm CFL}\sim \frac{\Delta r}{c\,m_{\max}}}
$$


这是尺度估计。实际系数由交错网格、轴上正则条件和径向差分共同决定。轴上有专门处理，不能直接把 \(r=0\) 代入 \(m/r\)。

**WarpX中的RZ CFL处理**

记 \(M=\texttt{warpx.n\_rz\_azimuthal\_modes}\)。它**包含 \(m=0\)**，所以 \(M=m_{\max}+1\)。WarpX 的 `CylindricalYeeAlgorithm::ComputeMaxDt` 使用 [warpx.readthedocs.io](https://warpx.readthedocs.io/en/26.07/_static/doxyhtml/_cylindrical_yee_algorithm_8_h_source.html?utm_source=chatgpt.com)


$$
\boxed{ \Delta t_{\rm CFL} =\frac{1}{c\sqrt{\dfrac{1+\alpha}{\Delta r^2}                         +\dfrac{1}{\Delta z^2}}} }
$$


其中参数 $\alpha$ 

|   最高模 \(m_{\max}\)   |   0    |   1    |   2    |   3    |    4    |    5    |     \(\ge 6\)      |
| :---------------------: | :----: | :----: | :----: | :----: | :-----: | :-----: | :----------------: |
| WarpX 使用的 \(\alpha\) | 0.2105 | 1.0000 | 3.5234 | 8.5104 | 15.5059 | 24.5037 | \(m_{\max}^2-0.4\) |

低阶值来自半解析计算，高阶项是源码采用的外推。高 \(m\) 时，公式就趋近于 \(\Delta r/(cm_{\max})\)。**这条具体公式适用于 WarpX 的 RZ Yee 场求解器**。 [warpx.readthedocs.io](https://warpx.readthedocs.io/en/26.07/_static/doxyhtml/_cylindrical_yee_algorithm_8_h_source.html?utm_source=chatgpt.com)

取 \(\Delta r=\lambda_0/22\)、\(\Delta z=\lambda_0/44\)，其中 \(\lambda_0=1\,\mu\mathrm m\)，\(T_0=\lambda_0/c\)。得到以下 CFL 上限。 [warpx.readthedocs.io](https://warpx.readthedocs.io/en/26.07/_static/doxyhtml/_cylindrical_yee_algorithm_8_h_source.html?utm_source=chatgpt.com)

|   算例    | 最高模 \(m_{\max}\) | CFL 上限 | 已完成对比所用 \(\Delta t\) / 上限 |
| :-------: | :-----------------: | :------: | :--------------------------------: |
| 全 3D Yee |          —          | 61.90 as |     \(58.37/61.90\approx94\%\)     |
|   RZ m1   |          1          | 61.90 as |     \(11.67/61.90\approx19\%\)     |
|   RZ m5   |          5          | 27.91 as |     \(11.67/27.91\approx42\%\)     |
|  RZ m11   |         11          | 13.53 as |     \(11.67/13.53\approx86\%\)     |
|  RZ m23   |         23          | 6.56 as  |                 —                  |
|  RZ m47   |         47          | 3.22 as  |                 —                  |

**m1、m5、m11 都走了 11,250 步，是因为我们主动让三组使用同一个、能满足 m11 CFL 的时间步 \(0.0035T_0\)。** 所以它们的耗时差反映的是同一步数下加模的成本。若各自按 CFL 选步长，m1 和 m5 还有增大时间步的余地。全 3D 那组用了 \(0.0175T_0\)，因此到同一个 \(39.375T_0\) 只计划走 2,250 步。

在 WarpX 输入里，自动选步时 `warpx.cfl` 乘以上述 CFL 上限。**一旦指定 `warpx.const_dt`，它就覆盖 `warpx.cfl`，程序能启动也不能证明时间步稳定。** 我们的 m47 强行压到 5,000 步时设的是 \(26.27\,\mathrm{as}\)，约为源码估计上限的 **8.15 倍**，应当把它视为超 CFL 测试。 











## RZ和全3D PIC的一些对比





## WarpX RZ的一些feature和参数设置



| 参数                                        | 当前值                         | 含义                                                         |
| ------------------------------------------- | ------------------------------ | ------------------------------------------------------------ |
| `geometry.dims`                             | `RZ`                           | 选择准圆柱几何                                               |
| `geometry.prob_lo` / `geometry.prob_hi`     | `0 -81.9e-6` / `74.6e-6 20e-6` | 依次给出 \((r,z)\) 的上下界，单位为米                        |
| `amr.n_cell`                                | `150 4000`                     | 网格顺序是 \((N_r,N_z)\)                                     |
| `warpx.n_rz_azimuthal_modes`                | `2`                            | 保留 \(m=0,1\)                                               |
| `electrons.num_particles_per_cell_each_dim` | `1 16 2`                       | 粒子采样顺序是 \((r,\theta,z)\)，即每个 \(r\!-\!z\) 网格单元布置 \(1\times16\times2=32\) 个电子宏粒子 |
| `boundary.field_lo`                         | `none pec`                     | 第一项对应 \(r=0\) 的轴线处理，第二项对应纵向下边界          |
| `fields.dump_rz_modes`                      | `1`                            | 在这份 `plotfile` 输出中保存各模，便于重建 \(E_x\) 或指定方位角的截面 |



### 模块搭配事项

`RZ` 几何下 `Yee` 求解器不支持 `pml` 场边界。







