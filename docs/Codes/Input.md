说明：WarpX的Input文件，一些固有板块和自定义板块。



# 1.激光

## 1.1 高斯激光

```
lasers.names        = laser1

laser1.position = 0. 0. zl
laser1.direction = 0. 0. 1.
laser1.polarization = 1. 0. 0.
laser1.a0 = a0
laser1.wavelength = lambda
laser1.phi0 = 0
laser1.profile =  Gaussian
laser1.profile_duration = 27e-15
laser1.profile_t_peak = 20e-15
laser1.profile_waist = 160e-6
laser1.profile_focal_distance = 8e-6
```

## 1.2 自定义

### 1.2.1 自定义A

主要特点： &#9312; 时间形状是改良的高斯上升/下降沿+平顶；改良主要是去掉了高斯太长的尾巴。 &#9313; 横向分布是trivial的平面波；圆偏振。

```
################ Laser ################

lasers.names = laser1 laser2

laser1.position = 0. 0. zl
laser1.direction = 0. 0. 1.
laser1.polarization = 1. 0. 0.
laser1.a0 = a0
laser1.wavelength = lambda
laser1.profile =  parse_field_function
laser1.field_function(X,Y,t) = E0*cos(w*t)*( e1*(t/s1)*(t>ts)*(t<ta)+exp(-(t-tb)^2/(2*s1^2))*(t>ta)*(t<tb)+1*(t>tb)*(t<tc)+exp(-(t-tc)^2/(2*s2^2))*(t>tc)*(t<td)+e1*(f-t/s2)*(t>td)*(t<te) )

laser2.position = 0. 0. zL
laser2.direction = 0. 0. 1.
laser2.polarization = 0. 1. 0.
laser2.a0 = a0
laser2.wavelength = lambda
laser2.profile =  parse_field_function
laser1.field_function(X,Y,t) = E0*sin(w*t)*( e1*(t/s1)*(t>ts)*(t<ta)+exp(-(t-tb)^2/(2*s1^2))*(t>ta)*(t<tb)+1*(t>tb)*(t<tc)+exp(-(t-tc)^2/(2*s2^2))*(t>tc)*(t<td)+e1*(f-t/s2)*(t>td)*(t<te) )

# 一种将高斯函数修改之后作为上升下降沿的平台型激光脉冲；对于电场E，将高斯过长的尾巴用一次函数平滑续接

#参数依赖

my_constants.e = 2.718282
my_constants.e1 = 1/sqrt(e) # e为自然常数，在warpx中没有内置需要定义

my_constants.s1 = T
my_constants.s2 = 2*T  #s1, s2是控制上升下降沿的参数，具体而言2*s1是上升沿整体宽度
my_constants.tau_p = 8*T

my_constants.ts = 0  #脉冲起始
my_constants.ta = ts + s1
my_constants.tb = ta + s1
my_constants.tc = tb + tau_p
my_constants.td = tc + s2
my_constants.te = td + s2

my_constants.f = te/s2
```

<img src="https://cdn.jsdelivr.net/gh/sampenn0326/PicGo@main/img/laser_profile_flattop_with_modified_gussian_rise%26down.png" alt="laser_profile_flattop_with_modified_gussian_rise&down" style="zoom: 33%;" />

### 1.2.2自定义B



```
lasers.names        = laser1

laser1.position = 0. 0. zl
laser1.direction = 0. 0. 1.
laser1.polarization = 1. 0. 0.
laser1.a0 = a0
laser1.wavelength = lambda
laser1.profile =  parse_field_function
laser1.field_function(X,Y,t) = E0*cos(w*t)*((t>ts)*(t<ta)*(t-ts)/tr+(t>ta)*(t<tb)*1+(t>tb)*(t<te)*(1-(t-tb)/tf))

#参数依赖

my_contants.tr = 0   #上升沿rise宽度
my_contants.tf = 0   #下降沿fall宽度
my_contants.tp = 0   #平顶宽度

my_contants.ts = 0           #上升沿开始start
my_contants.ta = ts + tr     #平顶开始
my_contants.tb = ta + tp     #平顶结束
my_contants.te = tb + tf     #下降沿结束end
```



# 2.等离子体靶

## 2.1 供密度、成分参考

一种CH2靶

据称 $n_e =220 n_c$ 是接近实验参数的

```
particles.species_names = ele H C

H.species_type = proton
H.injection_style = NUniformPerCell
H.num_particles_per_cell_each_dim = 2 2
H.momentum_distribution_type = at_rest
H.profile = parse_density_function
H.density_function(x,y,z) =  " n_H * (abs(x)<=x0)*((z<=D)*(z>=0) +(z<0)*(z>=z1)*exp(-abs(z)/L) ) "

C.charge = 6*q_e                 #注意一般离子的电荷、质量设置格式
C.mass = 12*m_p 
C.injection_style = NUniformPerCell
C.num_particles_per_cell_each_dim = 2 2
C.momentum_distribution_type = at_rest
C.profile = parse_density_function
C.density_function(x,y,z) =  " n_C * (abs(x)<=x0)*((z<=D)*(z>=0) +(z<0)*(z>=z1)*exp(-abs(z)/L) ) "


ele.species_type = electron
ele.injection_style = NUniformPerCell
ele.num_particles_per_cell_each_dim = 2 2
ele.momentum_distribution_type = at_rest
ele.profile = parse_density_function
ele.density_function(x,y,z) = " n_e * (abs(x)<=x0)*((z<=D)*(z>=0) + (z<0)*(z>=z1)*exp(-abs(z)/L) ) "

C60.charge = 10*q_e
C60.mass = 720*m_p 
C60.injection_style = NUniformPerCell
C60.num_particles_per_cell_each_dim = 2 2
C60.momentum_distribution_type = at_rest
C60.profile = parse_density_function
C60.density_function(x,y,z) =  " n_C * (abs(x)<=x0)*((z<=D)*(z>=0) +(z<0)*(z>=z1)*exp(-abs(z)/L) ) "
```

C60晶体的真实分子数密度1.38e21cm-3，或1.24nc。

## 2.2 供形状几何参考

一种横向正弦形靶。横向box恰好覆盖靶的一个横向空间周期时，可以恰当选用Periodic边界条件。

```
H.density_function(x,y,z) = " n_H * (z<=A0*sin(q*x))*(z>=-d0 + A0*sin(q*x)) "
```

一种um厚的平凸形靶。外加密度径向线性下降的调制。

```
H.density_function(x,y,z) = " nH*(z <= d0)*((z>=(x^2)/(2*Rc))*(1-abs(x)/RA)*(abs(x)<R0) ) "
```

一种nm数量级的凹凸形靶。

```
H.density_function(x,y,z) = " n_H*(z<=(d0*x^2)/(2*Rc^2))*(z>=(d0*(x^2/(2*Rc^2)-1)))*(abs(x)<=R0) "
```









# 3. Diags诊断

## 3.1 Full Diagnostics

```
diagnostics.diags_names = full

full.intervals = 100
full.diag_type = Full
full.format = openpmd
full.openpmd_backend = h5
full.write_species = 1
full.species = ele H C
full.ele.random_fraction = 0.01
full.H.random_fraction = 0.01
full.ele.variables = w ux uy uz x z
full.H.variables = w ux uy uz x z
full.fields_to_plot = Ex Ez rho_ele rho_H
full.coarsening_ratio = 2 2
```

设置时需要考虑每步输出文件大小，其中粒子数据约 $10\mathrm{w}->4.6\mathrm{MB}$ ，场数据 $1\mathrm{k}\times1 \mathrm{k}$  cells的一种场量对应 $8\mathrm{MB}$ 。

一次模拟总粒子数在 $100\mathrm{w}-1000\mathrm{w}%$ 为宜。



## 3.2 Time-Averaged Diagnostics

`TimeAveraged` 诊断有三种模式： `none` ， `fixed_start` 和 `dynamic_start` ，对应**不平均**、**固定开端平均**和**移动窗口平均**。

```
avrg.time_average_mode = fixed_start
avrg.average_start_step = 0

avrg.time_average_mode = dynamic_start
avrg.average_period_steps = 100
avrg.average_period_time = 2e-15  # 优先级比上一行高
```



## 3.3 BackTransformed Diagnostics









## 3.4 Boundary Scraping Diagnostics

WarpX的 `BoundaryScrapingDiagnostics` 专门收集在吸收边界被删除的粒子，并记录粒子撞击边界的时间等信息。









# 4.Reduced Diags 减量诊断

一个输出H、e能谱的案例

```
warpx.reduced_diags_names = spec_H spec_e

spec_H.type = ParticleHistogram
spec_H.intervals = 100
spec_H.species = H
spec_H.bin_number = 400
spec_H.bin_min = 0
spec_H.bin_max = 100
spec_H.histogram_function(t,x,y,z,ux,uy,uz) = "938.272*(sqrt(1+ux^2+uy^2+uz^2)-1)"
#筛选条件1：离子动能大于某阈值;如果只过滤能量较低的部分，直接设置bin_min即可
spec_H.filter_function(t,x,y,z,ux,uy,uz) = "938.272*(sqrt(1+ux^2+uy^2+uz^2)-1)>=10"
#筛选条件2：前向性离子
spec_H.filter_function(t,x,y,z,ux,uy,uz) = "uz>=0"

spec_e.type = ParticleHistogram
spec_e.intervals = 100
spec_e.species = ele
spec_e.bin_number = 400
spec_e.bin_min = 0
spec_e.bin_max = 100
spec_e.histogram_function(t,x,y,z,ux,uy,uz) = "0.510999*(sqrt(1+ux^2+uy^2+uz^2)-1)" #注意电子的静质量
#spec_e.filter_function(t,x,y,z,ux,uy,uz) = "uz>=0"
```

能谱按histogram诊断和实际粒子数的关系：

实际输出的每step的数据是分bin粒子数，按照ai解读官方文档的说法已经考虑了**粒子权重**，后处理时候该数据比上bin宽度就是真实的 $\mathrm{d}N/\mathrm{d}E$ 值。





























