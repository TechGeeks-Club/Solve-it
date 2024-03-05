#include <stdio.h>
#include "sol.h"

int main() {
    int score = 0, tests = 10;

    if (maxArr((int[]){1, 2, 3, 4, 5}, 5) == 2) score++;
    if (maxArr((int[]){5, 4, 3, 2, 1}, 5) == 5) score++;
    if (maxArr((int[]){1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 10) == 10) score++;
    if (maxArr((int[]){10, 9, 8, 7, 6, 5, 4, 3, 2, 1}, 10) == 10) score++;
    if (maxArr((int[]){1, 2, 0, 4, -5, -10, 9, 2, 7, 6}, 10) == 9) score++;
    if (maxArr((int[]){-1, -2, -3, -4, -5, -6, -7, -8, -9, -10}, 10) == -1) score++;
    if (maxArr((int[]){-10, -9, -8, -7, -6, -5, -4, -3, -2, -1}, 10) == -1) score++;
    if (maxArr((int[]){-1, -2, -3, -4, -5, -6, -7, -8, -9, 0}, 10) == 0) score++;
    if (maxArr((int[]){0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, 10) == 0) score++;
    if (maxArr((int[]){1, 1, 1, 1, 1, 1, 1, 1, 1, 1}, 10) == 1) score++;

    printf("%.2f\n", (tests/2 > score)? 0.00: ((float)score / tests) );


}
