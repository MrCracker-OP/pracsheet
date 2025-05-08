#include <stdio.h> 
#include <limits.h> 
#define V 4 
void printTable(int dist[], int iteration){ 
printf("%d: ", iteration); 
for(int i=0; i<V; i++){ 
if(dist[i] == INT_MAX){ 
printf("* "); 
} 
else{ 
printf("%d ", dist[i]); 
} 
} 
printf("\n"); 
} 
 
void printSolution(int dist[]) 
{ 
printf("\nVertex \t Distance from Source\n"); 
for (int i = 0; i < V; i++) 
printf("%d \t %d\n", i, dist[i]); 
 
} 
void bellman_ford(int graph[V][V], int src) 
{ 
int dist[V]; 
for (int i = 0; i < V; i++) 
dist[i] = INT_MAX; 
dist[src] = 0; 
 
printf("Table:\n"); 
printTable(dist, 0); 
 
for (int i = 1; i < V; i++) 
{ 
for (int u = 0; u < V; u++) 
{ 
for (int v = 0; v < V; v++) 
{ 
if (graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v]) 
{ 
dist[v] = dist[u] + graph[u][v]; 
} 
} 
} 
printTable(dist, i); 
} 
 
for (int u = 0; u < V; u++) 
{ 
for (int v = 0; v < V; v++) 
{ 
if (graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v]) 
{ 
printf("Negative weight cycle detected!\n"); 
return; 
} 
} 
} 
 
printSolution(dist); 
} 
 
int main() 
{ 
int graph[V][V] = { 
{0, 1, 4, 0}, 
{0, 0, -3, 2}, 
{0, 0, 0, 3}, 
 
{0, 0, 0, 0}, 
}; 
int source = 0; 
bellman_ford(graph, source); 
return 0; 
}