#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int n, j, a;
vector<int> theta, ans;


int main(){
    cin >> n;
    theta.push_back(0);

    for (int i=0; i < n; i++){
        cin >> j;
        theta.push_back(j);
    }

    // 角度を合計する
    for (int i = 0; i < n; i++){
        theta[i+1] = theta[i] + theta[i+1];

        if (theta[i+1] >= 360){
            theta[i+1] = theta[i+1] - 360;
        }
    }

    // ソートする
    sort(theta.begin(), theta.end());
    theta.push_back(360);

    // 前後の角度を引き算する
    ans.push_back(theta[0]);
    for (int i = 0; i < n+1; i++){
        ans.push_back(theta[i+1] - theta[i]);
    }

    // 答え
    cout << *max_element(ans.begin(), ans.end()) << endl;


    return 0;
}
