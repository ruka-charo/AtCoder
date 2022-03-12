#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;


int main(){
    // 標準入力
    int N;
    vector<int> x(N);
    vector<int> y(N);

    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> x[i] >> y[i];
    }

    // 距離の最大値を求める
    double distance;
    double max_distance = 0;
    for (int i = 0; i < N-1; i++){
        for (int j = i+1; j < N; j++){
            distance = sqrt(pow(x[i] - x[j], 2) + pow(y[i] - y[j], 2));

            if (max_distance < distance)
                max_distance = distance;
        }
    }

    // 答え
    cout << fixed << setprecision(10) << max_distance << endl;
}
