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

4.使用函数可有效改善重复和冗余

```C++
#include <iostream>

int getValueFromUser()
{
     std::cout << "Enter an integer: ";
    int input{};
    std::cin >> input;  

    return input;
}

int main()
{
    int x{ getValueFromUser() };
    int y{ getValueFromUser() };

    std::cout << x << " + " << y << " = " << x + y << '\n';

    return 0;
}
```

## 2.2 无返回值函数

```C++
#include <iostream>

// void 意味着函数不返回值给调用方
void printHi()
{
    std::cout << "Hi" << '\n';

    // 不返回数据，所以不需要return 语句
}

int main()
{
    printHi(); // 无需接收返回值

    return 0;
}
```

无返回值；不要写`return`；不要调用在需要值的语句处。

## 2.3 函数参数

1.函数参数是**函数头**中定义的变量，它的初始值由**函数调用方**提供。函数参数在函数头中定义，放在函数名后面的括号之间，多个参数用逗号分隔。

2.调用函数时，所有参数被创建为变量，每个值都被复制到匹配的参数中。该过程称为**按值传递**。

```C++
#include <iostream>

// 本函数有两个参数，x与y
// 调用函数需要提供两个值，分别给x与y
void printValues(int x, int y)
{
    std::cout << x << '\n';
    std::cout << y << '\n';
}

int main()
{
    printValues(6, 7); // 函数调用，传递6，7，分别给x和y

    return 0;
}
```

用参数6和7调用函数`printValues`时，会创建`printValues`的参数`x`并初始化为值6，创建`printValues`的参数`y`并初始化为值7。参数传递的本质就是**参数的初始化**。

3.使用函数的返回值作为参数

```C++
#include <iostream>

int getValueFromUser()
{
 	std::cout << "Enter an integer: ";
	int input{};
	std::cin >> input;  

	return input;
}

void printDouble(int value)
{
	std::cout << value << " doubled is: " << value * 2 << '\n';
}

int main()
{
    int num { getValueFromUser() };

	printDouble(num);       //用num传递

	printDouble(getValueFromUser());  //用返回值直接传递

	return 0;
}
```

4.更多案例

```C++
#include <iostream>

int add(int x, int y)
{
    return x + y;
}

int multiply(int z, int w)
{
    return z * w;
}

int main()
{
    std::cout << add(4, 5) << '\n'; //  add() x=4, y=5, x+y=9
    std::cout << add(1 + 2, 3 * 4) << '\n'; // add() x=3, y=12, x+y=15

    int a{ 5 };
    std::cout << add(a, a) << '\n'; // (5 + 5)

    std::cout << add(1, multiply(2, 3)) << '\n'; // 1 + (2 * 3)
    std::cout << add(1, add(2, 3)) << '\n'; // 1 + (2 + 3)

    return 0;
}
```

5.未使用的参数

在函数参数**需要存在**但未被使用的情况下，可以简单地省略名称。没有名称的参数称为**未命名参数**，同时建议使用注释来记录未命名参数的名称

```C++
void doSomething(int) // ok: 未命名参数
{
}

void doSomething(int /*count*/)
{
}
```

## 2.4 局部变量

1.在函数体中定义的变量称为**局部变量**（相对于在后面讨论的**全局变量**）；函数参数通常也被认为是局部变量

```C++
int add(int x, int y)  // 函数参数x y 是局部变量
{
    int z{ x + y }; // z 是局部变量

    return z;
}
```

2.**生命周期**

```C++
int add(int x, int y) // x y 在这里被创建和初始化
{ 
    int z{ x + y }; // z 在这里被创建和初始化

    return z;
} // z, y, and x 在这里被销毁
```

变量实例的**生命周期**被定义为<u>创建和销毁之间的时间</u>。注意，变量的创建和销毁发生在程序运行时（称为运行时），而不是在编译时。因此，生命周期是一个运行时属性。

3.**局部变量作用域**

变量的作用域决定了在源代码中能看到和使用变量的位置。当变量能被看到和使用时，它就在作用域内。当变量不可见、不能被使用时，它就超出了作用域。作用域是**编译**时属性，使用不在作用域内的变量将导致编译错误。

局部变量的作用域从变量**定义点**开始，到定义所在的花括号末尾（对于函数参数，到函数的末尾）。这确保了变量不能在定义点之前使用（即使编译器可能在定义点之前就创建了它）。在一个函数中定义的局部变量，其作用域不包括其他任何函数。

```C++
#include <iostream>

// x 不在 doSomething 函数内可见
void doSomething()
{
    std::cout << "Hello!\n";
}

int main()
{
    // 在这里x 不能被使用

    int x{ 0 }; // 从这里到函数末尾，x可以被使用

    doSomething();

    return 0;
} // 这里到了x 的作用域的末尾
```

处于生命周期内的变量，不一定在对应代码的作用域内；并不是所有类型的变量实例都在超出作用域时被销毁。

4.不同函数的同名局部变量不冲突。

5.定义局部变量的位置：在现代C++中，函数体中的局部变量应当定义<u>在尽可能靠近其首次使用的位置</u>

```C++
#include <iostream>

int main()
{
	std::cout << "Enter an integer: ";
	int x{}; // x 在这里定义
	std::cin >> x; // 在这里使用

	std::cout << "Enter another integer: ";
	int y{}; // y 在这里定义
	std::cin >> y; // 在这里使用

	int sum{ x + y }; // sum 在这里定义
	std::cout << "The sum is: " << sum << '\n';

	return 0;
}
```

## 2.5 为什么需要函数

**优点**

1. 可组织性——随着程序功能增加，将所有代码放在main()中会变得越来越复杂。函数就像一个小程序，能独立于主程序编写，不必在编写时考虑程序的其余部分。它将复杂的程序简化为更小、更易于管理的模块，降低了程序管理的整体复杂性。
2. 可重用性——一旦编写了函数，就可以在程序中多次调用。这避免了重复代码，并将复制/粘贴错误的概率降至最低。函数也可以与其他程序共享，减少了每次从头编写（并重新测试）的代码量。
3. 可测试性——由于函数减少了代码冗余，需要测试的代码更少。此外，因为函数是自包含的，一旦测试确认函数工作正常，除非有更改，否则不需要再次测试。这减少了需要测试的代码量，从而更容易发现错误（或从一开始就避免错误）。
4. 可扩展性——当需要扩展程序来处理以前没有处理的情况时，函数在一处更改，并在每次调用时生效。
5. 抽象——使用函数时，只需要知道它的名称、输入、输出以及所在位置，无需了解它如何工作，也无需知道它依赖的其他代码。这降低了使用他人代码（包括标准库）所需的知识量。

**编写函数的一些基本准则**

1. 程序中出现多次的语句组通常应编写成函数。例如，如果以相同方式多次读取用户的输入，将其组织成函数是很好的做法。如果在多个位置以相同的方式输出内容，也可以编写成函数。
2. 具有明确输入和输出的代码（特别是逻辑较复杂时）适合编写成函数。例如，如果有一个要排序的列表，那么执行排序的代码就很适合做成函数，即使只被使用一次。输入是未排序的列表，输出是已排序的列表。另一个适合组织成函数的功能是模拟六面骰子的投掷结果。当前程序可能只使用一次，但如果将其转换为函数，以后就可以在扩展程序或其他程序中重用。
3. 函数通常应执行一个（且只执行一个）任务。
4. 当函数变得太长、太复杂或难以理解时，可以将其拆分为多个子函数。这称为重构。

## 2.6 前向声明

1.在多个函数存在相互调用的情况下，人为控制函数定义的顺序并不一定能奏效。此时可以通过**前向声明**来解决，前向声明允许在实际定义标识符之前告诉编译器标识符的存在。

对于函数，前向声明允许在定义函数体之前告诉编译器该函数的存在。这样，当编译器遇到函数调用时，就能理解这是一个函数调用，并检查是否正确地调用了该函数，即使编译器还不知道函数的实际定义。

2.声明形式

```C++
#include <iostream>

int add(int x, int y); // 函数add()的前向声明

int main()
{
    std::cout << "The sum of 3 and 4 is: " << add(3, 4) << '\n'; // 可以通过编译
    return 0;
}

int add(int x, int y) // 函数add()在这里定义
{
    return x + y;
}
```

函数声明不需要指定参数的名称，如

```C++
int add(int, int); // 有效的前向声明语句
```

3.声明的必要性

即使可以重新排序函数的顺序使程序工作，也要使用前向声明。因为大多数情况下，前向声明用于告诉编译器<u>在其他代码文件中定义的函数</u>。

此外，前向声明也可以让我们以不受顺序限制的方式定义函数，以最容易阅读和理解的顺序来组织函数。

在循环依赖情况下，只能通过前向声明来解决。

4.声明与定义

**声明**告诉编译器标识符的存在及其关联的类型信息

```C++
int add(int x, int y); // 告诉编译器函数add的存在，参数是2个int，返回值是int，无函数体
int x;                 // 告诉编译器变量x的存在，类型是int
```

**定义**是一个声明，它实际实现（对于函数和类型）或实例化（对于变量）标识符

```C++
int add(int x, int y) // 函数add()的实现
{
    int z{ x + y };   // 实例化变量 z

    return z;
}

int x;                // 实例化变量 x
```

在C++中，所有定义都是声明。因此`int x;` 既是定义又是声明（区别于初始化）。

但并非所有的声明都是定义。不是定义的声明称为**纯声明**。纯声明的类型包括函数、变量和类型的前向声明。

在此前提下：术语”声明”用于表示”纯声明”，”定义”用于表示”同时也是声明的定义”。因此，`int x;` 通常被称为定义，即使它既是定义又是声明。

























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
