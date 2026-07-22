说明：WarpX的Input文件，一些固有板块和自定义板块。



# 1.激光

## 1.1 高斯激光

## 1.2 自定义

### 1.2.1 自定义A



```
################ Laser ################

lasers.names = laser1 laser2

laser1.position = 0. 0. zL
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

my.constants.e = 2.718282
my.constants.e1 = 1/sqrt(e) # e为自然常数，在warpx中没有内置需要定义

my.constants.s1 = T
my.constants.s2 = 2*T
my.constants.tau_p = 8*T

my.constants.ts = 0  #脉冲起始
my.constants.ta = ts + s1
my.constants.tb = ta + s1
my.constants.tc = tb + tau_p
my.constants.td = tc + s2
my.constants.te = td + s2

my.constants.f = te/s2
```

<img src="https://cdn.jsdelivr.net/gh/sampenn0326/PicGo@main/img/laser_profile_flattop_with_modified_gussian_rise%26down.png" alt="laser_profile_flattop_with_modified_gussian_rise&down" style="zoom: 33%;" />















































































# 2.等离子体靶



一种CH2靶

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
```







# Diags



## Full Diags

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

设置时需要考虑每步输出文件大小，其中粒子数据约10w->4.6MB，场数据$1k\times 1k $ cells的一种场量对应8MB。

一次模拟总粒子数在100w-1000w为宜。





# Reduced Diags

```
warpx.reduced_diags_names = histH ElecTemp      

histH.type = ParticleHistogram
histH.intervals = 100
histH.species = hydrogen
histH.bin_number = 400
histH.bin_min = 5
histH.bin_max = 100
histH.histogram_function(t,x,y,z,ux,uy,uz) = "938.272*(sqrt(1+ux^2+uy^2+uz^2)-1)"
#筛选条件1：离子动能大于某阈值
histH.filter_function(t,x,y,z,ux,uy,uz) = "938.272*(sqrt(1+ux^2+uy^2+uz^2)-1)>=10"
#筛选条件2：前向性离子
histH.filter_function(t,x,y,z,ux,uy,uz) = "uz>=0"

```































