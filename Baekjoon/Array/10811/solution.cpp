#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    short int N, M, a, b;

    cin >> N >> M;

    vector<int> arr(N);

    for (int i=0; i<N; i++){
        arr[i] = i+1;
    }

    for (int i=0; i<M; i++){
        cin >> a >> b;

        std::reverse(arr.begin() + a-1, arr.begin() + b);
    }

    for (int i=0; i<N; i++){
        cout << arr[i] << "\n";
    }

    cout << "\n";

    return 0;
}