#include <iostream>

using namespace std;


int main()

{
string s;
int laenge, verschieben;

cout << "Verschlüsselung: ";
cin >> s;

for (int i=0;i<30;i++)
{
cout << "Verschieben: ";
cin >> verschieben;
laenge = s.length();

for (int z=0;z< laenge;z++)
    {
    cout << static_cast<char>(s[z] - verschieben);
    }
    cout << endl;
}



    return 0;}
