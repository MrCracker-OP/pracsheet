#include<stdio.h>

#define MAX 100

int adj[MAX][MAX]; // Adjacency matrix
int visited[MAX]; // Visited array

void dfs(int v, int n){
    int i;
    visited[v] = 1;
    printf("%d ", v);

    for(i = 0; i < n; i++){
        if (adj[v][i]== 1 && !visited[i]){
            dfs(i,n);
	}
    }
}

int main(){
    int i, n,edges, u, v;

    printf("Enter the number of vertices: ");
    scanf("%d", &n);

    printf("Enter the number of edges: ");
    scanf("%d", &edges);

    for (i=0; i < edges; i++){
	printf("Enter edge(u v): ");
	scanf("%d %d", &u, &v);
	adj[u][v] = 1;
	adj[v][u] = 1; // Assuming undirected graph
    }

    printf("DFS Traversal: ");
    dfs(0, n);
    printf("\n");

    return 0;
}

