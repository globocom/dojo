#include <iostream>
#include <cassert>
#include <vector>

using namespace std;

vector<vector<char> > campo_minado(vector<vector<char> > campo) {
    vector<vector<char> > tabuleiro(campo.size(), vector<char>(campo[0].size(), '0'));

    for(int i = 0; i < campo.size(); i++) {
        for(int j = 0; j < campo[i].size(); j++) {
            if (campo[i][j] == '*') {
                tabuleiro[i][j] = '*';

                if (j > 0) {
                    tabuleiro[i][j-1]++;
                    if (i > 0) {
                        tabuleiro[i-1][j-1]++;
                    }
                    if (i < campo.size()-1) {
                        tabuleiro[i+1][j-1]++;
                    }
                }

                if(j < campo[i].size()-1) {
                    tabuleiro[i][j+1]++;
                    if (i > 0) {
                        tabuleiro[i-1][j+1]++;
                    }
                    if (i < campo.size()-1) {
                        tabuleiro[i+1][j+1]++;
                    }
                }

                if (i > 0) {
                    tabuleiro[i-1][j]++;
                }

                if (i < campo.size()-1) {
                    tabuleiro[i+1][j]++;
                }
            }
        }
    }
    return tabuleiro;
}

void assert_array(vector<vector<char> > campo_minado_esperado, vector<vector<char> > campo_minado) {
    for (int i = 0; i < campo_minado_esperado.size(); i++) {
        for (int j = 0; j < campo_minado_esperado[i].size(); j++) {
            assert(campo_minado[i][j] == campo_minado_esperado[i][j] ||
                    cout << "Falhou :( [" << i << "," << j << "]" << endl << "esperado " << campo_minado[i][j] << " != " << "veio " << campo_minado_esperado[i][j]  << endl);
        }
    }
}

void test_1_linha_2_colunas() {
    /*
     ['*', '1']
     */
    vector<vector<char> > campo_minado_esperado(1, vector<char>(2, 0));
    vector<vector<char> > campo_minado_entrada(1, vector<char>(2, 0));
    campo_minado_esperado[0][0] = '*';
    campo_minado_esperado[0][1] = '1';
    campo_minado_entrada[0][0] = '*';
    campo_minado_entrada[0][1] = '.';
    assert_array(campo_minado(campo_minado_entrada), campo_minado_esperado);
}

void test_1_linha_3_colunas() {
    /*
     ['*', '1', '0']
     */
    vector<vector<char> > campo_minado_esperado(1, vector<char>(3, 0));
    vector<vector<char> > campo_minado_entrada(1, vector<char>(3, 0));
    campo_minado_esperado[0][0] = '*';
    campo_minado_esperado[0][1] = '1';
    campo_minado_esperado[0][2] = '0';
    campo_minado_entrada[0][0] = '*';
    campo_minado_entrada[0][1] = '.';
    campo_minado_entrada[0][2] = '.';
    assert_array(campo_minado(campo_minado_entrada), campo_minado_esperado);
}

void test_1_linha_3_colunas_outra_mina() {
    /*
     ['0', '1', '*']
     */
    vector<vector<char> > campo_minado_esperado(1, vector<char>(3, 0));
    vector<vector<char> > campo_minado_entrada(1, vector<char>(3, 0));
    campo_minado_esperado[0][0] = '0';
    campo_minado_esperado[0][1] = '1';
    campo_minado_esperado[0][2] = '*';
    campo_minado_entrada[0][0] = '.';
    campo_minado_entrada[0][1] = '.';
    campo_minado_entrada[0][2] = '*';
    assert_array(campo_minado(campo_minado_entrada), campo_minado_esperado);
}

void test_1_linha_4_colunas_outra_mina() {
    /*
     ['0', '1', '*', '1']
     */
    vector<vector<char> > campo_minado_esperado(1, vector<char>(4, 0));
    vector<vector<char> > campo_minado_entrada(1, vector<char>(4, 0));
    campo_minado_esperado[0][0] = '0';
    campo_minado_esperado[0][1] = '1';
    campo_minado_esperado[0][2] = '*';
    campo_minado_esperado[0][3] = '1';
    campo_minado_entrada[0][0] = '.';
    campo_minado_entrada[0][1] = '.';
    campo_minado_entrada[0][2] = '*';
    campo_minado_entrada[0][3] = '.';
    assert_array(campo_minado(campo_minado_entrada), campo_minado_esperado);
}


void test_1_linha_4_colunas_outra_mina_e_2_minas() {
    /*
     ['*', '2', '*', '1']
     */
    vector<vector<char> > campo_minado_esperado(1, vector<char>(4, 0));
    vector<vector<char> > campo_minado_entrada(1, vector<char>(4, 0));
    campo_minado_esperado[0][0] = '*';
    campo_minado_esperado[0][1] = '2';
    campo_minado_esperado[0][2] = '*';
    campo_minado_esperado[0][3] = '1';
    campo_minado_entrada[0][0] = '*';
    campo_minado_entrada[0][1] = '.';
    campo_minado_entrada[0][2] = '*';
    campo_minado_entrada[0][3] = '.';
    assert_array(campo_minado(campo_minado_entrada), campo_minado_esperado);
}


void test_2_linha_2_colunas_outra_mina() {
    /*
     ['*', '1',
      '1', '1']
     */
    vector<vector<char> > campo_minado_esperado(2, vector<char>(2, 0));
    vector<vector<char> > campo_minado_entrada(2, vector<char>(2, 0));
    campo_minado_esperado[0][0] = '*';
    campo_minado_esperado[0][1] = '1';
    campo_minado_esperado[1][0] = '1';
    campo_minado_esperado[1][1] = '1';
    campo_minado_entrada[0][0] = '*';
    campo_minado_entrada[0][1] = '.';
    campo_minado_entrada[1][0] = '.';
    campo_minado_entrada[1][1] = '.';
    assert_array(campo_minado(campo_minado_entrada), campo_minado_esperado);
}

void test_3_linhas_3_colunas_outra_mina() {
    /*
     ['*', '2', '*',
     '2', '4', '2',
     '*', '2', '*']
     */
    vector<vector<char> > campo_minado_esperado(3, vector<char>(3, 0));
    vector<vector<char> > campo_minado_entrada(3, vector<char>(3, 0));
    campo_minado_esperado[0][0] = '*';
    campo_minado_esperado[0][1] = '2';
    campo_minado_esperado[0][2] = '*';
    campo_minado_esperado[1][0] = '2';
    campo_minado_esperado[1][1] = '4';
    campo_minado_esperado[1][2] = '2';
    campo_minado_esperado[2][0] = '*';
    campo_minado_esperado[2][1] = '2';
    campo_minado_esperado[2][2] = '*';

    campo_minado_entrada[0][0] = '*';
    campo_minado_entrada[0][1] = '.';
    campo_minado_entrada[0][2] = '*';
    campo_minado_entrada[1][0] = '.';
    campo_minado_entrada[1][1] = '.';
    campo_minado_entrada[1][2] = '.';
    campo_minado_entrada[2][0] = '*';
    campo_minado_entrada[2][1] = '.';
    campo_minado_entrada[2][2] = '*';

    assert_array(campo_minado(campo_minado_entrada), campo_minado_esperado);
}

int main() {
    test_1_linha_2_colunas();
    test_1_linha_3_colunas();
    test_1_linha_3_colunas_outra_mina();
    test_1_linha_4_colunas_outra_mina();
    test_1_linha_4_colunas_outra_mina_e_2_minas();
    test_2_linha_2_colunas_outra_mina();
    test_3_linhas_3_colunas_outra_mina();
    return 0;
}
