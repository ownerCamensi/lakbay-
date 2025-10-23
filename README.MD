# 🚀 Lakbay Programming Language

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/ownerCamensi/lakbay-.git)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Android-lightgrey.svg)](https://github.com/ownerCamensi/lakbay-.git)

**Lakbay** is a modern, object-oriented programming language that transpiles to C++ for high-performance execution.

## ✨ Features

- 🎯 **Object-Oriented** - Full support for classes, inheritance, and encapsulation
- ⚡ **Compiled** - Transpiles to C++ for native performance
- 🔧 **Simple Syntax** - Easy to learn, powerful to use
- 🌐 **Cross-Platform** - Works on Linux, macOS, and Android (Termux)
- 🎨 **Static Typing** - Type-safe with compile-time checking

## 📦 Installation

### Prerequisites

- Python 3.6 or higher
- C++ compiler (g++ or clang++)

### Quick Install

```bash
# Clone the repository
git clone https://github.com/ownerCamensi/lakbay-.git
cd lakbay-lang

# Run the installer
chmod +x install.sh
./install.sh
```

### Manual Installation

#### Linux/macOS
```bash
# Install dependencies
sudo apt-get install g++ python3  # Debian/Ubuntu
brew install gcc python3          # macOS

# Copy files
mkdir -p ~/.local/bin/lakbay
cp lakbay.py runner.py ~/.local/bin/lakbay/

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$HOME/.local/bin/lakbay:$PATH"
```

#### Android (Termux)
```bash
# Install dependencies
pkg install clang python

# Setup Lakbay
cd ~
git clone https://github.com/ownerCamensi/lakbay-.git
cd lakbay-lang
chmod +x install.sh
./install.sh
```

## 🎯 Quick Start

### Hello World

Create a file `hello.lakbay`:

```lakbay
class Greeter {
    public:
    string message;
    
    func Greeter() {
        message = "Hello, Lakbay!";
    }
    
    func greet(): void {
        return;
    }
}
```

Run it:
```bash
python runner.py hello.lakbay
```

## 📚 Language Syntax

### Classes

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
```

### Inheritance

```lakbay
class Student extends Person {
    public:
    string school;
    float gpa;
    
    func Student() {
        name = "Unknown";
        age = 0;
        school = "None";
        gpa = 0.0;
    }
    
    func study(): void {
        return;
    }
}
```

### Data Types

- `int` - Integer numbers
- `float` - Floating-point numbers
- `string` - Text strings
- `bool` - Boolean (true/false)
- `void` - No return value

### Control Flow

```lakbay
func checkAge(int age): void {
    if (age >= 18) {
        // Adult
    } else {
        // Minor
    }
    return;
}

func countDown(int n): void {
    while (n > 0) {
        n = n - 1;
    }
    return;
}

func iterate(): void {
    for (int i = 0; i < 10; i = i + 1) {
        // Loop body
    }
    return;
}
```

### Operators

- Arithmetic: `+`, `-`, `*`, `/`
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical: `&&`, `||`, `!`
- Assignment: `=`

## 📖 Examples

### Calculator

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
    
    func multiply(int a, int b): int {
        result = a * b;
        return result;
    }
}
```

### Bank Account

```lakbay
class BankAccount {
    private:
    float balance;
    string accountNumber;
    
    public:
    func BankAccount(string accNum) {
        accountNumber = accNum;
        balance = 0.0;
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

## 🛠️ Development

### Project Structure

```
lakbay-lang/
├── lakbay.py           # Core transpiler
├── runner.py           # CLI runner
├── install.sh          # Installation script
├── examples/           # Example programs
│   ├── hello.lakbay
│   ├── calculator.lakbay
│   └── bank.lakbay
├── tests/              # Test files
├── docs/               # Documentation
└── README.md           # This file
```

### Running Tests

```bash
cd tests
python test_lakbay.py
```

### Building from Source

```bash
# Clone repository
git clone https://github.com/ownerCamensi/lakbay-.git
cd lakbay-lang

# Run directly
python runner.py examples/hello.lakbay
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by modern programming languages
- Built with Python for simplicity and power
- Transpiles to C++ for performance

## 📞 Contact

- GitHub: [@ownerCamensi](https://github.com/ownerCamensi/lakbay-.git)
- Email: mannycamensi2011@gmail.com

## 🗺️ Roadmap

- [x] Basic OOP support
- [x] Class inheritance
- [x] Control flow statements
- [ ] Array support
- [ ] Standard library
- [ ] Package manager
- [ ] IDE integration
- [ ] Debugger support

---

Made with ❤️ by [Manny Mansilao Palasol]# lakbay-
# lakbay-
# lakbay-
