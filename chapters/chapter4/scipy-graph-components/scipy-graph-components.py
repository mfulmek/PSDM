from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
graph = [
    [ 0, 1 , 1, 0 , 0 ],
    [ 0, 0 , 1 , 0 ,0 ],
    [ 0, 0, 0, 0, 0],
    [0, 0 , 0, 0, 1],
    [0, 0, 0, 0, 0]
]
graph = csr_matrix(graph)
n_components, labels = connected_components(
    csgraph=graph,
    directed=False,
    return_labels=True
)
print(f'Der Graph hat {n_components} Zusammenhangskomponenten.')
