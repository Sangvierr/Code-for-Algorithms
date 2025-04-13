#include <iostream>

using namespace std;

int main(){
    unsigned short int h, m, t;

    cin >> h >> m >> t;

    int total_min = h * 60 + m + t;
    int new_hour = (total_min / 60) % 24;
    int new_min = total_min % 60;

    cout << new_hour << " " << new_min << endl;

    return 0;
}