#include <iostream>

using namespace std;


int main()

{
char b;
int v;

for(int z=0;z<10;z++)
{
cout << "Buchstabe ";
cin >> b;
cout << "verschieben um ";
cin >> v;

cout << static_cast<char>( b + v) << endl;}





    return 0;}
