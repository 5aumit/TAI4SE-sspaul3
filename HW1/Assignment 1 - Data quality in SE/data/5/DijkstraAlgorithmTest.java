package dijkstra.test;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

import org.junit.Test;

import dijkstra.algorithm.DijkstraAlgorithm;
import dijkstra.model.Edge;
import dijkstra.model.Graph;
import dijkstra.model.Vertex;
public class DijkstraAlgorithmTest {
    private List<Vertex> nodes;
    private List<Edge> edges;
    
    @Test
    public void testExcute() {
        initialize();
        Graph graph = new Graph(nodes, edges);
        DijkstraAlgorithm dijkstra = new DijkstraAlgorithm(graph, nodes.get(0), nodes.get(5));
        dijkstra.execute();
        LinkedList<Vertex> path = dijkstra.getPath();
        
        assertNotNull(path);
        assertTrue(path.size() > 0);
        
        for(Vertex v : path) {
            System.out.println(v.toString());
        }
    }
    
    private void initialize() {
        nodes = new ArrayList<Vertex> ();
        edges = new ArrayList<Edge> ();
        
        for(int i=0; i< 6 ; i++) {
            nodes.add(new Vertex("Node_" + i, "Node_" + i));
        }
        
        edges.add(new Edge("edge_0", nodes.get(0),nodes.get(2),3));
        edges.add(new Edge("edge_1", nodes.get(0),nodes.get(1),2));
        edges.add(new Edge("edge_2", nodes.get(2),nodes.get(5),10));
        edges.add(new Edge("edge_3", nodes.get(2),nodes.get(3),2));
        edges.add(new Edge("edge_4", nodes.get(2),nodes.get(1),2));
        edges.add(new Edge("edge_5", nodes.get(1),nodes.get(3),5));
        edges.add(new Edge("edge_6", nodes.get(1),nodes.get(4),5));
        edges.add(new Edge("edge_7", nodes.get(3),nodes.get(4),3));
        edges.add(new Edge("edge_8", nodes.get(4),nodes.get(5),3));
        edges.add(new Edge("edge_9", nodes.get(3),nodes.get(5),1));
    }

}
