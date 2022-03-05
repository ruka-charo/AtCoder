#include <iostream>
#include <vector>
#include <numeric>
using namespace std;


int main(){
    // 標準入力
    int N;
    cin >> N;

    vector<int> A(4*N-1);
    for (int i = 0; i < 4*N-1; i++)
        cin >> A[i];

    // カードを取る前後での合計値の差分で見つける
    int before = 0;
    int after = 0;

    before = 4 * (N * (N + 1) / 2);
    after = accumulate(A.begin(), A.end(), 0);

    cout << before - after << endl;
}
