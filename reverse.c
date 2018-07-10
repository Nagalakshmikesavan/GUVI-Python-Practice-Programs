#include <stdio.h>
void reverse(int a[]);
int main(void)
{
	int a[]={1,2,3};
	reverse(a);
		

	return 0;
}

void reverse(int a[])
{
	int i,j,c[100],k;
	for(i=3-1,j=0;i>=0;i--,j++)
	{
		c[j]=a[i];
	}
		for(k=0;k<3;k++)
	{
		printf("%d ",c[k]);
	}

}

