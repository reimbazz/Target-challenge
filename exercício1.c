#include <stdio.h>

int main() {

    int INDICE = 13, SOMA = 0, K = 0;
    while (K < INDICE)
    {
        K += 1;
        SOMA += K;

    }
    printf("%d", SOMA);
    
    return 0;
}
//A variável SOMA terá o valor 91
