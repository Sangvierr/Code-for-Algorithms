#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N = 9;
    int arr[N];

    for (int i=0; i<N; i++){
        cin >> arr[i];
    }

    int max_val=arr[0];
    int idx = 0;

    for (int i=0; i<N; i++){
        if (arr[i] > max_val){
            idx = i;
            max_val = arr[i];
        }
    }

    cout << max_val << "\n";
    cout << idx+1 << "\n";

    return 0;

}