#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int>&A){
    sort(A.begin(), A.end());

    int n = A.size();
    int last_three = A[n-1] * A[n-2] * A[n-3];
    int first_two_and_last_one = A[0] * A[1] * A[n-1];

    return max(last_three, first_two_and_last_one);
}

int main(){
    vector<int> A = {-5, -10, 0, 1, 3, 5, 2};
    cout << "Max product is: " << solution(A) << endl;
    return 0;
}