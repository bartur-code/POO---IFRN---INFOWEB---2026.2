#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> idades(n);

    for (int i = 0; i < n; i++) {
        cin >> idades[i];
    }

    vector<int> ordem_idosos;

    for (int idade : idades) {
        if (idade >= 60) {
            ordem_idosos.push_back(idade); // equivale a append
        }
    }

    sort(ordem_idosos.begin(), ordem_idosos.end());
    reverse(ordem_idosos.begin(), ordem_idosos.end());

    vector<int> lista_tempos;

    for (int i : ordem_idosos) {

        int contador = 0;

        auto pos_idades =
            find(idades.begin(), idades.end(), i);

        auto pos_ordem =
            find(ordem_idosos.begin(), ordem_idosos.end(), i);

        while (distance(idades.begin(), pos_idades) !=
               distance(ordem_idosos.begin(), pos_ordem)) {

            int indice = distance(idades.begin(), pos_idades);

            swap(idades[indice], idades[indice - 1]);

            contador++;

            pos_idades =
                find(idades.begin(), idades.end(), i);
        }

        lista_tempos.push_back(contador);
    }

    cout << "Idosos ordenados: ";
    for (int x : ordem_idosos)
        cout << x << " ";
    cout << endl;

    cout << "Tempos: ";
    for (int x : lista_tempos)
        cout << x << " ";
    cout << endl;

    cout << "Lista final: ";
    for (int x : idades)
        cout << x << " ";
    cout << endl;

    int maior = *max_element(
        lista_tempos.begin(),
        lista_tempos.end()
    );

    cout << "Levaria " << maior << " segundos!" << endl;

    return 0;
}