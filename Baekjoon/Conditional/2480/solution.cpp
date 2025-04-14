#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    unsigned short int a, b, c;

    cin >> a >> b >> c;

    int money;

    if (a == b and b == c and c == a){
        money = 10000 + a * 1000;
    }
    else{
        if (a == b){
            money = 1000 + a * 100;
        }
        else if (b == c){
            money = 1000 + b * 100;
        }
        else if (c == a){
            money = 1000 + c * 100;
        }
        else{
            money = std::max({a, b, c})*100;
        }
    }

    cout << money << endl;

    return 0;
}