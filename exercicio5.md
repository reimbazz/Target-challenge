## 5. Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

```
#include <stdio.h>
#include <string.h>

int main(){
    char string[100], invertida[100];
    
    //coleta da string a ser convertida
    printf("Digite uma string: ");
    fgets(string, sizeof(string), stdin);

    //invertendo string
    int i, len = strlen(string);

    for (i = 0; i < len; i++) {
        invertida[len - 1 - i] = string[i];
    }    

    invertida[len] = '\0'; // Adiciona o caractere null terminator

    //string invertida :)
    printf("String invertida: %s\n", invertida);       

    return 0;
