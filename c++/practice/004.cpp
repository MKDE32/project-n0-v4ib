#include <iostream>

using namespace std;


int main()

{
string s;
int laenge, v;

cin >> s;
cin >> v;
laenge = s.length();

for (int z=0;z< laenge;z++)
    {
    cout << static_cast<char>(s[z] + v+(z+1));
    }




    return 0;}
