#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


int main(){
    // 標準入力
    string s;
    cin >> s;

    // 並び替え
    sort(s.begin(), s.end());

    // 答え
    cout << s << endl;

}
