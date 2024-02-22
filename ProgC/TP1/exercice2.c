#include <stdio.h>


void question1(void) {
	printf("Hello World \n");
	
}

void question2(void) {
	int i = 65;
	while (i <= 90) {
		printf("%i ", i);
		i++;
	};
	printf("\n");	
}

void question3(void){
	int i = 65;
	while (i <= 90) {
		printf("%c ", i);
		i++;
	};
	printf("\n");	
}

void question4(void){
	 char * s = "Pi vaut";
	 float x = 3.1415926;
	 printf("%s %f", s,x);
	 printf("\n");	
}

void question5(void){
	char c= 'a';
	int i = c + 1;
	printf("valeur de c en caractere est '%c' et son equivalent decimal vaut %d\n", c,c);
	printf("valeur de i en caractere est '%c' et son equivalent decimal vaut %d\n", i,i);
}

void question6(void){
	char d = 'a'; /* d: debut */
	char f = 'z'; /* f: fin */
	int i_d = d; /* ASCII de d  */
	int i_f = f; /* ASCII de f  */
	while (i_d <= i_f) {
		printf("%c ", i_d);
		i_d++;
	};
	printf("\n");
}	

void question6prof(void){
	int i ;
	for  (i='a', i<='z', i++) {
		printf("%c ",i);
	};
	printf("\n");	
}	


void question6prim(void){
	int i = 65;
	while (i <= 90) {
		printf("%c ", i+32);
		i++;
	};
	printf("\n");	
}	


int main(void) {
	question1();
	question2();
	question3();
	question4();
	question5();
	question6();
	question6prim();
	return 0;
}
	
