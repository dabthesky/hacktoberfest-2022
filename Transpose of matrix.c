#include<stdio.h>
int main()
{
		int row,col,a[10][10],i,j;
	printf("Enter the number of rows and column you want to enter in the matrix: ");
	scanf("%d%d",&row,&col);
	for(i=0;i<row;i++)
	{
		for(j=0;j<col;j++)
		{
			scanf("%d",&a[i][j]);
		}
	}
	printf("Matrix original\n\n",row,col);
	for(i=0;i<row;i++)
	{
		for(j=0;j<col;j++)
		{
			printf("%d",a[i][j]);
			printf("\t");
		}
	printf("\n");
	}
	printf("\nTranspose of the matrix:\n\n");
	for(j=0;j<col;j++)
	{
		for(i=0;i<row;i++)
		{
			printf("%d\t",a[i][j]);
		}
		printf("\n");
	}
}
