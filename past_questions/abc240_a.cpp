#include <iostream>
using namespace std;


void solve(int a, int b){
    if(b - a == 1){
        cout << "Yes" << endl;
    }
    else if(a == 1 && b == 10){
        cout << "Yes" << endl;
    }
    else{
        cout << "No" << endl;
    }
}


int main(){
    int a, b;
    cin >> a >> b;

    solve(a, b);

    return 0;
}
