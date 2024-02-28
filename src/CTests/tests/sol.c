#include <stdio.h>


int maxArr(int arr[], int size){
    int max = arr[0];
    for (int i = 1; i < size; i++)
    {
        if (max < arr[i]) max = arr[i];
    }
    return max;
    
}

int mains() {
    printf("======================");
    return 0;
}