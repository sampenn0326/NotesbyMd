说明：来源于对WarpX源码进行拆解学习时，顺便捡回记录一些C++基本知识，供之后自己查阅。

很大一部分来自各大论坛/网站/AI，如

菜鸟教程：[C++ 教程 | 菜鸟教程](https://www.runoob.com/cplusplus/cpp-tutorial.html)

C++学习网：[C++学习网 – 世界上最好的中文C++学习网站](https://www.studycpp.cn/)

在线汇编工具：

菜鸟工具[C++ 在线工具 | 菜鸟工具](https://www.jyshare.com/compile/12/)

onlineGDB[GDB online Debugger | Compiler - Code, Compile, Run, Debug online C, C++](https://www.onlinegdb.com/)

Replit：[Home - Replit](https://replit.com/~)



缓慢更新中(26.07.14)

### 变量

声明（使用`extern`关键字）

```C++
extern int a;        // 声明：告诉编译器a是int类型，在其他地方定义
extern int b = 10;   // 注意：这是定义！有初始化时extern失效
```

定义（无`extern`或带有初始化）

```C++
int a;               // 定义：分配内存，未初始化（全局变量默认0）
int b = 10;          // 定义：分配内存并初始化
static int c;        // 定义：静态变量
```



#### 常量变量

```C++
const int PI = 3.14;
constexpr double PI = 3.141592653589793;
```

`constexpr`编译期常量。



# 二、函数



## 2.0 基本简介

1.用户定义函数的形式

```C++
返回值类型 函数名() // 函数头，告知编译器函数的存在
{
    // 函数体
}
```

2.定义和调用函数的示例

```C++
#include <iostream>

// 用户自定义函数 doPrint()
void doPrint() // doPrint() 是被调函数
{
    std::cout << "In doPrint()\n";
}

// 定义函数 main()
int main()
{
    std::cout << "Starting main()\n";
    doPrint(); // 去执行函数 doPrint().  main() 是调用者.
    std::cout << "Ending main()\n"; // doPrint() 执行结束后，返回这里继续执行

    return 0;
}
```

3.可多次调用；可嵌套地调用

```C++
#include <iostream>

void doB()
{
    std::cout << "In doB()\n";
}


void doA()
{
    std::cout << "Starting doA()\n";

    doB();

    std::cout << "Ending doA()\n";
}

// Definition of function main()
int main()
{
    std::cout << "Starting main()\n";

    doA();

    std::cout << "Ending main()\n";

    return 0;
}
```

4.函数不能在函数中定义

## 2.1 返回值

1.返回值给变量初始化

```C++
#include <iostream>

int getValueFromUser() // 本函数返回一个int值
{
     std::cout << "Enter an integer: ";
    int input{};
    std::cin >> input;  

    return input; // 将用户输入的值返回给调用函数
}

int main()
{
    int num { getValueFromUser() }; // 使用getValueFromUser()的结果初始化变量num

    std::cout << num << " doubled is: " << num * 2 << '\n';

    return 0;
}
```

2.应确保具有非void返回类型的函数在所有情况下都返回值。

3.函数只能返回单个值，但有各种方法可以解决函数只能返回单个值的限制。

































































# C++ 头文件、源文件与声明/定义的完整关系

---

## 一、直观比喻（建立画面感）

想象你要**盖一栋房子**：

- **头文件（.h）** = **设计图纸**（告诉工人这里要有什么，但还没动手建）
- **源文件（.cpp）** = **施工过程**（按照图纸真正砌砖、搭梁）
- **声明** = 图纸上写的"这里要有一扇门"（承诺存在）
- **定义** = 工人在那个位置真的装了一扇门（实际创建）

**关键：** 声明可以多次，但定义只能一次（否则工人会装两扇门冲突）。

---

## 二、声明 vs 定义（必须先分清）

### 1. 声明（Declaration）
**告诉编译器"这个东西存在"**，但不分配内存/不生成代码。

```cpp
// 函数声明（没有函数体）
int add(int a, int b);

// 变量声明（使用 extern，不分配内存）
extern int globalCount;

// 类声明（前向声明）
class Student;  // 告诉编译器 Student 是一个类
```















































### 指针



指针变量的声明形式

```C++
int *p;      // p是一个指向int的指针
char *q;     // q是一个指向char的指针
double *r;   // r是一个指向double的指针
```

声明后初始化

```C++
int a = 10;
int *p = &a;   // 声明并初始化，指向a的地址
```

声明后幅值

```C++
int a = 10;
int *p;        // 先声明
p = &a;        // 后赋值（不是*p = &a）
```



### 函数

**C++的函数并不强制属于某个类或命名空间，但现代C++编程强烈建议这么做。**







### `namespace`命名空间



命名空间可以放什么：

```C++
namespace MyNamespace {
    // ✅ 变量
    int counter = 0;
    double pi = 3.14159;
    std::string name = "test";
    
    // ✅ 常量
    const int MAX_SIZE = 100;
    constexpr double GRAVITY = 9.81;
    
    // ✅ 函数
    double square(double x) { return x * x; }
    
    // ✅ 函数模板
    template<typename T>
    T add(T a, T b) { return a + b; }
    
    // ✅ 类/结构体
    struct Point {
        double x, y;
    };
    
    class Calculator {
    private:
        double memory;
    public:
        void set(double v) { memory = v; }
    };
    
    // ✅ 类型别名
    using Vector = std::vector<double>;
    typedef int Integer;
    
    // ✅ 枚举
    enum Color { RED, GREEN, BLUE };
    enum class Status { OK, ERROR };
    
    // ✅ 内联命名空间
    inline namespace V2 {
        void new_feature() {}
    }
    
    // ✅ 其他命名空间
    namespace Sub {
        int sub_value = 42;
    }
}
```















### 类class

C++ 在 C 语言的基础上增加了面向对象编程，C++ 支持面向对象程序设计。类是 C++ 的核心特性，通常被称为用户定义的类型。

**类**用于指定对象的形式，是一种<u>用户自定义的数据类型</u>，它是一种封装了数据和函数的组合。类中的数据称为成员变量，函数称为成员函数。类可以被看作是一种模板，可以用来创建具有相同属性和行为的多个对象。

定义一个类，本质上是定义一个数据类型的蓝图，它定义了类的对象包括了什么，以及可以在这个对象上执行哪些操作。

```C++
#include <iostream>
#include <string>

// 1. 定义类（蓝图）
class Student {
public: // 访问修饰符：公共成员，外部可以访问
    // 成员变量（属性）
    std::string name;
    int age;

    // 成员函数（方法）
    void introduce() {
        std::cout << "我叫" << name << "，今年" << age << "岁。" << std::endl;
    }
};

int main() {
    // 2. 实例化对象（栈上创建）
    Student stu1;
    stu1.name = "张三";
    stu1.age = 20;
    stu1.introduce(); // 输出：我叫张三，今年20岁。

    // 3. 堆上创建对象（使用指针）
    Student* stu2 = new Student();
    stu2->name = "李四"; // 指针用 ->
    stu2->age = 22;
    stu2->introduce();
    delete stu2; // 必须手动释放内存

    return 0;
}
```





## SoA和AoS

- **AoS（Array of Structures）**：结构体的数组。数据按“对象”聚集，每个对象拥有所有属性。
- **SoA（Structure of Arrays）**：数组的结构体。数据按“属性”聚集，每个属性单独放在一个连续数组中。

例如
