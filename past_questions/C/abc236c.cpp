#include <iostream>
#include <vector>
#include <string>
using namespace std;


int main(){
    // 標準入力
    int N, M;
    cin >> N >> M;

    vector<string> s(N);
    vector<string> t(M);
    for (int i = 0; i < N; i++) cin >> s[i];
    for (int i = 0; i < M; i++) cin >> t[i];

    // algorithm
    int t_count = 0;
    for (int i = 0; i < N; i++){
        if (s[i] == t[t_count]){
            cout << "Yes\n";
            t_count++;
        }
        else
            cout << "No\n";
    }
    
}
