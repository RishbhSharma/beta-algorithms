#include<iostream>
#include<iomanip>
#define ull unsigned long long
#define ld long double
#define Ct_ CMF*=Ct(n);
#define next_ ld Next=o_N/(CMF*CMF);
#define cond_ (Ct(n)==1.0)
#define cond_fail_ sR(Next,CMF,o_N);
int DigLen(ull x)
{
	return x?1+DigLen(x/10):0;
}
ld pow(ld x,int y)
{
	return x*(y?pow(x,y-1):1/x);
}
ld SSq(ld a)
{
	return (1+(ld)(a*1E9-1E9)/2E9);
}	
ld Ct(ull a)
{
	ull b = DigLen(a), x=(ull)a;
	return (!x%100?Ct(x/10):(a<=2?SSq(a):(a<4?(ld)a/2:(a<10?3.0:(a<20?4.0:a/pow(10,(b/2+(b%2))))))));
}
ld Ct(ld a)
{
	int b = DigLen(a);
	return (a<=2?SSq(a):(a<4?a/2:(a<10?3.0:(a<20?4.0:a/pow(10,(b/2+(b%2)))))));
}
ld sR(ld n,ld CMF,ull o_N)
{
	Ct_
	next_
	return cond_?CMF:cond_fail_;
}
ld sR(ull n,ld CMF,ull o_N)
{
	Ct_
	next_
	return cond_?CMF:cond_fail_;
}
ld sqrt(ull n)
{
	return sR(n,Ct(n),n);
}
int main()
{
	ull n;
	std::cin>>n;
	std::cout<<std::setprecision(14)<<sqrt(n)<<"\n";
	return 0;
}
