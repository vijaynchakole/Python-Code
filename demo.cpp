#include <iostreamc>
using namespace  std;



class Arithmatic
{
//characteristics

public:
int ino1,ino2;
int ans ;


//behaviour

void Addition()
{
ans = ino1 + ino2 ;
}

void Subtraction()
{
ans = ino1 - ino2 ;
}

} ;

int main()
{
    Arithmatic obj1 ;

    obj1.ino1 = 20 ;
    obj1.ino2 = 6 ;
    obj1.Addition() ;

    cout<<obj1.ans ;

}