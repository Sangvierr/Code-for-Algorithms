#include <iostream>

using namespace std;

int main(){
    unsigned short int N;
    signed short int v;
    signed short int count = 0;

    cin >> N;

    int array[N+1];

    for (int i=0; i<N; i++){
        cin >> array[i];
    }

    cin >> v;

    for (int i=0; i<N; i++){
        if (array[i]==v){
            count+=1;
        }
    }

    cout << count << "\n";

    return 0;

}