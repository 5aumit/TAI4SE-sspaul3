
package test.problems;

import java.util.ArrayList;
import java.util.List;

public class StringPermute {
   //holder for permuted strings
	private StringBuilder out = new StringBuilder();
	
	//flag for check if the position is already in permuted string
	private boolean[] used;
	
	//input String
	private String in;
	
	public StringPermute( final String str ){
		in = str;
		used = new boolean[ in.length() ];
	}
	public void permute( ){
		//if we have passed the last position of the input string, return
		if( out.length() == in.length() ){
			System.out.println( out );
			return;
		}
		//for each character in the input
		for( int i = 0; i < in.length(); ++i ){
			//if already marked then skip
			if( used[i] ) 
				continue;
			//otherwise put the character in current position of permuted string
			out.append( in.charAt(i) );
			//mark the position as visited
			used[i] = true;
			//permute remaining characters
			permute();
			//unmark the position
			used[i] = false;
			//clear the permuted string to start over again
			out.setLength( out.length() - 1 );
		}
	}
	
	public void permuteAnotherWay(String prefix, String str){
		int n = str.length();
		if (n == 0)
			System.out.println(prefix);
		else {
			for (int i = 0; i < n; i++)
				permuteAnotherWay(prefix + str.charAt(i), str.substring(0, i) + str.substring(i + 1, n));
		}
	}
	
	public void permuteBySwap(String str){
		char[] input = str.toCharArray();
		int start = 0;
		int end = str.length();
		permuteBySwap(input,start,end);
	}
	private void permuteBySwap(char[] input, int start, int end) {
		if(start == end){
			System.out.println(new String(input));
		}
		else{
			//swap start and i
			for(int i=start;i<end;i++){
				char temp = input[start];
				input[start] = input[i];
				input[i] = temp;
				permuteBySwap(input, start+1, end);
			}
			
		}
		
	}
	public void permuteWithoutRecursion(String input){
		char[] inputChars = input.toCharArray();
		List output = new ArrayList();
		//add first character to the output list
		output.add(""+inputChars[0]);
		//loop over the remaining elements in the input array
		for(int i=1;i<inputChars.length;i++){
			//get the next char in the input array
			char next = inputChars[i];
			int sizeOfList = output.size();
			//loop over the list
			for(int j=0;j<sizeOfList;j++){
				//remove current element from list
				String str = (String)output.remove(0);
				for(int k=0;k<=str.length();k++){
					//add the next character between each character in the permuted string
					//eg: for abc... b is next character. so two string ba and ab will be added to list now
					output.add(str.substring(0, k)+next+str.substring(k));
				}
			}
		}
		//the output list contains the permuted string
		System.out.println(output);
		
	}
	public static void main(String args[]){
		StringPermute p = new StringPermute("abc");
		/*System.out.println("Permutation with recursion:");
		p.permute();
		System.out.println("Permutation without recursion:");
		p.permuteWithoutRecursion("abc");
		System.out.println("Permute another way");
		p.permuteAnotherWay("", "abc");*/
		
		p.permuteBySwap("abc");
	}


}
