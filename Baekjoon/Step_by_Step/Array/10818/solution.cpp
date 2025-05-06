#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    unsigned int N;

    cin >> N;

    int arr[N];

    for (int i=0; i<N; i++){
        cin >> arr[i];
    }

    int min_val = arr[0];
    int max_val = arr[0];

    for (int i=0; i<N; i++){
        if (arr[i] < min_val){
            min_val = arr[i];
        }
        if (arr[i] > max_val){
            max_val = arr[i];
        }
    }

    cout << min_val << " " << max_val << "\n";

    return 0;
}