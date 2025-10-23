# Lakbay Language Specification v1.0

## Table of Contents

1. [Introduction](#introduction)
2. [Lexical Structure](#lexical-structure)
3. [Data Types](#data-types)
4. [Variables](#variables)
5. [Operators](#operators)
6. [Control Flow](#control-flow)
7. [Functions and Methods](#functions-and-methods)
8. [Classes and Objects](#classes-and-objects)
9. [Inheritance](#inheritance)
10. [Comments](#comments)
11. [Examples](#examples)

---

## Introduction

Lakbay is a statically-typed, object-oriented programming language that transpiles to C++. It is designed to be simple, readable, and powerful.

### Design Goals
- **Simplicity**: Easy to learn syntax
- **Performance**: Compiles to native C++ code
- **Safety**: Static typing with compile-time checks
- **Object-Oriented**: Full OOP support with classes and inheritance

---

## Lexical Structure

### Keywords

```
class      extends    func       return
if         else       while      for
new        this       public     private
int        float      string     bool
void       true       false      print
array
```

### Identifiers

Identifiers must start with a letter or underscore, followed by any number of letters, digits, or underscores.

```lakbay
// Valid identifiers
name
_value
counter1
myVariable
calculateTotal
```

### Literals

#### Integer Literals
```lakbay
42
0
-15
1000
```

#### Float Literals
```lakbay
3.14
0.5
-2.718
100.0
```

#### String Literals
```lakbay
"Hello, World!"
"Lakbay Programming"
"Line 1\nLine 2"
```

#### Boolean Literals
```lakbay
true
false
```

---

## Data Types

### Primitive Types

| Type | Description | Example |
|------|-------------|---------|
| `int` | Integer numbers | `42`, `-10`, `0` |
| `float` | Floating-point numbers | `3.14`, `-0.5`, `100.0` |
| `string` | Text strings | `"Hello"`, `"World"` |
| `bool` | Boolean values | `true`, `false` |
| `void` | No value (return type only) | N/A |

### Type Declaration

```lakbay
int age;
float price;
string name;
bool isActive;
```

### Type Initialization

```lakbay
int count = 10;
float temperature = 36.5;
string greeting = "Hello";
bool ready = true;
```

---

## Variables

### Declaration

Variables must be declared with a type before use.

```lakbay
int x;
float y;
string message;
```

### Assignment

```lakbay
x = 42;
y = 3.14;
message = "Hello";
```

### Declaration with Initialization

```lakbay
int age = 25;
float price = 99.99;
string name = "John";
bool active = true;
```

### Scope

Variables are scoped to the block in which they are declared.

```lakbay
func example(): void {
    int x = 10;  // x is visible within this function
    
    if (x > 5) {
        int y = 20;  // y is visible only within this if block
    }
    
    // y is NOT accessible here
    return;
}
```

---

## Operators

### Arithmetic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `a + b` |
| `-` | Subtraction | `a - b` |
| `*` | Multiplication | `a * b` |
| `/` | Division | `a / b` |

```lakbay
int sum = 10 + 5;        // 15
int diff = 10 - 5;       // 5
int product = 10 * 5;    // 50
int quotient = 10 / 5;   // 2
```

### Comparison Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `<` | Less than | `a < b` |
| `>` | Greater than | `a > b` |
| `<=` | Less than or equal | `a <= b` |
| `>=` | Greater than or equal | `a >= b` |

```lakbay
bool isEqual = (10 == 10);      // true
bool notEqual = (10 != 5);      // true
bool lessThan = (5 < 10);       // true
bool greaterThan = (10 > 5);    // true
```

### Logical Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `&&` | Logical AND | `a && b` |
| `||` | Logical OR | `a || b` |
| `!` | Logical NOT | `!a` |

```lakbay
bool result1 = true && false;   // false
bool result2 = true || false;   // true
bool result3 = !true;           // false
```

### Assignment Operator

| Operator | Description | Example |
|----------|-------------|---------|
| `=` | Assignment | `a = b` |

```lakbay
int x = 10;
x = x + 5;  // x is now 15
```

### Operator Precedence

From highest to lowest:
1. `()` - Parentheses
2. `!`, `-` (unary) - Logical NOT, Negation
3. `*`, `/` - Multiplication, Division
4. `+`, `-` - Addition, Subtraction
5. `<`, `>`, `<=`, `>=` - Comparison
6. `==`, `!=` - Equality
7. `&&` - Logical AND
8. `||` - Logical OR
9. `=` - Assignment

---

## Control Flow

### If Statement

```lakbay
if (condition) {
    // code executed if condition is true
}

if (condition) {
    // code if true
} else {
    // code if false
}
```

**Example:**
```lakbay
int age = 20;

if (age >= 18) {
    // Adult
} else {
    // Minor
}
```

### While Loop

```lakbay
while (condition) {
    // code executed while condition is true
}
```

**Example:**
```lakbay
int count = 0;
while (count < 10) {
    count = count + 1;
}
```

### For Loop

```lakbay
for (initialization; condition; update) {
    // loop body
}
```

**Example:**
```lakbay
for (int i = 0; i < 10; i = i + 1) {
    // loop body executes 10 times
}
```

---

## Functions and Methods

### Function Declaration

```lakbay
func functionName(type param1, type param2): returnType {
    // function body
    return value;
}
```

### Function with No Return Value

```lakbay
func greet(): void {
    // function body
    return;
}
```

### Function with Parameters

```lakbay
func add(int a, int b): int {
    int result;
    result = a + b;
    return result;
}
```

### Function with Multiple Parameters

```lakbay
func calculateArea(float width, float height): float {
    float area;
    area = width * height;
    return area;
}
```

---

## Classes and Objects

### Class Declaration

```lakbay
class ClassName {
    public:
    // public members
    
    private:
    // private members
}
```

### Constructor

A constructor is a special method with the same name as the class.

```lakbay
class Person {
    public:
    string name;
    int age;
    
    func Person(string n, int a) {
        name = n;
        age = a;
    }
}
```

### Methods

```lakbay
class Calculator {
    public:
    int result;
    
    func Calculator() {
        result = 0;
    }
    
    func add(int a, int b): int {
        result = a + b;
        return result;
    }
    
    func getResult(): int {
        return result;
    }
}
```

### Access Modifiers

- `public:` - Members are accessible from outside the class
- `private:` - Members are only accessible within the class

```lakbay
class BankAccount {
    private:
    float balance;
    
    public:
    string accountNumber;
    
    func BankAccount() {
        balance = 0.0;
        accountNumber = "000000";
    }
    
    func deposit(float amount): void {
        balance = balance + amount;
        return;
    }
    
    func getBalance(): float {
        return balance;
    }
}
```

### Creating Objects

```lakbay
// Using 'new' keyword (returns pointer)
ClassName obj = new ClassName(args);

// Direct instantiation
ClassName obj(args);
```

### Accessing Members

```lakbay
// Access property
obj.propertyName

// Call method
obj.methodName(args)
```

**Example:**
```lakbay
class Person {
    public:
    string name;
    int age;
    
    func Person(string n, int a) {
        name = n;
        age = a;
    }
    
    func introduce(): void {
        return;
    }
}

// Usage (in main or other context)
// Person john = new Person("John", 25);
// john.introduce();
```

---

## Inheritance

### Extending Classes

```lakbay
class ChildClass extends ParentClass {
    // child class members
}
```

### Example

```lakbay
class Animal {
    public:
    string name;
    int age;
    
    func Animal() {
        name = "Unknown";
        age = 0;
    }
    
    func makeSound(): void {
        return;
    }
}

class Dog extends Animal {
    public:
    string breed;
    
    func Dog() {
        name = "Dog";
        age = 0;
        breed = "Mixed";
    }
    
    func bark(): void {
        return;
    }
}
```

### Accessing Parent Members

Child classes can access public members of the parent class directly.

```lakbay
class Student extends Person {
    public:
    float gpa;
    
    func Student() {
        name = "Unknown";    // Accessing parent's property
        age = 0;             // Accessing parent's property
        gpa = 0.0;
    }
}
```

---

## Comments

### Single-Line Comments

```lakbay
// This is a single-line comment
int x = 10;  // Comment after code
```

### Best Practices

```lakbay
// Good: Explains WHY, not WHAT
// Calculate tax based on local regulations
float tax = price * 0.08;

// Bad: States the obvious
// Assign 10 to x
int x = 10;
```

---

## Examples

### Example 1: Simple Calculator

```lakbay
class Calculator {
    public:
    int result;
    
    func Calculator() {
        result = 0;
    }
    
    func add(int a, int b): int {
        result = a + b;
        return result;
    }
    
    func subtract(int a, int b): int {
        result = a - b;
        return result;
    }
    
    func multiply(int a, int b): int {
        result = a * b;
        return result;
    }
}
```

### Example 2: Bank Account System

```lakbay
class BankAccount {
    private:
    float balance;
    
    public:
    string accountNumber;
    
    func BankAccount(string accNum) {
        accountNumber = accNum;
        balance = 0.0;
    }
    
    func deposit(float amount): void {
        if (amount > 0.0) {
            balance = balance + amount;
        }
        return;
    }
    
    func withdraw(float amount): bool {
        if (amount > 0.0) {
            if (balance >= amount) {
                balance = balance - amount;
                return true;
            }
        }
        return false;
    }
    
    func getBalance(): float {
        return balance;
    }
}
```

### Example 3: Student Grade System

```lakbay
class Student {
    public:
    string name;
    int studentId;
    float gpa;
    
    func Student(string n, int id) {
        name = n;
        studentId = id;
        gpa = 0.0;
    }
    
    func updateGPA(float newGPA): void {
        if (newGPA >= 0.0) {
            if (newGPA <= 4.0) {
                gpa = newGPA;
            }
        }
        return;
    }
    
    func isPassing(): bool {
        if (gpa >= 2.0) {
            return true;
        }
        return false;
    }
}
```

### Example 4: Geometric Shapes

```lakbay
class Shape {
    public:
    string name;
    float area;
    
    func Shape() {
        name = "Generic Shape";
        area = 0.0;
    }
    
    func getArea(): float {
        return area;
    }
}

class Rectangle extends Shape {
    public:
    float width;
    float height;
    
    func Rectangle(float w, float h) {
        name = "Rectangle";
        width = w;
        height = h;
        area = 0.0;
    }
    
    func calculateArea(): float {
        area = width * height;
        return area;
    }
}

class Circle extends Shape {
    public:
    float radius;
    
    func Circle(float r) {
        name = "Circle";
        radius = r;
        area = 0.0;
    }
    
    func calculateArea(): float {
        area = 3.14159 * radius * radius;
        return area;
    }
}
```

---

## Type System

### Static Typing

Lakbay is statically typed. All variables must be declared with a type.

```lakbay
int x;           // OK
x = 10;          // OK
x = "string";    // ERROR: Type mismatch
```

### Type Compatibility

- Integer and float operations may have implicit conversions in C++
- String concatenation is not supported (use C++ string operations in transpiled code)
- Boolean types cannot be used in arithmetic operations

---

## Best Practices

### Naming Conventions

```lakbay
// Classes: PascalCase
class StudentRecord { }

// Variables and functions: camelCase
int studentCount;
func calculateTotal(): int { }

// Constants: UPPER_CASE (when supported)
int MAX_SIZE = 100;
```

### Code Organization

```lakbay
class MyClass {
    // 1. Private members first
    private:
    int privateData;
    
    // 2. Public members
    public:
    int publicData;
    
    // 3. Constructor
    func MyClass() {
        privateData = 0;
        publicData = 0;
    }
    
    // 4. Public methods
    func doSomething(): void {
        return;
    }
    
    // 5. Private methods (if any)
}
```

### Error Handling

Currently, Lakbay does not have built-in exception handling. Use return values and boolean flags for error checking.

```lakbay
func divide(int a, int b): int {
    if (b == 0) {
        return 0;  // Error indicator
    }
    return a / b;
}
```

---

## Limitations

### Current Version Limitations (v1.0)

- No exception handling
- No generic types
- No arrays (declared but not fully implemented)
- No string concatenation operators
- No operator overloading
- No multiple inheritance
- No interfaces or abstract classes
- No standard library functions

### Planned Features

- Array support
- String manipulation functions
- Standard library
- Exception handling
- Generic types
- Interfaces

---

## Compilation Process

### Transpilation Steps

1. **Lexical Analysis**: Source code → Tokens
2. **Parsing**: Tokens → Abstract Syntax Tree (AST)
3. **Transpilation**: AST → C++ Code
4. **Compilation**: C++ Code → Executable (via g++/clang++)
5. **Execution**: Run the compiled program

### File Extensions

- Source files: `.lakbay`
- Transpiled files: `.cpp`
- Executable: platform-dependent

---

## Grammar Reference

### Program Structure

```
Program ::= ClassDeclaration*

ClassDeclaration ::= 'class' Identifier ['extends' Identifier] '{' ClassBody '}'

ClassBody ::= AccessModifier ':' MemberDeclaration*

AccessModifier ::= 'public' | 'private'

MemberDeclaration ::= PropertyDeclaration | MethodDeclaration

PropertyDeclaration ::= Type Identifier [= Expression] ';'

MethodDeclaration ::= 'func' Identifier '(' ParameterList ')' [':' Type] Block

ParameterList ::= [Parameter (',' Parameter)*]

Parameter ::= Type Identifier

Block ::= '{' Statement* '}'

Statement ::= IfStatement | WhileStatement | ForStatement | ReturnStatement | 
              VariableDeclaration | ExpressionStatement

Expression ::= LogicalOrExpression

Type ::= 'int' | 'float' | 'string' | 'bool' | 'void' | Identifier
```

---

## Version History

### v1.0.0 (Current)
- Initial release
- Basic OOP support
- Class inheritance
- Control flow statements
- Static typing
- Transpilation to C++

---

## Additional Resources

- **GitHub Repository**: https:/yourusername/ownerCamensi/lakbay-lang
- **Issue Tracker**: https:/yourusername/ownerCamensi/lakbay-lang/issues
- **Community**: [Discord/Forum link]
- **Contributing**: See CONTRIBUTING.md

---

*Last Updated: October 2025*
*Lakbay Programming Language v1.0*