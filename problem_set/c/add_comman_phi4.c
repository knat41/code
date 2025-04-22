#include <stdio.h>
#include <string.h>

#define MAX_BUFFER_SIZE 50

int main() {
    char buffer[MAX_BUFFER_SIZE], answer[MAX_BUFFER_SIZE] = "";
    long number;
    int count = 0;

    printf("Enter a decimal number: ");
    scanf("%ld", &number);

    while (number > 0) {
        int remainder = number % 10;
        number = number / 10;
        count++;

        // Prepend the remainder to the answer string
        sprintf(buffer, "%d", remainder);
        strcat(answer, buffer);

        // Add a comma every three digits, except for the last group
        if (count % 3 == 0 && number != 0) {
            strcat(answer, ",");
        }
    }

    // Reverse the answer string to get the correct order
    int len = strlen(answer);
    for (int i = 0; i < len / 2; i++) {
        char temp = answer[i];
        answer[i] = answer[len - i - 1];
        answer[len - i - 1] = temp;
    }

    printf("%s\n", answer);
    return 0;
}
