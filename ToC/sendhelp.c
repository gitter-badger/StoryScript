#include <stdio.h>
#include <stdlib.h>

// Exception Raising
void raiseException(int code, char* description)
{
	switch(code)
	{
		case 100:
			printf("InvalidSyntax: %s", description);
			break;
		case 101:
			printf("AlreadyDefined: %s", description);
			break;
		case 102:
			printf("NotImplementedException %s", description);
			break;
		case 103:
			printf("NotDefinedException: %s", description);
			break;
		case 104:
			printf("GeneralException: %s", description);
			break;
		case 105:
			printf("DivideByZeroException: %s", description);
			break;
		case 106:
			printf("InvalidValue: %s", description);
			break;
		case 107:
			printf("InvalidTypeException: %s", description);
			break;
	}
	exit(code);
}

int main() {
	// Heap allocation 
	int *a = (int*)malloc(sizeof(int));
	int *b = (int*)malloc(sizeof(int));
	*b = 10;
	*a = 20;
	
	// Stack allocation 
	int c;
	int d = 69;
	c = 25 + 20;
	c -= 5;
	
	printf("Hello world");
	switch (d)
	{
		case 10:
			printf("The value of d is 10");
			break;
		case 69:
			printf("**SIXTYNINE**");
			break;
	}
	
	for (int __sts_loopcount_JJE = 0; __sts_loopcount_JJE < 10; __sts_loopcount_JJE++) {
		for (int __sts_loopcount_Dps = 0; __sts_loopcount_Dps < 10; __sts_loopcount_Dps++) {
			printf("ting");
		}
		
		printf("owo");
	}
	
	raiseException(104, "No Description provided");
	
	// Deleting variables 
	free(a)
	free(b)
	return 0;
}