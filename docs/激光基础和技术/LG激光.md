# Laguerre–Gaussian（LG）激光

LG 光束是真空傍轴波动方程在圆柱坐标下的一族模式，记作 \(\mathrm{LG}_p^\ell\)。它有两个独立指标：径向指标 \(p=0,1,2,\ldots\) 决定径向节点，方位指标 \(\ell=0,\pm1,\pm2,\ldots\) 决定相位绕轴一周转过多少。最常见的甜甜圈光斑是 \(p=0,\ell\ne0\) 的情形，而普通基模高斯光束就是 \(\mathrm{LG}_0^0\)。

## 1. 从波动方程到 LG 模式

设光沿 \(+z\) 传播，\(k=2\pi/\lambda\)，采用 \(e^{i(kz-\omega t)}\) 的载波约定。以固定横向偏振矢量 \(\hat{\mathbf e}\) 为例，写成


$$
\mathbf E_\perp =\operatorname{Re}\!\left[ E_0\hat{\mathbf e}\,u(r,\phi,z)e^{i(kz-\omega t)} \right]
$$


把它代入真空 Helmholtz 方程，对慢变包络略去 \(\partial_z^2u\)，得到


$$
2ik\,\partial_z u+ \left[ \partial_r^2+\frac1r\partial_r+ \frac1{r^2}\partial_\phi^2 \right]u=0
$$


由于方程具有旋转对称性，可以令 \(u=f(r,z)e^{i\ell\phi}\)。场绕轴一圈应回到原值，因此 \(\ell\) 必须是整数。此时径向方程里出现 \(-\ell^2 f/r^2\)。靠近轴时，径向主导项满足


$$
f''+\frac1r f'-\frac{\ell^2}{r^2}f\simeq 0
$$


取轴上正则的解便有 \(f\propto r^{|\ell|}\)。**这一步已经解释了涡旋暗核**：当 \(\ell\ne0\) 时，轴上方位角无定义，正则的标量包络以 \(r^{|\ell|}\) 趋于零。

完整的 LG 模式可写为 [harvest.aps.org](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevA.45.8185/fulltext?utm_source=chatgpt.com)。


$$
\boxed{ u_p^\ell= C_{p\ell}\frac{w_0}{w(z)} \left(\frac{\sqrt2 r}{w(z)}\right)^{|\ell|} L_p^{|\ell|}\!\left(\frac{2r^2}{w^2(z)}\right) e^{-r^2/w^2(z)} e^{i\ell\phi} e^{ikr^2/[2R(z)]} e^{-i(2p+|\ell|+1)\psi(z)} }
$$


其中 \(L_p^{|\ell|}\) 是广义 Laguerre 多项式，\(C_{p\ell}\) 是归一化常数，束腰位于 \(z=0\)。


$$
z_R=\frac{\pi w_0^2}{\lambda},\qquad w(z)=w_0\sqrt{1+(z/z_R)^2},\qquad R(z)=z\left[1+(z_R/z)^2\right],\qquad \psi(z)=\arctan(z/z_R)
$$


| 因子              | 物理含义                        |
| ----------------- | ------------------------------- |
| (r^{              | \ell                            |
| (L_p^{            | \ell                            |
| \(e^{-r^2/w^2}\)  | 高斯包络限制光束的横向范围      |
| \(e^{i\ell\phi}\) | 绕轴一周，相位累积 \(2\pi\ell\) |
| \(e^{ikr^2/2R}\)  | 波前曲率，束腰处 \(1/R=0\)      |
| (e^{-i(2p+        | \ell                            |

## 2. 从束腰光斑读出 \(p\)、\(|\ell|\) 和 \(w_0\)

先看最简单的 \(\mathrm{LG}_0^\ell\)。因为 \(L_0^{|\ell|}=1\)，傍轴强度满足

\[ I(r,z)\propto \left(\frac{w_0}{w(z)}\right)^2 \left(\frac{2r^2}{w^2(z)}\right)^{|\ell|} e^{-2r^2/w^2(z)}. \]

对 \(r\) 求极值，就得到亮环半径

\[ \boxed{r_{\rm peak}(z)=w(z)\sqrt{\frac{|\ell|}{2}}.} \]

所以在设置激光参数时，**\(w_0\) 是高斯包络的尺度，亮环半径由 \(w_0\) 和 \(|\ell|\) 共同决定**。例如 \(\lambda_0=1\,\mu\mathrm m\)、\(w_0=2\lambda_0\) 时，\(z_R=12.57\,\mu\mathrm m\)。\(\mathrm{LG}_0^1\) 的束腰亮环半径为 \(1.41\,\mu\mathrm m\)，\(\mathrm{LG}_0^2\) 则为 \(2.00\,\mu\mathrm m\)。

| 模式                   | 束腰强度                       | 相位绕轴一周的变化                           |
| ---------------------- | ------------------------------ | -------------------------------------------- |
| \(\mathrm{LG}_0^0\)    | 中心最亮                       | \(0\)                                        |
| \(\mathrm{LG}_0^{+1}\) | 中心暗，单亮环                 | \(+2\pi\)                                    |
| \(\mathrm{LG}_0^{-1}\) | 与 \(\mathrm{LG}_0^{+1}\) 相同 | \(-2\pi\)                                    |
| \(\mathrm{LG}_0^{+2}\) | 中心暗，单亮环，峰值半径更大   | \(+4\pi\)                                    |
| \(\mathrm{LG}_1^{+1}\) | 两个亮环，中间有一个径向零点   | \(+2\pi\)，另有跨径向节点的 \(\pi\) 相位跳变 |

固定 \(z\)，沿亮环测复场相位，可以区分 \(\ell=+1\) 和 \(\ell=-1\)。实验上把它与倾斜的参考平面波干涉，相位奇点会在干涉条纹中表现为叉形分叉。模拟里可直接在避开暗核与径向节点的闭合圆上计算相位绕转。

## 3. 螺旋波前怎样产生轨道角动量？

在束腰附近、固定半径上，忽略曲率相位和 Gouy 相位的局部变化，有

\[ \Phi\simeq kz+\ell\phi-\omega t. \]

固定时间、追踪同一等相位面，便有

\[ \frac{dz}{d\phi}\simeq-\frac{\ell}{k}. \]

这就是螺旋波前的几何来源。进一步看相位梯度，它有方位分量

\[ (\nabla\Phi)_\phi=\frac1r\,\partial_\phi\Phi=\frac{\ell}{r}. \]

在傍轴近似中，这对应轨道能流的方位分量。在强度显著且傍轴近似成立的区域，其与纵向能流之比约为 \(S^{\rm orb}_\phi/S_z\simeq \ell/(kr)\)。所以单个 LG 模式的**强度可以完全轴对称，同时能流携带绕轴的角动量**。这里的方位分量有 \(1/r\)，而轴附近的强度按 \(r^{2|\ell|}\) 消失。 [harvest.aps.org](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevA.45.8185/fulltext?utm_source=chatgpt.com)

用算符写更直接。绕 \(z\) 轴的轨道角动量算符作用在标量模式上，

\[ \hat L_z u_p^\ell=-i\hbar\,\partial_\phi u_p^\ell =\ell\hbar\,u_p^\ell. \]

因此单色傍轴 LG 模式每光子的轴向轨道角动量是 \(\ell\hbar\)。圆偏振还提供自旋角动量 \(\sigma\hbar\)，其中 \(\sigma=\pm1\) 由偏振旋向决定。两者相加得到 \(J_z=(\ell+\sigma)\hbar\)。线偏振的平均轴向自旋为零，同时可以保留由 \(e^{i\ell\phi}\) 决定的轨道角动量。 [doi.org](https://doi.org/10.1103%2FPhysRevA.45.8185?utm_source=chatgpt.com)

一个能把“相位”变成“光斑”的例子是相干叠加同阶、等幅的 \(+\ell\) 和 \(-\ell\) 模式。它们的共同径向因子记作 \(A(r,z)\)，则

\[ u=A(r,z)(e^{i\ell\phi}+e^{-i\ell\phi}) =2A(r,z)\cos(\ell\phi), \qquad I\propto |A|^2\cos^2(\ell\phi). \]

单个模式是圆环，叠加后出现 \(2|\ell|\) 个亮瓣。两个相反的轨道角动量等权叠加，平均轨道角动量为零。



















![beam_field_one_cycle](C:\Users\zsxl0\Downloads\beam_field_one_cycle.gif)