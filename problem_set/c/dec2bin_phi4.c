#include <stdio.h>
#include <string.h>
#include <limits.h>

int main(void) {
    char table[16] = "0123456789ABCDEF"; // Hexadecimal digits
    char buffer[30], answer[30] = "";    // Buffer for intermediate and final binary representation
    unsigned long long number;           // Input number
    int remainder, base = 2;             // Remainder and base for conversion

    // Read input number
    scanf("%llu", &number);

    // Special case for zero
    if (number == 0) {
        snprintf(answer, sizeof(answer), "0");
    } else {
        // Convert number to binary
        while (number > 0) {
            remainder = number % base; // Get remainder
            number = number / base;    // Update number
            strncat(buffer, answer, sizeof(buffer) - strlen(answer) - 1); // Append current binary digits
            snprintf(answer + strlen(answer), sizeof(answer) - strlen(answer), "%c", table[remainder]); // Append new digit
        }
    }

    // Print the final binary representation
    printf("%s", answer);
    return 0;
}
