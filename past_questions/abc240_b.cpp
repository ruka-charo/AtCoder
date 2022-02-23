#include <iostream>
#include <set>
using namespace std;


int solve(){
    int n, j;
    cin >> n;

    set<int> input;
    for(int i = 0; i < n; i++){
        cin >> j;
        input.insert(j);
    }

    return input.size();

}


int main(){


    cout << solve();


    return 0;
}
