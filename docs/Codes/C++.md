说明：来源于对WarpX源码进行拆解学习时，顺便捡回记录一些C++基本知识，供之后自己查阅。

很大一部分来自各大论坛/网站/AI，如

菜鸟教程：[C++ 教程 | 菜鸟教程](https://www.runoob.com/cplusplus/cpp-tutorial.html)

C++学习网：[C++学习网 – 世界上最好的中文C++学习网站](https://www.studycpp.cn/)

基本上是边学边copy，有不同的地方就是觉得多余或者不必要摘录了，偶有改删。

有用的在线汇编工具：

菜鸟工具[C++ 在线工具 | 菜鸟工具](https://www.jyshare.com/compile/12/)

onlineGDB[GDB online Debugger | Compiler - Code, Compile, Run, Debug online C, C++](https://www.onlinegdb.com/)

Replit：[Home - Replit](https://replit.com/~)



缓慢更新中(26.07.16)

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

5.单定义规则

单定义规则（简称ODR，The one definition rule）由三部分组成：

1. 在同一文件的同一作用域内，<u>函数、变量、类型、模板</u>只能定义一次。不同作用域中的同名定义不违反此规则（例如不同函数中的同名变量，不同命名空间内的同名函数）。
2. 在同一程序中，函数或变量只能定义一次。因为程序可能有多个文件，发生冲突时无法处理。不被链接器可见的定义不受此规则限制。
3. 类型、模板、内联函数、内联变量可以在多个文件中同时定义，只要它们的定义是一致的。

有不同参数的同名函数是不同的函数，见**函数重载**章。

## 2.7 多代码文件程序

1.示例

`main.cpp`：

```C++
#include <iostream>

int add(int x, int y); // 让 main.cpp 知道 add() 是在其它地方定义的函数

int main()
{
    std::cout << "The sum of 3 and 4 is: " << add(3, 4) << '\n';
    return 0;
}
```

`add.cpp`：

```C++
int add(int x, int y)
{
    return x + y;
}
```

分多文件时，也需要必要的前向声明。因为：

编译器是<u>单独编译</u>每个文件的。它不知道其他代码文件的内容，也不记得从之前编译的其他代码文件中看到的内容。

这种有限的可见性和短暂的记忆是有意设计的，原因有三：

1. 一个项目中的多个文件可以按任意顺序编译。
2. 如果修改了单个文件，只有修改过的文件需要重新编译。
3. 减少了不同文件之间发生命名冲突的概率。

由于编译器单独编译每个代码文件（然后忘记它看到的内容），因此使用`std::cout`或`std:∶cin`的每个代码文件都需要 `#include <iostream>`。

## 2.8 命名冲突和命名空间

C++要求所有标识符都是不含歧义的。如果编译器或链接器无法区分两个相同的标识符，就会提示程序出错。此错误称为**命名冲突**。如果将冲突的标识符引入同一文件，则会产生编译器错误。如果将冲突的标识符引入属于同一程序的不同文件中，则会产生链接错误。

大多数命名冲突发生在两种情况下：

1. 两个同名函数（或全局变量）在程序不同文件中同时存在，会导致上述**链接错误**。
2. 两个同名函数（或全局变量）在同一文件中存在，导致**编译错误**。

### 命名空间

**命名空间**是一个区域，在其中声明名称以消除歧义。命名空间为其内部声明的名称提供了一个作用域区域（称为命名空间作用域）——意味着在命名空间内声明的任何名称都不会与其他作用域中的<u>相同名称</u>混淆。

在同一命名空间中，所有名称必须唯一，否则将导致命名冲突。

命名空间通常用于对大型项目中的相关标识符进行分组，以帮助确保它们不会与其他标识符意外冲突。例如，如果将所有数学函数放在名为math的命名空间中，则数学函数不会与math命名空间外部的同名函数冲突。

### 全局命名空间

在C++中，任何未在类、函数或命名空间内定义的名称，都被认为属于**全局命名空间**（有时也称为全局作用域）这一隐式定义的命名空间。

（例如到目前为止示例的所有函数）

在全局命名空间中<u>只能出现声明和定义语句</u>。这意味着应尽量避免在全局命名空间中定义变量。同时也意味着其他类型的语句（如表达式语句）不能放在全局命名空间中（全局变量的初始化值是例外）。

```C++
#include <iostream> // 被预处理器处理

// 下面所有的语句都是在全局命名空间中
void foo();    // 前向函数声明
int x;         // 可以编译通过但不推荐，全局命名空间中的未初始化变量
int y { 5 };   // 可以编译通过但不推荐，全局命名空间中的初始化变量
x = 5;         // 编译失败，可执行语句

int main()     // 函数定义
{
    return 0;
}

void goo();    // 前向函数声明
```

### std命名空间

C++将**标准库**中的所有功能放到了名为”std”（standard的缩写）的命名空间中。

让编译器从`std`命名空间中使用`cout`的最直接的方法是显式使用`std::`前缀；

「`::`」符号是一个称为作用域解析运算符的符号。`::`符号左侧表示命名空间，`::`符号右侧是命名空间中的标识符。如果`::`符号左侧没有提供标识符，则默认为全局命名空间；

这是使用`cout`的最安全的方法，而`using namespace`应当尽量避免。

## 2.8 预处理器简介

在编译之前，每个代码（.cpp）文件都要经过**预处理阶段**。在这个阶段，预处理器会对代码文件进行一些更改。预处理器不会修改原始代码文件——所做的更改都是临时地发生在内存中或使用临时文件。

预处理器所做的大多数工作都很琐碎。例如，<u>去除注释，确保每个代码文件以换行结束</u>。然而，预处理器确实有一个非常重要的作用：它会处理`#include`指令。

预处理器完成对代码文件的处理后，处理结果称为**翻译单元**。翻译单元是编译器随后编译的基本单元。翻译单元既包含来自代码文件的代码，也包含所有#included文件的处理代码。

预处理、编译和链接的整个过程称为翻译。

### 预处理命令

预处理器运行时，会扫描代码文件（从上到下），查找预处理指令。**预处理指令**是以#符号开头、以换行符（不是分号）结尾的指令。这些指令告诉预处理器执行某些文本操作任务。注意，预处理器不理解C++语法——它有自己的语法（在某些情况下类似于C++语法，在其他情况下则差异较大）。

#### include

当`#include`一个文件时，预处理器<u>将`#include`指令替换为所包含文件的内容</u>。然后对包含的内容进行预处理（这可能导致递归地预处理其他`#include`文件），接着处理文件的其余部分。

#### 宏定义

`\#define`指令用于创建**宏**。C++中，宏是一条规则，定义如何将输入文本转换为替换输出文本。

宏有两种基本类型：<u>类对象宏和类函数宏</u>。

类函数宏的行为类似于函数，并有类似的用途。使用它们通常是不安全的，它能做的事情都可以用普通函数完成。

类对象宏可以用两种方法定义

```C++
#define 标识符
#define 标识符 替换文本
```

宏的标识符与普通标识符使用相同的命名规则：可以使用字母、数字和下划线，不能以数字开头，也不能以下划线开头。按照惯例，宏名称通常全部使用大写字母，用下划线分隔。

#### 具有替换文本的类对象宏

当预处理器遇到该指令时，后续出现的每个该标识符都将被替换为substitution_text。标识符按惯例使用全大写字母，用下划线表示空格。例如

```C++
#include <iostream>

#define MY_NAME "Fly"

int main()
{
    std::cout << "My name is: " << MY_NAME << '\n';

    return 0;
}
```

预处理器将上述转换为以下内容

```C++
// iostream 中的内容将会被替换到这里

int main()
{
    std::cout << "My name is: " << "Fly" << '\n';

    return 0;
}
```

具有替换文本的类对象宏在C中用于为文本分配名称。但在C++中提供了更好的替代方案。具有替换文本的类对象宏现在只能在旧代码中看到。

建议**避免**使用这种类型的宏，因为有更好的实现方式。后续章节会讨论——常量变量和符号常量。

#### 无文本替换的类对象宏

```C++
#define USE_YEN
```

工作方式：标识符的任何后续出现都将被删除，且不替换为任何内容！

这种形式的宏<u>通常被认可使用</u>。

#### 条件编译

条件编译预处理器指令允许指定在某些条件下编译或不编译某些代码，最常用的有三个：`#ifdef`、`#ifndef`和`#endif`。

`\#ifdef`预处理器指令允许预处理器检查某个标识符是否已被`#define`定义过。如果是，则编译`#ifdef`和匹配的`#endif`之间的代码。如果不是，则忽略这些代码。例如

```C++
#include <iostream>

#define PRINT_JOE

int main()
{
#ifdef PRINT_JOE
    std::cout << "Joe\n"; // PRINT_JOE被定义，这一行会被编译
#endif

#ifdef PRINT_BOB
    std::cout << "Bob\n"; // PRINT_BOB未被定义，这一行不会被编译
#endif

    return 0;
}
```

`#ifndef`与`#ifdef`相反，允许检查标识符是否未定义。

```C++
#include <iostream>

int main()
{
#ifndef PRINT_BOB
    std::cout << "Bob\n";
#endif

    return 0;
}  //该程序打印“Bob”，因为PRINT_BOB未定义
```

`#if defined(PRINT_BOB)`和`#if !defined(PRINT_BOB)`这两种写法也是合法的。

#### `if 0`

条件编译的另一个常见用法是使用`#if 0`来排除不需要编译的代码块（效果和使用注释块一样）：

```C++
#include <iostream>

int main()
{
    std::cout << "Joe\n";

#if 0 // 从这里开始的不编译
    std::cout << "Bob\n";
    std::cout << "Steve\n";
#endif // 到这里结束

    return 0;
}
```

这提供了一种方便的方法<u>来”注释掉”包含多行注释的代码</u>（由于多行注释不可嵌套，无法使用另一个多行注释来注释掉已有的多行注释）

```C++
#include <iostream>

int main()
{
    std::cout << "Joe\n";

#if 0 // 从这里开始的不编译
    std::cout << "Bob\n";
    /* 一些
     * 多行
     * 注释
     */
    std::cout << "Steve\n";
#endif // 到这里结束

    return 0;
}
```

要临时重新启用被`#if 0`包裹的代码，可以将`#if 0`改成`#if 1`。

#### 类对象宏不影响其他预处理器指令

也就是，宏只会导致普通代码中的文本替换，而会忽略其他预处理器指令。例如

```C++
#define PRINT_JOE

#ifdef PRINT_JOE    //这里的PRINT_JOE存在于预处理代码中，不会被#define替换为空
// ...
```

#### `#define`的作用范围

考虑

```C++
#include <iostream>

void foo()
{
#define MY_NAME "Fly"
}

int main()
{
	std::cout << "My name is: " << MY_NAME << '\n';

	return 0;
}
```

尽管`#define MY_NAME “Fly"`写在函数`foo`内部，但预处理器不理解C++的概念（如函数）。因此，该程序的行为与`#define MY_NAME “Fly"`放在函数`foo`之前或之后是一样的。为了可读性，通常应将`#define`放在函数外部。

一旦预处理器处理完成，该文件中所有通过`#define`定义的标识符将被丢弃。这意味着指令仅从定义点到定义它们的文件末尾有效。在一个代码文件中定义的指令不会影响同一项目中的其他代码文件。

示例

`function.cpp`

```C++
#include <iostream>

void doSomething()
{
#ifdef PRINT
    std::cout << "Printing!\n";
#endif
#ifndef PRINT
    std::cout << "Not printing!\n";
#endif
}
```

`main.cpp`

```C++
void doSomething(); // 前向声明 doSomething()

#define PRINT

int main()
{
    doSomething();

    return 0;
}                    //运行结果将是  Not printing!
```

## 2.10 头文件

### 头文件及用途

复杂程序中，不同cpp文件中会需要大量重复的前向声明。如果能将所有的前向声明放在一个地方，在需要时导入，会方便很多。C++中还有一种类型的文件称为**头文件**。头文件通常使用.h扩展名，偶尔也会使用.hpp扩展名或没有扩展名。头文件的主要目的是<u>将声明传播到代码（.cpp）文件中</u>。

总之：头文件允许将声明集中放在一起，在需要的地方导入。这可以省去多文件程序中大量冗余且单调的工作。

当`#include`引用一个文件时，所引用文件的内容将替换到`#include`所在的位置。这提供了一种从另一个文件中拉入声明的便捷方法。

### 使用头文件传播前向声明

为每个位于其他文件中的函数手动添加前向声明是重复且冗余的，编写一个头文件可以减轻这个负担。

编写头文件非常容易，因为头文件仅由两部分组成：

1. 头文件保护，下一节中讨论。
2. 头文件的实际内容。包含其它文件要使用的前向声明。

头文件通常与代码文件配对，头文件为相应的代码文件提供前向声明。(即`add.h`&`add.cpp`)例如

`add.h`

```C++
// 1) 这里需要一个头文件保护。

// 2) 这里是 .h 文件内容
int add(int x, int y); // add函数声明，不要忘记分号
```

在`main.cpp`中使用此头文件，需`#include`引用它

```C++
#include "add.h" // add.h 的内容会被插入这里。需要使用双引号
#include <iostream>

int main()
{
    std::cout << "The sum of 3 and 4 is " << add(3, 4) << '\n';
    return 0;
}
```

`add.cpp`

```C++
#include "add.h" // add.h 的内容会被插入这里。需要使用双引号

int add(int x, int y)
{
    return x + y;
}
```

![img](https://www.studycpp.cn/basic/chapter2/header-file/IncludeHeader.webp)

### 避免在头文件包含定义

因为如果头文件被多个源文件使用，这样做会违反单定义规则（ODR）。

如果两个`cpp`文件同时`#include`了一个包含函数定义的`h`文件，在二者编译时不会出现问题，单链接器运行时将看到某函数`fun()`有两处定义。

### 其余注意事项

1.推荐头文件与源文件配对，这可以让编译器在编译时而不是链接时捕获某些类型的错误。

2.不要`#include` `.cpp`文件

3.尖括号：预处理器知道这不是程序员自己编写的头文件。预处理器将仅在系统目录指定的目录中搜索头文件。双引号：预处理器知道这是编写的头文件。预处理器首先在当前目录中搜索头文件。如果找不到匹配的头文件，将搜索系统目录。

4.头文件可以include其他头文件，但尽量通过显式`#include`代码文件所需的所有头文件，避免依赖于递归的include。

5.头文件include的顺序无关紧要。

6.相互依赖的情况下要注意顺序，如`main.cpp`中先include了`B.h`，后include`A.h`，那么即便`A.h`中存在对`B.h`的依赖，仍能正常编译；顺序交换则不行。

7.最佳`#include`顺序：

- 与当前cpp文件对应的h文件
- 本项目中的其它头文件
- 第三方库的头文件
- 标准库的头文件

每个分组的头文件应按字母顺序排序（除非第三方库的文档有明确指示）。

### 头文件最佳实践

下面是创建和使用头文件的一些建议。

1. 始终使用头文件保护（将在下一课中介绍）。
2. 不要在头文件中定义变量和函数（目前）。
3. 为头文件提供与其关联的源文件相同的名称（例如，grades.h与grades.cpp成对出现）。
4. 每个头文件都应该有一个特定的功能，并且尽可能独立。例如，将与功能A相关的声明放在A.h中，将与功能B相关的声明放在B.h中。如果只关心A，则可只包含A.h，而不获取与B相关的内容。
5. 注意为代码文件中使用的功能显式包含对应的头文件。
6. 头文件都应该能单独编译（应该#include需要的每个依赖项）。
7. 仅#include 需要的内容（不要因为允许而include所有内容）。
8. 不要#include .cpp文件。
9. 在头文件中放置关于某段代码的作用或使用文档。它更可能在那里被看到。描述代码如何工作的文档应保留在源文件中。

## 2.11 头文件保护

### 重复定义问题

> 为了演示说明，这里在头文件中做了函数定义；但一般不建议这样做！

使用头文件，很容易导致头文件中的定义被多次包含。例如

`square.h`

```C++
int getSquareSides()
{
    return 4;
}
```

`wave.h`

```C++
#include "square.h"
```

`main.cpp`

```C++
#include "square.h"
#include "wave.h"

int main()
{
    return 0;
}
```

此程序无法编译！在解析所有`#include`之后，`main.cpp`最终如下所示

```C++
int getSquareSides()  // from square.h
{
    return 4;
}

int getSquareSides() // from wave.h (via square.h)
{
    return 4;
}

int main()
{
    return 0;
}
```

**重复定义**导致了编译错误。每个文件可以单独编译通过。然而，由于`main.cpp`包含了两次`square.h`的内容，所以出现了这个问题。如果`wave.h`需要`getSquareSides()`，同时`main.cpp`又需要`wave.h`和`square.h`，该如何解决此问题？

### 头文件保护

头文件保护采用如下形式的条件编译指令

```C++
#ifndef SOME_UNIQUE_NAME_HERE
#define SOME_UNIQUE_NAME_HERE

// 这里放置你的声明

#endif
```

当包含此头文件时，预处理器检查`SOME_UNIQUE_NAME_HERE`是否已经定义过。如果是第一次包含该头文件，`SOME_UNIQUE_NAME_HERE`不会被定义。因此，预处理器会定义`SOME_UNIQUE_NAME_HERE`并包含文件的内容。如果该头文件再次被包含到同一文件中，`SOME_UNIQUE_NAME_HERE`已经被定义，头文件的内容将被忽略（由于`#ifndef`）。

所有头文件都应有头文件保护。`SOME_UNIQUE_NAME_HERE`可以取任何名称，但根据惯例，通常设置为头文件的完整文件名，使用大写字母，用下划线替代空格或标点。例如，`square.h`将具有如下头文件保护

```C++
#ifndef SQUARE_H
#define SQUARE_H

int getSquareSides()
{
    return 4;
}

#endif
```

在大型程序中，可能有两个位于不同目录下的头文件具有相同的文件名（例如`directoryA\config.h`和`directoryB\config.h`）。如果仅用文件名来命名保护宏（例如`config_h`），则这两个文件的保护宏会重名。这将导致任何同时包含（直接或间接）这两个`config.h`文件的代码文件只会包含其中一个的内容，从而导致编译错误。

为了减少名称冲突的可能性，建议在头文件保护中使用更复杂/唯一的名称。推荐使用`PROJECT_PATH_FILE_H`、`FILE_LARGE-RANDOM-NUMBER_H`或`FILE_CREATION-DATE_H`作为命名约定。

总之：头文件保护防止了重复包含：因为第一次遇到保护时，会引入被保护的内容并定义保护宏，后续再遇到时就会排除被保护内容的副本。

### 头文件保护不会阻止头文件被不同文件各包含一次

如果在`h`文件中定义了函数，即便使用头文件保护，不能阻止它被`add.cpp`和`main.cpp`

各自包含一次，仍旧出现链接器错误。因此要避免在头文件中定义函数。

### 头文件中的其它定义

在许多情况下，需要将<u>非函数的定义</u>放在头文件中。例如，C++允许创建自己的类型。这些自定义类型通常在头文件中定义，因此类型定义可以传播到需要使用它们的代码文件。如果没有头文件保护，代码文件可能会以给一个类型多个（相同）副本，编译器会将其标记为错误。

### pragma once

现代编译器使用`#pragma`预处理器指令支持更简单的替代形式的头文件保护

```C++
#pragma once

// your code here
```

`\#pragma once`与头文件保护具有相同的用途：避免头文件被多次包含。使用传统的头文件保护，开发人员负责保护头文件（通过使用预处理器指令`#ifndef`、`#define`和`#endif`）。使用`#pragma once`，我们请求编译器保护头文件。

对于大多数项目，`#pragma once`工作得很好，而且更容易，不容易出错。许多IDE还在通过IDE生成的新头文件的顶部自动包含`#pragma once`。目前对`#pragma once`的支持是相当普遍的，如果使用`#pragma once`，在现代C++中是普遍接受的。











































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
