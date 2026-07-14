# 序言

AMReX（Adaptive Mesh Refinement in C++ for Exascale）是一个开源的、高性能的C++软件框架，专为构建大规模并行、自适应网格细化（Adaptive Mesh Refinement, AMR）应用程序而设计。





| BoxArray / DistributionMapping | 描述网格块的分布与并行划分                     |
| ------------------------------ | ---------------------------------------------- |
| AmrCore / AmrLevel             | AMR 层级管理框架                               |
| ParticleContainer              | 高性能粒子系统，支持粒子-网格交互              |
| MultiFab / iMultiFab           | 分布式多块数组，用于存储场变量（如密度、速度） |
| LinearSolvers                  | 多重网格、Krylov 子空间等求解器                |
| EB2（Embedded Boundary）       | 嵌入边界方法，处理复杂几何                     |

其它基本概念：

MPI：负责协调超算里**不同节点**（不同电脑）之间的通信。比如节点A算完后，把结果告诉节点B。











# AMReX on Laptop

1.安装基础编译工具。AMReX需要C++17编译器，在Ubuntu终端运行：

```
sudo apt install build-essential cmake g++ -y
```

2.获取并编译AMReX

```
git clone https://github.com/AMReX-Codes/amrex.git
cd amrex
mkdir build && cd build
cmake .. -DAMReX_MPI=NO  # 可以先关闭MPI，方便在个人电脑上测试
make -j$(nproc)          # 利用所有CPU核心进行编译
```







