#include <stdio.h> 
#include <string.h> 
#define N 100 
 
int LCS(char s1[], char s2[]) { 
int i,j; 
int m = strlen(s1); 
int n = strlen(s2); 
int tab[N+1][N+1]; 
for (i = 0; i <= m; i++) { 
for (j = 0; j <= n; j++) { 
tab[i][j] = 0; 
} 
} 
for (i = 1; i <= m; i++) { 
 
for (j = 1; j <= n; j++) { 
if (s1[i - 1] == s2[j - 1]) { 
tab[i][j] = tab[i - 1][j - 1] + 1; 
} else { 
if(tab[i - 1][j] > tab[i][j - 1]){ 
tab[i][j] = tab[i - 1][j]; 
} 
else{ 
tab[i][j] =tab[i][j - 1]; 
} 
} 
} 
} 
printf("\nLCS Table:\n"); 
for (int i = 0; i <= m; i++) { 
for (int j = 0; j <= n; j++) { 
printf("%d\t", tab[i][j]); 
} 
printf("\n"); 
} 
 
int index = tab[m][n]; 
char lcs[index + 1]; 
lcs[index] = '\0'; 
 
i = m, j = n; 
while (i > 0 && j > 0) { 
if (s1[i - 1] == s2[j - 1]) { 
lcs[index - 1] = s1[i - 1]; 
i--; 
j--; 
index--; 
} else if (tab[i - 1][j] > tab[i][j - 1]) { 
i--; 
} else { 
j--; 
} 
} 
printf("\nLongest Common Subsequence: %s\n", lcs); 
return tab[m][n]; 
} 
 
int main() { 
char x[N], y[N]; 
 
int i,j; 
printf("Enter String 1: "); 
scanf("%s", x); 
printf("Enter String 2: "); 
scanf("%s", y); 
int length = LCS(x, y); 
printf("Length of LCS: %d\n", length); 
return 0; 
}