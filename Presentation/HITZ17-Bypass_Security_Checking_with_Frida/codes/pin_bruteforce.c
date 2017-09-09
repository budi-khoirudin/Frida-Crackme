/*
HITZ'17 - Frida

Brute Force PIN

*/

#include <stdio.h>

int check_pin(int pin)
{
    int right = pin % 1000;
    int left  = pin / 1000;

    left  = left * 10 + right;
    right = right * 15 + 33;

    int finalval = left + right;

    return (finalval == 8323);
}

int main()
{
    int pin = 0;
    printf("Addr: %p\n\n", check_pin);
    printf("Masukkan pin: ");
    scanf("%d", &pin);

    if (check_pin(pin))
    {
        printf("PIN diterima.");
    } else {
        printf("PIN ditolak.");
    }

    return 0;
}