#include <iostream>

using namespace std;

int main(){
    unsigned int X;
    unsigned short int N;
    unsigned int a;
    unsigned short int b;

    cin >> X >> N;

    unsigned int total=0;

    for (int i=0; i<N; i++){
        cin >> a >> b;

        total += a * b;
    }

    if (total == X){
        cout << "Yes" << endl;
    }
    else{
        cout << "No" << endl;
    }

    return 0;
}
