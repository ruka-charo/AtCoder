#include <iostream>
#include <vector>
#include <cstring>
using namespace std;


// 回文の判定
bool judge(char str[]){
    int N = strlen(str);

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
    char drop_word[1000001];
    char word[1000001];
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
        bool ans = true;
        int word_count = strlen(word);
        int diff = count_back - count_front;
        if (diff >= 0){
            for (int i = 0; i < word_count - diff; i++){
                if (word[i] == word[word_count-diff-1-i])
                    continue;
                else
                    ans = false;
                    break;
            }

            if (ans)
                cout << "Yes\n";
            else
                cout << "No\n";
        }
        else
            cout << "No\n";
    }
}
