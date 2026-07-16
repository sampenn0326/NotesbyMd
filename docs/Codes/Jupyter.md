说明：在Jupyter上分析WarpX跑完之后的诊断文件。针对不同的模拟有一些可以固定的notebook，遂记录备用。但超算运行Jupyter画图好像不如直接提交作业快，迟早进入故纸堆。



## 1.物种数密度



### 1.1 单步



### 1.2 多步静态叠加

适合于薄靶RPA，选取合适的cmap(最低值对应白色)，可以比较紧凑地展示靶的形状变化。不同时间步之间避免重合，因为是数密度值的直接相加。

```python
# =========== 多步叠加数密度图(直接相加) v1.1.13===========
import numpy as np
import matplotlib.pyplot as plt
from openpmd_viewer import OpenPMDTimeSeries
import os
import warnings
from scipy import constants as C

# ==================== 参数配置 ====================
data_path = '../diagCP/field'
fig_dir = '../fig'
SPECIES = 'hydrogen'           # 物种
FIELD = f'rho_{SPECIES}'       # 场量

# 文件名设置
FILENAME = 'ni_multistep_CP.png'  # 保存文件名

# 物理常数
lambda0 = 1e-6
CHARGE = C.e
T0 = lambda0/C.c
nc = 1.1e27                    # 临界密度

# 单位换算因子（原始数据 -> 绘图单位）
DX = 7e-6         # 横轴（z方向）: m -> um
DY = 8e-6         # 纵轴（x方向）: m -> um
DT = T0           # 时间: s -> T0
DN = CHARGE * nc  # 电荷密度 -> nc单位（除以DN得到归一化密度）

# 单位标签
Z_UNIT = '$R_c$'
X_UNIT = '$R_0$'
T_UNIT = '$T_0$'
N_UNIT = '$n_c$'

# 绘图参数
FIG_SIZE = (10, 6)              # 图形大小
DPI = 150                       # 保存分辨率
CMAP = 'gnuplot2_r'                # 颜色映射

# 字体大小配置
AXIS_LABEL_FONTSIZE = 20        # 坐标轴标签字号
AXIS_TICK_FONTSIZE = 18         # 坐标轴数字（刻度）字号
CBAR_LABEL_FONTSIZE = 20        # colorbar标签字号
CBAR_TICK_FONTSIZE = 18         # colorbar数字（刻度）字号

# ==================== 叠加配置 ====================
# 选择的时间步（帧索引或时间值）
TIME_STEPS = [0,11,22,33,44,57,68]  # 要叠加的时间步

# 空间范围
Z_RANGE = None              # None/(z1,z2)
X_RANGE = None              # None/(x1,x2)

# 密度范围（所有时间步共用相同的颜色映射）
N_RANGE = (0, 150)             # 密度范围, None表示自动

# ==================== 加载数据 ====================
print("正在加载诊断数据...")
ts = OpenPMDTimeSeries(data_path)

# 创建保存目录
os.makedirs(fig_dir, exist_ok=True)

# 获取所有迭代和时间
all_iterations = ts.iterations
all_times = ts.t
all_times_T0 = all_times / DT
print(f"总可用步数: {len(all_iterations)}")

# ==================== 处理时间步 ====================
def get_iteration_from_time(ts, time_value):
    """根据时间值获取对应的迭代索引"""
    time_sec = time_value * DT
    idx = np.argmin(np.abs(ts.t - time_sec))
    return idx, ts.iterations[idx]

selected_frames = []
selected_times_val = []

for step in TIME_STEPS:
    if isinstance(step, int) and step < len(all_iterations):
        selected_frames.append(step)
        selected_times_val.append(all_times_T0[step])
        print(f"选择帧 {step}, 时间 t={all_times_T0[step]:.2f} {T_UNIT}")
    elif isinstance(step, (float, int)):
        idx, iteration = get_iteration_from_time(ts, step)
        selected_frames.append(idx)
        selected_times_val.append(step)
        print(f"选择时间 t={step} {T_UNIT}, 对应帧 {idx}")
    else:
        raise ValueError(f"无法识别的时间步格式: {step}")

n_steps = len(selected_frames)
print(f"\n共选择 {n_steps} 个时间步进行叠加")

# ==================== 获取坐标信息 ====================
_, info_first = ts.get_field(field=FIELD, iteration=all_iterations[selected_frames[0]])
z_coords_full = info_first.z / DX
x_coords_full = info_first.x / DY

# 应用空间范围
def get_indices_and_extent(coords, range_val, unit_label):
    if range_val is None:
        return slice(None), (coords[0], coords[-1])
    else:
        mask = (coords >= range_val[0]) & (coords <= range_val[1])
        indices = np.where(mask)[0]
        if len(indices) == 0:
            warnings.warn(f"范围 {range_val} {unit_label} 内无数据")
            return slice(None), (coords[0], coords[-1])
        return indices, [range_val[0], range_val[1]]

z_indices, z_extent = get_indices_and_extent(z_coords_full, Z_RANGE, Z_UNIT)
x_indices, x_extent = get_indices_and_extent(x_coords_full, X_RANGE, X_UNIT)
extent = [z_extent[0], z_extent[1], x_extent[0], x_extent[1]]

# ==================== 读取并叠加数据 ====================
print("\n正在读取并叠加数据...")
sum_density = None

for idx, frame in enumerate(selected_frames):
    iteration = all_iterations[frame]
    rho, _ = ts.get_field(field=FIELD, iteration=iteration)
    n_norm = rho / DN
    
    # 应用空间裁剪
    n_cropped = n_norm[z_indices, :][:, x_indices]
    
    # 直接相加
    if sum_density is None:
        sum_density = n_cropped.copy()
    else:
        sum_density += n_cropped
    
    print(f"  已叠加: t={selected_times_val[idx]:.2f}{T_UNIT}")

# ==================== 计算密度范围 ====================
if N_RANGE is None:
    VMIN, VMAX = 0, np.max(sum_density)
    print(f"\n自动密度范围: 0 - {VMAX:.2f} {N_UNIT}")
else:
    VMIN, VMAX = N_RANGE
    print(f"\n指定密度范围: {VMIN} - {VMAX} {N_UNIT}")

# ==================== 绘制叠加结果 ====================
fig, ax = plt.subplots(figsize=FIG_SIZE)

# 转置用于显示
sum_display = sum_density.T

# 绘制叠加结果
im = ax.imshow(sum_display, cmap=CMAP, extent=extent,
               origin='lower', aspect='auto',
               vmin=VMIN, vmax=VMAX)

# 设置坐标轴标签和刻度字号
ax.set_xlabel(f'z ({Z_UNIT})', fontsize=AXIS_LABEL_FONTSIZE)
ax.set_ylabel(f'x ({X_UNIT})', fontsize=AXIS_LABEL_FONTSIZE)

# 设置坐标轴刻度数字字号
ax.tick_params(axis='both', which='major', labelsize=AXIS_TICK_FONTSIZE)

# 添加颜色条（分别设置标签和刻度字号）
cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label(f'$n_i$ ({N_UNIT})', fontsize=CBAR_LABEL_FONTSIZE)
cbar.ax.tick_params(labelsize=CBAR_TICK_FONTSIZE)

# 添加网格
ax.grid(True, alpha=0.2, linestyle=':', linewidth=0.5)

# ==================== 保存图片 ====================
save_path = os.path.join(fig_dir, FILENAME)
plt.savefig(save_path, dpi=DPI, bbox_inches='tight')
print(f"\n图片已保存: {save_path}")

# ==================== 显示信息 ====================
print("\n=== 叠加信息 ===")
print(f"叠加时间步数: {n_steps}")
print(f"时间步列表: {[f'{t:.2f}' for t in selected_times_val]} {T_UNIT}")
print(f"时间范围: {selected_times_val[0]:.2f} - {selected_times_val[-1]:.2f} {T_UNIT}")
print(f"密度范围: {VMIN:.2f} - {VMAX:.2f} {N_UNIT}")
print(f"最大叠加值: {np.max(sum_density):.2f} {N_UNIT}")

plt.show()
```



多步叠加双模拟对比版(不过是共享坐标轴与colorbar)

```python
# =========== 多步叠加数密度(直接相加) 双模拟对比v1.1.13 ===========
import numpy as np
import matplotlib.pyplot as plt
from openpmd_viewer import OpenPMDTimeSeries
import os
import warnings
from scipy import constants as C

# ==================== 参数配置 ====================
# 模拟1路径
data_path1 = '../diagc1/field'      # 修改为你的第一个模拟路径
# 模拟2路径
data_path2 = '../diagp1/field'     # 修改为你的第二个模拟路径

fig_dir = '../fig'
SPECIES = 'hydrogen'           # 物种
FIELD = f'rho_{SPECIES}'       # 场量

# 文件名设置
FILENAME = 'ni_multistep_compare.png'  # 保存文件名

# 物理常数
lambda0 = 1e-6
CHARGE = C.e
T0 = lambda0/C.c
nc = 1.1e27                    # 临界密度

# 单位换算因子（原始数据 -> 绘图单位）
DX = 1e-6         # 横轴（z方向）: m -> um
DY = 1e-6         # 纵轴（x方向）: m -> um
DT = T0           # 时间: s -> T0
DN = CHARGE * nc  # 电荷密度 -> nc单位（除以DN得到归一化密度）

# 单位标签
Z_UNIT = '$\mu m$'
X_UNIT = '$\mu m$'
T_UNIT = '$T_0$'
N_UNIT = '$n_c$'

# 绘图参数
FIG_SIZE = (12, 5)              # 图形大小
DPI = 150                       # 保存分辨率
FONT_SIZE = 12                  # 字体大小
SUBPLOT_ADJUST = {'wspace': 0.05}  # 子图间距

# ==================== 叠加配置 ====================
# 选择的时间步（帧索引或时间值）
TIME_STEPS = [12, 24, 36, 48, 60, 72, 84]  # 要叠加的时间步

# 空间范围
Z_RANGE = (-1,9)              # z方向范围，None表示全部
X_RANGE = None              # x方向范围，None表示全部

# 颜色映射
CMAP = 'hot_r'                 # 颜色映射

# 密度范围（两个模拟共用相同的颜色映射）
N_RANGE = (0, 600)             # 密度范围, None表示自动

# ==================== 定义加载和处理函数 ====================
def load_and_sum(data_path, time_steps, z_indices, x_indices):
    """加载并叠加指定时间步的密度数据"""
    print(f"\n正在处理: {data_path}")
    ts = OpenPMDTimeSeries(data_path)
    
    all_iterations = ts.iterations
    all_times = ts.t
    all_times_T0 = all_times / DT
    
    def get_iteration_from_time(ts, time_value):
        """根据时间值获取对应的迭代索引"""
        time_sec = time_value * DT
        idx = np.argmin(np.abs(ts.t - time_sec))
        return idx, ts.iterations[idx]
    
    selected_frames = []
    selected_times_val = []
    
    for step in time_steps:
        if isinstance(step, int) and step < len(all_iterations):
            selected_frames.append(step)
            selected_times_val.append(all_times_T0[step])
            print(f"选择帧 {step}, 时间 t={all_times_T0[step]:.2f} {T_UNIT}")
        elif isinstance(step, (float, int)):
            idx, iteration = get_iteration_from_time(ts, step)
            selected_frames.append(idx)
            selected_times_val.append(step)
            print(f"选择时间 t={step} {T_UNIT}, 对应帧 {idx}")
        else:
            raise ValueError(f"无法识别的时间步格式: {step}")
    
    # 读取并叠加数据
    sum_density = None
    for idx, frame in enumerate(selected_frames):
        iteration = all_iterations[frame]
        rho, _ = ts.get_field(field=FIELD, iteration=iteration)
        n_norm = rho / DN
        
        # 应用空间裁剪
        n_cropped = n_norm[z_indices, :][:, x_indices]
        
        if sum_density is None:
            sum_density = n_cropped.copy()
        else:
            sum_density += n_cropped
        
        print(f"  已叠加: t={selected_times_val[idx]:.2f}{T_UNIT}")
    
    return sum_density, selected_times_val

# ==================== 获取坐标信息（使用第一个模拟） ====================
print("正在加载诊断数据...")
ts1 = OpenPMDTimeSeries(data_path1)
all_iterations1 = ts1.iterations

_, info_first = ts1.get_field(field=FIELD, iteration=all_iterations1[0])
z_coords_full = info_first.z / DX
x_coords_full = info_first.x / DY

# 应用空间范围
def get_indices_and_extent(coords, range_val, unit_label):
    if range_val is None:
        return slice(None), (coords[0], coords[-1])
    else:
        mask = (coords >= range_val[0]) & (coords <= range_val[1])
        indices = np.where(mask)[0]
        if len(indices) == 0:
            warnings.warn(f"范围 {range_val} {unit_label} 内无数据")
            return slice(None), (coords[0], coords[-1])
        return indices, [range_val[0], range_val[1]]

z_indices, z_extent = get_indices_and_extent(z_coords_full, Z_RANGE, Z_UNIT)
x_indices, x_extent = get_indices_and_extent(x_coords_full, X_RANGE, X_UNIT)
extent = [z_extent[0], z_extent[1], x_extent[0], x_extent[1]]

# ==================== 加载两个模拟的数据 ====================
# 创建保存目录
os.makedirs(fig_dir, exist_ok=True)

# 处理模拟1
sum_density1, times1 = load_and_sum(data_path1, TIME_STEPS, z_indices, x_indices)

# 处理模拟2
sum_density2, times2 = load_and_sum(data_path2, TIME_STEPS, z_indices, x_indices)

# ==================== 计算密度范围 ====================
if N_RANGE is None:
    vmin = 0
    vmax = max(np.max(sum_density1), np.max(sum_density2))
    print(f"\n自动密度范围: {vmin:.2f} - {vmax:.2f} {N_UNIT}")
else:
    vmin, vmax = N_RANGE
    print(f"\n指定密度范围: {vmin} - {vmax} {N_UNIT}")

# ==================== 绘制对比图 ====================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIG_SIZE)
plt.subplots_adjust(**SUBPLOT_ADJUST)  # 设置子图间距

# 转置用于显示
sum_display1 = sum_density1.T
sum_display2 = sum_density2.T

# 绘制模拟1

im1 = ax1.imshow(sum_display1, cmap=CMAP, extent=extent,
                 origin='lower', aspect='auto',
                 vmin=vmin, vmax=vmax)
ax1.axhline(y=0, color='black', linestyle='--', linewidth=1.5, alpha=0.8)
ax1.set_xlabel(f'z ({Z_UNIT})', fontsize=FONT_SIZE )
ax1.set_ylabel(f'x ({X_UNIT})', fontsize=FONT_SIZE )
ax1.grid(True, alpha=0.2, linestyle=':', linewidth=0.5)
ax1.tick_params(axis='y', labelsize=12)
ax1.tick_params(axis='x', labelsize=12)

# 绘制模拟2 - 保留z坐标，只隐藏y轴（x方向）的刻度数字和标签
im2 = ax2.imshow(sum_display2, cmap=CMAP, extent=extent,
                 origin='lower', aspect='auto',
                 vmin=vmin, vmax=vmax)
ax2.axhline(y=0, color='black', linestyle='--', linewidth=1.5, alpha=0.8)
ax2.set_xlabel(f'z ({Z_UNIT})', fontsize=FONT_SIZE )  # 保留z坐标标签
ax2.set_ylabel('')  # 清空y轴标签（x方向）

# 只隐藏y轴（左侧）的刻度数字，保留x轴的刻度数字
ax2.tick_params(axis='y', labelleft=False, labelsize=12)  # 隐藏y轴刻度数字
ax2.tick_params(axis='x', labelbottom=True, labelsize=12)  # x轴刻度数字保留（默认就是True）

ax2.grid(True, alpha=0.2, linestyle=':', linewidth=0.5)

# 添加右侧colorbar（两个子图共用）
cbar = fig.colorbar(im2, ax=[ax1, ax2], label=f'$n_i$ ({N_UNIT})',
                    fraction=0.046, pad=0.02)
cbar.ax.tick_params(labelsize=FONT_SIZE )
cbar.set_label(f'$n_i$ ({N_UNIT})', fontsize=12) 

# ==================== 保存图片 ====================
save_path = os.path.join(fig_dir, FILENAME)
plt.savefig(save_path, dpi=DPI, bbox_inches='tight')
print(f"\n图片已保存: {save_path}")

# ==================== 显示信息 ====================
print("\n=== 叠加信息 ===")
print(f"叠加时间步数: {len(TIME_STEPS)}")
print(f"时间步列表: {[f'{t:.2f}' for t in times1]} {T_UNIT}")
print(f"时间范围: {times1[0]:.2f} - {times1[-1]:.2f} {T_UNIT}")
print(f"密度范围: {vmin:.2f} - {vmax:.2f} {N_UNIT}")
print(f"模拟1最大叠加值: {np.max(sum_density1):.2f} {N_UNIT}")
print(f"模拟2最大叠加值: {np.max(sum_density2):.2f} {N_UNIT}")

plt.show()
```































## 2.数密度的横向FT

```Python
# =========== 氢离子数密度对z平均的时间演化（独立图1） ===========
import numpy as np
import matplotlib.pyplot as plt
from openpmd_viewer import OpenPMDTimeSeries
import os

# ==================== 参数配置 ====================
data_path = '../diags_inputp1/field'
fig_dir = '../fig'
SPECIES = 'electrons'
FIELD = f'rho_{SPECIES}'

# 物理常数
c = 3e8
lambda0 = 1e-6
T0 = lambda0 / c
nc = -1.1e27
CHARGE = 1.6e-19

# 物理采样参数
dx_phys_meters = 4e-6 / 2000
k0 = 2 * np.pi / lambda0

# 绘图单位
X_UNIT = '$\mu \mathrm{m}$'
KX_UNIT = '$k_0$'
TIME_UNIT = '$T_0$'

# ==================== 绘图参数设置 ====================
PLOT_CONFIG = {
    'save_fig': 0,           # 是否保存图片
    'show_fig': True,           # 是否显示图片
    'fig_format': 'png',        # 图片格式: png, pdf, svg, jpg
    'fig_dpi': 150,             # 图片分辨率
    'fig_width': 6,             # 图片宽度（英寸）
    'fig_height': 5,            # 图片高度（英寸）
    
    # 全局字体设置
    'label_fontsize': 15,       # 坐标轴标签字号
    'tick_fontsize': 14,        # 坐标轴数字字号
    'cbar_label_fontsize': 14,  # colorbar标签字号
    'cbar_tick_fontsize': 13,    # colorbar数字字号
    
    # 图1 (密度图) 显示范围
    'density_vmin': None,           # 密度图颜色最小值
    'density_vmax':None,        # 密度图颜色最大值
    'time_range': [0, 52],    # 时间范围 [t_min, t_max]
    
    # 图2 (频谱图) 显示范围
    'spectrum_vmin': -6,        # 频谱图对数颜色最小值
    'spectrum_vmax': -1,        # 频谱图对数颜色最大值
    'kx_range': [0, 20],        # kx范围 [kx_min, kx_max]
    
    # 输出文件名（不含扩展名）
    'fig1_name': f'P1_{SPECIES}_n1_xt_density',      # 图1文件名
    'fig2_name': f'P1_{SPECIES}_n1_xt_spectrum_log', # 图2文件名
}

# ==================== 加载数据 ====================
ts = OpenPMDTimeSeries(data_path)
os.makedirs(fig_dir, exist_ok=True)

_, info_first = ts.get_field(field=FIELD, iteration=ts.iterations[0])
x_coords = info_first.x / lambda0

# ==================== 计算平均密度 ====================
print("正在加载数据...")
n_xt = []
for iteration in ts.iterations:
    rho, _ = ts.get_field(field=FIELD, iteration=iteration)
    n_i = rho / CHARGE
    n_i_nc = n_i / nc
    n1_x = np.mean(n_i_nc, axis=0)
    n_xt.append(n1_x)

n_xt = np.array(n_xt)
time_axis = ts.t / T0
print(f"数据加载完成: 时间点 {len(time_axis)} 个, 空间点 {len(x_coords)} 个")

# ==================== 傅里叶变换 ====================
print("正在进行傅里叶分析...")
kx_phys = np.fft.fftfreq(len(x_coords), d=dx_phys_meters) * (2 * np.pi)
kx_in_k0 = kx_phys / k0

n1_kxt = np.fft.fft(n_xt, axis=1) / len(x_coords)
n1_spectrum = np.abs(n1_kxt)

positive_k_mask = kx_in_k0 > 0
kx_positive = kx_in_k0[positive_k_mask]
n1_spectrum_positive = n1_spectrum[:, positive_k_mask]

# ==================== 应用显示范围 ====================
# 时间范围裁剪
t_min, t_max = PLOT_CONFIG['time_range']
if t_min is None:
    t_min = time_axis[0]
if t_max is None:
    t_max = time_axis[-1]
time_mask = (time_axis >= t_min) & (time_axis <= t_max)
time_axis_cropped = time_axis[time_mask]
n_xt_cropped = n_xt[time_mask, :]
n1_spectrum_cropped = n1_spectrum_positive[time_mask, :]

# kx范围裁剪
kx_min, kx_max = PLOT_CONFIG['kx_range']
if kx_min is None:
    kx_min = kx_positive[0]
if kx_max is None:
    kx_max = kx_positive[-1]
kx_mask = (kx_positive >= kx_min) & (kx_positive <= kx_max)
kx_positive_cropped = kx_positive[kx_mask]
n1_spectrum_cropped = n1_spectrum_cropped[:, kx_mask]

print(f"裁剪后: 时间范围 [{t_min:.2f}, {t_max:.2f}], kx范围 [{kx_min:.2f}, {kx_max:.2f}]")


# ==================== 图1: n₁(x,t) 密度图 ====================
print("正在绘制图1: 密度图...")
fig1, ax1 = plt.subplots(figsize=(PLOT_CONFIG['fig_width'], PLOT_CONFIG['fig_height']))

im1 = ax1.imshow(n_xt_cropped.T, 
                 extent=[time_axis_cropped[0], time_axis_cropped[-1], 
                         x_coords[0], x_coords[-1]],
                 aspect='auto', origin='lower', cmap='afmhot_r',
                 vmin=PLOT_CONFIG['density_vmin'],
                 vmax=PLOT_CONFIG['density_vmax'])

# 设置坐标轴和colorbar
ax1.set_xlabel(f'Time ({TIME_UNIT})', fontsize=PLOT_CONFIG['label_fontsize'])
ax1.set_ylabel(f'x ({X_UNIT})', fontsize=PLOT_CONFIG['label_fontsize'])
ax1.tick_params(labelsize=PLOT_CONFIG['tick_fontsize'])

cbar1 = plt.colorbar(im1, ax=ax1, label='$n_{ix} / n_c$')
cbar1.ax.set_ylabel('$\\langle n_i \\rangle_z / n_c$', fontsize=PLOT_CONFIG['cbar_label_fontsize'])
cbar1.ax.tick_params(labelsize=PLOT_CONFIG['cbar_tick_fontsize'])

plt.tight_layout()

# 保存图1
if PLOT_CONFIG['save_fig']:
    output_file1 = os.path.join(fig_dir, f"{PLOT_CONFIG['fig1_name']}.{PLOT_CONFIG['fig_format']}")
    plt.savefig(output_file1, dpi=PLOT_CONFIG['fig_dpi'], bbox_inches='tight')
    print(f"图1已保存至: {output_file1}")

# 显示图1
if PLOT_CONFIG['show_fig']:
    plt.show()
else:
    plt.close(fig1)


# ==================== 图2: 傅里叶频谱图（对数坐标） ====================
print("正在绘制图2: 频谱图...")
fig2, ax2 = plt.subplots(figsize=(PLOT_CONFIG['fig_width'], PLOT_CONFIG['fig_height']))

log_spectrum = np.log10(n1_spectrum_cropped + 1e-12)
im2 = ax2.imshow(log_spectrum, 
                 extent=[kx_positive_cropped[0], kx_positive_cropped[-1], 
                         time_axis_cropped[0], time_axis_cropped[-1]],
                 aspect='auto', origin='lower', cmap='jet',
                 vmin=PLOT_CONFIG['spectrum_vmin'],
                 vmax=PLOT_CONFIG['spectrum_vmax'])

# 设置坐标轴和colorbar
ax2.set_xlabel(f'$k_x$ ({KX_UNIT})', fontsize=PLOT_CONFIG['label_fontsize'])
ax2.set_ylabel(f'Time ({TIME_UNIT})', fontsize=PLOT_CONFIG['label_fontsize'])
ax2.tick_params(labelsize=PLOT_CONFIG['tick_fontsize'])

cbar2 = plt.colorbar(im2, ax=ax2, label='$\\log_{{10}}|\mathrm{FT}\;[n_{ix}|]$')
cbar2.ax.set_ylabel('$\\log_{{10}}|\mathrm{FT}\;[n_{ix}]|$', fontsize=PLOT_CONFIG['cbar_label_fontsize'])
cbar2.ax.tick_params(labelsize=PLOT_CONFIG['cbar_tick_fontsize'])

plt.tight_layout()

# 保存图2
if PLOT_CONFIG['save_fig']:
    output_file2 = os.path.join(fig_dir, f"{PLOT_CONFIG['fig2_name']}.{PLOT_CONFIG['fig_format']}")
    plt.savefig(output_file2, dpi=PLOT_CONFIG['fig_dpi'], bbox_inches='tight')
    print(f"图2已保存至: {output_file2}")

# 显示图2
if PLOT_CONFIG['show_fig']:
    plt.show()
else:
    plt.close(fig2)

print("完成！")


# ==================== 辅助函数 ====================
def print_data_info():
    """打印数据统计信息"""
    print("\n=== 数据统计信息 ===")
    print(f"密度范围: [{np.min(n_xt):.3e}, {np.max(n_xt):.3e}]")
    print(f"频谱范围: [{np.min(n1_spectrum_positive):.3e}, {np.max(n1_spectrum_positive):.3e}]")
    print(f"对数频谱范围: [{np.log10(np.min(n1_spectrum_positive)+1e-12):.2f}, "
          f"{np.log10(np.max(n1_spectrum_positive)):.2f}]")
    print(f"时间步长: {np.mean(np.diff(time_axis)):.3f} {TIME_UNIT}")
    print(f"kx分辨率: {np.mean(np.diff(kx_positive)):.3f} {KX_UNIT}")

# 取消注释以查看数据信息
# print_data_info()
```







## 3.电场分布

### 3.1 单步电场

```python
# =========== 绘制单步电场 ===========
import numpy as np
import matplotlib.pyplot as plt
from openpmd_viewer import OpenPMDTimeSeries
from scipy import constants as C
import os

# ==================== 参数配置 ====================
# 路径设置
data_path = '../diagPL/field'
SAVE_PLOT = True             # 是否保存图片
FILENAME = 'Ex_PL.png'  # 保存文件名
fig_dir = '../fig'           # 保存目录

# 时间步选择
TIMESTEP = 10  # 指定时间步

# 绘图设置
FIG_SIZE = (10, 8)           # 图形大小
DPI = 150                    # 分辨率
CMAP = 'RdBu_r'              # 颜色映射
AXIS_LABEL_FONTSIZE = 20     # 坐标轴标签字号
AXIS_TICK_FONTSIZE = 18      # 坐标轴数字（刻度）字号
CBAR_LABEL_FONTSIZE = 20     # colorbar标签字号
CBAR_TICK_FONTSIZE = 18      # colorbar数字（刻度）字号

# 单位转换因子
X_UNIT_FACTOR = 1e6          # m -> μm
Z_UNIT_FACTOR = 1e6          # m -> μm
X_UNIT = 'μm'
Z_UNIT = 'μm'

# ==================== 加载数据 ====================
print("正在加载诊断数据...")
ts = OpenPMDTimeSeries(data_path)

# =========== 获取数据，处理坐标轴 ===========
iteration = ts.iterations[TIMESTEP]  

# 获取电场E_x
Ex, info = ts.get_field(field='E', coord='x', iteration=iteration)

print(f"\n数据信息:")
print(f"   场数据形状: {Ex.shape}")
print(f"   坐标轴顺序: {info.axes}")  # {0: 'z', 1: 'x'} 或 {0: 'z', 1: 'y', 2: 'x'}
print(f"   原始坐标范围 (m):")
print(f"     x: [{info.xmin:.2e}, {info.xmax:.2e}], 点数: {len(info.x)}")
print(f"     z: [{info.zmin:.2e}, {info.zmax:.2e}], 点数: {len(info.z)}")

# =========== 坐标转换 ============
z_coords = info.z * Z_UNIT_FACTOR  # 转换为微米
x_coords = info.x * X_UNIT_FACTOR  # 转换为微米

# =========== 处理数据维度 ============
# 根据数据维度进行相应处理
if Ex.ndim == 2:
    # 2D数据 (z, x)
    Ex_2d = Ex
    print(f"\n数据是2维的 (z, x)，直接使用")
elif Ex.ndim == 3:
    # 3D数据 (z, y, x)，取y=0的中平面
    Ex_2d = Ex[:, 0, :]
    print(f"\n数据是3维的 (z, y, x)，取y=0平面")
else:
    raise ValueError(f"意外的数据维度: {Ex.ndim}")

# =========== 确定电场显示范围 ============
vmin, vmax = np.min(Ex_2d), np.max(Ex_2d)
# 对称化范围
vmax_abs = max(abs(vmin), abs(vmax))
vmin, vmax = -vmax_abs, vmax_abs
print(f"\n电场范围: {vmin:.2e} - {vmax:.2e} V/m")

# =========== 绘制Ex分布图 ============
# 创建保存目录
if SAVE_PLOT:
    os.makedirs(fig_dir, exist_ok=True)

fig, ax = plt.subplots(figsize=FIG_SIZE)

# 创建网格用于pcolormesh
X_grid, Z_grid = np.meshgrid(x_coords, z_coords)

# 绘制（注意：pcolormesh需要Z, X的顺序）
im = ax.pcolormesh(Z_grid, X_grid, Ex_2d, 
                   cmap=CMAP, shading='auto',
                   vmin=vmin, vmax=vmax)

# 设置坐标轴标签和刻度字号
ax.set_xlabel(f'z ({Z_UNIT})', fontsize=AXIS_LABEL_FONTSIZE)
ax.set_ylabel(f'x ({X_UNIT})', fontsize=AXIS_LABEL_FONTSIZE)

# 设置坐标轴刻度数字字号
ax.tick_params(axis='both', which='major', labelsize=AXIS_TICK_FONTSIZE)

# 添加颜色条
cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('$E_x$ (V/m)', fontsize=CBAR_LABEL_FONTSIZE)
cbar.ax.tick_params(labelsize=CBAR_TICK_FONTSIZE)

# 添加网格
ax.grid(True, alpha=0.2, linestyle=':', linewidth=0.5)

plt.tight_layout()

# 保存图片
if SAVE_PLOT:
    save_path = os.path.join(fig_dir, FILENAME)
    plt.savefig(save_path, dpi=DPI, bbox_inches='tight')
    print(f"\n图片已保存: {save_path}")

# 显示信息
print(f"\n=== 绘图信息 ===")
print(f"时间步: {TIMESTEP}")
print(f"迭代编号: {iteration}")
print(f"物理时间: {ts.t[TIMESTEP]*1e15:.2f} fs")
print(f"z范围: [{z_coords[0]:.2f}, {z_coords[-1]:.2f}] {Z_UNIT}")
print(f"x范围: [{x_coords[0]:.2f}, {x_coords[-1]:.2f}] {X_UNIT}")
print(f"电场范围: [{vmin:.2e}, {vmax:.2e}] V/m")

plt.show()
```



### 3.2 单步电场，可选空间范围

```python
# =========== 绘制单步电场 ===========
import numpy as np
import matplotlib.pyplot as plt
from openpmd_viewer import OpenPMDTimeSeries
from scipy import constants as C
import os

# ==================== 参数配置 ====================
# 路径设置
data_path = '../diagPL/field'
SAVE_PLOT = True             # 是否保存图片
FILENAME = 'Ex_PL.png'  # 保存文件名
fig_dir = '../fig'           # 保存目录

# 时间步选择
TIMESTEP = 10  # 指定时间步

# 范围限制，None表示自动
Z_RANGE = (0,8)  # 例如: (-10, 50) 或 None
X_RANGE = (2,10)  # 例如: (0, 15) 或 None
EX_RANGE = None  # 例如: (-1e8, 1e8) 或 None

# 绘图设置
FIG_SIZE = (10, 8)           # 图形大小
DPI = 150                    # 分辨率
CMAP = 'RdBu_r'              # 颜色映射
AXIS_LABEL_FONTSIZE = 20     # 坐标轴标签字号
AXIS_TICK_FONTSIZE = 18      # 坐标轴数字（刻度）字号
CBAR_LABEL_FONTSIZE = 20     # colorbar标签字号
CBAR_TICK_FONTSIZE = 18      # colorbar数字（刻度）字号

# 单位转换因子
X_UNIT_FACTOR = 1e6          # m -> μm
Z_UNIT_FACTOR = 1e6          # m -> μm
X_UNIT = 'μm'
Z_UNIT = 'μm'

# ==================== 加载数据 ====================
print("正在加载诊断数据...")
ts = OpenPMDTimeSeries(data_path)

# =========== 获取数据，处理坐标轴 ===========
iteration = ts.iterations[TIMESTEP]  

# 获取电场E_x
Ex, info = ts.get_field(field='E', coord='x', iteration=iteration)

print(f"\n数据信息:")
print(f"   场数据形状: {Ex.shape}")
print(f"   坐标轴顺序: {info.axes}")  # {0: 'z', 1: 'x'} 或 {0: 'z', 1: 'y', 2: 'x'}
print(f"   原始坐标范围 (m):")
print(f"     x: [{info.xmin:.2e}, {info.xmax:.2e}], 点数: {len(info.x)}")
print(f"     z: [{info.zmin:.2e}, {info.zmax:.2e}], 点数: {len(info.z)}")

# =========== 坐标转换 ============
z_coords = info.z * Z_UNIT_FACTOR  # 转换为微米
x_coords = info.x * X_UNIT_FACTOR  # 转换为微米

# =========== 处理数据维度 ============
# 根据数据维度进行相应处理
if Ex.ndim == 2:
    # 2D数据 (z, x)
    Ex_2d = Ex
    print(f"\n数据是2维的 (z, x)，直接使用")
elif Ex.ndim == 3:
    # 3D数据 (z, y, x)，取y=0的中平面
    Ex_2d = Ex[:, 0, :]
    print(f"\n数据是3维的 (z, y, x)，取y=0平面")
else:
    raise ValueError(f"意外的数据维度: {Ex.ndim}")

# =========== 应用空间范围 ============
def apply_range(data_2d, coords_z, coords_x, z_range, x_range):
    """应用空间范围裁剪"""
    # 确定z范围
    if z_range is None:
        z_mask = slice(None)
        z_extent = (coords_z[0], coords_z[-1])
    else:
        z_mask = (coords_z >= z_range[0]) & (coords_z <= z_range[1])
        z_extent = [z_range[0], z_range[1]]
    
    # 确定x范围
    if x_range is None:
        x_mask = slice(None)
        x_extent = (coords_x[0], coords_x[-1])
    else:
        x_mask = (coords_x >= x_range[0]) & (coords_x <= x_range[1])
        x_extent = [x_range[0], x_range[1]]
    
    # 裁剪数据
    if isinstance(z_mask, slice) and isinstance(x_mask, slice):
        cropped_data = data_2d
        cropped_z = coords_z
        cropped_x = coords_x
    else:
        cropped_data = data_2d[z_mask, :][:, x_mask]
        cropped_z = coords_z[z_mask]
        cropped_x = coords_x[x_mask]
    
    return cropped_data, cropped_z, cropped_x, z_extent, x_extent

Ex_cropped, z_cropped, x_cropped, z_extent, x_extent = apply_range(
    Ex_2d, z_coords, x_coords, Z_RANGE, X_RANGE
)

print(f"\n裁剪后范围:")
print(f"   z: [{z_extent[0]:.2f}, {z_extent[1]:.2f}] {Z_UNIT}")
print(f"   x: [{x_extent[0]:.2f}, {x_extent[1]:.2f}] {X_UNIT}")
print(f"   数据形状: {Ex_cropped.shape}")

# =========== 确定电场显示范围 ============
if EX_RANGE is None:
    vmin, vmax = np.min(Ex_cropped), np.max(Ex_cropped)
    # 对称化范围
    vmax_abs = max(abs(vmin), abs(vmax))
    vmin, vmax = -vmax_abs, vmax_abs
    print(f"\n自动电场范围: {vmin:.2e} - {vmax:.2e} V/m")
else:
    vmin, vmax = EX_RANGE
    print(f"\n指定电场范围: {vmin:.2e} - {vmax:.2e} V/m")

# =========== 绘制Ex分布图 ============
# 创建保存目录
if SAVE_PLOT:
    os.makedirs(fig_dir, exist_ok=True)

fig, ax = plt.subplots(figsize=FIG_SIZE)

# 创建网格用于pcolormesh
X_grid, Z_grid = np.meshgrid(x_cropped, z_cropped)

# 绘制（注意：pcolormesh需要Z, X的顺序）
im = ax.pcolormesh(Z_grid, X_grid, Ex_cropped, 
                   cmap=CMAP, shading='auto',
                   vmin=vmin, vmax=vmax)

# 设置坐标轴标签和刻度字号
ax.set_xlabel(f'z ({Z_UNIT})', fontsize=AXIS_LABEL_FONTSIZE)
ax.set_ylabel(f'x ({X_UNIT})', fontsize=AXIS_LABEL_FONTSIZE)

# 设置坐标轴刻度数字字号
ax.tick_params(axis='both', which='major', labelsize=AXIS_TICK_FONTSIZE)

# 添加颜色条
cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('$E_x$ (V/m)', fontsize=CBAR_LABEL_FONTSIZE)
cbar.ax.tick_params(labelsize=CBAR_TICK_FONTSIZE)

# 添加网格
ax.grid(True, alpha=0.2, linestyle=':', linewidth=0.5)

plt.tight_layout()

# 保存图片
if SAVE_PLOT:
    save_path = os.path.join(fig_dir, FILENAME)
    plt.savefig(save_path, dpi=DPI, bbox_inches='tight')
    print(f"\n图片已保存: {save_path}")

# 显示信息
print(f"\n=== 绘图信息 ===")
print(f"时间步: {TIMESTEP}")
print(f"迭代编号: {iteration}")
print(f"物理时间: {ts.t[TIMESTEP]*1e15:.2f} fs")
print(f"z范围: [{z_extent[0]:.2f}, {z_extent[1]:.2f}] {Z_UNIT}")
print(f"x范围: [{x_extent[0]:.2f}, {x_extent[1]:.2f}] {X_UNIT}")
print(f"电场范围: [{vmin:.2e}, {vmax:.2e}] V/m")

plt.show()
```



## 4. 能谱

### 4.1 指定步的质子能谱

```python
# =========== H离子单步能谱(线性坐标)v1.1.13 ===========
import numpy as np
import matplotlib.pyplot as plt

# 读取数据文件
filename = '../diagCP/reducedfiles/histH.txt'  # 替换为你的实际文件路径

# 读取头部获取bin中心值
with open(filename, 'r') as f:
    header = f.readline().strip()

# 解析bin中心值
bins = []
for item in header.split()[2:]:
    bin_value = float(item.split('=')[1].split('(')[0])
    bins.append(bin_value)

bin_centers = np.array(bins)

# 读取数据
data = np.loadtxt(filename, comments='#')

# 选择要绘制的时间步
time_step_idx = 57  # -1表示最后一个，0表示第一个
step = int(data[time_step_idx, 0])
time = data[time_step_idx, 1] * 1e15  # 转换为fs
spectrum = data[time_step_idx, 2:]  # 能谱数据

# 计算总粒子数和峰值能量
total_particles = np.sum(spectrum)
peak_idx = np.argmax(spectrum)  # 最大值索引
peak_energy = bin_centers[peak_idx]  # 峰值对应的能量
peak_count = spectrum[peak_idx]  # 峰值计数

# 绘制能谱
plt.figure(figsize=(5, 4))
plt.plot(bin_centers, spectrum, 'b-', linewidth=2)
plt.fill_between(bin_centers, 0, spectrum, alpha=0.3)

plt.xlabel('Energy (MeV)', fontsize=12)
plt.ylabel('Particle Count', fontsize=12)
plt.title(f'H⁺ Energy Spectrum at t={time:.1f} fs', fontsize=14)
plt.grid(True, alpha=0.3)

# 标注峰值（靠右的峰值）
if total_particles > 0:
    # 添加竖直线标注峰值位置
    plt.axvline(peak_energy, color='r', linestyle='--', alpha=0.7, 
                label=f'Peak: {peak_energy:.2f} MeV')
    # 在峰值位置添加点标记
    plt.plot(peak_energy, peak_count, 'ro', markersize=8)
    plt.legend()

plt.tight_layout()
plt.savefig('../fig/H_spectrum_single_step.png', dpi=300)
plt.show()

print(f"时间步: {step}")
print(f"时间: {time:.1f} fs")
print(f"总粒子数: {total_particles:.2e}")
if total_particles > 0:
    print(f"峰值能量: {peak_energy:.2f} MeV")
    print(f"峰值计数: {peak_count:.2e}")
```











