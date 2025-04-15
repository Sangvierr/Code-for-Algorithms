#include <iostream>

using namespace std;

int main(){
    int N, s;
    
    cin >> N;
    int arr[N];

    for (int i=0; i<N; i++){
        cin >> s;
        arr[i] = s;
    }

    double max_val = 0;

    for (int i=0; i<N; i++){
        if (arr[i] > max_val){
            max_val = arr[i];
        }
    }

    double total = 0;
    for (int i=0; i<N; i++){
        total += arr[i]/max_val * 100;
    }
    
    cout << total / N << "\n";

    return 0;
}