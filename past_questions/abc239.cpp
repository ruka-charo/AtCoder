#include <iostream>
#include <math.h>
using namespace std;


long long x, ans;

long long solve(long long x){

    ans = x / 10 - (x % 10 < 0);

    return ans;
}


int main(){
    cin >> x;
    ans = solve(x);

    cout << ans << endl;

    return 0;
}
