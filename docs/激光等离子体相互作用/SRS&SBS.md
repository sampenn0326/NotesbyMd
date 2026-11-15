

# 受激Raman散射











# 前向拉曼放大

从 Maxwell–电子流体方程到三波耦合、线性时空增益与泵浦耗尽。以 Lei 等，*Phys. Rev. Lett.* **134**, 255001 (2025) 及其补充材料为主线。全文采用 SI 单位。 $z$ 为传播方向。

## 1. 模型、变量和近似

|                  符号                  |                   定义                   |
| :------------------------------------: | :--------------------------------------: |
|            \(e>0\)、\(m_e\)            |          元电荷绝对值、电子质量          |
|     \(n_b\)、\(\eta=\delta n/n_b\)     |      均匀背景电子密度、相对密度扰动      |
| \(\omega_p^2=n_b e^2/(\epsilon_0m_e)\) |           电子等离子体频率平方           |
|           \(a=eA_y/(m_ec)\)            |    归一化横向矢势，此处 \(a\) 为实场     |
|             \(u\)、\(E_x\)             |       纵向电子流体速度、纵向静电场       |
|          \(v_T^2=k_BT_e/m_e\)          |  一维电子热速平方，采用 Bohm–Gross 闭合  |
|               \(0,1,2\)                | 泵浦、Stokes 种子、电子等离子体波（EPW） |
| \(v_j=\partial\omega_j/\partial k_j\)  |     带符号群速度，后向分支 \(v_1<0\)     |

假设无外磁场、光束**共线**且线偏振，离子在所考察的电子波时间尺度上近似固定。保留最低阶的非线性耦合。电子纵向运动在推导中线性化，但保留横向运动产生的二阶有质动力。采用**弱相对论极限** \( |a|\ll1 \)。单支 Stokes 模型随后还要作载波选择和慢变包络近似。电子温度只通过压力闭合进入，Landau 阻尼需要单独建模。

## 2. 从电子运动推到光–密度双向耦合

### 2.1 横向正则动量和电流

设激光沿 $x$ 传播，沿 $y$ 偏振。场只依赖 \(x,t\)，因此 \(y\) 是循环坐标，电子横向正则动量 \(p_y-eA_y\) 守恒。取电子在场到来前横向静止，于是 \(p_y=eA_y\)，弱相对论下 \(v_y\simeq ca\)。这给出

$$
J_y=-e n_e v_y\simeq-\frac{e^2n_b}{m_e}(1+\eta)A_y
$$

取横向失势 $A_y(x,t)$ ，于是
$$
E_y =- \partial _t A_y,\quad B_z =\partial _x A_y
$$
 考虑Ampere方程的 $y$ 分量，得到  
$$
\nabla \times \vec{B} =\mu _0\varepsilon _0\frac{\partial \vec{E}}{\partial t}+\mu _0 \vec{J}\quad \to\quad -\partial _x B_z =\mu _0 J_y +\frac{1}{c^2} \partial _tE_y
$$
带入、整理得到（把背景密度 $n_b$ 的贡献归到左侧，且以 $a$ 为变量）
$$
\boxed{(\partial_t^2-c^2\partial_x^2+\omega_p^2)a
=-\omega_p^2\eta a} \tag{1}
$$

左边给出普通冷等离子体光学色散（取 $\eta$=0 带入平面波就得到色散关系 $\omega ^2 =c^2 k^2 +\omega _p^2$ ）；右边是密度扰动对横向电流的调制，也是频率混合的来源。

### 2.2 纵向有质动力、连续性和 Poisson 方程

对于 \(A_y(x,t)\)，有 \(B_z=\partial_x A_y\)，所以

$$
-\frac{e}{m_e}v_yB_z=-c^2a\,\partial_xa
=-\frac{c^2}{2}\partial_xa^2 
$$

这是纵向洛伦兹力的磁场项 $(\vec{v}\times \vec{B})_x = v_y B_z$ ，把这个力放入纵向动量方程，再联立连续性和 Poisson 方程

$$
\partial_t u=-\frac{e}{m_e}E_x-3v_T^2\partial_x\eta
-\frac{c^2}{2}\partial_x a^2,\qquad
\partial_t\eta=-\partial_x u,\qquad
\partial_xE_x=-\frac{en_b}{\epsilon_0}\eta
$$

其中 $v_T$ 相关项来自电子热压梯度产生的纵向加速度，即流体动量方程的压力项
$$
-\frac{1}{m_e n_e} \partial _x p_e \approx- \frac{1}{m_e n_b} \partial _x (\delta p_e) = 3v_T^2 \partial \eta \qquad \left( \delta p_e =3k_B T_e  \delta n_e,\;v_T^2 =k_BT_e/m_e \right)
$$
其中采用了一维绝热闭合。对连续性方程再取一次时间导数，得到
$$
\begin{aligned}
\partial_t^2\eta
&=-\partial_x\partial_tu\\
&=\frac{e}{m_e}\partial_xE_x+3v_T^2\partial_x^2\eta
+\frac{c^2}{2}\partial_x^2a^2
\end{aligned}
$$

（带入Poisson方程）消去 \(E_x\) 后，

$$
\boxed{(\partial_t^2-3v_T^2\partial_x^2+\omega_p^2)\eta
=\frac{c^2}{2}\partial_x^2a^2} \tag{2}
$$

式 (2) 表示光场拍频驱动电子密度波，式 (1) 表示密度波将泵浦散射到种子。两条方程形成闭合反馈。

## 3. 共振匹配与慢变包络

### 3.1 载波约定与频率选择

令 \(\theta_j=k_jx-\omega_jt\)，用峰值复包络表示实场（记得0，1，2分别标记泵浦、种子和电子等离子体波EPW）

$$
a=\tfrac12(a_0e^{i\theta_0}+a_1e^{i\theta_1}+\mathrm{c.c.}),\qquad
\eta=\tfrac12(Ne^{i\theta_2}+\mathrm{c.c.})   \tag{a}
$$

取泵浦 \(k_0>0\)，种子波数 \(k_1\) 带符号。\(a^2\) 中 \(e^{i(\theta_0-\theta_1)}\) 的系数是 \(a_0a_1^*/2\)，两种乘积排列都必须计入。\(\eta a\) 中 \(e^{i(\theta_1+\theta_2)}\) 的系数是 \(Na_1/4\)，\(e^{i(\theta_0-\theta_2)}\) 的系数是 \(N^*a_0/4\)。这三个因子决定耦合系数的归一化。

差频驱动与 EPW 载波匹配，同时 EPW 散射泵浦生成 Stokes 光

$$
\omega_0=\omega_1+\omega_2,\qquad k_0=k_1+k_2 \tag{3}
$$

若用三个独立参考载波，定义 \(\Psi=\theta_0-\theta_1-\theta_2\)。泵浦方程的右端乘 \(e^{-i\Psi}\)，种子和电子波方程的右端乘 \(e^{i\Psi}\)。不同文献若把失谐吸收进电子波包络，相位指数会移到导数项里。

### 3.2 展开波动算符

对任一包络 \(f\)，有

$$
\begin{aligned}
(\partial_t^2-c^2\partial_x^2+\omega_p^2)(fe^{i\theta})
=e^{i\theta}\big[&
(-\omega^2+c^2k^2+\omega_p^2)f\\
&-2i\omega(\partial_t+v_g\partial_x)f\\
&+(\partial_t^2-c^2\partial_x^2)f\big]
\end{aligned} \tag{b}
$$

其中 \(v_g=c^2k/\omega\)。选取满足色散关系的载波，第一项消去。包络变化尺度远长于光学周期和波长时，最后一项相对一阶导数项可略。EPW 算符同理，只需将 \(c^2\) 换为 \(3v_T^2\) （即查看方程1、2左侧算符对一般形式包络的作用），所以

$$
\omega_{0,1}^2=\omega_p^2+c^2 k_{0,1}^2,\quad
\omega_2^2=\omega_p^2+3v_T^2 k_2^2,\quad
v_2=\frac{3v_T^2 k_2}{\omega_2}
$$

上式中前两个式子是从”选取满足色散关系的载波“而得来，而 $v_2$ 则是把 $v_g$ 中的 $c^2$ 替换而得到的电子等离子体波群速度 电子波的相速度 \(v_{\phi,2}=\omega_2/k_2\) 可很大，即使冷极限的群速度 \(v_2\) 为零。

### 3.3 三波方程和对称归一化

设 \(D_j=\partial_t+v_j\partial_x\)。精确共振意味着 $\theta _0 =\theta _1 +\theta _2$ 。下面在精确共振条件下、在缓变包络近似下，将预设解的形式(a)带入(1)(2)式，得到
$$
(1)LHS&=-ie^{i\theta _0}\omega _0D_0 a_0 -ie^{i\theta _1}\omega _1 D_1 a_1 +c.c. \\
(1)RHS&=-\frac{\omega _p^2}{4} \left[Na_0e^{i(\theta_2+\theta_0)}+Na_0^*e^{i(\theta_2-\theta_0)}
+Na_1e^{i(\theta_2+\theta_1)}
+Na_1^*e^{i(\theta_2-\theta_1)} \right]\\
&-\frac{\omega_p^2}{4}\left[ N^*a_0e^{i(\theta_0-\theta_2)}
+N^*a_0^*e^{-i(\theta_2+\theta_0)}
+N^*a_1e^{i(\theta_1-\theta_2)}
+N^*a_1^*e^{-i(\theta_2+\theta_1)} \right]
$$
比较三个谐波的系数，例如左侧 $\exp[i\theta_0]$ 项对应右侧 $\exp[i(\theta _2 +\theta _1)]$ ，系数相等得到
$$
-i \omega _0 D_0 a_0 =-\frac{\omega _p ^2}{4}Na_1
$$
同理处理，则有
$$
D_0 a_0=-iC_0 Na_1,\qquad
D_1 a_1=-iC_1 N^*a_0,\qquad
D_2 N=-iH a_0a_1^*,
$$

$$
C_j=\frac{\omega_p^2}{4\omega_j}\ (j=0,1),\qquad
H=\frac{c^2k_2^2}{4\omega_2}
$$

例如 EPW 的正频方程是 \(-i\omega_2D_2N=-c^2k_2^2 a_0a_1^*/4\)。取 \(N=-iq\)，再定义

$$
P=a_0,\qquad S=\sqrt{\omega_1/\omega_0}\,a_1,\qquad
B=\sqrt{C_0/H}\,q,\qquad \kappa=\sqrt{C_1H}
$$

则（P为pump，S为stokes seed，B表示纵向电子密度波）

$$
\boxed{
D_0 P=-\kappa S B,\qquad
D_1 S=+\kappa P B^*,\qquad
D_2 B=+\kappa P S^* 
} \tag{4}
$$

这里的 \(P,S,B\)​ 是便于检查守恒律的归一化包络。式 (4) 可以看成一个**由电子密度波闭合的反馈回路**。把三行按物理过程重排，更直观

$$
\begin{aligned} D_2 B &=+\kappa P S^* &&\text{泵浦与种子拍频，激发电子密度波},\\ D_1 S &=+\kappa P B^* &&\text{密度波散射泵浦，把新光叠加到种子上},\\ D_0 P &=-\kappa S B &&\text{种子与密度波共同作用，使泵浦耗尽} \end{aligned}
$$
**密度波是一道运动的光栅**。设一束弱种子刚进入泵浦，起初 \(B=0\)。第一步是 \(PS^*\) 驱动电子密度波。密度波形成后，就像一道**运动的折射率光栅**，从泵浦散射出与种子同频、同波数的光。若散射光与原种子同相，两者的**场振幅**相加。更强的种子又产生更强的拍频，进一步加深光栅。所以，小信号阶段的图像是 **种子增强 → 密度波增强 → 泵浦向种子的散射增强**。即使一开始没有密度波，只要有种子，回路就能启动。

## 4. Manley–Rowe 关系与能量流向

将式 (4) 乘对应包络的共轭后取实部。定义 \(Q=2\kappa\operatorname{Re}(P^*SB)\)，得到

$$
D_0|P|^2=-Q,\qquad D_1|S|^2=Q,\qquad D_2|B|^2=Q \tag{c}
$$

可以从上式得到作用量守恒和能量守恒。可以直接用每支线性波的周期平均能量密度 \(\mathcal E_j\) 来验证，波作用量密度定义为
$$
\mathcal{J} _j =\frac{\mathcal{E}_j}{\omega _j}
$$
回顾由横向矢势  $A_j$ 表达的复场和速度
$$
\tilde E_y = i\omega_j A_y,\quad \tilde {B}_z=ik_j A_j,\quad \tilde{v}_y= \frac{e}{m_e} A_j
$$
对于横向电磁波，总能量是电场磁场能和跟随的横向电子振荡动能之和，分别算平均能量
$$
\begin{aligned}
\mathcal E_E
&=\frac{\epsilon_0}{2}\langle E_y^2\rangle
=\frac{\epsilon_0}{4}\omega_j^2|A_j|^2,\\[3pt]
\mathcal E_B
&=\frac{1}{2\mu_0}\langle B_z^2\rangle
=\frac{\epsilon_0}{4}c^2k_j^2|A_j|^2,\\[3pt]
\mathcal E_{\rm kin}
&=\frac{n_bm_e}{2}\langle v_y^2\rangle
=\frac{n_be^2}{4m_e}|A_j|^2
=\frac{\epsilon_0}{4}\omega_p^2|A_j|^2
\end{aligned}
$$
用上色散关系相加得到
$$
\begin{aligned}
\mathcal E_j
&=\frac{\epsilon_0|A_j|^2}{4}
\left(\omega_j^2+c^2k_j^2+\omega_p^2\right)\\
&=\frac{\epsilon_0}{2}\omega_j^2|A_j|^2
=\frac{n_bm_ec^2}{2\omega_p^2}\,\omega_j^2|a_j|^2
\end{aligned}
$$
这里还含有一个直观的关系：**磁场能加电子振荡动能，恰好等于电场能**。真空中电子动能项为零，磁场能和电场能各占一半。在冷等离子体中，磁场能的占比下降，电子振荡动能补足这一部分。最后除以 \(\omega_j\)，就得到前面用到的光波作用量密度 \(\mathcal J_j\propto\omega_j|a_j|^2\)​。这就解释了为什么取 \(P=a_0\)，同时给种子乘一个频率因子 \(S=\sqrt{\omega_1/\omega_0}\,a_1\)。令
$$
K=\frac{n_bm_ec^2\omega_0}{2\omega_p^2}
$$
便有 \(\mathcal J_0=K|P|^2\)、\(\mathcal J_1=K|S|^2\)。总之这种归一化选取使得 $|P|^2$ 等项正比于波的作用量密度。

同一个交换项 \(Q\)​ 使泵浦每减少一份作用量，种子和电子等离子体波（EPW）的作用量**各增加一份**
$$
\begin{aligned} \partial_t(I_0+I_1)+\partial_x(v_0I_0+v_1I_1)&=0,\\ \partial_t(I_0+I_2)+\partial_x(v_0I_0+v_2I_2)&=0\\
\left( \frac{\partial I}{\partial t} +\nabla \cdot(\vec{v}I) =0 \right)\end{aligned}

$$
其中记 $I_0=|P|^2, I_1 =|S|^2,I_2 =|B|^2$ ，这就是 Manley–Rowe 关系。

整体能量守恒来自按 \(\omega_j\) 对三式加权后相加，因为 \(-\omega_0+\omega_1+\omega_2=0\)。对有限空间区域，积分时还要保留边界通量。具体而言就是由(c)式得到
$$
\begin{aligned} \partial_t\mathcal E_0+\partial_x(v_0\mathcal E_0)&=-K\omega_0Q,\\ \partial_t\mathcal E_1+\partial_x(v_1\mathcal E_1)&=+K\omega_1Q,\\ \partial_t\mathcal E_2+\partial_x(v_2\mathcal E_2)&=+K\omega_2Q \end{aligned}
$$
这里沿用均匀背景下频率和群速度为常数的三波模型。三式相加时，右边变为
$$
KQ(-\omega_0+\omega_1+\omega_2)=0
$$
因为 Raman 共振要求 \(\omega_0=\omega_1+\omega_2\)。于是
$$
\boxed{\partial_t(\mathcal E_0+\mathcal E_1+\mathcal E_2) +\partial_x(v_0\mathcal E_0+v_1\mathcal E_1+v_2\mathcal E_2)=0} 
$$
物理上，在某一处、某一小段时间 \(dt\) 内，如果泵浦因耦合损失 \(KQ\,dt\) 的作用量，种子和电子波就各获得 \(KQ\,dt\) 的作用量。**同样一份作用量，在不同频率下对应不同的能量。** 泵浦损失的能量 \(KQ\,dt\,\omega_0\)，恰好等于种子得到的 \(KQ\,dt\,\omega_1\) 加上电子波得到的 \(KQ\,dt\,\omega_2\)。因此，耦合只在三波之间转移能量。

写相对相位 \(\phi=\arg P-\arg S-\arg B\)，则 \(Q=2\kappa|PSB|\cos\phi\)。**\(Q(x,t)\) 是局部、瞬时的交换速率，可以随时间和位置变化。** 三个方程在同一个 \((x,t)\) 上使用同一个 \(Q\)，所以无论它当时多大、是什么符号，守恒关系都逐点成立。

具体来说，
$$
Q=2\kappa|P||S||B|\cos\phi,\qquad \phi=\arg P-\arg S-\arg B
$$
振幅和相位都在演化，所以 \(Q\) 可以先变大、再减小，也可以变号。\(Q>0\) 时泵浦向种子和电子波供能，\(Q<0\) 时能量回传。对于理想、单支 Stokes、无损的三波转化，转入种子的能量为所耗尽泵浦能量的 \(\omega_1/\omega_0\)。如果定义泵浦到种子的效率为 \((U_{1,\rm out}-U_{1,\rm in})/U_{0,\rm in}\)，还需乘上泵浦耗尽分数。峰值强度则另外取决于脉宽、脉冲形状和横向光斑。

## 5. 线性阶段

### 5.1 局域增长率

令 \(P=P_0\) 为常数，并取其相位为零。这里是在线性增长推导里使用**未耗尽泵浦近似**。它的意思是：泵浦确实在损失能量，但在小信号阶段，这点损失占泵浦初始能量的比例很小，因此计算 \(S\) 和 \(B\) 的驱动项时，可以用 \(P_0\) 代替实际的 \(P(t)\)。此外，在均匀时间增长问题中略去空间导数，得到

$$
\dot S=gB^*,\qquad \dot B^*=gS,\qquad
\ddot S=g^2 S,\qquad g=\kappa|P_0|
$$

于是

$$
g=\frac{|a_0|c|k_2|\omega_p}{4\sqrt{\omega_1\omega_2}}
\ \xrightarrow{\omega_2\simeq\omega_p}\
\frac{|a_0|c|k_2|}{4}\sqrt{\frac{\omega_p}{\omega_1}} \tag{5}
$$

这是振幅增长率。单纯的均匀指数增长中，强度按 \(e^{2gt}\) 增长。若用包络时间阻尼率 \(\nu_1,\nu_2\) 并取精确共振，局域模满足

$$
(s+\nu_1)(s+\nu_2)=g^2,\qquad
s_+=-\frac{\nu_1+\nu_2}{2}+
\sqrt{g^2+\frac{(\nu_1-\nu_2)^2}{4}}.
$$

因此有局域正增长的条件是 \(g^2>\nu_1\nu_2\)。对于无阻尼的纯频率失谐 \(\Delta=\omega_0-\omega_1-\omega_2\)，将差频相位均分到两个包络，得到指数的实增长部分 \(\operatorname{Re}\sqrt{g^2-(\Delta/2)^2}\)。这两个结果描述均匀、固定泵浦的局部问题。实际传播中还需考虑空间失谐、群速滑移和有限泵浦。

### 5.2 传播中的时空解

取冷极限 \(v_2=0\)，用种子随动时间 \(\zeta=t-x/v_1\) 和传播坐标 \(\tau=x/v_1\)。坐标原点取在种子注入边界，\(\tau\) 沿其传播方向增大。此时

$$
D_1=\partial_\tau,\qquad D_2=\partial_\zeta,\qquad
\partial_\tau S=g B^*,\quad \partial_\zeta B^*=gS 
$$

(这里算符变换可参见附录) 施加阶跃种子 \(S(0,\zeta)=S_{\rm in}\)（这里参数依次为 \(\tau,\zeta\)）和 \(B(\tau,0)=0\)。消元并积分

$$
S(\tau,\zeta)=S_{\rm in}
+g^2\int_0^\tau d\tau'\int_0^\zeta d\zeta'\,S(\tau',\zeta')
$$

迭代时每积分一次得到一个 \(1/m!\)，所以

$$
S(\tau,\zeta)=S_{\rm in}\sum_{m=0}^{\infty}
\frac{(g^2\tau\zeta)^m}{(m!)^2}
=S_{\rm in}I_0(2g\sqrt{\tau\zeta}) \tag{6}
$$

这里\(I_0\) 是**零阶第一类修正贝塞尔函数**。用 Laplace 变换也可得到同一结果

$$
\widehat S(\tau,s)=\frac{S_{\rm in}}{s}e^{g^2\tau/s}
$$

若改用一般因果种子 \(S_{\rm in}(\zeta)\)，右边的 \(S_{\rm in}/s\) 换成 \(\widehat S_{\rm in}(s)\)，实际时域解相应成为卷积。大参数下 \(I_0(y)\sim e^y/\sqrt{2\pi y}\)，因此图 2(b) 的增益指数含 \(\sqrt{\zeta\tau}\)。式 (6) 的固定泵浦和阶跃种子是解析边界条件，有限高斯泵浦的放大区受两束光的重叠窗口约束。

## 6. 前向与后向的冷共振与算例

令 \(r=\omega_p/\omega_0\)。在冷极限，

$$
\omega_1=\omega_0(1-r),\quad
\frac{ck_0}{\omega_0}=\sqrt{1-r^2},\quad
\frac{ck_1}{\omega_0}=\pm\sqrt{1-2r}.
$$

前向取正，后向取负。两者的 Stokes 传播条件均为 \(r<1/2\)，相当于 \(\lambda_1<2\lambda_0\)。当 \(r\ll1\)，前向的 \(ck_2\simeq\omega_p\)，后向的 \(ck_2\simeq 2\omega_0\)，由式 (5) 得

$$
g_F\simeq\frac{|a_0|\omega_p}{4}\sqrt{\frac{\omega_p}{\omega_0}},
\qquad
g_B\simeq\frac{|a_0|}{2}\sqrt{\omega_p\omega_0}.
$$

取 Lei 正文的 \(\lambda_0=1.0\,\mu\mathrm m\)、\(\lambda_1=1.8\,\mu\mathrm m\)、\(a_0=0.0854\)。以下采用由波长比反推的精确冷共振密度，论文用约 \(0.20n_{c,0}\) 表示：

$$
r=\frac49,\quad
n_e/n_{c,0}=r^2\simeq0.19753,\quad
n_e/n_{c,1}=0.64 .
$$

| 量                   |       前向 |       后向 |
| -------------------- | ---------: | ---------: |
| \(v_0/c\)            |      0.896 |      0.896 |
| \(v_1/c\)            |     +0.600 |     −0.600 |
| \(ck_2/\omega_0\)    |      0.562 |      1.229 |
| \(v_{\phi,2}/c\)     |      0.790 |      0.362 |
| \(g/\omega_0\)       |     0.0107 |     0.0235 |
| \(1/g\)              |   约 49 fs |   约 23 fs |
| 泵浦相对种子滑移速度 | \(0.296c\) | \(1.496c\) |

两个 \(1/g\) 都是局域**振幅**时间尺度。用一个定长泵浦作几何估计，重叠时间约为其在等离子体中的空间长度 \(L_p\) 除以 \(|v_0-v_1|\)。如果输入的是泵浦在固定位置测得的时间宽度 \(T_p\)，在忽略展宽的近似下 \(L_p\simeq v_0T_p\)。这个算例中，前向局域增长率较低，但同样空间长度的泵浦对应约五倍的重叠时间。预测最终增益仍需沿特征线使用真实包络，特别是在泵浦开始耗尽后。

## 7. 非线性泵浦耗尽与自相似约化

### 7.1 先用局域解理解能量回传

暂时忽略传播，令三波相位锁定为实包络。以初始泵浦 \(P_m>0\)、种子 \(S_i>0\)、\(B_i=0\) 为例，有

$$
P^2+B^2=P_m^2,\qquad S^2-B^2=S_i^2.
$$

可以令 \(P=P_m\cos\vartheta\)，\(B=P_m\sin\vartheta\)，则

$$
\dot\vartheta=\kappa S,\qquad
S^2=S_i^2+P_m^2\sin^2\vartheta.
$$

在 \(\vartheta=\pi/2\)，泵浦振幅第一次到零，种子达到局域最大。其后 \(P\) 变号，交换项 \(Q\) 变号。这个局域解说明了能量回传的可能性。有限脉冲中，泵浦滑出种子、阻尼、失谐及传播都会改变这一过程。

### 7.2 随动坐标下的传播方程与边界

仍用 \((\zeta,\tau)\)，保留泵浦耗尽，令 \(\mu=1-v_0/v_1\)。冷 EPW 和相位锁定的实包络满足

$$
\left(\mu\partial_\zeta+\frac{v_0}{v_1}\partial_\tau\right)P
=-\kappa SB,\qquad
\partial_\tau S=\kappa PB,\qquad
\partial_\zeta B=\kappa PS . \tag{7}
$$

当泵浦随 \(\tau\) 的变化项相对其随 \(\zeta\) 的变化项小，即
\(\left|(v_0/v_1)P_\tau\right|\ll|\mu P_\zeta|\)，可做短种子约化。此时由第一和第三式直接得到

$$
\partial_\zeta\left(P^2+\frac{B^2}{\mu}\right)=0. \tag{8}
$$

在此坐标中，\(\mu\) 的符号至关重要。后向时 \(\mu>0\)，泵浦和冷 EPW 的特征线都朝 \(\zeta\) 增大的方向。前向且 \(v_0>v_1\) 时 \(\mu<0\)，泵浦特征线朝 \(\zeta\) 减小的方向，冷 EPW 则沿 \(\zeta\) 增大演化。因而前向约化需要从不同侧施加泵浦入流与 EPW 初始条件。式 (8) 的前向减号是随动坐标里的通量关系，与实验室坐标的正作用量密度守恒相容。

### 7.3 后向的圆函数支与径向 sine–Gordon 形式

对 \(\mu>0\)，取式 (8) 的积分常数为固定的 \(P_m^2\)，写成

$$
P=P_m\cos(U/2),\qquad B=\sqrt{\mu}P_m\sin(U/2).
$$

由 EPW 方程得 \(S=\sqrt{\mu}\,U_\zeta/(2\kappa)\)，代入种子方程：

$$
U_{\zeta\tau}=\kappa^2P_m^2\sin U.
$$

若初值和边界适合自相似形式，令 \(\xi=2\kappa P_m\sqrt{\zeta\tau}\)，取 \(U=U(\xi)\)。由于

$$
\xi_\zeta\xi_\tau=\kappa^2P_m^2,\qquad
\xi_{\zeta\tau}=\frac{\kappa^2P_m^2}{\xi},
$$

所以

$$
U''+\frac{U'}{\xi}=\sin U. \tag{9}
$$

对小 \(U\) 线性化并要求 \(\xi=0\) 正则，得 \(U\simeq U(0)I_0(\xi)\)。在 \(U=\pi+w\)、\(|w|\ll1\) 附近，\(w''+w'/\xi=-w\)，局部解是 \(J_0\) 与 \(Y_0\) 的线性组合。若在非零 \(\xi_*\) 将两个分段近似接起来，要匹配 \(U\) 和 \(U'\)。仅调一个 \(J_0\) 系数通常只能保证一项。正文和 SI 的 Bessel 拼接可作为形状近似，数值积分完整非线性 ODE 更适合检查峰值和回传位置。

在小 \(\xi\) 区域，\(U'/\xi\simeq U(0)/2\)，同时 \(\partial_\zeta\xi=2\kappa^2P_m^2\tau/\xi\)，故 \(S\propto P_m^2\tau U(0)\)，强度随传播坐标平方增长。这个计算展示了自相似早段平方标度的来源。其系数依赖有效种子面积、归一化和分支边界。

### 7.4 前向分支的符号检查与 SI 对照

对 \(\mu=-\alpha<0\)，若为检查局部方程，暂把式 (8) 的积分常数选作正的固定 \(P_m^2\)，可写

$$
P=P_m\cosh(U/2),\qquad B=\sqrt{\alpha}P_m\sinh(U/2).
$$

将其代回式 (7) 的短种子约化，得到 \(S=\sqrt{\alpha}\,U_\zeta/(2\kappa)\)，以及

$$
U_{\zeta\tau}=\kappa^2P_m^2\sinh U,\qquad
U''+\frac{U'}{\xi}=\sinh U
$$

（最后一步仍假定相同的自相似形式）。这里固定正积分常数只是用于核查代数。实际前向问题的积分常数由两侧边界共同决定，可以随 \(\tau\) 变化。固定正积分常数的实双曲函数支本身无法描述 \(P\) 穿过零。

SI I.C 先得到双曲形式，再用 \(\tilde\nu=i\tilde u\) 写成正弦形式。作为标量 ODE 的复解析延拓，这一步成立。**把延拓后的解解释为原前向三波方程中的物理包络，还要重新核对复共轭和入流边界。** 检查方法很直接：将重建的 \(P,S,B\) 代入原一阶方程，并核对式 (8) 中的模方与符号。在具有复共轭的方程组里，直接旋转变量到复轴并不保证继续满足同一物理方程。正文图 3 可作为作者自相似模型的结果阅读。对于前向有限脉冲的定量泵浦耗尽、首峰和回传位置，式 (7) 的全双曲系统及 PIC 是更直接的验证对象。

## 8. 超出理想三波模型的物理

### 8.1 有限温度和动理学

温度首先通过 Bohm–Gross 项提高 \(\omega_2\)，从而改动频率匹配。弱热修正下

$$
\omega_2-\omega_p\simeq\frac{3k_2^2v_T^2}{2\omega_p}.
$$

固定密度和光频时，后向分支较大的 \(k_2\) 使热频移更显著。电子在 \(v_x\simeq v_{\phi,2}\) 附近能与 EPW 共振，Landau 阻尼取决于速度分布在该处的斜率。EPW 很强时，俘获、非线性频移和波破还可能改变饱和。SI 图 S8 以本算例前向 \(v_{\phi,2}\simeq0.79c\) 和较低的背景电子速度作比较。用温度依赖的流体压力闭合可以描述热频移，速度分布及俘获则需动理学模型。

### 8.2 非均匀密度

若背景缓慢变化，给每个载波写局域相位
\(\theta_j(x,t)=\int^x k_j(x')dx'-\omega_j t\)。混频项的相位包含
\(\int^x[k_0(x')-k_1(x')-k_2(x')]dx'\)。也可选用由两束光直接确定的电子波拍频相位，然后把 \(\omega_0-\omega_1-\omega_2(x)\) 放进 EPW 的失谐项。这两种写法需要一致地处理所选参考相位。SI 图 S9–S10 的梯度和波动算例说明，在有限重叠、有限带宽下，显著增益可以分布在共振位置附近的一段区域。用非均匀密度时，单个密度波动百分比无法确定积累的相位误差。

### 8.3 Anti-Stokes、有限带宽与 SRS/SBS 区分

密度波也可将泵浦散射到 \(\omega_0+\omega_2\)、\(k_0+k_2\) 附近。是否需要跟踪这个 anti-Stokes 分支，要检查它与电磁色散面之间的失谐，以及作用长度和带宽。低密度近前向传播时，光学色散曲线在相关频段较平坦，Stokes 与 anti-Stokes 都可能需要保留，形成多波耦合。Decker 等的前向散射理论从这里接上。SBS 则把纵向中介改成离子声波，低频响应和耦合参数需要从含离子运动的模型重新推导。

### 8.4 自压缩与增益分开诊断

冷等离子体的线性波数 \(k(\omega)=\sqrt{\omega^2-\omega_p^2}/c\) 给出

$$
k''(\omega)=-\frac{\omega_p^2}{c(\omega^2-\omega_p^2)^{3/2}}<0.
$$

种子脱离泵浦后，强场诱导的折射率变化可使其积累自相位调制，随后由色散调整不同频率分量的相对到达时间。这个过程需要种子的强度与谱相位信息。正文图 4 的 1D 输出为 \(120\) fs 到 \(9.19\) fs，峰值强度由 \(10^{12}\) 增至 \(8.9\times10^{16}\,\mathrm{W/cm^2}\)。\(9.19\) fs 对应约 1.5 个入射种子载波周期。SI 图 S4 的短种子在放大阶段先展宽，随后自压缩。分辨两段时，分别记录泵浦刚滑过种子时和真空出口处的种子能量、FWHM、峰值、光谱强度与光谱相位。多维模拟还要记录光斑随时间的变化。

## 9. 对照正文、SI 与经典文献

| 阅读位置                    | 推导或检验                                                   |
| --------------------------- | ------------------------------------------------------------ |
| SI I.A，式 (1)–(14)         | 对照本文第 2–3 节，从实场展开逐项检查 \(1/2\) 因子、复共轭和正负波数。 |
| SI I.B、图 S1 与正文图 2    | 对照第 5–6 节，检查 Bessel 解、局域增长率和有限重叠窗口。    |
| SI I.C、图 S2–S3 与正文图 3 | 对照第 7 节。先导出守恒式，再验证自相似重建解与一阶方程的相容性。 |
| 正文图 4–6、SI 图 S4–S10    | 对照第 8 节，区分能量增益、时间压缩、横向变化和动理学失稳。  |

1. Z.-Y. Lei et al., *Towards the Generation of Petawatt Near-Infrared Few-Cycle Light Pulses via Forward Raman Amplification in Plasma*, PRL **134**, 255001 (2025)。[正文](https://doi.org/10.1103/cshj-jgz7) · [补充材料](https://link.aps.org/supplemental/10.1103/cshj-jgz7)
2. D. W. Forslund, J. M. Kindel, E. L. Lindman, *Theory of stimulated scattering processes in laser-irradiated plasmas*, Phys. Fluids **18**, 1002 (1975)。[DOI](https://doi.org/10.1063/1.861248)
3. C. D. Decker, W. B. Mori, T. Katsouleas, D. E. Hinkel, *Spatial temporal theory of Raman forward scattering*, Phys. Plasmas **3**, 1360 (1996)。[DOI](https://doi.org/10.1063/1.871728)
4. D. L. Fisher, T. Tajima, *Enhanced Raman forward scattering*, PRE **53**, 1844 (1996)。[DOI](https://doi.org/10.1103/PhysRevE.53.1844)
5. V. M. Malkin, G. Shvets, N. J. Fisch, *Fast Compression of Laser Beams to Highly Overcritical Powers*, PRL **82**, 4448 (1999)。[DOI](https://doi.org/10.1103/PhysRevLett.82.4448)
6. O. Shorokhov, A. Pukhov, I. Kostyukov, *Self-Compression of Laser Pulses in Plasma*, PRL **91**, 265002 (2003)。[DOI](https://doi.org/10.1103/PhysRevLett.91.265002)

## 附录

把 \(S(x,t)\) 写成同一个场在新坐标下的形式 \(\widetilde S(\zeta,\tau)\)。算符变换就是对这个复合函数用**链式法则**。要特别留意每次求偏导时固定的是哪个变量。

### 1. 固定 \(x\)，改变 \(t\)

由 \(\zeta=t-x/v_1\)、\(\tau=x/v_1\) 可见，固定 \(x\) 时，\(t\) 增加 \(dt\)，\(\zeta\) 就增加 \(dt\)，而 \(\tau\) 不变。因此

\[ \left.\partial_t\right|_x =\left.\partial_\zeta\right|_\tau. \]

### 2. 固定 \(t\)，改变 \(x\)

固定 \(t\) 时，\(x\) 增加 \(dx\)，\(\zeta\) 减少 \(dx/v_1\)，而 \(\tau\) 增加 \(dx/v_1\)。因此

\[ \left.\partial_x\right|_t =-\frac{1}{v_1}\left.\partial_\zeta\right|_\tau +\frac{1}{v_1}\left.\partial_\tau\right|_\zeta. \]

### 3. 代回两个传播算符

对种子，

\[ D_1=\partial_t+v_1\partial_x =\partial_\zeta+v_1\left(-\frac{1}{v_1}\partial_\zeta +\frac{1}{v_1}\partial_\tau\right) =\boxed{\partial_\tau}. \]

直观上，**沿种子群速度轨迹走**意味着 \(dx=v_1dt\)，所以 \(d\zeta=dt-dx/v_1=0\)，而 \(d\tau=dt\)。你始终跟着种子的同一个随动时间切片，看它沿传播方向如何增长。

对电子波，冷等离子体近似下 \(v_2\simeq0\)，所以

\[ D_2=\partial_t+v_2\partial_x\simeq\partial_t =\boxed{\partial_\zeta}. \]

这对应**停在固定位置 \(x\)**，看电子波如何随时间建立。若保留 \(v_2\)，则完整变换是

\[ D_2=\left(1-\frac{v_2}{v_1}\right)\partial_\zeta +\frac{v_2}{v_1}\partial_\tau. \]

因此原方程变成 \(\partial_\tau S=gB^*\)、\(\partial_\zeta B^*=gS\)。