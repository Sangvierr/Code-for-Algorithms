#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    unsigned int N;
    unsigned short int A, B;

    cin>>N;

    for (int i=0; i<N; i++){
        cin >> A >> B;

        cout << A+B << "\n";
    }
}