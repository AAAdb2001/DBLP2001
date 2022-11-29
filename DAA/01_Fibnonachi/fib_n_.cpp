#include<iostream>
using namespace std;
int fib_iterative(int n){
    if(n<=1){
        return n;
    }
    int a = 0;
    int b = 1;
    int sum1 = 0;
    int mod1 = 1000000007;
    for(int i=2;i<=n;i+=1){
        sum1 = (a+b)%mod1;
        a = b;
        b = sum1;
    }
    return sum1;
}
int main(){
    for(int i=0;i<5;i+=1){
        cout<<i<<": "<<fib_iterative(i)<<endl;
    }
     return 0;
}   