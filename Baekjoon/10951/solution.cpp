#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    unsigned short int a, b;

    while (1){
        cin >> a >> b;

        if (cin.eof()) break;
        else cout << a+b << "\n";
    }

    return 0;
}