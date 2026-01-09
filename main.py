from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
from collections import defaultdict, deque

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Node(BaseModel):
    id: str
    type: str
    data: Dict[str, Any] = {}
    position: Dict[str, float] = {}

class Edge(BaseModel):
    id: str = ""
    source: str
    target: str
    sourceHandle: str = ""
    targetHandle: str = ""

class PipelineRequest(BaseModel):
    nodes: List[Node]
    edges: List[Edge]

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

def is_dag(nodes: List[Node], edges: List[Edge]) -> bool:
    """
    Check if the graph formed by nodes and edges is a Directed Acyclic Graph (DAG).
    Uses Kahn's algorithm for topological sorting.
    Returns True if the graph is a DAG, False otherwise.
    """
    if not nodes or not edges:
        return True  # Empty graph or no edges is considered a DAG
    
    # Create a set of node IDs for quick lookup
    node_ids = {node.id for node in nodes}
    
    # Build adjacency list and in-degree count
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Initialize in-degree for all nodes
    for node in nodes:
        in_degree[node.id] = 0
    
    # Build the graph from edges
    for edge in edges:
        source = edge.source
        target = edge.target
        
        # Only process edges where both nodes exist
        if source in node_ids and target in node_ids:
            graph[source].append(target)
            in_degree[target] += 1
    
    # Find all nodes with no incoming edges
    queue = deque([node_id for node_id in node_ids if in_degree[node_id] == 0])
    processed_count = 0
    
    # Process nodes
    while queue:
        current = queue.popleft()
        processed_count += 1
        
        # Reduce in-degree for all neighbors
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If we processed all nodes, it's a DAG
    # If not, there's a cycle
    return processed_count == len(node_ids)

@app.post('/pipelines/parse')
def parse_pipeline(pipeline: PipelineRequest):
    """
    Parse the pipeline and return node count, edge count, and DAG status.
    """
    nodes = pipeline.nodes
    edges = pipeline.edges
    
    num_nodes = len(nodes)
    num_edges = len(edges)
    is_dag_result = is_dag(nodes, edges)
    
    return {
        'num_nodes': num_nodes,
        'num_edges': num_edges,
        'is_dag': is_dag_result
    }
