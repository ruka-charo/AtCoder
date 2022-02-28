#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;



vector<vector<int>> lattice(int x, int y){
    // (0, 0)の時の格子点情報をベクトルに格納する
    vector<vector<int>> lattice = {{1+x, 2+y}, {2+x, 1+y},
                                  {-1+x, 2+y}, {2+x, -1+y},
                                  {1+x, -2+y}, {-2+x, 1+y},
                                  {-1+x, -2+y}, {-2+x, -1+y}};

    return lattice;
}

int main(){
    // 標準入力
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    // それぞれの格子点を算出
    vector<vector<int>> lattice_1, lattice_2;
    lattice_1 = lattice(x1, y1);
    lattice_2 = lattice(x2, y2);

    // 一致している格子点の数を数える
    int correct = 0;
    for (int i = 0; i < 8; i++){
        for (int j = 0; j < 8; j++){
            if (equal(lattice_1[i].begin(), lattice_1[i].end(),
            lattice_2[j].begin(), lattice_2[j].end()))
                correct++;
            else
                continue;
        }
    }

    // 一致している格子点が1つ以上あればYes
    if (correct >= 1)
        cout << "Yes";
    else
        cout << "No";
}
