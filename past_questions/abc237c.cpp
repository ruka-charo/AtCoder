#include <iostream>
#include <string>
using namespace std;


// 回文の判定
bool judge(string str){
    int N = str.length();

    bool judge = true;
    for (int i = 0; i <= N; i++){
        if (str[i] == str[N-i-1])
            continue;
        else
            judge = false;
            break;
    }

    return judge;
}



int main(){
    // 標準入力
    string word;
    cin >> word;

    if (judge(word))
        cout << "Yes\n";

    else{
        // 先頭のaの個数を数える
        int count_front = 0;
        for (int i = 0; word[i] != '\0'; i++){
            if (word[i] == 'a')
                count_front++;
            else
                break;
        }

        // 末尾のaの個数を数える
        int count_back = 0;
        for (int i = 0; word[i] != '\0'; i++){
            if (word[i] == 'a')
                count_back++;
            else
                count_back = 0;
        }


        // 差分の数だけ末尾からaを削る
        int diff = count_back - count_front;
        if (diff > 0){
            word.erase(word.end()-diff, word.end());

            if (judge(word))
                cout << "Yes\n";
            else
                cout << "No\n";
            }
        else
            cout << "No\n";
    }
}
