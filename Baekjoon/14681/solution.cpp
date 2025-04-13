#include <iostream>

using namespace std;

int main(){
    signed short int x, y;

    cin >> x >> y;

    // 1 or 4
    if (x > 0){
        if (y>0){
            cout << 1 << endl;
        }else{
            cout << 4 << endl;
        }
    }
    //2 or 4
    else{
        if (y>0){
            cout << 2 << endl;
        }else{
            cout << 3 << endl;
        }
    }

    return 0;
}