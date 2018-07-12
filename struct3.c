#include <stdio.h>
struct student
{
	int hour,min;
	
}s,s1,s2;
void details(struct student s1,struct student s2);
int main()
{
	scanf("%d",&s1.hour);
	scanf("%d",&s1.min);
	scanf("%d",&s2.hour);
	scanf("%d",&s2.min);
	details(s1,s2);
	
}
void details(struct student s1,struct student s2)
{
	s.hour=s1.hour-s2.hour;
	s.min=s1.min-s2.hour;
	printf("%d.%d",s.hour,s.min);
	
	
	
	
}
