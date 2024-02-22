#include <stdio.h> 

/* FONCTION */ 
void incremente(int *a){
	++*a; /* incrementer la valeur de a */
}


void echange(int *a,int *b){
	int c = *a;
	*a = *b;
	*b = c;
	
}

int trier(int *a,int *b){
	int c = *a;
	int d = *b;
	int ech = 0;
	
	if (c > d){
		echange(&c, &d);
		ech = 1;
	};
	return ech;
	
}






/* FONCTION EXE */ 

void question1(void){
	int a = 3;
	incremente(&a);
}

void question2(void){
	int a = 3;
	int b = 4;
	echange(&a, &b);
	printf("a = %d, b = %d\n", a, b);
	
}

void question3(void){
	int a = 12;
	int b = 4;
	int res = trier(&a, &b);
	printf("res = %d\n", res);
	
}



int main(void){
	
	question1();
	question2();
	question3();
	
	return 0;
}

