#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
    vector<unsigned short int> dice(3);
    
    cin >> dice[0] >> dice[1] >> dice[2];

    sort(dice.begin(), dice.end());

    int money;
    if (dice[0]==dice[2]){
        money = 10000 + dice[0] * 1000;
    }
    else if (dice[0]==dice[1]){
        money = 1000 + dice[0] * 100;
    }else if (dice[1]==dice[2]){
        money = 1000 + dice[1] * 100;
    }else{
        money = dice[2]*100;
    }

    cout << money << endl;

    return 0;
}

