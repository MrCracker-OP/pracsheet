#include <stdio.h>
void main() {
int arr[30];
int l,s,i,n;
printf("Enter size of an array: ");
scanf("%d",&n);
printf("\nEnter array elements:");
for(i=0;i<n;i++){
scanf("%d",&arr[i]);
}
l=arr[0];
s=arr[0];
for(i=0;i<n;i++){
if(arr[i]<s)
s=arr[i];
if(arr[i]>l)
l=arr[i];
}
printf("Minimum= %d",s);
printf("\tMaximum= %d",l);
}
