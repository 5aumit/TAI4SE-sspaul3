import java.util.ArrayList;
import java.util.Collections;

public class ListDemo {
	
	public static void main(String[] args) {
		
		ArrayList<Integer> a = new ArrayList<Integer>();
		a.add(2);
		a.add(5);
		a.add(13);
		a.add(64);
		a.add(9);
		a.add(7);
		a.add(65);
		a.add(13);
		
		System.out.println(a.size());		//print size
		//System.out.println(a);
		Collections.sort(a);				//sorts list
		System.out.println(a);
		
		ArrayList<Integer> b = new ArrayList<Integer>();
		b.addAll(a);						//add all list a to b
		System.out.println(b);
		
		Collections.reverse(b);				//reverse list
		//System.out.println(b);
		
		Collections.swap(b, 0, 1);			//swap specified elements
		//System.out.println(b);
		
		
		System.out.println(b.indexOf(13));	//show index of element
		b.remove(2);						//remove element at nth index
		System.out.println(b);
	}
}


			