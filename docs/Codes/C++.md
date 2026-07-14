

















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



`constexpr`编译时已知

```c++
constexpr double PI = 3.141592653589793;
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



