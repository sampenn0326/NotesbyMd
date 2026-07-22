



# Theory

![Yee grid layout and leapfrog time integration](https://warpx.readthedocs.io/en/latest/_images/Yee_grid.png)





## 调用链

```C++
main()
  ↓
WarpX::GetInstance()
  ↓
WarpX::InitData()
  ↓
WarpX::Evolve()
  ↓
WarpX::OneStep()
  ↓
WarpX::PushParticlesandDeposit()
  ↓
MultiParticleContainer::Evolve()
  ↓
PhysicalParticleContainer::Evolve()
  ↓
PhysicalParticleContainer::PushPX()
  ↓
doGatherShapeN()
  ↓
doParticleMomentumPush()
  ↓
UpdateMomentumBoris()
  ↓
UpdatePosition()
  ↓
DepositCurrent()
  ↓
DepositCharge()
```

## 对象分层关系

### `WarpX`

`WarpX` 是最高层模拟**对象**，主要负责：

- 时间推进；
- AMR level；
- 网格场；
- field solver；
- 粒子容器；
   -边界与 PML；
   -诊断和负载均衡。

它不直接逐粒子执行 Gather 或 Boris。







# Particles



## `ParticleContainer`

`ParticleContainer`是"一类粒子的**管理器（manager）**"，它负责管理很多很多粒子，而不是描述单个粒子。

类似于

```
PhysicalParticleContainer
    ├── ux[]
    ├── uy[]
    ├── uz[]
    ├── x[]
    ├── y[]
    ├── z[]
    ├── weight[]
    ├── id[]
    └── ...
```

GPU偏好**SoA（Struct of Arrays）**而非**AoS（Arrays of Struct）**。Container 的本质就是管理很多SoA数组。

不同类型的粒子，对其进行的操作可能会不同。主要是按粒子行为进行分类组织的。

`PhysicalParticleContainer`管理普通带电粒子，如`electron proton C6+ Au79+`。这是要执行标准 PIC 粒子推进流程的一类粒子。

` MultiParticleContainer`是管理所有`Container`的`Container`。

```
MultiParticleContainer

    ├── electrons
    │      PhysicalParticleContainer
    │
    ├── protons
    │      PhysicalParticleContainer
    │
    ├── laser
    │      LaserParticleContainer
    │
    └── photons
           PhotonParticleContainer
```











