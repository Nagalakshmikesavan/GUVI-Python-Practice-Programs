#include <stdio.h>

int main(void) {
	char a[30],b[30];
	int j,n,i,m,s;
	gets(a);
	gets(b);
	n=strlen(a);
	m=strlen(b);
	s=n+m;
	j=n;
	for(i=0;a[i]!='\0';i++)
	{
		
		a[j]=b[i];
		j++;
	}
	a[j]='\0';
	printf("%s",a);
}
	
