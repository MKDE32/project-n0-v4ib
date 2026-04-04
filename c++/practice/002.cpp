#include <iostream>
using namespace std;

int main()

{int zahl, position = 0;
int reste[16];
int Zsys;

for (int index =0;index < 16; index++)
    reste[index] = 0;

do {cout << "geben Sie einen Wert ein";
    cin >> zahl;}
    while (zahl > 65535);

do {cout << "geben Sie ein in welches Zahlensystem umgerechnet werden soll";
    cin >> Zsys;}
    while (Zsys > 9);

do  {reste[position] = zahl % Zsys;
    position++;
    zahl = zahl / Zsys;}
    while (zahl !=0);

for (int index = 15; index >= 0; index--)
    {cout <<reste[index];

if (index % 4 == 0)
    cout << " ";}

    return 0;}
