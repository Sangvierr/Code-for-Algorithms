#include <iostream>
#include <vector>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    unsigned short int N, M;

    cin >> N >> M;

    vector<int> arr(N, 0);

    unsigned short int a, b, c;

    for (int i=0; i<M; i++){
        cin >> a >> b >> c;

        for (int j=a-1; j<b; j++){
            arr[j] = c;
        }
    }

    for (int i=0; i<N; i++){
        cout << arr[i] << " ";
    }

    cout << "\n";

    return 0;

}