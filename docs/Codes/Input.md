







## L激光

### 高斯激光







### 自定义激光A

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

















































































## T靶形状和组成

































