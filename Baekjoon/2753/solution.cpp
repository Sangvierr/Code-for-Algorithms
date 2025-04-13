#include <iostream>

using namespace std;

int main(){
    unsigned short int y;

    cin >> y;

    if (y % 4 == 0){
        if (y % 100 != 0 or y % 400 == 0){
            cout << 1 << endl;
        }
        else{
            cout << 0 << endl;
        }
    } else{
        cout << 0 << endl;
    }

    return 0;
}