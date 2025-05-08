#include<stdio.h> 
#include<stdlib.h> 
#include<string.h> 
void prefixSearch(char* pat, int m, int* pps) { 
int length = 0; 
pps[0] = 0; 
int i = 1; 
while(i < m) { 
if(pat[i] == pat[length]) { 
length++; 
pps[i] = length; 
}else { 
if(length != 0) { 
length = pps[length - 1]; 
i--; 
} else 
pps[i] = 0; 
} 
i++; 
} 
} 
 
void patrnSearch(char* orgnString, char* patt, int m, int *locArray, int *loc) { 
int n, i = 0, j = 0; 
n = strlen(orgnString); 
 
int* prefixArray = (int*)malloc(m * sizeof(int)); 
prefixSearch(patt, m, prefixArray); 
*loc = 0; 
while(i < n) { 
if(orgnString[i] == patt[j]) { 
i++; 
j++; 
} 
if(j == m) { 
locArray[*loc] = i-j; 
(*loc)++; 
j = prefixArray[j-1]; 
}else if(i < n && patt[j] != orgnString[i]) { 
if(j != 0) 
j = prefixArray[j-1]; 
else 
i++; 
} 
} 
free(prefixArray); 
} 
int main() { 
char* orgnStr = "BCDABCABDAA"; 
char* patrn = "CAB"; 
int m = strlen(patrn); 
int locationArray[strlen(orgnStr)]; 
int index; 
patrnSearch(orgnStr, patrn, m, locationArray, &index); 
for(int i = 0; i<index; i++) { 
printf("Pattern found at location: %d\n", locationArray[i]); 
} 
} 
