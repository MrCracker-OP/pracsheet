#include <stdio.h>
#include <limits.h>
int main() {
int V;
printf("Enter the number of vertices: ");
scanf("%d", &V);
int graph[V][V];
printf("Enter the adjacency matrix:\n");
for (int i = 0; i < V; i++) {
for (int j = 0; j < V; j++) {
scanf("%d", &graph[i][j]);
}
}
int selected[V];
for (int i = 0; i < V; i++) {
selected[i] = 0;
}
int no_of_edges = 0;
selected[0] = 1;
printf("Edgesin MST:\n");
while (no_of_edges < V - 1) {
int min = INT_MAX, x = 0, y = 0;
for (int i = 0; i < V; i++) {
if (selected[i]) {
for (int j = 0; j < V; j++) {
if (!selected[j] && graph[i][j] && graph[i][j] < min) {
min = graph[i][j];
x = i;
y = j;
}
}
}
}
printf("%d -- %d == %d\n", x, y, min);
selected[y] = 1;
no_of_edges++;
}
return 0;
}