#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


int main(){
    // 標準入力
    int L, R;
    cin >> L >> R;

    string S;
    cin >> S;


    //algorithm
    reverse(S.begin()+L-1, S.end()-S.length()+R);

    cout << S << endl;

}
