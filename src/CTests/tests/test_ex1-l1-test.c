#include <stdio.h>

// Function to find the maximum element in an array
int findMax(int arr[], int size) {
    int max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

// Test function for findMax
void testFindMax() {
    int arr1[] = {1, 2, 3, 4, 5};
    int arr2[] = {10, 20, 30, 40, 50};
    int arr3[] = {-1, -2, -3, -4, -5};

    int max1 = findMax(arr1, sizeof(arr1) / sizeof(arr1[0]));
    int max2 = findMax(arr2, sizeof(arr2) / sizeof(arr2[0]));
    int max3 = findMax(arr3, sizeof(arr3) / sizeof(arr3[0]));

    printf("Max of arr1: %d\n", max1);
    printf("Max of arr2: %d\n", max2);
    printf("Max of arr3: %d\n", max3);
}

int main() {
    testFindMax();
    return 0;
}