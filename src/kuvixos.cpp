#include "kuvixos.hpp"

// Altta kernel fonksiyonunu çağırıyoruz
extern "C" void commands_puts(const char* c);
// veya extern "C" void printk(const char* c);

void print(const char* c) {
    commands_puts(c); // veya printk(c);
}
