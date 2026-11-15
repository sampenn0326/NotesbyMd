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
u(x,z)=\int _{-\infty}^{\infty} \hat{u}(k_x,z) e^{ik_x x}\mathrm{d}k_x \tag{2}
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
H(k_x;\Delta z,\omega ) = \exp \left[ i\Delta z\sqrt{nk_0^2 -k_x^2} \right] \tag{8}
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

### 2.1 式中的平方根色散关系

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

## 6．等离子体密度如何变成透镜？

SI S7 使用的密度模型为

$$
n_e(r)=n_{e0}\left[1+0.33\frac{r^2}{r_{\rm ch}^2}\right],
$$

$$
n_{e0}=0.7364\,n_a.
$$

这里 $r_{\rm ch}$ 是毛细管半径，$n_a$ 是初始**原子氢**密度。若从氢分子气压换算，在理想气体和相应温度假设下，

$$
n_a=2\frac{p}{k_BT}.
$$

这个因子 2 不能漏掉。

等离子体折射率为

$$
n(r,\omega)=\sqrt{1-\frac{\omega_p^2(r)}{\omega^2}},\qquad\omega_p^2(r)=\frac{e^2n_e(r)}{\varepsilon_0m_e}.
$$

在 XUV 条件下，$\omega\gg\omega_p$，所以

$$
n(r,\omega)\approx1-\frac{\omega_p^2(r)}{2\omega^2}.
$$

因此：

$$
\text{离轴密度较高}\Rightarrow\text{离轴折射率较低}\Rightarrow\text{形成聚焦所需的横向相位曲率}
$$

假设透镜内光束横向移动不大，长度为 $L$，相对于同长度真空的相位为

$$
\phi(r,\omega)=k_0[n(r,\omega)-1]L.
$$

代入抛物线密度：

$$
\phi(r,\omega)\approx-\frac{\omega_{p0}^2L}{2c\omega}-\frac{0.33\,\omega_{p0}^2L}{2c\omega r_{\rm ch}^2}r^2.
$$

第一项与横向位置无关，主要影响频谱相位及群延迟；第二项是透镜所需的二次相位。

与薄透镜相位

$$
\phi_{\rm lens}=-\frac{k_0r^2}{2f}
$$

比较，得到

$$
\boxed{f(\omega)\approx\frac{\omega^2r_{\rm ch}^2}{0.33\,\omega_{p0}^2L}\approx\frac{3\omega^2r_{\rm ch}^2}{\omega_{p0}^2L}}
$$

这就是 SI S13 的焦距关系。

它直接说明：

$$
f\propto\frac{\omega^2}{n_{e0}L}
$$

较低频率受到更强聚焦；提高密度曲率或增加长度，可以增强透镜作用。

但这个 $f$ 是有效薄透镜焦距。**实际束腰位置还受入射束腰、波前曲率、衍射以及透镜内部传播影响。**

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





































