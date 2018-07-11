#include <stdio.h>

int main(void) {
	char a[30],b[30];
	int j,n,i;
	gets(a);
	n=strlen(a);
	j=0;
	for(i=n-1;i>=0;i--)
	{
		
		b[j]=a[i];
		j++;
	}
	b[j]='\0';
	printf("%s",b);
	if(a[i]==b[j])
	{
		printf("\npalindrome");
		
	}
	else
	{
		printf("\nit is not  a palindrome");
	}
	
}
