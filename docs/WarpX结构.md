# 1 WarpX编译和运行

## 1.1 运行前提准备

### 目录结构要求

```
~（用户家目录）/
├── WarpX_Full/                    # 工作主目录（名称可自定）
│   ├── WarpX/                     # WarpX主代码（必须）
│   │   ├── amrex/               # AMReX库（必须，与WarpX同级或上一级）
│   │   ├── picsar/              # PICSAR库（必须，与WarpX同级或上一级）
│   │   ├── Source/              # WarpX源码（必须）
│   │   ├── GNUmakefile          # 主编译文件（必须）
│   │   └── Bin/                 # 编译后生成（开始不存在）
│   ├── *.zip                    # 原始压缩包（临时，编译后可删除）
│   └── ...其他工作文件
└── warpx_run/                   # 运行目录（独立，保持干净）
    ├── warpx.exe               # 可执行文件（从Bin/复制来）
    ├── inputs文件              # 输入文件
    └── diags/, plt*/           # 运行时生成
```

### 编译前提（make命令之前）

（a）代码完整性检查（在WarpX目录内执行）

```
cd ~/WarpX_Full/WarpX  # 或你的WarpX目录

# 四个必须存在的项目（✅ 成功标志）
ls -d amrex/ picsar/ Source/ GNUmakefile

# 关键子目录验证（✅ 成功标志）
[ -d "amrex/Tools/GNUMake" ] && echo "AMReX工具链完整"
[ -d "picsar/multi_physics" ] && echo "PICSAR物理模块完整"
```

（b）路径关系检查

```
# 检查amrex和picsar的访问路径
ls -la ../amrex 2>/dev/null || echo "注意：需要../amrex符号链接"
ls -la ../picsar 2>/dev/null || echo "注意：需要../picsar符号链接"

# 解决方案：如果不存在，创建符号链接
cd ~/WarpX_Full  # WarpX的父目录
ln -sfn WarpX/amrex ./
ln -sfn WarpX/picsar ./
```

（c）编译环境检查

```
# 必要工具
which make g++ gfortran  # 都应该有路径输出

# 如果缺失，安装
sudo apt update
sudo apt install build-essential g++ gfortran make -y
```

### 运行前提（`./warpx.exe inputs`之前）

（a）运行目录准备

```
# 最佳实践：创建独立的运行目录
cd ~
mkdir -p warpx_run && cd warpx_run

# 三个必须项检查
ls -l warpx.exe inputs_* 2>/dev/null
```

（b）可执行文件验证

```
# 从编译目录复制可执行文件
cp ~/WarpX_Full/WarpX/Bin/main3d.gnu.*.exe ./warpx.exe

# 验证可执行权限
chmod +x warpx.exe
file warpx.exe  # 应显示ELF可执行文件
```

（c）输入文件完整性

```
# 检查输入文件是否存在
ls inputs_*

# 检查输入文件的依赖（如果有#include）
grep -i "include" inputs_* 2>/dev/null

# 如果有关联文件，一并复制
# 例如：inputs_test 可能包含 #include "inputs_base"
```

### 核心总结

1. **三个核心目录** ：`WarpX/`、`amrex/`、`picsar/` 必须在正确层级关系
2. **两个关键符号链接** ：`../amrex` 和 `../picsar` 必须指向正确位置
3. **分离原则** ：编译目录(`WarpX_Full`)和运行目录(`warpx_run`)分开
4. **输入文件完整性** ：检查 `#include`依赖，复制所有相关文件

# 2 WarpX组件

## 2.1 WarpX（主程序）

1.物理算法协调器——组织整个PIC循环：场求解→粒子推进→电流沉积

2.输入输出管理器——读取输入文件、写入诊断数据

3.组件集成器——调用AMReX和PICSAR的功能

关键目录：`Source/` 包含所有WarpX特有的物理算法和主循环逻辑。

## 2.2 AMReX - **基础设施与骨架**

| 模块         | 功能                          | 重要性                      |
| ------------ | ----------------------------- | --------------------------- |
| **网格管理** | 自适应网格细化(AMR)、负载均衡 | 让模拟更高效，可局部加密    |
| **并行框架** | MPI通信、域分解               | 未来扩展到多核/多节点的基础 |
| **I/O系统**  | 读写 `pltxxxxx`文件           | 生成可视化数据              |
| **工具库**   | 线性代数、插值、边界处理      | 提供数学基础设施            |

 **为什么需要** ：WarpX专注于物理，AMReX处理复杂的计算基础设施问题。

## 2.3 PICSAR - 高性能计算内核

| 组件           | 功能                    | 特点                       |
| -------------- | ----------------------- | -------------------------- |
| **场求解器**   | 求解Maxwell方程组       | 高度优化，支持多种数值方法 |
| **粒子推进器** | 推进粒子（Boris方法等） | 向量化，支持多种形状因子   |
| **QED模块**    | 量子电动力学效应        | 前沿物理功能               |
| **数学内核**   | 特殊函数、快速算法      | 性能关键部分用Fortran/汇编 |

**为什么单独一个库** ：这些计算密集的核心被提取出来，可用不同语言优化，甚至未来移植到GPU。

## 2.4 运行机制：`warpx.exe inputs` 时发生了什么

### 阶段1：初始化（约1-5%时间）

```
1. 读取 inputs 文件 → WarpX::ReadParameters()
2. 创建网格 → AMReX::AmrCore::InitAmr()
3. 初始化粒子 → WarpX::InitParticles()
4. 分配数组 → AMReX::MultiFab 分配场数据
```

### 阶段2：主循环（约90%时间）

```
for (int step = 0; step < max_step; step++) {
    // 1. 推进粒子 (调用PICSAR内核)
    AdvanceParticles();  // → PICSAR::particle_push()
  
    // 2. 沉积电流 (WarpX+PICSAR)
    DepositCurrent();    // → PICSAR::current_deposition()
  
    // 3. 求解Maxwell方程 (PICSAR核心)
    SolveMaxwell();      // → PICSAR::field_solver()
  
    // 4. 处理边界 (AMReX)
    FillBoundary();      // → AMReX::FillBoundary()
  
    // 5. 诊断输出 (WarpX)
    if (step % diag_interval == 0) 
        WriteDiagnostics(); // → AMReX::WritePlotFile()
}
```

### 阶段3：清理与输出（约5%时间）

## 2.5 输入文件结构分析

以的 `inputs_test_3d_uniform_plasma` 为例：

```
# 典型的三层结构
inputs_test_3d_uniform_plasma  # 主文件（测试特定设置）
  ↓ #include
inputs_base_3d                  # 基础文件（通用3D设置）
  ↓ 可能还有更多#include
WarpX源码默认值                 # 硬编码的默认值
```

**为什么这样设计** ：模块化！`base`文件定义通用参数，测试文件覆盖特定值。

## 2.6 关键理解点

### 分离关注点设计

```
WarpX    - 物理建模 (写论文关心的部分)
AMReX   - 计算工程 (计算机专家关心的部分)  
PICSAR  - 性能优化 (HPC专家关心的部分)
```

### 编译时 vs 运行时

| 时期       | 确定的组件                   | 可调整的部分                   |
| ---------- | ---------------------------- | ------------------------------ |
| **编译时** | 维度(2D/3D)、物理模块(QED等) | 通过 `make DIM=3 USE_QED=TRUE` |
| **运行时** | 网格大小、粒子数、物理参数   | 通过 `inputs`文件              |

## 2.7 为什么WarpX如此设计？

| 设计原则     | 体现           | 好处                         |
| ------------ | -------------- | ---------------------------- |
| **模块化**   | 三个独立代码库 | 可独立更新、复用、优化       |
| **可扩展性** | AMReX支持AMR   | 可局部加密感兴趣区域         |
| **高性能**   | PICSAR优化内核 | 可利用最新CPU/GPU特性        |
| **可维护性** | 清晰接口分离   | 物理学家、计算机专家各司其职 |

### Q&A

1. **Q** ：`amrex`和 `picsar`能删除吗？
   **A** ：不能！它们如同WarpX的“双腿”，删除后无法运行。
2. **Q** ：我能只修改WarpX而不碰其他吗？
   **A** ：可以！修改 `Source/`中的物理模型，无需重新下载AMReX/PICSAR。
3. **Q** ：如何换用其他物理模块？
   **A** ：编译时选项，如 `make USE_QED=TRUE`启用量子电动力学。
4. **Q** ：为什么需要 `inputs_base_3d`？
   **A** ：避免重复，多个测试共享基础设置。

# # 编译

WarpX编译阶段**不针对特定物理问题** ，而是构建一个“通用模拟器框架”；物理问题的特异性在**运行时**通过输入文件定义。

**编译 vs 运行：关注点分离**

|         阶段 | 决定什么      | 如何决定      | 影响范围     |
| -----------: | ------------- | ------------- | ------------ |
| **编译阶段** | **能力/框架** | `make` 参数   | 所有后续模拟 |
| **运行阶段** | **具体问题**  | `inputs` 文件 | 单次模拟     |

## 编译时确定的“框架能力”

### 1.几何维度

### **（唯一强相关的物理参数）**

```
# 编译时指定维度
make DIM=2      # 2D模拟器
make DIM=3      # 3D模拟器（默认）
make DIM=rz     # 柱对称RZ几何

# 维度决定：
# - 数组维度：Field_3D vs Field_2D
# - 差分算子：∂/∂z是否存在
# - 粒子推进：2D vs 3D洛伦兹力
```

### 2.启用的物理模块（开关）

```
# 量子电动力学（QED）效应
make USE_QED=TRUE   # 启用量子辐射
make USE_QED=FALSE  # 禁用（默认）

# 高性能计算后端
make USE_GPU=TRUE   # GPU加速（需CUDA）
make USE_OPENMP=TRUE # CPU多线程

# 算法变体
make USE_PSATD=TRUE # 伪谱时域求解器
```

### 3.性能与调试选项

```
# 调试版本
make DEBUG=TRUE    # 包含断言、边界检查
                    # 运行慢但易调试

# 优化版本  
make DEBUG=FALSE   # 完全优化（默认）
                    # 运行快但难调试

# 性能分析
make TINY_PROFILING=TRUE  # 轻量级性能分析
```

## 运行时定义的“具体问题”

所有物理问题特性都在输入文件中定义：

### 粒子相关

```
# 编译：知道“如何推进粒子”
# 运行：定义“推什么粒子”
particles.nspecies = 2
particles.species_names = electrons protons

electrons.charge = -1.0
electrons.mass = 0.000545  # MeV/c²
electrons.injection_style = "thermal"
electrons.temperature = 100  # eV

protons.charge = 1.0
protons.mass = 938.272
protons.density_function = "parabolic(x)"
```

### 场与源项

```
# 编译：知道“如何解Maxwell方程”
# 运行：定义“源是什么”
laser.profile = gaussian
laser.wavelength = 0.8e-6      # 800nm
laser.a0 = 2.0                 # 归一化振幅
laser.waist = 5e-6             # 光腰
laser.duration = 30e-15        # 30fs

# 或者外部场
external_fields.type = "static_magnetic"
external_fields.B0 = 10.0      # 10特斯拉
```

### 几何与边界

```
# 编译：知道“如何处理边界”
# 运行：定义“边界在哪、什么条件”
geometry.prob_lo = 0.0 0.0 0.0     # 计算域起点
geometry.prob_hi = 100e-6 50e-6 50e-6  # 计算域终点

boundary.field_lo = periodic absorbing periodic
boundary.field_hi = periodic absorbing periodic
```

## 实际工作流中的编译策略

### 方案1：通用编译

```
# 编译一个“全能”版本
make -j 4 DIM=3 USE_QED=TRUE USE_OPENMP=TRUE
# 得到：main3d.gnu.TPROF.OMP.QED.ex

# 然后用不同输入文件运行：
./warpx.exe inputs_laser_accel     # 激光加速
./warpx.exe inputs_plasma_wake     # 等离子体尾波
./warpx.exe inputs_beam_physics    # 束流物理
```

### 方案2：专用编译

```
# 2D激光等离子体专用（节省内存）
make -j 4 DIM=2 USE_QED=FALSE DEBUG=FALSE
# 更小、更快，但不能做3D或QED模拟

# 高精度QED研究专用
make -j 4 DIM=3 USE_QED=TRUE USE_PSATD=TRUE
# 支持量子辐射和伪谱方法
```

# 3 分析与可视化

在运行目录内（含 `warpx.exe`和 `xxx.in`等）将生成 `diags`文件夹。

# *未整理部分

在WSL上使用非MPI模式运行WarpX，主要包括**编译**和**运行**两个阶段。

#### *1 执行编译命令

WarpX的编译主要通过 `GNUmakefile`控制。

使用 `make`执行编译命令，并设置 `USE_MPI=FALSE`来指定非MPI编译。

```
make -j 4 USE_MPI=FALSE
```

* `-j 4` 表示使用4个线程进行并行编译，加快速度。你可以根据WSL的CPU核心数进行调整。
* **关键说明** ：编译选项也可以在 `GNUmakefile`文件中修改，但通过命令行直接传递参数更快捷。

编译成功后，可执行文件会生成在 `Bin/`目录下，可以查看生成的文件：

```
ls Bin/
```

* 如果之前尝试过编译，最好先执行 `make realclean`来清理之前的编译结果，确保全新开始。
* WarpX需要为不同的维度（1D、2D、3D、RZ）生成不同的二进制文件。编译生成的可执行文件名称可能类似 `main3d.gnu.DEBUG.NOMPI.ex`（取决于编译器、几何维度和是否启用调试模式）。

#### *2 准备与运行示例

1.**创建并进入运行目录** ：建议将模拟运行在独立的目录中。

```
mkdir -p ~/warpx_runs/first_test
cd ~/warpx_runs/first_test
```

2.**复制可执行文件** ：将编译好的WarpX可执行文件复制到当前目录。需要根据实际生成的文件名进行调整。

```
cp ~/WarpX/Bin/main3d.gnu.DEBUG.NOMPI.ex ./warpx.exe
```

*提示：`main3d.gnu.DEBUG.NOMPI.ex` 仅是一个文件名示例，具体需要在 `Bin/`目录下实际看到的文件替换。*

3.**获取示例输入文件** ：WarpX源码中自带很多示例。一个简单的入门示例是 `Examples/Physics_applications/laser_acceleration/inputs_2d`。可以复制它来使用：

```
cp ~/WarpX/Examples/Physics_applications/laser_acceleration/inputs_2d .
```

4.**运行模拟** ：由于选择了非MPI模式，你只需直接运行可执行文件并指定输入文件。

```
./warpx.exe inputs_2d
```

程序运行后，会在终端打印状态信息，并默认在 `diags/`目录下生成诊断输出文件。

#### *3 常见问题排查

* **编译失败** ：如果编译出错，请确保WSL已安装必要的依赖。根据官方文档，需要一个支持C++17的编译器（如GCC 8.4+）以及CMake等构建工具。可以参考 `apt`安装命令来安装这些基础依赖。
* **运行时找不到文件** ：请确认输入文件的路径和名称正确。
* **示例输入文件与可执行文件维度不匹配** ：例如，用3D的可执行文件运行一个2D的输入文件可能会报错。此时可以检查输入文件开头的 `geometry.dims`等参数，或重新编译对应维度的WarpX（通过修改 `GNUmakefile`中的 `DIM`选项）。
* WarpX使用 **非CMake的传统Makefile系统** ，需要在 **源代码根目录** （即 `~/WarpX_Full/WarpX/`）编译。

```
# 1. 返回到WarpX源代码根目录
cd ~/WarpX_Full/WarpX

# 2. 直接在此目录编译（不要进入build子目录）
make -j 4 USE_MPI=FALSE

# 3. 编译成功后，可执行文件会生成在 Bin/ 目录下
ls -la Bin/
```

#### *4 WarpX的编译方式

* **传统Makefile** ：WarpX使用 `GNUmakefile` 控制编译，而不是CMake的 `Makefile`
* **编译位置** ：直接在源代码根目录运行 `make`，它会自动处理依赖和输出
* **输出目录** ：编译产物（可执行文件）默认放在 `Bin/` 目录，而非 `build/`
* Makefile期望 `amrex` 和 `picsar` 在 **WarpX目录的父级** （`../`）

#### *5 创造符号链接

在目录结构中，`amrex` 和 `picsar` 在 `~/WarpX_Full/WarpX/` 内，但Makefile期望它们在 `~/WarpX_Full/`。创建符号链接来满足这个要求：

```
# 1. 进入WarpX_Full目录（WarpX的父目录）
cd ~/WarpX_Full

# 2. 创建指向内部子目录的符号链接（从上层指向内部）
ln -sfn WarpX/amrex ./
ln -sfn WarpX/picsar ./

# 3. 验证符号链接
ls -la amrex picsar
# 应该显示类似：
# amrex -> WarpX/amrex
# picsar -> WarpX/picsar

# 4. 进入WarpX目录开始编译
cd WarpX
make USE_MPI=FALSE
```

修正前后对比

```
# 修正前（有问题）：
~/WarpX_Full/
├── WarpX/
│   ├── amrex/          # Makefile期望在../amrex
│   ├── picsar/         # Makefile期望在../picsar
│   └── Source/...      # 寻找../amrex/Tools/GNUMake/Make.rules

# 修正后（通过符号链接）：
~/WarpX_Full/
├── amrex -> WarpX/amrex      # 符号链接
├── picsar -> WarpX/picsar    # 符号链接
└── WarpX/
    ├── amrex/                # 实际目录
    ├── picsar/               # 实际目录
    └── Source/...            # 现在能找到../amrex了
```

#### *6  Warpx运行指令

```
mpirun -np 4 ./warpx my_simulation.in
```

# $ Linux指令