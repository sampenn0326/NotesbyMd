# 0.安装和使用

安装随时借用AI就好了。











# 1. FDTD方法











# 2. 介质响应

等离子体对每个频率有一个不同的介电常数，在meep中可以通过Drude响应来恰当地建模，这样可以一次地通过FDTD配合计算啁啾脉冲在等离子体介质中的传播问题。但是meep中可以看成是抽象的连续介质，可以给电磁波正常的反馈，但本身没有粒子动力学参与其中，这是和PIC的一大差别。

对于一个啁啾脉冲的反射算例而言，只要给定平衡密度 $n_0 (z)$ ，Meep就能在一次时域模拟中算出各频率分量不同的传播、截止和反射特性。

## 2.1 冷等离子体的色散来自电子惯性 

以 1D 平面反射为例，令激光沿 \(z\) 传播，\(E_\perp\) 表示横向电场。在线性、冷、无外磁场的模型里，离子提供静止背景，电子在横向电场下振荡。用 SI 单位写电子动量和电流
$$
m_e(\partial_t+\nu)v_\perp=-eE_\perp, \qquad J_\perp=-en_0(z)v_\perp
$$
这里 \(\nu\) 是电子动量阻尼率。因为平衡密度 \(n_0(z)\) 已给定，两式直接合并成
$$
\boxed{ \partial_tJ_\perp+\nu J_\perp =\varepsilon_0\omega_p^2(z)E_\perp, \qquad \omega_p^2(z)=\frac{n_0(z)e^2}{\varepsilon_0m_e} }
$$
这一步把电子对光场的作用压缩成了一个局域变量 \(J_\perp(z,t)\)。 同一位置上所有电子的线性横向运动，用一个电流就能表示。电子密度越高，同样电场驱动的电流变化率越大。无碰撞时，\(\partial_tJ_\perp\propto E_\perp\)，因此电流记录了此前电场作用的累积。这就是时域里的材料记忆。

## 2.2 同一条时域方程，自动给出不同频率的响应

Meep 用辅助极化 \(P_\perp\) 表示这股电流。令 \(J_\perp=\partial_tP_\perp\)，上式就成为 Drude 方程
$$
\partial_t^2P_\perp+\nu\partial_tP_\perp =\varepsilon_0\omega_p^2(z)E_\perp, \qquad D_\perp=\varepsilon_0 E_\perp+P_\perp 
$$
为了看清频率依赖，取一个 \(e^{-i\omega t}\) 的分量。代入后，\(\partial_t\to-i\omega\)，所以
$$
(-\omega^2-i\nu\omega)P_\perp =\varepsilon_0\omega_p^2(z)E_\perp, \qquad \boxed{\varepsilon_r(z,\omega) =1-\frac{\omega_p^2(z)}{\omega(\omega+i\nu)}}
$$
设 \(\nu=0\) 时
$$
\varepsilon_r(z,\omega)=1-\frac{\omega_p^2(z)}{\omega^2}
$$
这个 \(1/\omega^2\) 可以直接从电子运动理解。对于相同的电场振幅，电子加速度振幅相同。振荡频率越高，电场反向越快，电子速度振幅按 \(1/\omega\) 减小，位移振幅按 \(1/\omega^2\) 减小。极化正比于电子位移，所以高频下 \(\varepsilon_r\) 更接近真空值 \(1\)。低频下，电子位移更大，极化对总响应的修正更强。**介电常数的频率依赖已经写进了电子运动方程。**

## 2.3 Meep 在一次 FDTD 模拟中的具体使用

Meep 在时间步进中同时推进 Maxwell 场和辅助极化。用均匀时间步长 \(\Delta t\) 作示意，在无碰撞情况下，对极化方程作中心差分就得到
$$
P^{j+1} =2P^j-P^{j-1} +\varepsilon_0\omega_p^2(z)(\Delta t)^2 E^j
$$
这个递推式说明了实现为什么省事。**每个网格点只需用当前局域电场、已有的极化状态和预设的 \(\omega_p^2(z)\) 更新极化。** 极化再通过 \(E_\perp=(D_\perp-P_\perp)/\varepsilon_0\) 反馈到电场。计算中无需逐步做 FFT，也无需为每个频率重新设介质、单独跑一次。这个差分式用于说明局域更新原理，Meep 实际实现与其场分量的时间和空间排布配合。[MEEP Documentation](https://meep.readthedocs.io/en/latest/Materials/?utm_source=chatgpt.com)

例如，某一点的电场同时含有 \(\omega_1\) 和 \(\omega_2\)。**同一个 \(P(t)\) 更新式会同时产生两项极化响应**。在线性模型下，每项分别得到自己的 \(\chi(\omega_1)\) 和 \(\chi(\omega_2)\)。因此，Meep 在脉冲前沿或后沿都无需先判断“此刻的瞬时频率是多少”。即使多个频率在同一时刻重叠，同一条时域方程也能处理。

## 2.4 在具体的1D反射算例中

设中心波长取 \(\lambda_0=1\,\mu\mathrm m\)，长度单位取 \(\lambda_0\)，时间单位就是 \(T_0=\lambda_0/c\)。这样，中心频率在 Meep 的单位里是 \(f_0=1\)。定义中心频率对应的临界密度
$$
n_{c0}=\frac{\varepsilon_0m_e\omega_0^2}{e^2}, \qquad N(z)=\frac{n_0(z)}{n_{c0}} 
$$
在背景 `epsilon=1` 时，算例的参数可以写成

```
mp.DrudeSusceptibility(frequency=1.0, gamma=0.0, sigma=N)
```

这里的 `N` 是**当前位置**的归一化密度。`frequency=1.0` 固定了 Drude 项的频率标度，`sigma=N` 决定其强度。两者合起来给出该位置的实际等离子体频率 \(f_p(z)/f_0=\sqrt{N(z)}\)。因此，即使每个位置都设 `frequency=1.0`，临界频率仍随位置变化。Meep 接口中的 `frequency` 使用普通频率单位，直接填 `1.0` 即可。[MEEP Documentation](https://meep.readthedocs.io/en/latest/Materials/?utm_source=chatgpt.com)

把探测频率写成 \(f=\omega/\omega_0\)，局域介电函数就是
$$
\varepsilon_r(z,f)=1-\frac{N(z)}{f^2}
$$
例如，在 \(N=1\) 的同一个位置，三个频率看到的是

| 频率 \(f\) | 局域 \(\varepsilon_r\) |            对应状态            |
| :--------: | :--------------------: | :----------------------------: |
|  \(0.8\)   |      \(-0.5625\)       | 已越过自身的截止点，进入倏逝区 |
|  \(1.0\)   |         \(0\)          |         恰在局域截止点         |
|  \(1.2\)   |       \(0.3056\)       |         仍在局域传播区         |

在单调上升的密度梯度中，各分量的局域截止条件为 \(N(z_{\rm cut})=f^2\)。所以低频在较低密度处截止，高频能进入更深的区域。在到达各自截止区之前，它们在欠密区积累的传播相位也不同。**Meep 推进的是完整的波场，反射相位由整个密度剖面的波动解给出。** 这正是啁啾反射压缩所依赖的量。用频域语言写，反射场满足 \(\widetilde E_{\rm ref}(\omega)=r(\omega)\widetilde E_{\rm in}(\omega)\)，入射谱相位和 \(\arg r(\omega)\) 相加。当两者的频率依赖相互补偿时，反射脉冲就可以变短。[MEEP Documentation](https://meep.readthedocs.io/en/latest/Materials/?utm_source=chatgpt.com)

和一维 SRS 问题比较，**Drude 简化的是给定 \(n_0(z)\) 时电子对光场的线性响应。** 对反射算例，这已经保留了所需的宽带色散和截止物理。SRS 还需要光场驱动 \(\delta n(z,t)\)，再由 \(\delta n\) 调制电流、把泵浦能量转入散射光。标准 Drude 的电流方程只含预设的 \(n_0(z)\)，所以同一套计算能给出反射压缩的线性基准，但无法从中得到受激拉曼增益。

## 2.5 概括

### 2.5.1 电磁PIC和MEEP中的Yee推进对比

#### A. 电磁PIC

**连续方程**
$$
 \begin{aligned} \partial_t\mathbf B&=-\nabla\times\mathbf E,\\ \varepsilon_0\partial_t\mathbf E &=\frac{1}{\mu_0}\nabla\times\mathbf B-\mathbf J_{\rm p},\\ \nabla\cdot\mathbf B&=0,\\ \varepsilon_0\nabla\cdot\mathbf E&=\rho_{\rm p}. \end{aligned}
$$
前两式推进场，后两式约束场。\(\rho_{\rm p}\) 和 \(\mathbf J_{\rm p}\) 是粒子的电荷密度和电流密度，满足 \(\partial_t\rho_{\rm p}+\nabla\cdot\mathbf J_{\rm p}=0\)。在 PIC 中，粒子受洛伦兹力推进，粒子运动产生的电流再沉积到 Yee 网格。

**Yee更新**

令 \(\mathbf E\) 位于整数时间步，\(\mathbf B\) 位于半整数时间步，\(\nabla_h\times\) 表示 Yee 网格上的离散旋度。一步更新为
$$
\boxed{ \begin{aligned} \mathbf B^{n+1/2} &=\mathbf B^{n-1/2} -\Delta t\,\nabla_h\times\mathbf E^n,\\[2pt] \mathbf E^{n+1} &=\mathbf E^n+ \frac{\Delta t}{\varepsilon_0} \left[ \frac{1}{\mu_0}\nabla_h\times\mathbf B^{n+1/2} -\mathbf J_{\rm dep}^{n+1/2} \right] \end{aligned}}
$$
这里 \(\mathbf J_{\rm dep}^{n+1/2}\) 由粒子在 \(t_n\) 到 \(t_{n+1}\) 之间的运动沉积到各电场分量所在的位置。使用电荷守恒的电流沉积时，离散连续性方程与这条电场更新式相容，初始满足的电高斯定律会随步进保持。

#### B. Meep + Drude

**连续方程**

把等离子体电流并入极化，写成 \(\mathbf J_{\rm p}=\partial_t\mathbf P\)，并定义 \(\mathbf D=\varepsilon_0\mathbf E+\mathbf P\)。在无外加电荷和电流的区域，
$$
\begin{aligned} \partial_t\mathbf B&=-\nabla\times\mathbf E,\\ \partial_t\mathbf D&=\frac{1}{\mu_0}\nabla\times\mathbf B,\\ \nabla\cdot\mathbf B&=0,\\ \nabla\cdot\mathbf D&=0 \end{aligned} 
$$
再加上 Drude 材料方程和本构关系，
$$
\partial_t^2\mathbf P+\nu\partial_t\mathbf P =\varepsilon_0\omega_p^2(\mathbf r)\mathbf E, \qquad \mathbf E=\frac{\mathbf D-\mathbf P}{\varepsilon_0}
$$
这里 \(\omega_p^2(\mathbf r)=e^2n_0(\mathbf r)/(\varepsilon_0m_e)\) 由预设的三维密度分布决定。若有外加电流 \(\mathbf J_{\rm ext}\)，它仍以 \(-\mathbf J_{\rm ext}\) 进入 \(\partial_t\mathbf D\)。

**Yee 更新**

\(\mathbf E,\mathbf D,\mathbf P\) 的对应分量位于同一类 Yee 网格位置和整数时间步。取无碰撞设置 \(\nu=0\)，一步更新可写成
$$
\boxed{ \begin{aligned} \mathbf B^{n+1/2} &=\mathbf B^{n-1/2} -\Delta t\,\nabla_h\times\mathbf E^n,\\[2pt] \mathbf D^{n+1} &=\mathbf D^n+ \frac{\Delta t}{\mu_0}\nabla_h\times\mathbf B^{n+1/2},\\[2pt] \mathbf P^{n+1} &=2\mathbf P^n-\mathbf P^{n-1} +\varepsilon_0\omega_p^2(\mathbf r)\Delta t^2\,\mathbf E^n,\\[2pt] \mathbf E^{n+1} &=\frac{\mathbf D^{n+1}-\mathbf P^{n+1}}{\varepsilon_0} \end{aligned}}
$$
前两行来自 Maxwell 方程，第三行是 Drude 方程的中心差分，第四行用本构关系恢复新电场。空间上仍然用完整的三维旋度。

#### C. 统一对比

把 Meep 更新式里的 \(\mathbf D\) 消掉，两种算法都可以写成
$$
\varepsilon_0\frac{\mathbf E^{n+1}-\mathbf E^n}{\Delta t} = \frac{1}{\mu_0}\nabla_h\times\mathbf B^{n+1/2} - \begin{cases} \mathbf J_{\rm dep}^{n+1/2}, & \text{PIC},\\[6pt] \dfrac{\mathbf P^{n+1}-\mathbf P^n}{\Delta t}, & \text{Meep + Drude} \end{cases} 
$$
**两边的磁场更新完全相同，电流也出现在电场更新的同一位置。** PIC 用粒子轨迹沉积这项电流。Meep 用局域 Drude 方程推进 \(\mathbf P\)，其时间差分就是等效电流。进一步把这个差分记作 \(\mathbf J_{\rm D}^{n+1/2}\)，第三行也可以直接写成
$$
\mathbf J_{\rm D}^{n+1/2} =\mathbf J_{\rm D}^{n-1/2} +\Delta t\,\varepsilon_0\omega_p^2(\mathbf r)\mathbf E^n 
$$
这样就能直接对照每一步在做什么。**PIC 推进粒子来生成电流，Drude 推进网格上的材料状态来生成电流。**

#### D. 如何从密度分布介入

设定归一化的密度分布，令 \(N(\mathbf r)=n_0(\mathbf r)/n_{c0}\)。Meep 的 `DrudeSusceptibility(frequency, gamma, sigma)` 直接对应下面这个**频域电极化率**。用 \(f\) 表示要考察的光频率，所有频率都用 Meep 单位，并采用 \(e^{-i2\pi f t}\) 约定
$$
\boxed{ \chi_{\mathrm D}(f)= -\frac{\mathtt{sigma}\,\mathtt{frequency}^{\,2}} {f\,(f+i\,\mathtt{gamma})} }
$$
这里 `frequency` 是分子里的频率标度，\(f\) 是分母里随光谱分量变化的频率。把实际物理公式和计算式对比设激光中心角频率为 \(\omega_0=2\pi/T_0\)。

|                 |                        Drude 电极化率                        |
| :-------------: | :----------------------------------------------------------: |
| **SI 物理公式** | \(\displaystyle \chi_{\mathrm D}(z,\omega)=-\frac{\omega_p^2(z)}{\omega(\omega+i\nu)}\) |
| **Meep 参数式** | \(\displaystyle \chi_{\mathrm D}(z,f)=-\frac{\mathrm{sigma}(z)\,\mathrm{frequency}^{2}}{f(f+i\,\mathrm{gamma})}\) |

把 **SI 公式的分子和分母都除以 \(\omega_0^2\)**
$$
\chi_{\mathrm D} =-\frac{\bigl(\omega_p(z)/\omega_0\bigr)^2} {(\omega/\omega_0)\bigl(\omega/\omega_0+i\nu/\omega_0\bigr)}=-\frac{n_e/n_{cr0}} {f\,(f+i\,\mathtt{gamma})} =\frac{N} {f\,(f+i\,\mathtt{gamma})} 
$$
对应和归一化设置如下

|                   归一化后的物理量                   |      Meep 里的对应量      |
| :--------------------------------------------------: | :-----------------------: |
|         \(\omega/\omega_0\)，光谱分量的频率          |           \(f\)           |
|          \(\nu/\omega_0\)，电子电流的阻尼率          |          `gamma`          |
| \(\omega_p^2(z)/\omega_0^2\)，局域等离子体频率的平方 | `sigma(z) * frequency**2` |

把 `frequency=1.0, gamma=0.0, sigma=N(z)` 直接代进去，就得到
$$
\chi_{\mathrm D}(z,f)=-\frac{N(z)}{f^2}, \qquad \varepsilon_r(z,f)=1-\frac{N(z)}{f^2} \quad\text{（背景 epsilon=1）}
$$
这里直接对应的是**频域**本构关系
$$
\widetilde{\mathbf P} =\varepsilon_0\chi_{\rm D}(\mathbf r,\omega)\widetilde{\mathbf E}, \qquad \chi_{\rm D}(\mathbf r,\omega) =-\frac{N(\mathbf r)\omega_0^2}{\omega^2}
$$
**从频域接到时域的关键，就是把分母里的 \(-\omega^2\) 变成二阶时间导数。** 先把分母乘过去，再用傅里叶变换的对应关系 \(-\omega^2\widetilde{\mathbf P}\leftrightarrow\partial_t^2\mathbf P\)
$$
-\omega^2\widetilde{\mathbf P} =\varepsilon_0N(\mathbf r)\omega_0^2\widetilde{\mathbf E} \quad\Longleftrightarrow\quad \partial_t^2\mathbf P =\varepsilon_0N(\mathbf r)\omega_0^2\mathbf E
$$
右边这条就是 FDTD 可以直接离散的方程。每个网格点用当地的 \(N(\mathbf r)\) 和当前电场推进 \(P\)，再通过 \(E=(D-P)/\varepsilon_0\) 把极化反馈给电场。所以，**空间依赖 \(N(\mathbf r)\) 留在网格系数里，频率依赖 \(1/\omega^2\) 由 \(P\) 的时域演化实现。** 上式在离散形式下用于更新辅助场，在 FDTD 中，对二阶时间导数做中心差分，就能用当前电场 \(\mathbf E^n\) 和前两步的极化求出下一步的极化
$$
\mathbf P^{n+1} =2\mathbf P^n-\mathbf P^{n-1} +\varepsilon_0 N(\mathbf r)\omega_0^2(\Delta t)^2\mathbf E^n
$$
随后，新极化 \(\mathbf P^{n+1}\) 通过本构关系参与**电场 \(\mathbf E\) 的更新**
$$
\mathbf E^{n+1} =\frac{\mathbf D^{n+1}-\mathbf P^{n+1}}{\varepsilon_0}
$$
其中 \(\mathbf D^{n+1}\) 由安培–麦克斯韦方程推进。也就是说，这条 Drude 方程在每一步中的作用是 \(\mathbf E^n \rightarrow \mathbf P^{n+1} \rightarrow \mathbf E^{n+1}\)。

最后一个值得澄清的点：从 $\mathbf P^{n+1}$​ 的显示更新式中，似乎看不到不同频率的依赖有分别。但实际上FDTD作为时域更新，是不区分频率的，更新的就是一个时域总场，他就是各频率分量的相干加和。那么既然是混合在总场中更新，如何实现了不同分频的场较为独立的演化？

简单来说，设只有两个频率叠加，把同一个网格点的总电场写成 \(E^n=E_1^n+E_2^n\)，并把 Drude 系数记作 \(C=\varepsilon_0N(\mathbf r)\omega_0^2(\Delta t)^2\)。假设两个分量各自驱动出的极化是 \(P_1\) 和 \(P_2\)。把两条更新式相加，就得到
$$
P_1^{n+1}+P_2^{n+1} =2(P_1^n+P_2^n)-(P_1^{n-1}+P_2^{n-1}) +C(E_1^n+E_2^n)
$$
恰好就是用总场和总极化做一次更新。所以，**先把电场加起来再推进，和让各个频率分别产生自己的极化响应再相加，结果一样。** 每个分量的频率依赖仍由它在相邻时间步之间的相位差决定。FDTD 直接推进总场，就已经得到了这些不同响应的叠加。