#include <iostream>
#include <cstdlib>

using namespace std;

int main(){
    unsigned short int a;
    char b[4]; // 널 문자 ('\0')를 포함해서 4바이트

    cin >> a;
    cin >> b;

    cout << a * (b[2] - '0') << endl; // 아스키 값을 사용해서 원래 정수로 변환
    cout << a * (b[1] - '0') << endl;
    cout << a * (b[0] - '0') << endl;
    cout << a * atoi(b) << endl; // ASCII to integer를 사용해서 정수로 만들어줌

    return 0;
}