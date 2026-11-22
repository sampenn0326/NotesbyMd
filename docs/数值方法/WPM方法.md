# WPM方法



## 1. 从理论推导积基本形式

### 1.1 均匀介质中的时域波动方程

在均匀、无自由电荷、无外加电流的线性非磁化介质中，Maxwell方程写为



$$
\nabla \times \vec{E} = -\mu _0 \frac{\partial \vec{H}}{\partial t}, \quad \nabla \times \vec{H} =\frac{\partial \vec{D}}{\partial t}
$$



首先考虑无色散介质，即



$$
\vec{D} =\varepsilon \vec{E},\quad \varepsilon = \varepsilon _0 n^2
$$



考虑到均匀介质中



$$
\nabla \cdot \vec{D}=0,\quad \nabla \cdot \vec{E}=0
$$



所以波动方程可以写为



$$
\nabla ^2 \vec{E}-\mu _0 \varepsilon \frac{\partial ^2 \vec{E}}{\partial t^2 }=0  \quad\text{or}\quad  \nabla ^2 \vec{E}-\frac{n^2}{c^2} \frac{\partial ^2 \vec{E}}{\partial t^2 }=0 
$$



在均匀介质中，每个笛卡尔电场分量都满足这个方程，所以可以用标量 $E$ 为代表推导传播公式，它可以是任意一个分量。

### 1.2 固定频率的Helmholtz方程

采用时间约定



$$
E(x,z,t)=\mathrm{Re} [u(x,z;\omega)e^{-i \omega t}]
$$



其中 $u$ 是完整的单频复振幅，将以上带入波动方程，得到



$$
\nabla ^2 u +\frac{n^2 \omega ^2}{c^2}u=0
$$



定义 $k_0 = \omega /c$ ，在二维 $x-z$ 情况下，上式改写为



$$
\frac{\partial ^2 u}{\partial x^2 }+\frac{\partial ^2 u}{\partial z^2 }+n^2 k_0 ^2 u =0 \tag{1}
$$



这就是2D单频情况下要解的Helmholtz方程（当说二维时，本质上是说一切物理量不随着 $y$ 方向变化）。到此为止没有引入近轴近似或者缓变假设等，但所基于的**介质确实是均匀的**。

### 1.3 对横向 $x$ 做Fourier变换

做Fourier变换的动机是：导数会在Fourier空间写为乘法，所以可以简化偏微分方程。定义横向Fourier变换



$$
\hat{u}(k_x,z) = \int _{-\infty}^{\infty} u(x,z)e^{-ik_xx}\mathrm{d}x
$$



其逆变换为



$$
u(x,z)=\frac{1}{2\pi} \int _{-\infty}^{\infty} \hat{u}(k_x,z) e^{ik_x x}\mathrm{d}k_x \tag{2}
$$



对于(2)式，其物理含义是：一个横向光场，可以表示为许多 $e^{ik_xx}$ 分量的叠加，每个 $k_x$ 对应一种横向振荡速度，对于 $u(x,z)$ 来说，也对应一种传播倾角。

导数的Fourier变换，当然有



$$
\mathcal{F} _x \left[ \frac{\partial u}{\partial x} \right] = ik_x \hat{u},\qquad \mathcal{F} _x \left[ \frac{\partial^2 u}{\partial x^2} \right] = -k_x^2 \hat{u}\tag{3}
$$



 $\mathcal{F}_x$ 不改变 $z$ 导数。因此，(1)式的Fourier变换为



$$
-k_x ^2 \hat{u} +\frac{\partial ^2 \hat{u}}{\partial z^2}+ n^2 k_0 ^2 \hat{u}=0 
$$

即



$$
\frac{\partial ^2 \hat{u}}{\partial z^2}+ \left( n^2 k_0 ^2 -k_x^2\right)\hat{u}=0 \tag{4}
$$



此时，原来的二维偏微分方程，改写为了对每一个 $k_x$ ，各自求解一个关于 $z$ 的常系数二阶微分方程。

### 1.4 求解每个角谱分量的纵向演化

定义纵向波数



$$
k_z(k_x;\omega) = \sqrt{n^2 k_0 ^2 -k_x ^2}\tag{5}
$$



则(4)式改写为



$$
\frac{\partial ^2 \hat{u}}{\partial z^2}+k_z^2  \hat{u}=0
$$



它的一般解为



$$
\hat {u}(k_x ,z) = a(k_x)e^{ik_zz} +b(k_x)e^{-ik_zz} \tag{6}
$$



两个分量分别代表沿着 $+z$ 方向和 $-z$ 方向传播的波，这是因为：如果补上时间因子，则第一项的相位就是 $k_zz -\omega t$ ，它的相速度为正。这里其实也揭示一个重要事实

> Helmholtz方程本身同时包含正向波和反向波，当使用基本传播公式时，需要额外指定正向传播的条件。

### 1.5 施加单向条件，得到传播因子

设所研究区域中只有沿 $+z$ 传播的场，即 $b(k_x) =0$ ，则



$$
\hat {u}(k_x ,z) = a(k_x)e^{ik_zz} 
$$



传播到 $z+\Delta z$ 后，则



$$
\hat{u} (k_x ,z+\Delta z) = a(k_x)e^{ik_z (z+\Delta z)} = a(k_x)e^{ik_zz}e^{ik_z\Delta z}
$$



因此



$$
\hat{u}(k_x ,z+\Delta z)=\hat{u}(k_x,z)e^{ik_z \Delta z} \tag{7}
$$



定义传播函数



$$
H(k_x;\Delta z,\omega ) = \exp \left[ i\Delta z\sqrt{n^2k_0^2 -k_x^2} \right] \tag{8}
$$



于是



$$
\hat {u}(z+\Delta z)=H \hat{u}(z)
$$

### 1.6 逆Fourier变换，回到位置空间

对(7)式做逆变换



$$
u(x,z+\Delta z)=\frac{1}{2\pi}\int _{-\infty}^{\infty}\hat{u}(k_x,z)e^{ik_z\Delta z}e^{ik_xx}\mathrm{d}k_x
$$



其中



$$
\hat{u}(k_x,z)=\mathcal{F}_x[u(x,z)]
$$



所以



$$
\boxed{u(x,z+\Delta z)=\mathcal{F}^{-1}_x\left[ e^{i\Delta z \sqrt{n^2 k_0^2-k_x^2}}\mathcal{F}_x[u(x,z)] \right]}\tag{9}
$$



这就是基本传播形式。

再次概括基本过程就是：(1)将横向光场分解为不同倾角的平面波；(2)让每个平面波累积各自的传播相位；(3)将所有分量相干叠加，得到新平面的光场。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

所谓”将横向光场分解为不同倾角的平面波“，可以理解为，在特定 $z_1$ 截面，当然存在横向电场分布 $u_1(x)$， 认为这个 $u_1(x)$ 是具有不同 $\hat {k}$ 朝向的平面波，以不同强度、不同相位相干叠加而成。



## 2. 常见问题

### 2.0 非均匀介质的处理

推导得出基本传播形式 (9) 时，有一个假设是均匀介质。因此即便 (9) 式中显式包含着 $n$ ，也未必可以直接把非均匀介质 $n(x,z)$ 带入其中。关键在于，当介质均匀，推导时 \(n\) 是一个可以移出横向 Fourier 变换的常数；一旦 \(n\) 随 \(x\) 变化，各个 \(k_x\) 分量就会耦合。

**非均匀介质的差别**

先假定标量 Helmholtz 方程成立，并固定频率


$$
\partial_z^2u+\partial_x^2u+k_0^2 n^2(x,z)u=0
$$


例如，在二维 \(x\)-\(z\) 几何中，若电场只有 \(E_y\) 分量、\(\partial_y=0\)、磁导率恒定，那么这个标量方程对 \(E_y\) 成立，包括介电常数随 \(x,z\) 改变的情形。对于一般偏振，均匀介质中“任取一个笛卡尔分量”的结论需要重新检查。

对 \(x\) 做 Fourier 变换


$$
\partial_z^2\hat u-k_x^2\hat u+ k_0^2\mathcal F_x[n^2u]=0
$$


如果 \(n\) 横向均匀，最后一项就是 \(k_0^2n^2\hat u\)。如果 \(n=n(x,z)\)，则（乘积的 $\mathcal{F}$ 等于 $\mathcal{F}$ 后的卷积）


$$
\mathcal F_x[n^2u](k_x,z) =\frac{1}{2\pi}\int \widehat{n^2}(k_x-q,z)\,\hat u(q,z)\,\mathrm dq
$$


这一步直接说明了差别。某个 \(q\) 分量可以经由介质的横向空间频率 \(K\) 耦合到 \(k_x=q+K\)。所以，之前“**每个 \(k_x\) 各自求解一个二阶常系数方程**”的结论，在横向非均匀介质里就失效了。式 (9) 根号里的 \(n\) 可以取任何给定的**均匀介质折射率**，但它在推导中始终是参数。

**WPM方法如何用传播核**

当前平面为 \(z_j\)，输出点为 $z_{j+1},x_i$。一种常见的 WPM 写法是，计算 \(z_{j+1}\) 层的第 \(i\) 个点 \(x_i\) 时，就用


$$
n_{j+1,i}=n(x_i,z_{j+1})
$$


来选传播核，并用 \(z_j\) 层的**整个横向场**作为输入。具体来说，先对 \(u(x,z_j)\) 做一次 Fourier 变换，得到 \(\hat u_j(k_x)\)。然后计算


$$
u(x_i,z_{j+1})\approx \frac{1}{2\pi}\int \hat u_j(k_x)\, \exp\!\left[i\Delta z\sqrt{k_0^2n_{j+1,i}^2-k_x^2}\right] e^{ik_xx_i}\,\mathrm dk_x
$$


算第 \(i+1\) 个点时，沿用同一份 \(\hat u_j(k_x)\)，把传播核里的折射率换成 \(n_{j+1,i+1}\)，并在 \(x_{i+1}\) 处求值；也可以在步长中点 \(z_j+\Delta z/2\) 取 \(n(x_i,z_j+\Delta z/2)\)。总之，**折射率按输出点取，入射场按整个横截面取**。

可以这样理解这条式子：

1. 对当前平面的**整个横向场**做 Fourier 变换，得到 \(\hat u(k_x,z_j)\) ；
2. 为求下一平面某个点 \(x_o\) 的场，用该点对应的折射率 \(n_{j+1}(x_o)\) 构造一个均匀介质传播核；
3. 用这个核传播整个角谱，只取输出点 \(x_o\) 处的值。另一个输出点的局部折射率不同，就使用另一个核。

所以，“局部”指的是**每个输出点怎样选传播核**。每个点的结果仍然由整个输入横截面共同决定。由于传播核随输出位置变化，重新对输出场做 Fourier 变换后，角谱一般也会发生变化。WPM 因此可以描述折射、聚焦等横向场重分布，但它给出的是对真实耦合的近似。**虽然保留完整的平方根避免了对传播角做近轴展开，但局部均匀化仍然是一个独立的近似。**

### 2.1 平方根色散关系

在均匀、无损介质中，波矢 $|\vec{k}| = nk_0 $ ，二维情况下


$$
\vec{k}=(k_x,k_y),\qquad k_x ^2 +k_y^2 =n^2 k_0^2
$$


此时


$$
k_z = \sqrt{n^2 k_0^2-k_x^2}
$$


若平面波与 $+z$ 轴的夹角是 $\theta$ ，则


$$
k_x =k_0 n \sin \theta, \quad k_z =k_0n \cos \theta 
$$


此时传播因子也可以写成


$$
H= e^{ink_0\cos \theta  \Delta z}
$$


不同倾角的平面波，在两个固定 $z$ 平面之间获得不同的相位增量，重新叠加后，横向强度分布就可能发生变化。

### 2.2 传播分量、倏逝分量

一般取 $n$ 为正实数，则如果 $|k_x| <nk_0$，则 $k_z$ 为实数，$H=e^{ik_z \Delta z}$ 对应能够沿 $+z$ 传播的平面波；当 $|k_x| >nk_0$ ，令 $\alpha =\sqrt{k_x^2 -n^2 k_0^2}$ ，则物理解应该选


$$
k_z=i \alpha
$$


因此 $H = e^{i(i\alpha)}\Delta z = e^{-\alpha \Delta z}$ ，它随传播距离衰减，是倏逝分量。对于复折射率


$$
\tilde{n}=n+i\kappa
$$


同样要选取符合被动介质衰减条件的分支。

### 2.3 Fresnel传播公式

基本公式保留了完整平方根，若传播角度小，即 $|k_x|/nk_0\ll 1$，可以展开


$$
k_z= nk_0 \sqrt{1-k_x^2/(n^2 k_0^2)}\approx nk_0 -\frac{k_x^2}{2nk_0}
$$


此时


$$
H \approx e^{ink_0}\exp\left[ -i \frac{k_x^2}{2nk_0}\Delta z \right]
$$


其中 $\exp[ink_0]$ 是所有横向分量共有的载波相位。定义去掉改载波的场


$$
A(x,z)=u(x,z)e^{-ink_0z}
$$


就得到该场的演化


$$
A(x,z+\Delta z)= \mathcal{F}_x^{-1}[e^{-ik_x^2 \Delta z/(2nk_0)}\mathcal{F}_x[A(x,z)]]
$$


这就是近轴Fresnel传播的频域公式。



## 3. WPM的RZ形式

从Maxwell方程组到 RZ WPM 形式，有两处物理近似：**一是把矢量电磁场近似为一个标量振幅，二是在纵向只保留前向传播。** 在这两步之间，冷等离子体的线性电流响应给出 \(-\omega_p^2/c^2\) 项。

### 3.1 麦克斯韦方程 + 冷电子响应

设离子固定，背景电子密度 \(n_e(r,z)\) 已知。做线性化，电子速度 \(\mathbf v_e\) 满足


$$
m_e\partial_t\mathbf v_e=-e\mathbf E, \qquad \mathbf J=-en_e\mathbf v_e
$$


由于背景密度不随时间变，


$$
\partial_t\mathbf J =\frac{n_e e^2}{m_e}\mathbf E =\varepsilon_0\omega_p^2(r,z)\mathbf E, \qquad \omega_p^2(r,z)=\frac{n_e(r,z)e^2}{\varepsilon_0m_e}
$$


再用法拉第定律和安培–麦克斯韦定律，


$$
\nabla\times\mathbf E=-\partial_t\mathbf B, \qquad \nabla\times\mathbf B=\mu_0\mathbf J+\frac{1}{c^2}\partial_t\mathbf E
$$


对第一式取旋度，代入第二式和电子电流响应，得到


$$
\nabla\times\nabla\times\mathbf E +\frac{1}{c^2}\partial_t^2\mathbf E +\frac{\omega_p^2(r,z)}{c^2}\mathbf E=0
$$


这一步仍然是矢量方程。取时间约定 \(e^{-i\omega t}\)，就有


$$
\nabla\times\nabla\times\mathbf E_\omega =\underbrace{\frac{\omega^2-\omega_p^2(r,z)}{c^2}}_{k^2\varepsilon_r(r,z,\omega)} \mathbf E_\omega, \qquad \varepsilon_r=1-\frac{\omega_p^2}{\omega^2}
$$


对给定频率，密度越高，局部折射率越低。如果密度从轴向外升高，轴心折射率较高，则通道具有聚焦作用。

### 3.2 从矢量方程到 RZ 标量方程

用恒等式 \(\nabla\times\nabla\times\mathbf E=\nabla(\nabla\cdot\mathbf E)-\nabla^2\mathbf E\)，可把频域方程写成


$$
\big(\nabla^2+k^2\varepsilon_r\big)\mathbf E_\omega =\nabla(\nabla\cdot\mathbf E_\omega)
$$


这里容易跳过一步。高斯定律在线性介质形式下给出 \(\nabla\cdot(\varepsilon_r\mathbf E_\omega)=0\)。在非均匀等离子体中，\(\varepsilon_r\) 随空间变化，因此一般仍有


$$
\nabla\cdot\mathbf E_\omega =-\frac{\nabla\varepsilon_r\cdot\mathbf E_\omega}{\varepsilon_r}
$$


（在 \(\varepsilon_r\ne 0\) 的区域）。视参数条件有时可省略矢量方程右侧这一项。进一步，一些情况下可以用 \(U_\omega(r,z)\) 表示主横向偏振的标量振幅， 例如，线偏振光束可以具有轴对称的振幅分布，但电场偏振仍沿固定的笛卡尔方向。

对这个标量振幅取 \(\partial_\phi U_\omega=0\)，便得到


$$
\boxed{ \left[ \partial_z^2 +\frac{1}{r}\partial_r(r\partial_r) +k^2-\frac{\omega_p^2(r,z)}{c^2} \right]U_\omega=0} 
$$


这里的 \(r^{-1}\partial_r(r\partial_r)\) 就是圆形光束的径向衍射算符。

### 3.3 从二阶波动方程到前向模态传播

把密度沿 \(z\) 分层，每层内保留完整的径向密度分布。对第 \(j\) 层定义


$$
Q_j=\frac{1}{r}\partial_r(r\partial_r) -\frac{\omega_{p,j}^2(r)}{c^2}
$$

如果某个径向场型 \(\phi_m\) 满足 \(Q_j\phi_m=\lambda_m\phi_m\)，那么把 \(U_\omega=a_m(z)\phi_m(r)\) 代入上式，就只剩下

$$
a_m''+(k^2+\lambda_m)a_m=0
$$


平方根在这一步出现。 对传播模态，二阶方程给出沿 \(+z\) 和 \(-z\) 的两支解 \(e^{\pm i k_{z,m}z}\)，其中 \(k_{z,m}=\sqrt{k^2+\lambda_m}\)。脚本保留 \(+z\) 支。若 \(k^2+\lambda_m<0\)，则取 \(\operatorname{Im}k_{z,m}>0\)，使该模态向下游衰减。

再写成 \(U_\omega=e^{ikz}u_\omega\)，剥离真空传播相位，代码中每个模态在层内走过距离 \(d\) 的更新就变成


$$
\boxed{ a_{m,\mathrm{out}}^{(u)} =a_{m,\mathrm{in}}^{(u)} \exp\!\left[i\left(\sqrt{k^2+\lambda_m}-k\right)d\right] }
$$


**层内**，这个指数是离散标量方程对应模态的传播解，所以均匀平台可以一次推进。**换层时**，代码把上一层出口的横向场投影到下一层的本征基底，继续前向推进。这一步只传递横向场，没有同时匹配 \(U_\omega\) 和 \(\partial_z U_\omega\) 来求反射。因此，保留完整平方根改善的是**层内的纵向色散关系**，界面反射仍由单向近似省略。

最后，静态等离子体允许各频率独立传播。求解器算出每个频率的 \(u_\omega(r,z)\)，Notebook 再乘上含啁啾的入射谱 \(S_\eta(\omega)\)，按 \(e^{-i(\omega-\omega_0)(t-z/c)}\) 相干叠加。这就把麦克斯韦方程中的**电子电流响应**，一路连到了时空图中的**飞行焦点强度峰**。

> 以上相当于对 $U_{\omega}$ 进行了分离变量，而且要求径向函数满足本征方程，这就仅凭算符 $Q_j$ 一下求出了径向部分 $\phi _m$ 和对应的本征值 $\lambda _m$ ，进而可以拿去求解系数，或者纵向部分需要满足的条件。这么做的依据在哪里，可以有几个角度：
>
> A. 从问题本身来说
>
> 在第 \(j\) 层内，把等离子体密度近似为 \(n_{e,j}(r)\)。也就是说，这一层的密度可以沿 \(r\) 非均匀，但每个 \(z\) 截面具有相同的径向密度剖面。固定频率后，标量波动方程写成
>
> 
> $$
> \left[\partial_z^2+Q_j+k^2\right]U_\omega(r,z)=0, \qquad Q_j= \frac{1}{r}\partial_r(r\partial_r) -\frac{\omega_{p,j}^2(r)}{c^2}
> $$
> 
>
> 因为 \(Q_j\) 不随 \(z\) 改变，纵向因子 \(e^{i\beta z}\) 在方程的各项作用下都保持原样。对 \(z\) 求二阶导数只会乘上 \(-\beta^2\)，而 \(Q_j\) 只作用于径向场型。因此，可以逐个寻找具有单一纵向波数 \(\beta\) 的解，
>
> 
> $$
> U_\omega(r,z)=\phi(r)e^{i\beta z}
> $$
> 
>
> 它的物理含义是，沿 \(z\) 前进距离 \(d\) 时，整个横截面的复场都乘上同一个因子 \(e^{i\beta d}\)。对于实数 \(\beta\)，各处只积累同样的相位，径向场型保持不变。把上式代回波动方程并消去 \(e^{i\beta z}\)，得到
>
> 
> $$
> -\beta^2\phi(r)+Q_j\phi(r)+k^2\phi(r)=0
> $$
> 
>
> 也就是
>
> 
> $$
>  \boxed{Q_j\phi(r)=(\beta^2-k^2)\phi(r)} 
> $$
> 
>
> 这里就出现了本征方程。**我们选定的是“寻找具有单一 \(\beta\) 的解”，由此推出来的是“径向场型必须满足本征方程”。** 因为纵向导数项和 \(k^2\) 项都与原场型 \(\phi(r)\) 成比例，所以径向衍射与密度项合起来也必须与同一个 \(\phi(r)\) 成比例，方程才能在每个 \(r\) 上成立。
>
> 结合轴上的正则条件和外侧径向边界条件，就可以求出允许的场型 \(\phi_m\) 和本征值 \(\lambda_m\)，
>
> 
> $$
> Q_j\phi_m=\lambda_m\phi_m, \qquad \beta_m^2=k^2+\lambda_m
> $$
> 
>
> B. 从数学上来说
>
> <u>在有限径向计算区间上，取常用的自伴边界条件时，\(Q_j\) 的本征模构成一组完备基。</u>因此，一般输入场可以写成
>
> 
> $$
> U_\omega(r,z)=\sum_m a_m(z)\phi_m(r)
> $$
> 
>
> 代回原方程后，每个模态的系数独立满足
>
> 
> $$
> a_m''(z)+(k^2+\lambda_m)a_m(z)=0
> $$
> 
>
> 这一步仍然保留二阶方程的两支解。随后选取 \(+z\) 传播支，才得到每个传播模态乘上 \(e^{i\beta_m d}\) 的单向推进公式。单个模态保持自己的径向形状，多个模态却会因积累不同的相位而改变叠加后的总场形状。
>
> 这和前面均匀介质里用 Fourier 平面波展开是同一个思路。均匀介质里的 \(e^{ik_xx}\) 是横向算符的本征函数。这里的横向算符还包含径向密度分布，因此用**由这一层介质剖面和径向边界共同决定的本征模**来展开。

### 3.4 实际进入程序的离散格式



























## 3. 一个实例





```python
"""80 eV 单色 XUV 光束通过 200 mbar 氢等离子体毛细管的独立 WPM 算例。

本文件可独立运行，不依赖其他项目脚本。依赖：numpy、matplotlib。
运行：python wpm_hydrogen_capillary_200mbar_80eV_zh.py
输出：脚本同目录下的 wpm_hydrogen_capillary_200mbar_80eV.png

物理模型来源与边界
------------------
1. 论文补充材料 S7 给出毛细管放电等离子体的径向密度模型：
       n_e(r) = n_e0 [1 + 0.33 (r/r_ch)^2],
       n_e0 = 0.7364 n_a。
   初始氢气压力通过理想气体状态方程换算为原子氢密度 n_a。氢分子完全
   电离时，每个 H2 分子提供两个电子，因此 n_a = 2 P/(k_B T)。
2. 自由电子等离子体的折射率采用 n = sqrt(1 - n_e/n_c)，其中
       n_c = epsilon_0 m_e omega^2/e^2。
   本例不加入碰撞吸收；管壁仍采用 S8 给出的复折射率 0.966+i*0.0413。
3. S8 说明“等离子体与毛细管壁的交界区域”使用 apodizing function 平滑，
   以减少计算伪影，但没有在文中给出平滑函数的具体解析式及宽度。因此，
   本脚本用可调的余弦 smoothstep，在壁芯界面附近平滑混合等离子体折射率
   与管壁折射率。默认宽度 5 µm 是本算例的数值设定，不是论文报告值。
4. 模型沿横向使用一维平面坐标 x，并令 r=|x|。这是论文 S8 的二维
   (transverse, z) 标量 WPM 表述；它不是轴对称 Hankel 求解，也不是全矢量
   Maxwell 求解。计算域在毛细管前后均为真空。
5. 入射高斯束参数在论文补充材料中没有明确数值。下面 w0=100 µm、束腰
   位于 z=-6 cm 是示例设定，便于和前一个真空毛细管脚本保持可比；用户可
   在参数区修改。这里的 w0 指 1/e 电场半径（等价于 1/e^2 强度半径）。
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# 一、物理参数（SI 单位或变量名所标示的单位）
# =============================================================================

PHOTON_ENERGY_EV = 80             # 单色光子能量，eV
HYDROGEN_PRESSURE_MBAR = 200.0      # 毛细管初始氢气压强，mbar
GAS_TEMPERATURE_K = 295.0           # 补充材料理想气体换算所用温度，K

# 全局纵向坐标。原文 S8 的示意计算域为毛细管前后延伸的真空区，
# 当前项目采用 z=-6 至 55 cm，毛细管本身 z=-5 至 5 cm。
Z_START_CM = -6.0
Z_END_CM = 60.0
CAPILLARY_START_CM = -5.0
CAPILLARY_END_CM = 5.0

# 几何尺寸：300 µm 通道直径；管壁厚度 50 µm 是模型设定。
CAPILLARY_INNER_RADIUS_UM = 150.0
CAPILLARY_OUTER_RADIUS_UM = 200.0

# 论文 S8 给出的管壁复折射率。采用 exp[i(kz-ωt)] 约定，
# Im(n)>0 会使传播因子 exp(i k n z) 振幅衰减。
WALL_N_REAL = 0.966
WALL_KAPPA = 0.0413

# 管芯与管壁交界的数值平滑带宽。S8 只说明用了 apodizing function，
# 没有报告函数形式/带宽；这里将余弦平滑的全宽设为 5 µm，且需做敏感性
# 检查（例如 2、5、10 µm），确认预测焦斑不依赖这个数值参数。
INTERFACE_SMOOTH_WIDTH_UM = 5.0

# 入射束参数：S3 给出了高斯束形式，但这里使用的具体数值是示例输入。
INPUT_WAIST_UM = 100.0              # 束腰半径 w0，µm
WAIST_Z_CM = -5.0                   # 束腰位置，全局 z 坐标，cm


# =============================================================================
# 二、数值参数
# =============================================================================

DX_UM = 1.0                         # 横向网格间距，µm
DZ_UM = 50.0                        # 纵向传播步长，µm
X_MAX_UM = 500.0                    # 横向半宽，µm
SAVE_EVERY_STEPS = 5                # 每隔多少个传播步保存一帧

# 画图设置。强度以入射峰值归一化；统一色标上限 1.1，便于与原文比较。
INTENSITY_VMIN = 0.0
INTENSITY_VMAX = 4.2

# 折射率图显示 (1-Re(n))*1e6。取 0.75--1.25 的窗口突出等离子体剖面；
# 真实真空值为 0、管壁值由复折射率给出，均不做绘图掩膜或替换。
INDEX_DECREMENT_VMIN = 0.75
INDEX_DECREMENT_VMAX = 1.25

# SI 常数
C = 299_792_458.0
H_PLANCK = 6.626_070_15e-34
E_CHARGE = 1.602_176_634e-19
EPSILON_0 = 8.854_187_8128e-12
M_E = 9.109_383_7015e-31
K_B = 1.380_649e-23


def calculate_plasma_parameters(wavelength_m: float) -> dict[str, float]:
    """由 200 mbar 氢气计算原子密度、电子密度和临界密度。

    论文使用初始原子氢密度 n_a；对分子氢气，n_a 是氢原子数密度，
    因此理想气体分子数密度要乘 2。随后假设氢近乎完全电离。
    """
    pressure_pa = HYDROGEN_PRESSURE_MBAR * 100.0  # 1 mbar = 100 Pa
    n_h2 = pressure_pa / (K_B * GAS_TEMPERATURE_K)
    n_atomic = 2.0 * n_h2
    n_e_axis = 0.7364 * n_atomic

    omega = 2.0 * np.pi * C / wavelength_m
    n_critical = EPSILON_0 * M_E * omega**2 / E_CHARGE**2
    n_e_edge = n_e_axis * (1.0 + 0.33)
    n_index_axis = np.sqrt(1.0 - n_e_axis / n_critical)
    n_index_edge = np.sqrt(1.0 - n_e_edge / n_critical)

    return {
        "pressure_pa": pressure_pa,
        "n_h2_m3": n_h2,
        "n_atomic_m3": n_atomic,
        "n_e_axis_m3": n_e_axis,
        "n_e_edge_m3": n_e_edge,
        "n_critical_m3": n_critical,
        "n_index_axis": n_index_axis,
        "n_index_edge": n_index_edge,
    }


def plasma_electron_density(r_m: np.ndarray, n_e_axis_m3: float) -> np.ndarray:
    """论文 S7 的径向电子密度。r_m 是距轴线的径向距离。"""
    r_ch_m = CAPILLARY_INNER_RADIUS_UM * 1e-6
    # S7 把密度剖面定义在通道半径范围内。为界面混合区提供连续的边界值，
    # 将 r 截断在 r_ch；进入管壁后不再把抛物线向外延伸。
    r_limited = np.minimum(np.abs(r_m), r_ch_m)
    return n_e_axis_m3 * (1.0 + 0.33 * (r_limited / r_ch_m) ** 2)


def cosine_smoothstep(value: np.ndarray) -> np.ndarray:
    """把 0..1 的数组平滑映射到 0..1，且两端一阶导数为零。"""
    clipped = np.clip(value, 0.0, 1.0)
    return 0.5 - 0.5 * np.cos(np.pi * clipped)


def make_refractive_index_profile(
    x_m: np.ndarray,
    wavelength_m: float,
    plasma_parameters: dict[str, float],
) -> np.ndarray:
    """构造毛细管横截面的复折射率 n(x)。

    区域顺序：轴上等离子体 → 平滑过渡带 → 吸收管壁 → 管外真空。
    过渡带中心位于 r=r_ch；宽度由 INTERFACE_SMOOTH_WIDTH_UM 控制。
    平滑权重 0 表示纯等离子体，权重 1 表示纯管壁。
    """
    r_m = np.abs(x_m)
    n_e_axis = plasma_parameters["n_e_axis_m3"]
    n_critical = plasma_parameters["n_critical_m3"]

    n_e = plasma_electron_density(r_m, n_e_axis)
    # 碰撞less、冷等离子体折射率。这里给定压力下 ne << nc，根号为实数。
    n_plasma = np.sqrt(np.maximum(1.0 - n_e / n_critical, 0.0)).astype(
        np.complex128
    )

    n_x = np.ones_like(x_m, dtype=np.complex128)  # 默认管外真空
    r_inner = CAPILLARY_INNER_RADIUS_UM * 1e-6
    r_outer = CAPILLARY_OUTER_RADIUS_UM * 1e-6
    smooth_width = INTERFACE_SMOOTH_WIDTH_UM * 1e-6

    # 平滑带限制在管芯与管壁交界处，且不超过可用管壁厚度。
    half_width = min(0.5 * smooth_width, 0.5 * (r_outer - r_inner))
    r_blend_start = r_inner - half_width
    r_blend_end = r_inner + half_width

    # 纯等离子体区域（进入过渡带前）。
    plasma_mask = r_m < r_blend_start
    n_x[plasma_mask] = n_plasma[plasma_mask]

    # 界面 apodization：以余弦 smoothstep 混合复折射率。
    # 该具体函数和带宽是本脚本的数值实现选择，并非原文明确规定的形式。
    blend_mask = (r_m >= r_blend_start) & (r_m <= r_blend_end)
    t = (r_m[blend_mask] - r_blend_start) / (r_blend_end - r_blend_start)
    wall_weight = cosine_smoothstep(t)
    n_wall = WALL_N_REAL + 1j * WALL_KAPPA
    n_x[blend_mask] = (
        (1.0 - wall_weight) * n_plasma[blend_mask]
        + wall_weight * n_wall
    )

    # 过渡带外、外半径以内是均匀复折射率管壁；管壁外仍为真空。
    wall_mask = (r_m > r_blend_end) & (r_m <= r_outer)
    n_x[wall_mask] = n_wall
    return n_x


def gaussian_input_field(
    x_m: np.ndarray,
    wavelength_m: float,
    z_start_cm: float,
) -> np.ndarray:
    """按高斯束复振幅生成 z=z_start 的入射场（已去除载波 exp(i k0 z)）。"""
    w0 = INPUT_WAIST_UM * 1e-6
    z_waist_m = WAIST_Z_CM * 1e-2
    z_input_from_waist = z_start_cm * 1e-2 - z_waist_m
    k0 = 2.0 * np.pi / wavelength_m
    z_rayleigh = np.pi * w0**2 / wavelength_m

    w_z = w0 * np.sqrt(1.0 + (z_input_from_waist / z_rayleigh) ** 2)
    if abs(z_input_from_waist) < 1e-30:
        radius_curvature = np.inf
    else:
        radius_curvature = z_input_from_waist * (
            1.0 + (z_rayleigh / z_input_from_waist) ** 2
        )
    gouy_phase = np.arctan2(z_input_from_waist, z_rayleigh)

    field = ((w0 / w_z) * np.exp(-(x_m / w_z) ** 2)).astype(np.complex128)
    if np.isfinite(radius_curvature):
        field *= np.exp(-1j * k0 * x_m**2 / (2.0 * radius_curvature))
    field *= np.exp(1j * gouy_phase)
    return field


def angular_spectrum_step(
    field: np.ndarray,
    dz_m: float,
    k0: float,
    kx_rad_m: np.ndarray,
) -> np.ndarray:
    """真空单向角谱推进，使用精确平方根 kz=sqrt(k0^2-kx^2)。

    先提取光学载波，故只乘 exp[i(kz-k0)dz]，使输出仍为去载波包络。
    |kx|>k0 的分量由复平方根自然成为倏逝衰减分量。
    """
    kz = np.sqrt((k0**2 - kx_rad_m**2).astype(np.complex128))
    spectrum = np.fft.fft(field)
    spectrum *= np.exp(1j * (kz - k0) * dz_m)
    return np.fft.ifft(spectrum)


def propagate_wpm():
    """执行对称分步 WPM，并返回强度图和折射率剖面。"""
    photon_energy_j = PHOTON_ENERGY_EV * E_CHARGE
    wavelength_m = H_PLANCK * C / photon_energy_j
    k0 = 2.0 * np.pi / wavelength_m

    # 坐标统一转为米，以免在传播相位中混用单位。
    x_max_m = X_MAX_UM * 1e-6
    dx_requested_m = DX_UM * 1e-6
    dz_requested_m = DZ_UM * 1e-6
    z_start_m = Z_START_CM * 1e-2
    z_end_m = Z_END_CM * 1e-2
    cap_start_m = CAPILLARY_START_CM * 1e-2
    cap_end_m = CAPILLARY_END_CM * 1e-2

    # 奇数网格保证 x=0 正好落在网格点上。
    nx = int(round(2.0 * x_max_m / dx_requested_m)) + 1
    x_m = np.linspace(-x_max_m, x_max_m, nx)
    dx_m = x_m[1] - x_m[0]
    kx = 2.0 * np.pi * np.fft.fftfreq(nx, d=dx_m)

    # 调整步数，使计算域两端恰好落在 z 网格上。
    total_length_m = z_end_m - z_start_m
    n_steps = int(round(total_length_m / dz_requested_m))
    dz_m = total_length_m / n_steps
    cap_start_index_float = (cap_start_m - z_start_m) / dz_m
    cap_end_index_float = (cap_end_m - z_start_m) / dz_m
    cap_start_index = int(round(cap_start_index_float))
    cap_end_index = int(round(cap_end_index_float))
    if not (
        np.isclose(cap_start_index_float, cap_start_index, atol=1e-9)
        and np.isclose(cap_end_index_float, cap_end_index, atol=1e-9)
    ):
        raise ValueError(
            "当前 dz 未使毛细管入口/出口落在纵向网格上；请调整 DZ_UM。"
        )

    z_m = z_start_m + np.arange(n_steps + 1) * dz_m
    plasma_parameters = calculate_plasma_parameters(wavelength_m)
    n_x = make_refractive_index_profile(x_m, wavelength_m, plasma_parameters)

    # 对局部折射率项作 Strang 对称分裂：每步前后各施加 dz/2，
    # 中间再做一次精确真空角谱传播。传播只在毛细管纵向范围内含 n(x)。
    index_phase_half = np.exp(1j * k0 * (n_x - 1.0) * dz_m / 2.0)
    field = gaussian_input_field(x_m, wavelength_m, Z_START_CM)
    input_peak = np.max(np.abs(field) ** 2)

    saved_z_cm = [z_m[0] * 100.0]
    saved_intensity = [(np.abs(field) ** 2 / input_peak).astype(np.float32)]

    for iz in range(n_steps):
        inside_capillary = cap_start_index <= iz < cap_end_index
        if inside_capillary:
            field *= index_phase_half

        field = angular_spectrum_step(field, dz_m, k0, kx)

        if inside_capillary:
            field *= index_phase_half

        next_iz = iz + 1
        if next_iz % SAVE_EVERY_STEPS == 0 or next_iz == n_steps:
            saved_z_cm.append(z_m[next_iz] * 100.0)
            saved_intensity.append(
                (np.abs(field) ** 2 / input_peak).astype(np.float32)
            )

    return (
        x_m,
        n_x,
        np.asarray(saved_z_cm),
        np.asarray(saved_intensity),
        wavelength_m,
        dz_m,
        plasma_parameters,
    )


def plot_result(x_m, n_x, z_cm, intensity, wavelength_m, dz_m, plasma_parameters):
    """绘出折射率横截面与归一化单色强度传播图。"""
    x_um = x_m * 1e6

    # 上图显示折射率降低量 (1-Re(n))*1e6，横纵坐标覆盖整个计算域。
    # 直接画 Re(n) 时，约 10^-6 量级的等离子体变化会被 n≈1 的背景压扁；
    # 因此减去 1 并放大 10^6。毛细管外填入真实真空 n=1，管壁填入模型的
    # 复折射率，管芯填入等离子体折射率。整个二维数组都直接绘制，不做 mask。
    fig, (ax_n, ax_i) = plt.subplots(
        2, 1, figsize=(10.5, 7.4), sharex=True, constrained_layout=True
    )

    n_2d = np.ones((len(x_um), len(z_cm)), dtype=np.complex128)
    cap_mask_z = (z_cm >= CAPILLARY_START_CM - 1e-12) & (
        z_cm <= CAPILLARY_END_CM + 1e-12
    )
    # 物理分布：整个空间先设为真空 n=1；只在毛细管 z 段替换为横向剖面 n(x)。
    # 这里的轴向选择只定义毛细管的物理位置，不对任何数据点做绘图掩膜。
    n_2d[:, cap_mask_z] = n_x[:, None]
    index_decrement_2d = 1e6 * (1.0 - np.real(n_2d))
    mesh_n = ax_n.pcolormesh(
        z_cm,
        x_um,
        index_decrement_2d,
        shading="auto",
        cmap="inferno_r",
        vmin=INDEX_DECREMENT_VMIN,
        vmax=INDEX_DECREMENT_VMAX,
        rasterized=True,
    )
    fig.colorbar(mesh_n, ax=ax_n, label=r"$(1-\mathrm{Re}(n))\times10^6$")
    ax_n.set_ylabel("Transverse coordinate x (µm)")
    ax_n.set_title("Refractive-index decrement across full domain (inferno_r)")
    ax_n.axvline(CAPILLARY_START_CM, color="white", ls="--", lw=1.0)
    ax_n.axvline(CAPILLARY_END_CM, color="white", ls="--", lw=1.0)

    mesh_i = ax_i.pcolormesh(
        z_cm,
        x_um,
        intensity.T,
        shading="auto",
        cmap="inferno",
        vmin=INTENSITY_VMIN,
        vmax=INTENSITY_VMAX,
    )
    fig.colorbar(mesh_i, ax=ax_i, label="Normalized monochromatic intensity")
    ax_i.set_xlabel("Distance z (cm)")
    ax_i.set_ylabel("Transverse coordinate x (µm)")
    ax_i.set_title("80 eV scalar WPM propagation through a 200 mbar plasma capillary")
    ax_i.axvline(CAPILLARY_START_CM, color="cyan", ls="--", lw=1.0,
                 label="capillary entrance/exit")
    ax_i.axvline(CAPILLARY_END_CM, color="cyan", ls="--", lw=1.0)
    ax_i.legend(loc="upper right", frameon=False)

    for ax in (ax_n, ax_i):
        ax.set_xlim(Z_START_CM, Z_END_CM)
        ax.set_ylim(-200.0, 200.0)
        ax.grid(False)

    fig.suptitle(
        f"λ={wavelength_m * 1e9:.3f} nm; p={HYDROGEN_PRESSURE_MBAR:g} mbar; "
        f"w₀={INPUT_WAIST_UM:g} µm; dz={dz_m * 1e6:g} µm",
        fontsize=12,
    )
    output_path = Path(__file__).resolve().with_name(
        "wpm_hydrogen_capillary_200mbar_80eV.png"
    )
    fig.savefig(output_path, dpi=220, bbox_inches="tight")

    print(f"图像已保存：{output_path}")
    print(f"光子能量：{PHOTON_ENERGY_EV:g} eV")
    print(f"真空波长：{wavelength_m * 1e9:.5f} nm")
    print(f"氢气压强：{HYDROGEN_PRESSURE_MBAR:g} mbar，温度：{GAS_TEMPERATURE_K:g} K")
    print(f"H2 分子数密度：{plasma_parameters['n_h2_m3']:.4e} m^-3")
    print(f"初始原子氢数密度 na：{plasma_parameters['n_atomic_m3']:.4e} m^-3")
    print(f"轴上电子密度 ne0：{plasma_parameters['n_e_axis_m3']:.4e} m^-3")
    print(f"通道边缘电子密度：{plasma_parameters['n_e_edge_m3']:.4e} m^-3")
    print(f"80 eV 临界密度：{plasma_parameters['n_critical_m3']:.4e} m^-3")
    print(
        "等离子体折射率 Re(n)：轴上 "
        f"{plasma_parameters['n_index_axis']:.8f}，通道边缘 "
        f"{plasma_parameters['n_index_edge']:.8f}"
    )
    print(
        f"界面余弦平滑带宽：{INTERFACE_SMOOTH_WIDTH_UM:g} µm "
        "（本脚本数值设定，S8 未给出具体函数和宽度）"
    )
    print(f"传播网格：dx={DX_UM:g} µm，dz={dz_m * 1e6:g} µm")
    plt.show()


def main():
    results = propagate_wpm()
    plot_result(*results)


if __name__ == "__main__":
    main()

```

















本文数值计算上的几个区别：

|                 研究内容                 |                       论文采用的方法                       |
| :--------------------------------------: | :--------------------------------------------------------: |
| 光束在等离子体内外的空间传播、聚焦、发散 |               SI S8：WPM，逐段传播单频复电场               |
|       阿秒脉冲的时空分布及脉宽变化       | SI S11：透镜内程函近似，透镜外小角衍射，再进行频域相干合成 |



















## 4．最容易写错的地方：本文的折射率在横向上变化

等离子体透镜的折射率是

$$
n=n(x,z;\omega)
$$

而不是一个常数。

这时，不能简单地写成

```python
H = exp(1j * dz * sqrt(n_x**2 * k0**2 - kx**2))
u = ifft(H * fft(u))
```

即使 `n_x` 和 `kx` 数组长度相同，这样计算通常也不成立。因为：

$$
\boxed{n(x)\text{ 定义在位置空间，}\quad k_x\text{ 定义在空间频率域。}}
$$

将两个数组逐元素对应，不代表正确的变折射率传播算符。

SI 的紧凑公式解释了传播核，但**没有完整展开变折射率时的数值实现细节**。它引用的 Diffractio 实现区分一般标量 WPM 和针对离散折射率的快速 Schmidt 实现；后者通过对不同折射率分别传播，再按空间掩膜组合结果。[Diffractio 源码文档](https://diffractio.readthedocs.io/en/latest/_modules/diffractio/scalar_fields_XZ.html)

例如，将一个切片内的折射率近似为若干等级 $n_j$，定义对应位置掩膜 $M_j(x)$，可以写出一类局部传播近似

$$
u_{m+1}(x)\approx\sum_j M_j(x)\mathcal F_x^{-1}\left[e^{i\Delta z\sqrt{n_j^2k_0^2-k_x^2}}\widehat u_m(k_x)\right]
$$

这里每个传播核使用的是**常数** $n_j$，因而没有混淆两个空间。

实际计算中，需要同时检查传播步长和折射率离散等级的收敛。不能仅因为程序中出现 FFT 和平方根传播核，就认定其正确实现了变折射率 WPM。

## 5．它与常见 BPM、分步 Fourier 方法的关系

为了看清联系，把场写成

$$
u(x,z)=A(x,z)e^{ik_{\rm ref}z},\qquad k_{\rm ref}=n_{\rm ref}k_0.
$$

代回 Helmholtz 方程，并忽略包络的二阶纵向导数，可得到近轴传播方程：

$$
\frac{\partial A}{\partial z}=\frac{i}{2k_{\rm ref}}\nabla_\perp^2A+i\frac{k_0^2(n^2-n_{\rm ref}^2)}{2k_{\rm ref}}A.
$$

记

$$
D=\frac{i}{2k_{\rm ref}}\nabla_\perp^2,\qquad V=i\frac{k_0^2(n^2-n_{\rm ref}^2)}{2k_{\rm ref}},
$$

则一个对称分步为

$$
A(z+\Delta z)\approx e^{V\Delta z/2}e^{D\Delta z}e^{V\Delta z/2}A(z).
$$

实际操作就是：

$$
\boxed{\text{半步介质相位}\rightarrow\text{一步 Fourier 衍射}\rightarrow\text{半步介质相位}.}
$$

这属于近轴 BPM 的典型实现。

| 方法              | 主要特点                                                 |
| ----------------- | -------------------------------------------------------- |
| 近轴 BPM          | 使用近轴展开，算法简单，适合平滑、弱折射、较小角度传播   |
| 本文所引用的 WPM  | 使用局部平面波及平方根传播核，减少近轴展开带来的角度误差 |
| 完整 Maxwell 求解 | 能处理更全面的矢量、反射、散射效应，代价更高             |

**WPM 与 BPM 的区别不在于“有没有 FFT”，而在于传播算符采用了什么近似，以及如何处理空间变化的折射率。**

对于本文的弱折射 XUV 问题，正确实现并收敛的近轴分步方法，也很适合作为独立核验工具。

## 7．为什么这里不必用 PIC 或全域 MEEP？

本文光学传播计算中，等离子体密度是**预先给定的介质参数**。

它不需要同时求解：

- 放电过程怎样产生密度分布；
- 每个电子、离子的运动；
- XUV 对密度的反馈；
- 强场相对论效应或等离子体不稳定性。

这些条件使问题变成一个线性色散介质中的光传播问题。

以 $80\ \mathrm{eV}$ 为例，

$$
\lambda\simeq15.5\ \mathrm{nm}.
$$

若显式解析厘米长的透镜，纵向已经包含数百万个波长；再考虑横向范围和时间步，全波时域计算会非常昂贵。

WPM 可以解析处理快速载波相位，主要数值分辨光束及介质变化，所以更有效率。

不过，**正向 WPM 不适合用来研究显著反射或临界密度转向。**如果问题变成此前讨论的脉冲在密度梯度中反射，就不能照搬这里的单向传播模型。

## 8．真正动手计算时，具体怎样做？

建议按以下流程实施。

### ① 定义入射复场

在入口平面给定

$$
u_{\rm in}(x;\omega)=A(\omega)\exp\left[-\frac{x^2}{w_{\rm in}^2(\omega)}\right]\exp\left[\frac{ik_0x^2}{2R_{\rm in}(\omega)}+i\Phi_{\rm in}(\omega)\right].
$$

需要明确：

- $w_{\rm in}$ 是 $1/e^2$ 强度半径；
- $R_{\rm in}$ 表示波前曲率，符号应与传播约定一致；
- $A(\omega)$ 是光谱**场振幅**；
- $\Phi_{\rm in}$ 是输入频谱相位。

若已知的是光谱强度，应取平方根得到场振幅。

### ② 构建介质

由密度计算

$$
n(x,z;\omega).
$$

SI S8 还考虑了毛细管壁，在其示例中使用

$$
\widetilde n_{\rm wall}=0.966+i\,0.0413,
$$

并平滑连接等离子体与管壁，以减少计算伪影。

这些光学常数属于相应光子能量下的材料参数，不能在整个宽频谱中直接当作通用常数。

### ③ 在等离子体内部逐步传播

从入口开始，连续执行

$$
u_{m+1}=\mathcal P[n(x,z_m;\omega),\Delta z]u_m.
$$

主要保留：

- 出口复电场；
- 稀疏采样的传播强度图；
- 光束宽度随 $z$ 的变化。

无需保存每一步的完整大数组。Diffractio 也提供只保存出口场、轴线和局部区域等结果的传播方式，以减少长距离计算的内存需求。[Diffractio 长距离 WPM 文档](https://diffractio.readthedocs.io/en/latest/source/functioning/WPM_ws.html)

### ④ 出等离子体后，直接使用真空角谱传播

这正是我们此前讨论“截断 plasma 区域”的数学依据。

保存出口场

$$
u_{\rm out}(x;\omega),
$$

则距离出口 $d$ 处：

$$
\boxed{u(x,d;\omega)=\mathcal F_x^{-1}\left[\widehat u_{\rm out}(k_x;\omega)e^{id\sqrt{k_0^2-k_x^2}}\right].}
$$

中间不需要逐步走完整个真空距离。

若已去除真空载波，可以改用

$$
e^{id[\sqrt{k_0^2-k_x^2}-k_0]},
$$

以减少无意义的大公共相位。

**只要出口之后是真空、且没有需要反馈处理的反射，出口复场足以决定后续正向传播。**必须保留相位，只有出口强度图是不够的。

### ⑤ 在多个观察平面寻找焦点

计算各平面的光束宽度，找到最小值，而不是直接把解析 $f$ 当作最终焦点位置。

对宽频脉冲，还需区分单频焦点与总脉冲的最佳聚焦平面。

## 9．阿秒脉冲如何计算？

静态线性介质中，各频率可以分别传播：

$$
u_{\rm in}(x;\omega_j)\longrightarrow u_{\rm obs}(x;\omega_j).
$$

然后进行**相干**频域合成：

$$
\mathcal E(x,t)=\frac{1}{2\pi}\int_0^\infty u_{\rm obs}(x;\omega)e^{-i\omega t}\,d\omega,
$$

$$
I(x,t)\propto|\mathcal E(x,t)|^2.
$$

空间积分后的时间曲线为

$$
P(t)\propto\int I(x,t)\,dx
$$

——这是论文二维模型对应的积分形式。

关键是：

$$
\boxed{\text{求脉宽必须合成复电场，不能把各频率强度直接相加。}}
$$

直接做

$$
\int|u(x,\omega)|^2\,d\omega
$$

得到的是时间积分意义下的空间分布，无法恢复啁啾与脉宽。

SI S11 为了简化计算，没有对每个频率都完整进行透镜内 WPM，而是采用

$$
u_{\rm exit}(x,\omega)\approx u_{\rm in}(x,\omega)\exp\left[i\frac{\omega L}{c}(n(x,\omega)-1)\right],
$$

随后进行小角自由空间衍射，再逆 Fourier 合成时间波形。

这个近似忽略了透镜内部明显的衍射及横向重分布。如果我们准备缩短透镜、增强径向梯度，就应重新检查这一点。

更统一的方案是：**每个频率在透镜内用 WPM，出口后用真空角谱传播，最后相干合成。**

## 10．色散为什么会压缩正啁啾脉冲？

弱等离子体近似下，轴上相对于真空的频谱相位为

$$
\phi(\omega)\approx-\frac{\omega_{p0}^2L}{2c\omega}.
$$

于是

$$
\frac{d\phi}{d\omega}=\frac{\omega_{p0}^2L}{2c\omega^2}>0,
$$

$$
\boxed{\mathrm{GDD}=\frac{d^2\phi}{d\omega^2}=-\frac{\omega_{p0}^2L}{c\omega^3}<0.}
$$

等离子体提供负 GDD，因而可能补偿正啁啾。

对于具有二次频谱相位的 Gaussian 脉冲，

$$
\tau_{\rm out}=\tau_{\rm TL}\sqrt{1+\left[\frac{4\ln2\,(C+\mathrm{GDD})}{\tau_{\rm TL}^2}\right]^2},
$$

其中 $C$ 是初始二次频谱相位系数，$\tau_{\rm TL}$ 是变换极限强度 FWHM。

SI 给出的例子是：

- 变换极限脉冲：$90\ \mathrm{as}\rightarrow117\ \mathrm{as}$；
- 正啁啾脉冲：约 $189\text{–}190\ \mathrm{as}\rightarrow127\ \mathrm{as}$；
- GDD 简单估算：$-2140\ \mathrm{as^2}$，预测 $90\ \mathrm{as}\rightarrow111\ \mathrm{as}$。

简单 GDD 结果与时空计算接近，但不完全相同，因为后者还包含频率相关聚焦及更完整的频谱相位。

## 11．网格该怎样选，怎样判断结果可信？

WPM 的网格依据与 FDTD 不同，但仍需要收敛检查。

| 项目                    | 实际选择依据                                     |
| ----------------------- | ------------------------------------------------ |
| 横向步长 $\Delta x$     | 分辨最小光斑、介质梯度以及最大横向波数           |
| 横向窗口                | 包含传播过程中扩展的光束，并留出边界缓冲区       |
| 传播步长 $\Delta z$     | 分辨纵向介质变化，控制局部传播近似和算符分裂误差 |
| 折射率等级数            | 若采用离散折射率 WPM，要使量化误差收敛           |
| 频率间隔 $\Delta\omega$ | 提供足够长的时间窗口 $T=2\pi/\Delta\omega$       |
| 总频率跨度              | 覆盖输入频谱，并提供足够的时间分辨率             |

横向采样至少要满足

$$
k_{x,\max}<\frac{\pi}{\Delta x}.
$$

若最大传播角为 $\theta_{\max}$，则在真空中相应有

$$
\Delta x<\frac{\lambda_{\min}}{2\sin\theta_{\max}},
$$

实际还应留出采样余量。

因此，**横向网格不一定要按“每个真空波长多少个点”选择，而要解析实际存在的横向变化和传播角度。**但若显式解析尖锐管壁、倏逝场或大角度分量，要求会明显提高。

最有价值的验证包括：

1. 真空 Gaussian 束传播能否恢复解析束宽；
2. 弱透镜极限下是否符合解析焦距；
3. 减小 $\Delta x$、$\Delta z$ 后，焦点、束腰及脉宽是否稳定；
4. 扩大窗口后是否消除 FFT 周期回绕；
5. 无损情况下功率是否守恒，损耗是否来自明确的吸收或边界截断。

还要特别注意 SI 的几何约定：它虽然使用 $r$ 记号，但普通一维横向 FFT **不自动等于严格圆柱轴对称传播**。真正的轴对称模型需要径向算符或 Hankel 变换，并用

$$
2\pi\int_0^\infty I(r,t)\,r\,dr
$$

计算横向积分。若要定量复现圆形光束的能量和峰值，这个区别必须核实。

对于我们后续的模拟，最合适的路线是：**先以单频透镜内传播验证空间聚焦，再扩展到多频相干合成；真空部分直接由出口复场传播。**这样既能对应 SI 的空间结果，也能进一步检查其阿秒脉冲计算中程函近似的适用程度。





































