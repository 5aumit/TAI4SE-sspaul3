package org.sample.graph;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class DirectedGraph {

	private List<Long> visited = new ArrayList<Long>();
	private Stack<Vertex<Integer>> stack = new Stack<Vertex<Integer>>();
	
	public void getAllPaths(Graph<Integer> graph) {
		
		// get any one topologically sorted path
		TopologicalSort obj = new TopologicalSort();
		Stack<Vertex<Integer>> result = obj.sort(graph);
		
		// source (one or multiple) must lie at the top
		while(!result.isEmpty()) {
			Vertex<Integer> currentVertex = result.pop();
			
			if(visited.contains(currentVertex.getId())) {
				continue;
			}
			
			stack = new Stack<Vertex<Integer>>();
			System.out.println("Paths: ");
			visited = new ArrayList<Long>();
			dfs(currentVertex);
			//System.out.println(stack);
			//GraphUtil.print(stack);			
		}

	}
	

	// dfs
	public void dfs(Vertex<Integer> vertex) {
		
		visited.add(vertex.getId());
		stack.push(vertex);
		
		if(vertex.getAdjacentVertexes().size() == 0) {
			//System.out.println(visited);
			System.out.println(stack);
			return; // reached vertex that doesn't have any other outgoing paths
		}

		
		for(Vertex<Integer> currentVertex : vertex.getAdjacentVertexes()) {
			if(stack.contains(currentVertex.getId())) { // to prevent cycle
				continue;
			}
			dfs(currentVertex);
			stack.pop();
		}
		
		
	}
	

	public static void main(String[] args) {
		
		Graph<Integer> graph = new Graph<Integer>(true);
		graph.addEdge(1,  3);
		graph.addEdge(2,  3);
		graph.addEdge(2,  4);
		graph.addEdge(3,  5);
		graph.addEdge(4,  6);
		graph.addEdge(5,  6);
		graph.addEdge(6,  7);
		
		DirectedGraph obj = new DirectedGraph();
		obj.getAllPaths(graph);
		
	}
	
}
