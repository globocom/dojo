#include<stdio.h>
#include<assert.h>
#include<stdlib.h>

char **alocar_e_inicializar_matriz(int linhas, int colunas) {
	int i, j;
	char **matriz;
	matriz = (char **)malloc(linhas * sizeof(char *));
	for (i = 0; i < linhas; i++) {
		matriz[i] = (char *)malloc(colunas * sizeof(char));
	}
	
	for (i = 0; i < linhas; i++) {
		for (j = 0; j < colunas; j++) {
			matriz[i][j] = '.';
		}
	}
	
	return matriz;
}

int calcula_dias_pro_primeiro_aeroporto(char** matriz, int linhas, int colunas) {
	int i, j;
	int nuvem_lin = 0;
	int nuvem_col = 0;
	
	int dias = linhas + colunas;
	
	for (i = 0; i < linhas; i++) {
		for (j = 0; j < colunas; j++) {
			if(matriz[i][j] == '*') {
				nuvem_lin = i;
				nuvem_col = j;
			}
		}
	}
	
	for (i = 0; i < linhas; i++) {
		for (j = 0; j < colunas; j++) {
			if(matriz[i][j] == 'a') {
				if (abs(nuvem_lin - i) + abs(nuvem_col - j) < dias)
					dias = abs(nuvem_lin - i) + abs(nuvem_col - j);
			}
		}
	}

	return dias;
}

int calcula_dias_pro_ultimo_aeroporto(char** matriz, int linhas, int colunas) {
	int i, j;
	int nuvem_lin = 0;
	int nuvem_col = 0;
	
	int dias = 0;
	
	for (i = 0; i < linhas; i++) {
		for (j = 0; j < colunas; j++) {
			if(matriz[i][j] == '*') {
				nuvem_lin = i;
				nuvem_col = j;
			}
		}
	}
	
	for (i = 0; i < linhas; i++) {
		for (j = 0; j < colunas; j++) {
			if(matriz[i][j] == 'a') {
				if (abs(nuvem_lin - i) + abs(nuvem_col - j) > dias)
					dias = abs(nuvem_lin - i) + abs(nuvem_col - j);
			}
		}
	}

	return dias;
}

void test_calcula_dias_com_matriz_2x1() {
	// ['*', 'a'];
	char **matriz = alocar_e_inicializar_matriz(2, 1);
	matriz[0][0] = '*';
	matriz[1][0] = 'a';
	int dia_do_primeiro_aeroporto = calcula_dias_pro_primeiro_aeroporto(matriz, 2, 1);
	assert(dia_do_primeiro_aeroporto == 1);
}

void test_calcula_dias_com_matriz_3x1_com_nuvem_na_coluna_1() {
	// ['*', '.', 'a'];
	char **matriz = alocar_e_inicializar_matriz(3, 1);
	matriz[0][0] = '*';
	matriz[2][0] = 'a';
	int dia_do_primeiro_aeroporto = calcula_dias_pro_primeiro_aeroporto(matriz, 3, 1);
	assert(dia_do_primeiro_aeroporto == 2);
}

void test_calcula_dias_com_matriz_3x1_com_nuvem_na_coluna_2() {
	// ['.', '*', 'a']
	char **matriz = alocar_e_inicializar_matriz(3, 1);
	matriz[1][0] = '*';
	matriz[2][0] = 'a';
	int dia_do_primeiro_aeroporto = calcula_dias_pro_primeiro_aeroporto(matriz, 3, 1);
	assert(dia_do_primeiro_aeroporto == 1);
}

void test_calcula_dias_com_matriz_2x1_com_nuvem_depois_do_aeroporto() {
	// ['a', '*']
	char **matriz = alocar_e_inicializar_matriz(2, 1);
	matriz[0][0] = 'a';
	matriz[1][0] = '*';
	int dia_do_primeiro_aeroporto = calcula_dias_pro_primeiro_aeroporto(matriz, 2, 1);
	assert(dia_do_primeiro_aeroporto == 1);
}

void test_calcula_dias_com_matriz_1x2() {
	// ['*', 'a'];
	char **matriz = alocar_e_inicializar_matriz(1, 2);
	matriz[0][0] = '*';
	matriz[0][1] = 'a';
	int dia_do_primeiro_aeroporto = calcula_dias_pro_primeiro_aeroporto(matriz, 1, 2);
	assert(dia_do_primeiro_aeroporto == 1);
}

void test_calcula_dias_com_matriz_1x3_com_nuvem_na_coluna_1() {
	// ['*', '.', 'a'];
	char **matriz = alocar_e_inicializar_matriz(1, 3);
	matriz[0][0] = '*';
	matriz[0][2] = 'a';
	int dia_do_primeiro_aeroporto = calcula_dias_pro_primeiro_aeroporto(matriz, 1, 3);
	assert(dia_do_primeiro_aeroporto == 2);
}

void test_calcula_dias_com_matriz_1x3_com_nuvem_na_coluna_2() {
	// ['.', '*', 'a']
	char **matriz = alocar_e_inicializar_matriz(1, 3);
	matriz[0][1] = '*';
	matriz[0][2] = 'a';
	int dia_do_primeiro_aeroporto = calcula_dias_pro_primeiro_aeroporto(matriz, 1, 3);
	assert(dia_do_primeiro_aeroporto == 1);
}

void test_calcula_dias_com_matriz_1x2_com_nuvem_depois_do_aeroporto() {
	// ['a', '*']
	char **matriz = alocar_e_inicializar_matriz(1, 2);
	matriz[0][0] = 'a';
	matriz[0][1] = '*';
	int dia_do_primeiro_aeroporto = calcula_dias_pro_primeiro_aeroporto(matriz, 1, 2);
	assert(dia_do_primeiro_aeroporto == 1);
}

void test_alocar_matriz() {
	char **matriz;
	matriz = alocar_e_inicializar_matriz(2, 2);
	assert(matriz[0][0] == '.');
}

void test_calcula_dias_com_matriz_2x2() {
	// ['*', 'a'];
	char **matriz = alocar_e_inicializar_matriz(2, 2);
	matriz[0][0] = '*';
	matriz[0][1] = 'a';
	int dia_do_primeiro_aeroporto = calcula_dias_pro_primeiro_aeroporto(matriz, 2, 2);
	assert(dia_do_primeiro_aeroporto == 1);
}

void test_calcula_dias_com_matriz_3x3_com_dois_aeroportos() {
	// ['*', '.', '.']
	// ['.', '.', 'a']
	// ['.', 'a', '.']
	char **matriz = alocar_e_inicializar_matriz(3, 3);
	matriz[0][0] = '*';
	matriz[1][2] = 'a';
	matriz[2][1] = 'a';
	int dia_do_primeiro_aeroporto = calcula_dias_pro_primeiro_aeroporto(matriz, 3, 3);
	assert(dia_do_primeiro_aeroporto == 3);
}

void test_calcula_dias_com_matriz_3x3_com_dois_aeroportos_com_distancias_diferentes_da_nuvem() {
	// ['*', '.', '.']
	// ['.', '.', 'a']
	// ['.', '.', 'a']
	char **matriz = alocar_e_inicializar_matriz(3, 3);
	matriz[0][0] = '*';
	matriz[1][2] = 'a';
	matriz[2][2] = 'a';
	int dia_do_primeiro_aeroporto = calcula_dias_pro_primeiro_aeroporto(matriz, 3, 3);
	assert(dia_do_primeiro_aeroporto == 3);
}

void test_calcula_mais_dias_com_matriz_3x3_com_dois_aeroportos() {
	// ['*', '.', '.']
	// ['.', '.', 'a']
	// ['.', 'a', '.']
	char **matriz = alocar_e_inicializar_matriz(3, 3);
	matriz[0][0] = '*';
	matriz[1][2] = 'a';
	matriz[2][1] = 'a';
	int dia_do_ultimo_aeroporto = calcula_dias_pro_ultimo_aeroporto(matriz, 3, 3);
	assert(dia_do_ultimo_aeroporto == 3);
}

void test_calcula_mais_dias_com_matriz_3x3_com_dois_aeroportos_com_distancias_diferentes_da_nuvem() {
	// ['*', '.', '.']
	// ['.', '.', 'a']
	// ['.', '.', 'a']
	char **matriz = alocar_e_inicializar_matriz(3, 3);
	matriz[0][0] = '*';
	matriz[1][2] = 'a';
	matriz[2][2] = 'a';
	int dia_do_ultimo_aeroporto = calcula_dias_pro_ultimo_aeroporto(matriz, 3, 3);
	assert(dia_do_ultimo_aeroporto == 4);
}

int main(void) {
	test_alocar_matriz();
	test_calcula_dias_com_matriz_1x2();
	test_calcula_dias_com_matriz_1x3_com_nuvem_na_coluna_1();
	test_calcula_dias_com_matriz_1x3_com_nuvem_na_coluna_2();
	test_calcula_dias_com_matriz_1x2_com_nuvem_depois_do_aeroporto();
	test_calcula_dias_com_matriz_2x1();
	test_calcula_dias_com_matriz_3x1_com_nuvem_na_coluna_1();
	test_calcula_dias_com_matriz_3x1_com_nuvem_na_coluna_2();
	test_calcula_dias_com_matriz_2x1_com_nuvem_depois_do_aeroporto();
	test_calcula_dias_com_matriz_2x2();
	test_calcula_dias_com_matriz_3x3_com_dois_aeroportos();
	test_calcula_dias_com_matriz_3x3_com_dois_aeroportos_com_distancias_diferentes_da_nuvem();
	test_calcula_mais_dias_com_matriz_3x3_com_dois_aeroportos();
	test_calcula_mais_dias_com_matriz_3x3_com_dois_aeroportos_com_distancias_diferentes_da_nuvem();
	return 0;
}