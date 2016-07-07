#include<iostream> 	//cin,cout
#include<cmath>		//log
#include<vector>    // bin vector

int pow(int a,int b){return b?a*pow(a,b-1):1;}
int bin(int x)
{
	int ans=0;
	int hi=log(x)/log(2);
	std::vector<int> bin;
	for(int i=hi;i>=0;i--)
	{
		if (x>=pow(2,i))
		{
			x-=(pow(2,i));
			bin.push_back(1);
		}
		else
		{
			bin.push_back(0);
		}
	}
	int i=hi;
	for(auto& bit:bin)
	{
		ans+=bit*pow(10,i)<<' ';
		i--;
	}
	return ans;
}
int main()
{
	int x;
	std::cin>>x;
	std::cout<<bin(x);
}
