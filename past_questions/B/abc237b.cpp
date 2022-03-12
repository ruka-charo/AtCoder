#include <iostream>
#include <vector>
using namespace std;


int main(){
    // 標準入力
    int H, W;
    cin >> H >> W;
    vector<vector<int>> data(H, vector<int>(W));

    for (int i = 0; i < H; i++){
        for (int j = 0; j < W; j++){
            cin >> data[i][j];
        }
    }

    // 転置行列の作成
    vector<vector<int>> ans(W, vector<int>(H));

    for (int i = 0; i < H; i++){
        for (int j = 0; j < W; j++){
            ans[j][i] = data[i][j];
        }
    }

    // 出力
    for (int i = 0; i < W; i++){
        for (int j = 0; j < H; j++){
            cout << ans[i][j] << " ";
        }
        cout << endl;
    }

}
