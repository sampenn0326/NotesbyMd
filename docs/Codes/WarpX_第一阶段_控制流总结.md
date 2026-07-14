# WarpX 源码学习：第一阶段总结

## 阶段目标

本阶段的目标是建立 WarpX 的第一层整体心智模型：

- 程序从哪里启动；
- 核心 `WarpX` 对象如何创建；
- 参数和模拟数据何时初始化；
- 主时间循环在哪里；
- 一次标准显式 PIC 时间步按什么顺序执行。

本阶段重点是**控制流和模块职责**，暂时不深入粒子推进器、电流沉积算法、FDTD/PSATD 数值公式和 AMR 同步细节。

---

## 1. 总体控制流

```text
main()
  ↓
initialize_external_libraries()
  ↓
WarpX::GetInstance()
  ↓
WarpX::MakeWarpX()
  ↓
new WarpX()
  ↓
WarpX::WarpX()
  ↓
WarpX::ReadParameters()
  ↓
WarpX::InitData()
  ↓
WarpX::Evolve()
  ↓
WarpX::OneStep()
  ↓
WarpX::OneStep_nosub()
```

这条主线描述了 WarpX 从程序启动，到进入标准显式电磁 PIC 时间步的完整路径。

---

## 2. `main()`：程序总入口

主要文件：

```text
Source/main.cpp
```

`main()` 的职责是调度程序生命周期，而不是执行具体物理算法。

主要流程：

```text
初始化外部运行环境
  ↓
获取 WarpX 核心对象
  ↓
初始化模拟数据
  ↓
运行时间推进
  ↓
结束和清理
```

其中核心调用包括：

```text
WarpX::GetInstance()
WarpX::InitData()
WarpX::Evolve()
WarpX::Finalize()
```

---

## 3. `WarpX::GetInstance()`：获取唯一模拟器对象

主要文件：

```text
Source/WarpX.H
Source/WarpX.cpp
```

WarpX使用单例模式保存核心模拟器对象。

简化逻辑：

```cpp
if (m_instance == nullptr) {
    MakeWarpX();
}
return *m_instance;
```

已确认：

- `m_instance` 是静态指针；
- 初始值为 `nullptr`；
- 第一次调用时通过 `MakeWarpX()` 创建对象；
- 后续调用返回同一个对象；
- 这是延迟初始化（lazy initialization）。

---

## 4. `WarpX::MakeWarpX()`：创建前准备与对象创建

实现位置：

```text
Source/WarpX.cpp
```

`MakeWarpX()` 并不是直接执行 `new WarpX()`，而是先调用一系列配置处理和检查函数。

调用顺序：

```text
check_dims()
  ↓
ReadMovingWindowParameters(...)
  ↓
ConvertLabParamsToBoost()
  ↓
parse_field_boundaries()
  ↓
get_periodicity_array(...)
  ↓
parse_particle_boundaries(...)
  ↓
CheckGriddingForRZSpectral()
  ↓
m_instance = new WarpX()
```

可以直接确认的是这些函数按上述顺序被调用。

尚未深入确认的是这些函数内部具体读取、修改和检查了什么。

---

## 5. `WarpX::WarpX()`：搭建模拟器骨架

`new WarpX()` 自动调用无参构造函数：

```cpp
WarpX::WarpX()
```

构造函数没有显式初始化列表。

进入构造函数体前：

1. 先构造 `amrex::AmrCore` 基类；
2. 再按成员声明顺序初始化成员；
3. 使用类内初始值或默认构造。

构造函数体主要完成：

- 将 `m_instance` 指向当前对象；
- 初始化 warning manager 和信号处理；
- 调用 `ReadParameters()`；
- 处理向后兼容配置；
- 根据参数创建若干管理对象；
- 创建 `MultiParticleContainer`；
- 创建粒子边界缓冲；
- 可选创建流体容器；
- 创建静电求解器；
- 可选创建 HybridPIC 模型；
- 可选创建宏观介质对象；
- 调整 PML、场求解器、负载均衡和 AMR 相关容器大小；
- 执行若干配置一致性检查。

### 构造函数结束后的状态

已经存在：

- WarpX 核心对象；
- 粒子系统管理对象 `mypc`；
- 粒子边界缓冲；
- 求解器管理对象或指针；
- 各类按 AMR 层数调整过大小的容器。

尚未完整建立：

- 实际 AMR 网格层级；
- 完整场数据；
- 实际粒子数据；
- diagnostics 对象；
- 正式时间推进状态。

---

## 6. `ReadParameters()`：决定本次模拟走哪条路线

`ReadParameters()` 是构造阶段的核心配置函数。

它决定的主要内容包括：

- 最大步数和结束时间；
- 电磁或静电求解模式；
- FDTD 或 PSATD；
- 粒子推进算法；
- 电流与电荷沉积算法；
- 场 gather 算法；
- 是否启用移动窗口；
- 是否启用 PML；
- 是否启用 AMR 子循环；
- 是否存在流体物种；
- 是否使用宏观介质；
- 是否启用 HybridPIC；
- 负载均衡策略；
- 粒子形状阶数和排序；
- boosted frame 和 PSATD 参数；
- diagnostics、slice 和 collision 参数。

### 它与构造函数的关系

`ReadParameters()` 写入成员变量，构造函数随后根据这些变量决定创建哪些对象、调整哪些容器和走哪些条件分支。

例如：

```text
do_fluid_species
  → 是否创建 MultiFluidContainer

electrostatic_solver_id
  → 创建哪种静电求解器

electromagnetic_solver_id
  → 是否创建 HybridPIC 模型
  → 分配谱求解器还是 FDTD 求解器容器

m_em_solver_medium
  → 是否创建 MacroscopicProperties

m_do_subcycling
  → 是否允许 AMR 子循环路径
```

---

## 7. `InitData()`：真正建立模拟数据

主要实现：

```text
Source/Initialization/WarpXInitData.cpp
```

`InitData()` 是“构造对象”和“正式运行”之间的桥梁。

### 从零开始运行

当不是从 checkpoint 重启时，大致流程为：

```text
计算时间步长
  ↓
建立 AMR 网格层级
  ↓
分配场数据
  ↓
分配并初始化粒子数据
  ↓
初始化 PML
  ↓
初始化 diagnostics
  ↓
初始化静电、HybridPIC 或介质相关对象
  ↓
计算初始空间电荷场或磁静态场
  ↓
叠加外场
  ↓
输出初始诊断
```

### 从 checkpoint 重启

大致流程：

```text
读取 checkpoint
  ↓
恢复网格、场、粒子和时间状态
  ↓
执行重启后处理
  ↓
恢复 diagnostics
```

### 构造函数与 `InitData()` 的分工

```text
构造函数：
创建管理对象和空容器

InitData()：
真正建立网格、场数组、粒子数据和 diagnostics
```

---

## 8. `Evolve()`：外层时间循环

主要实现：

```text
Source/Evolve/WarpXEvolve.cpp
```

`Evolve()` 是时间推进的总调度器。

主循环形式：

```cpp
for (int step = istep[0];
     step < numsteps_max && cur_time < stop_time;
     ++step)
```

因此主要终止条件为：

```text
达到最大步数
或
达到最大物理时间
```

每个循环中主要完成：

- 检查停止信号；
- diagnostics 开始新迭代；
- 检查负载均衡；
- 必要时更新时间步；
- 执行电离和 QED 事件；
- 调用 `OneStep()`；
- 粒子重采样；
- 更新 `istep`、`t_old`、`t_new` 和当前时间；
- 处理移动窗口；
- 处理粒子边界；
- 某些模式下追加静电或 HybridPIC 场更新；
- 输出 full diagnostics 和 reduced diagnostics；
- 检查用户终止条件。

### 时间状态

```text
当前循环编号：
局部变量 step

持久化步数：
istep[lev]

当前时间：
局部变量 cur_time

持久化时间：
t_new[lev]、t_old[lev]

时间步长：
dt[0]
```

---

## 9. `OneStep()`：选择时间推进路线

`OneStep()` 更像一个路由器，而不是单一算法。

主要分支：

```text
OneStep()
├── 隐式求解器路径
├── Electrostatic / HybridPIC 路径
└── 电磁 PIC 路径
    ├── OneStep_nosub()
    ├── OneStep_JRhom()
    └── OneStep_sub1()
```

### 主要选择条件

- `m_implicit_solver` 是否存在；
- `electromagnetic_solver_id`；
- `finest_level`；
- `m_JRhom`；
- `m_do_subcycling`。

标准显式电磁 PIC、无 AMR 子循环的主要入口是：

```text
WarpX::OneStep_nosub()
```

---

## 10. `OneStep_nosub()`：标准显式 PIC 时间步

`OneStep_nosub()` 描述了标准显式 PIC 时间步的顶层结构。

总体流程：

```text
推进粒子并沉积电流/电荷
  ↓
同步电流和电荷
  ↓
处理 PML 中的电流
  ↓
更新电磁场
  ↓
处理场边界和 guard cells
```

对应主要调用：

```text
PushParticlesandDeposit()
  ↓
SyncCurrentAndRho()
  ↓
CopyJPML() / DampJPML()
  ↓
PushPSATD()
或
EvolveB() / EvolveE()
  ↓
FillBoundary*()
  ↓
DampPML()
```

---

## 11. 粒子阶段：Gather、Push、Deposit

顶层调用：

```cpp
PushParticlesandDeposit(cur_time)
```

根据顶层源码注释，可以确认它完成了：

```text
粒子位置：
xⁿ → xⁿ⁺¹

粒子动量：
pⁿ⁻¹ᐟ² → pⁿ⁺¹ᐟ²

沉积：
Jⁿ⁺¹ᐟ²
ρ
```

标准 PIC 粒子阶段通常包含：

```text
从网格读取 E、B
  ↓
将场插值到粒子位置（gather）
  ↓
推进粒子动量和位置（push）
  ↓
将电流和电荷沉积到网格（deposit）
```

目前 gather 的具体调用位置尚未深入确认，但它很可能封装在 `PushParticlesandDeposit()` 的内部。

---

## 12. `SyncCurrentAndRho()`：为什么沉积后还要同步

沉积后的电流和电荷可能分散在：

- 不同 MPI 进程；
- guard cells；
- 不同 AMR 层；
- 粗细网格交界区域。

因此在场求解之前需要同步：

```text
过滤 J、ρ
  ↓
交换 guard cells
  ↓
跨 AMR 层同步
  ↓
处理边界
```

这保证场求解器看到的是一致的网格电流和电荷。

---

## 13. 场更新：PSATD 与非 PSATD

### PSATD 路径

顶层入口：

```text
PushPSATD()
```

在 `OneStep_nosub()` 中，PSATD 场更新表现为一个整体操作。

内部频域算法尚未深入。

### 非 PSATD 路径

源码直接显示出半步结构：

```text
B 推进半步
  ↓
E 推进一个整步
  ↓
B 再推进半步
```

对应：

```text
EvolveB(FirstHalf)
  ↓
EvolveE(full step)
  ↓
EvolveB(SecondHalf)
```

这体现了 leapfrog 时间交错结构。

---

## 14. 一次标准显式 PIC 时间步的通俗图

```text
时刻 n 的粒子和场
        │
        ▼
从网格获取粒子位置处的 E、B
        │
        ▼
推进粒子动量和位置
        │
        ▼
沉积电流 J 和电荷 ρ
        │
        ▼
同步不同进程、guard cells 和 AMR 层的 J、ρ
        │
        ▼
更新 B 半步
        │
        ▼
使用 J 更新 E 一个整步
        │
        ▼
更新 B 剩余半步
        │
        ▼
处理场边界、guard cells 和 PML
        │
        ▼
得到下一时间层的粒子和场
```

---

## 15. WarpX 与教科书 PIC 的对应关系

| 教科书 PIC 步骤 | WarpX 顶层位置 |
|---|---|
| 场插值到粒子 | `PushParticlesandDeposit()` 内部 |
| 推进粒子 | `PushParticlesandDeposit()` |
| 沉积电流/电荷 | `PushParticlesandDeposit()` |
| 同步电流/电荷 | `SyncCurrentAndRho()` |
| Maxwell 场更新 | `PushPSATD()` 或 `EvolveB()/EvolveE()` |
| 场边界与 guard cells | `FillBoundary*()` |
| PML 吸收 | `DampPML()` |
| 时间循环与诊断 | `Evolve()` |

---

## 16. 当前已经确认的内容

### 已完成第一轮浏览

- [x] `main()`
- [x] `WarpX::GetInstance()`
- [x] `WarpX::MakeWarpX()`
- [x] `WarpX::WarpX()`
- [x] `WarpX::ReadParameters()`
- [x] `WarpX::InitData()`
- [x] `WarpX::Evolve()`
- [x] `WarpX::OneStep()`
- [x] `WarpX::OneStep_nosub()`

### 已建立的认识

- WarpX 程序的完整生命周期；
- 构造函数与 `InitData()` 的职责区别；
- 参数如何决定算法分支；
- 主时间循环的位置和终止条件；
- 标准显式 PIC 时间步的顶层顺序；
- PSATD 与非 PSATD 场更新的顶层分流；
- 非 PSATD 路径的 `B 半步 → E 整步 → B 半步` 结构。

---

## 17. 尚未深入的内容

- [ ] `PushParticlesandDeposit()` 内部控制流
- [ ] 场 gather 的具体实现
- [ ] Boris、Vay、Higuera-Cary 粒子推进器
- [ ] Esirkepov 等电流沉积算法
- [ ] `SyncCurrentAndRho()` 内部同步流程
- [ ] `EvolveE()` / `EvolveB()` 的数值离散
- [ ] `PushPSATD()` 内部谱算法
- [ ] AMR 粗细层同步
- [ ] `OneStep_sub1()` 子循环路径
- [ ] `OneStep_JRhom()` 路径
- [ ] diagnostics 内部实现

---

## 18. 第一阶段结论

本阶段已经建立了 WarpX 从启动到完成一个标准显式 PIC 时间步的第一层地图：

```text
创建模拟器
  ↓
读取配置
  ↓
建立网格、场和粒子
  ↓
进入时间循环
  ↓
推进粒子并沉积
  ↓
同步电流和电荷
  ↓
更新电磁场
  ↓
处理边界和诊断
```

WarpX 的顶层算法仍然遵循标准 PIC 思路。其复杂性主要来自：

- 多种物理模型；
- 多种求解器；
- MPI 和 GPU 并行；
- AMR；
- PML；
- moving window；
- diagnostics；
- restart 和负载均衡。

后续学习应以这张控制流地图为基础，每次只深入一个模块，并始终明确它在整体流程中的位置。

---

## 19. 下一阶段建议

下一阶段建议从粒子主流程开始：

```text
PushParticlesandDeposit()
  ↓
Gather
  ↓
Particle Push
  ↓
Current / Charge Deposition
```

但在进入下一阶段前，应确保能够用自己的语言回答：

1. WarpX 对象何时创建？
2. 构造函数和 `InitData()` 有什么区别？
3. 主时间循环在哪里？
4. `OneStep()` 的作用是什么？
5. 标准显式 PIC 时间步为什么是“粒子 → 沉积 → 同步 → 场更新”？
