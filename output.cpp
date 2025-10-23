#include <iostream>
#include <string>
#include <vector>
using namespace std;


class Calculator {
public:
public:
    int result;
    Calculator() {
        result = 0;
    }
    int add(int a, int b) {
        result = (a + b);
        return result;
    }
    int multiply(int a, int b) {
        result = (a * b);
        return result;
    }
};

class Person {
public:
public:
    string name;
    int age;
    Person() {
        name = "Unknown";
        age = 0;
    }
    void setInfo(string n, int a) {
        name = n;
        age = a;
        return;
    }
    int getAge() {
        return age;
    }
};

int main() {
    cout << "Lakbay Program Running..." << endl;
    return 0;
}