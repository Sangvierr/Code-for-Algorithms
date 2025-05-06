#include <iostream>
#include <vector>

using namespace std;

int main(){
    unsigned short int N, M;
    
    
    cin >> N >> M;
    
    vector<int> arr(N, 0);
    
    for (int i=0; i<N; i++){
        arr[i] = i+1;
    }

    unsigned short int a, b;
    
    for (int i=0; i<M; i++){
        cin >> a >> b;

        int temp, temp2;
        
        temp = arr[a-1];
        temp2 = arr[b-1];
        
        arr[a-1] = temp2;
        arr[b-1] = temp;
    }
    
    for (int i=0; i<N; i++){
        cout << arr[i] << " ";
    }
    
    cout << "\n";
    
    return 0;
}