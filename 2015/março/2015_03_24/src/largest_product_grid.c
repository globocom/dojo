#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>
#include "largest_product_grid.h"

int line_product(int *line)
{
    int max_prod = 0;
    for (int i = 0; i <= GRID_SIZE - 4; i++) {
        int prod = 1;
        for (int j = i; j < i + 4; j++) {
            prod *= line[j];
        }
        if (prod > max_prod) {
            max_prod = prod;
        }
    }

    return max_prod;
}

void get_column(int grid[GRID_SIZE][GRID_SIZE], int col_num, int column[])
{
    for (int i = 0; i < GRID_SIZE; i++) {
        column[i] = grid[i][col_num];
    }
}

void get_diagonal_lr(int grid[GRID_SIZE][GRID_SIZE], int i, int j, int column[])
{   memset(column, 1, sizeof (int));
    int big = i > j ? i : j;
    for (int k = 0; k < GRID_SIZE - big; k++) {
        column[k] = grid[i+k][j+k];
    }
}


int calc_product(int grid[GRID_SIZE][GRID_SIZE])
{
    int largest_product = 0;

    // iterate over lines
    for (int i = 0; i < GRID_SIZE; i++) {
        int current = line_product(grid[i]);
        if (current > largest_product) {
            largest_product = current;
        }
    }

    // iterate over columns
    int column[GRID_SIZE];
    for (int i = 0; i < GRID_SIZE; i++) {
        get_column(grid, i, column);
        int current = line_product(column);
        if (current > largest_product) {
            largest_product = current;
        }
    }

    // iterate over diagonals LR bottom triang
    int diagonals[GRID_SIZE];
    for (int i = 0, j = 0; i < GRID_SIZE - 3; i++) {
        get_diagonal_lr(grid, i, j, diagonals);
        int current = line_product(diagonals);
        if (current > largest_product) {
            largest_product = current;
        }
    }

    // iterate over diagonals LR top triang
    for (int i = 0, j = 1; j < GRID_SIZE - 3; j++) {
        get_diagonal_lr(grid, i, j, diagonals);
        int current = line_product(diagonals);
        if (current > largest_product) {
            largest_product = current;
        }
    }

    return largest_product;
}
