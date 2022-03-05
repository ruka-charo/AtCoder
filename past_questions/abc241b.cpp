#include <iostream>
#include <vector>
using namespace std;


int main(){
    // 標準入力
    int N, M, a, b;
    vector<int> A;
    vector<int> B;

    cin >> N >> M;
    for (int i = 0; i < N; i++){
        cin >> a;
        A.push_back(a);
    }

    for (int i = 0; i < M; i++){
        cin >> b;
        B.push_back(b);
    }

    // Aの中にBの長さの麺があればそれを食べる
    bool judge = true;
    for (int i = 0; i < M; i++){
        for (int j = 0; j < N; j++){
            if (B[i] == A[j]){
                A[j] = 0;
                judge = true;
                break;
            }
            else{
                judge = false;
            }
        }
        // 全てのAの中を見てfalseなら終了
        if (not judge){
            cout << "No\n";
            return 0;
        }
    }
    cout << "Yes\n";
}
