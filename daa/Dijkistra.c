#include <stdio.h>
#include <limits.h>
#define V 4
int minDistance(int dist[], int sptSet[]) {
int min = INT_MAX, min_index;
for (int v = 0; v < V; v++) {
if (!sptSet[v] && dist[v] < min) {
min = dist[v];
min_index = v;
}
}
return min_index;
}
void printPath(int parent[], int j) {
if (parent[j] == -1) {
printf("%d ", j);
return;
}
printPath(parent, parent[j]);
printf("-> %d ", j);
}
void printTable(int dist[], int iteration) {
printf("Iteration %d: ", iteration);
for (int i = 0; i < V; i++) {
if (dist[i] == INT_MAX)
printf("INF ");
else
printf("%d ", dist[i]);
}
printf("\n");
}
void dijkstra(int graph[V][V], int start) {
int dist[V], sptSet[V], parent[V];
for (int i = 0; i < V; i++) {
dist[i] = INT_MAX;
sptSet[i] = 0;
parent[i] = -1;
}
dist[start] = 0;
printf("Initial shortest path distances:\n");
printTable(dist, 0);
for (int count = 0; count < V - 1; count++) {
int u = minDistance(dist, sptSet);
sptSet[u] = 1;
for (int v = 0; v < V; v++) {
if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] <
dist[v]) {
dist[v] = dist[u] + graph[u][v];
parent[v] = u;
}
}
printTable(dist, count + 1);
}
printf("\nFinal shortest paths:\n");
printf("Vertex\tDistance\tPath\n");
for (int i = 0; i < V; i++) {
printf("%d\t%d\t", i, dist[i]);
printPath(parent, i);
printf("\n");
}
}
int main() {
int graph[V][V] = {
{0, 10, 0, 30},
{10, 0, 50, 0},
{0, 50, 0, 10},
{30, 0, 10, 0}
};
dijkstra(graph, 0); // Start from vertex 0
return 0;
}