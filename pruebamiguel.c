#include <stdio.h>

int main(void)
{
    int a = 0, b = 0, res = 0;

    printf("NUMERO 1: ");
    scanf("%d", &a);
    printf("NUMERO 2: ");
    scanf("%d", &b);
    res = a % b;
    printf("Resultado: %d\n", res);
    return (0);
}