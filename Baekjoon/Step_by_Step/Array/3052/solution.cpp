#include <iostream>
#include <vector>

using namespace std;

int main(){
    int arr[42]={0};
    int n;

    for (int i=0; i<10; i++){
        cin >> n;
        arr[n%42]++;
    }

    int count=0;

    for (int i=0; i<42; i++){
        if (arr[i]>0){
            count++;
        }
    }

    cout << count << "\n";

    return 0;
}