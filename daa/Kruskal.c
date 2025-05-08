#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int parent[MAX];

// Find root of a set
int find(int v) {
    if (parent[v] != v)
        parent[v] = find(parent[v]);
    return parent[v];
}

// Union two sets
void unionSets(int u, int v) {
    parent[find(v)] = find(u);
}

// Sort edges by weight
int compare(const void *a, const void *b) {
    return ((int *)a)[2] - ((int *)b)[2];
}

void kruskal(int V, int E, int edges[MAX][3]) {
    int cost = 0;
    for (int i = 0; i < V; i++) parent[i] = i;
    qsort(edges, E, sizeof(edges[0]), compare);

    printf("\nMST edges:\n");
    for (int i = 0, count = 0; i < E && count < V - 1; i++) {
        int u = edges[i][0], v = edges[i][1], w = edges[i][2];
        if (find(u) != find(v)) {
            printf("%d -- %d == %d\n", u, v, w);
            unionSets(u, v);
            cost += w;
            count++;
        }
    }
    printf("Total cost: %d\n", cost);
}

int main() {
    int V, E, edges[MAX][3];
    printf("Enter nodes and edges: ");
    scanf("%d %d", &V, &E);
    printf("Enter edges (u v weight):\n");
    for (int i = 0; i < E; i++)
        scanf("%d %d %d", &edges[i][0], &edges[i][1], &edges[i][2]);
    kruskal(V, E, edges);
    return 0;
}
