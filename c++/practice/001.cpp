#include <iostream>
using namespace std;



string verknuepf(bool A, bool B)
{
if (!(A || B) == 1)
    {return "true";}
else{return "false";}

}



int main()
{
    bool Feld1[4];
    bool Feld2[4];

for (int S = 0;S < 4; S++)
    {
    cout << "Bitte Feld A eingeben";
    cin >> Feld1[S];
    cout << "Bitte Feld B eingeben";
    cin >> Feld2[S];
    }


    cout << "\nA\tB\t!A||B\n";


for (int T = 0;T < 4; T++)
    {
    if (Feld1[T] == 1)
        cout << "true";
    else cout << "false";

    if (Feld2[T] == 1)
        cout << "\ttrue\t";
    else cout << "\tfalse\t";

     cout << verknuepf(Feld1[T],Feld2[T]) << endl;

    }





return 0;
}
