





绘制Ex，Ey，rho_ele，rho_ion

```python
import h5py
import numpy as np
from matplotlib.colors import SymLogNorm
from scipy import constants as C
import matplotlib.pyplot as plt

diag = 'diags'  # 诊断名称
t = 3000  # 时间步
timestep = str(t).zfill(6)
q_e = -1.602176634e-19  # 电子电荷，单位为库仑
q_i = 1.602176634e-19  # 离子电荷，单位为库仑

# 是否交换绘图的横纵坐标（只交换，不翻转方向）
# True: 在绘图时对二维数据进行转置，并同时交换坐标刻度的标签含义
SWAP_XY = True

## parameters
dt = 6.372454818e-11
# micron = 1e-6
lambda1 = 1  # 波长
omega = 2 * np.pi * C.c / lambda1
laser_cycle = lambda1 / C.c
T0 = lambda1 / C.c  # 0.8*10^{-6}/
w0 = 3.0  # 激光束腰
r_laser =w0 * np.sqrt(np.log(2) / 2)   #######need change

# 模拟范围
x_max = 10
x_min = -x_max
z_max =  9
z_min = -1

def process_data(data, is_field=True):
    """
    处理数据，将3D数据切片为2D，并为绘图计算参数
    
    Parameters:
    -----------
    data : numpy.ndarray
        输入数据
    is_field : bool
        是否为场数据，如果是则使用对称对数标准化
        
    Returns:
    --------
    data_2d : numpy.ndarray
        2D切片数据
    norm : matplotlib.colors.Normalize
        标准化对象
    vmin, vmax : float
        数据范围
    """
    # 取二维切片（如果是3D数据，取中间一层）
    if data.ndim == 3:
        data_2d = data[:, data.shape[1] // 2, :]
    else:
        data_2d = data
    
    if is_field:
        # 对于场数据使用对称对数标准化
        abs_max = np.nanmax(np.abs(data_2d))
        linthresh = abs_max * 1e-3  # 线性阈值，防止0附近过亮
        norm = SymLogNorm(linthresh=linthresh, linscale=1.0, vmin=-abs_max, vmax=abs_max)
        return data_2d, norm, -abs_max, abs_max
    else:
        # 对于密度数据使用线性标准化
        vmin = np.nanmin(data_2d)
        vmax = np.nanmax(data_2d)
        return data_2d, None, vmin, vmax

# 读取HDF5文件
filename = f'{diag}/openpmd_{timestep}.h5'
with h5py.File(filename, 'r') as f:
    # 获取时间步路径
    ex_path = list(f['/data'].keys())[0]  # 获取第一个时间步
    
    # 读取数据
    E_x = f[f'/data/{ex_path}/fields/E/x'][()]
    E_z = f[f'/data/{ex_path}/fields/E/z'][()]
    rho_electrons = f[f'/data/{ex_path}/fields/rho_electrons'][()]
    rho_ions = f[f'/data/{ex_path}/fields/rho_protons'][()]
    
rho_electrons /= q_e  # 将电子密度转换为库仑单位
rho_ions /= q_i  # 将离子密度转换为库仑单位

# 处理所有数据
E_x_2d, E_x_norm, E_x_vmin, E_x_vmax = process_data(E_x, is_field=False)
E_z_2d, E_z_norm, E_z_vmin, E_z_vmax = process_data(E_z, is_field=False)
rho_e_2d, _, rho_e_vmin, rho_e_vmax = process_data(rho_electrons, is_field=False)
rho_i_2d, _, rho_i_vmin, rho_i_vmax = process_data(rho_ions, is_field=False)

# 如果需要交换横纵坐标，则对二维数据进行转置（不改变数值正负方向）
if SWAP_XY:
    E_x_2d = E_x_2d.T
    E_z_2d = E_z_2d.T
    rho_e_2d = rho_e_2d.T
    rho_i_2d = rho_i_2d.T

# 创建2×2子图
figsize = (10, 6) if SWAP_XY else (6, 10)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=figsize)

# 添加总标题（更多自定义选项）
fig.suptitle(r"{}T0".format('%.1f'%(t*dt/T0)), 
             fontsize=16, 
             fontweight='bold',
             y=0.98,  # 控制标题位置
             ha='center')  # 水平对齐

# 计算对称的范围，确保0在colormap中心
E_x_max_abs = max(abs(E_x_vmin), abs(E_x_vmax)) / 2
E_z_max_abs = max(abs(E_z_vmin), abs(E_z_vmax)) / 3

# # 将范围从米转换为微米
# x_max_um = x_max * 1e6
# x_min_um = x_min * 1e6
# z_max_um = z_max * 1e6
# z_min_um = z_min * 1e6

# 定义刻度
x_ticks = np.linspace(x_min, x_max, 5)  # 生成5个刻度标签（物理量）
y_ticks = np.linspace(z_min, z_max, 5)

def apply_ticks(ax, data2d, swap_xy: bool):
    if swap_xy:
        ax.set_xticks(np.linspace(0, data2d.shape[1] - 1, len(y_ticks)))
        ax.set_xticklabels([f'{tick:.1f}' for tick in y_ticks])
        ax.set_yticks(np.linspace(0, data2d.shape[0] - 1, len(x_ticks)))
        ax.set_yticklabels([f'{tick:.1f}' for tick in x_ticks])
    else:
        ax.set_xticks(np.linspace(0, data2d.shape[1] - 1, len(x_ticks)))
        ax.set_xticklabels([f'{tick:.1f}' for tick in x_ticks])
        ax.set_yticks(np.linspace(0, data2d.shape[0] - 1, len(y_ticks)))
        ax.set_yticklabels([f'{tick:.1f}' for tick in y_ticks])

# 绘制E_x - 使用对称范围
im1 = ax1.imshow(E_x_2d, cmap='RdBu_r', vmin=-E_x_max_abs, vmax=E_x_max_abs, origin='lower', aspect='auto')
ax1.set_title(r'$E_x$ Field')
ax1.set_xlabel(r'$Z$ ($ m$)' if SWAP_XY else r'$X$ ($ m$)')
ax1.set_ylabel(r'$X$ ($ m$)' if SWAP_XY else r'$Z$ ($ m$)')
apply_ticks(ax1, E_x_2d, SWAP_XY)
fig.colorbar(im1, ax=ax1, label=r'$E_x$')

# 绘制E_z - 使用对称范围
im2 = ax2.imshow(E_z_2d, cmap='RdBu_r', vmin=-E_z_max_abs, vmax=E_z_max_abs, origin='lower', aspect='auto')
ax2.set_title(r'$E_z$ Field')
ax2.set_xlabel(r'$Z$ ($ m$)' if SWAP_XY else r'$X$ ($ m$)')
ax2.set_ylabel(r'$X$ ($ m$)' if SWAP_XY else r'$Z$ ($ m$)')
apply_ticks(ax2, E_z_2d, SWAP_XY)
fig.colorbar(im2, ax=ax2, label=r'$E_z$')

# 绘制电子密度
im3 = ax3.imshow(rho_e_2d, cmap='jet', vmin=rho_e_vmin, vmax=rho_e_vmax/2, origin='lower', aspect='auto')
ax3.set_title(r'Electron Density ($\rho_e$)', pad=15)
ax3.set_xlabel(r'$Z$ ($ m$)' if SWAP_XY else r'$X$ ($ m$)')
ax3.set_ylabel(r'$X$ ($ m$)' if SWAP_XY else r'$Z$ ($ m$)')
apply_ticks(ax3, rho_e_2d, SWAP_XY)
fig.colorbar(im3, ax=ax3, label=r'$\rho_e$')

# 绘制离子密度
im4 = ax4.imshow(rho_i_2d, cmap='jet', vmin=rho_i_vmin, vmax=rho_i_vmax/2, origin='lower', aspect='auto')
ax4.set_title(r'Ion Density ($\rho_i$)', pad=15)
ax4.set_xlabel(r'$Z$ ($ m$)' if SWAP_XY else r'$X$ ($ m$)')
ax4.set_ylabel(r'$X$ ($ m$)' if SWAP_XY else r'$Z$ ($ m$)')
apply_ticks(ax4, rho_i_2d, SWAP_XY)
fig.colorbar(im4, ax=ax4, label=r'$\rho_i$')

plt.tight_layout()
suffix = '_swapxy' if SWAP_XY else ''
plt.savefig(f'figure/{diag}_{timestep}_fields_and_densities{suffix}.png', dpi=600, bbox_inches='tight')

```

