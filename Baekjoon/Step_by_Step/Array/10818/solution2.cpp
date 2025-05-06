#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    unsigned int N;

    cin >> N;

    vector<int> vec(N);

    for (int i=0; i<N; i++){
        cin >> vec[i];
    }

    auto min_valp = min_element(vec.begin(), vec.end());
    int min_val = *min_valp;

    auto max_valp = max_element(vec.begin(), vec.end());
    int max_val = *max_valp;

    cout << min_val << " " << max_val << "\n";

    return 0;
    
}