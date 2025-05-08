#include <stdio.h>

void add(int n, int A[n][n], int B[n][n], int result[n][n]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            result[i][j] = A[i][j] + B[i][j];
        }
    }
}

void subtract(int n, int A[n][n], int B[n][n], int result[n][n]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            result[i][j] = A[i][j] - B[i][j];
        }
    }
}

void multiply(int n, int A[n][n], int B[n][n], int result[n][n]) {
    if (n == 1) {
        result[0][0] = A[0][0] * B[0][0];
        return;
    }

    int mid = n / 2;
    int A11[mid][mid], A12[mid][mid], A21[mid][mid], A22[mid][mid];
    int B11[mid][mid], B12[mid][mid], B21[mid][mid], B22[mid][mid];
    int M1[mid][mid], M2[mid][mid], M3[mid][mid], M4[mid][mid];
    int M5[mid][mid], M6[mid][mid], M7[mid][mid];
    int temp1[mid][mid], temp2[mid][mid];

    for (int i = 0; i < mid; i++) {
        for (int j = 0; j < mid; j++) {
            A11[i][j] = A[i][j];
            A12[i][j] = A[i][j + mid];
            A21[i][j] = A[i + mid][j];
            A22[i][j] = A[i + mid][j + mid];
            B11[i][j] = B[i][j];
            B12[i][j] = B[i][j + mid];
            B21[i][j] = B[i + mid][j];
            B22[i][j] = B[i + mid][j + mid];
        }
    }

    add(mid, A11, A22, temp1);
    add(mid, B11, B22, temp2);
    multiply(mid, temp1, temp2, M1);

    add(mid, A21, A22, temp1);
    multiply(mid, temp1, B11, M2);

    subtract(mid, B12, B22, temp1);
    multiply(mid, A11, temp1, M3);

    subtract(mid, B21, B11, temp1);
    multiply(mid, A22, temp1, M4);

    add(mid, A11, A12, temp1);
    multiply(mid, temp1, B22, M5);

    subtract(mid, A21, A11, temp1);
    add(mid, B11, B12, temp2);
    multiply(mid, temp1, temp2, M6);

    subtract(mid, A12, A22, temp1);
    add(mid, B21, B22, temp2);
    multiply(mid, temp1, temp2, M7);

    add(mid, M1, M4, temp1);
    subtract(mid, temp1, M5, temp2);
    add(mid, temp2, M7, temp1);

    add(mid, M3, M5, temp2);

    add(mid, M2, M4, temp1);

    subtract(mid, M1, M2, temp2);
    add(mid, temp2, M3, temp2);
    add(mid, temp2, M6, temp2);

    for (int i = 0; i < mid; i++) {
        for (int j = 0; j < mid; j++) {
            result[i][j] = temp1[i][j];
            result[i][j + mid] = temp2[i][j];
            result[i + mid][j] = temp1[i][j];
            result[i + mid][j + mid] = temp2[i][j];
        }
    }
}

int main() {
    int n = 4;
    int A[4][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
    int B[4][4] = {{16, 15, 14, 13}, {12, 11, 10, 9}, {8, 7, 6, 5}, {4, 3, 2, 1}};
    int C[4][4] = {0};

    multiply(n, A, B, C);

    printf("Resulting Matrix C: \n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }

    return 0;
}
