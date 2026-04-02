#include <iostream>

extern "C" void printk(const char* c) {
    std::cout << c << std::endl;
}

void print(const char* c) {
    printk(c);
}
