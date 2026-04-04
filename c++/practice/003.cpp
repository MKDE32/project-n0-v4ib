#include <iostream>

using namespace std;

int exp(int Exponent)

{
int Ergebnis =1, Basis = 2;

for (int i=1;i<=Exponent;i++)
    Ergebnis=Ergebnis*Basis;

return Ergebnis;
}


int main()

{
int zahl,i=0,Endergebnis=0;
int reste[8];

for (int index =0;index < 8; index++)
    reste[index] = 0;

cin >> zahl;

do {reste[i]= zahl % 10;zahl= zahl / 10;i++;}
while (zahl !=0);

for(int ni =0;ni<8;ni++)
{reste[ni]=reste[ni]*exp(ni);
Endergebnis = Endergebnis+reste[ni];}

cout << Endergebnis;

    return 0;}
