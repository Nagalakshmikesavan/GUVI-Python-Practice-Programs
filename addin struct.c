#include <stdio.h>
struct student
{
	int num,sum;
	
}s1,s2;
void details(struct student s1,struct student s2);
int main()
{
	scanf("%d",&s1.num);
	scanf("%d",&s2.num);
	details(s1,s2);
	
}
void details(struct student s1,struct student s2)
{
	int sum;
	sum=s1.num+s2.num;
	printf("%d\n",sum);
	
	
	
}
