#include <iostream>
#include <vector>
using namespace std;


int main(){
    // 標準入力
    int N;
    vector<int> H;

    cin >> N;
    for (int i = 0; i < N; i++){
        int h;
        cin >> h;
        H.push_back(h);
    }

    // 移動した回数をカウントしておく
    int move_count = 0;
    for (int i = 0; i < N-1; i++){
        if (H[i] < H[i+1])
            move_count++;
        else
            break;
    }

    // 答え
    cout << H[move_count] << endl;
}
