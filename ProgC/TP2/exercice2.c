#include <stdio.h> 
#include <stdlib.h> 

/* FONCTION */ 

int longueur(char str[]){
	int i = 0;
	while (str[i] != '\0') {
		i++;
	}
	return i;
}

char* copie_chaine(char mot[]){
	int i;
	int len = longueur(mot)+1;
	char *str = malloc(len * sizeof(char));
	for (i=0; i<len; i++) {
		str[i] = mot[i];
	}
	return str;
}

void afficher(int tableau[], int longueur) {
	int i;
	for (i=0; i<longueur; i++) {
	printf("%d ",tableau[i]);
	}
	printf("\n");
}


/* FONCTION EXE */ 

void question1(void){
	char s[] = "HelloWorld";
	int len = longueur(s);
	printf("longeur = %d\n", len);
	
}

void question2(void){
	char mot[] = "HelloWorld";
	char * chaine = copie_chaine(mot);
	printf("%s\n", chaine);
	free(chaine);
	
}


int main(void){
	
	question2();
	
	
	return 0;
}









