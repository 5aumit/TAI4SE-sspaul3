import java.util.*;

public class sort 
{
	
	@SuppressWarnings("rawtypes")
	public static void main(String[] args)
	{
		@SuppressWarnings("unchecked")
		List<Integer> list = new ArrayList();
		
		for(int k = 0 ; k < 50; k++) //creates 2080 random numbers
		{
			Random n = new Random();
			int Low = 1;
			int High = 41;
			int N = n.nextInt(High-Low) + Low; //creates a random number between 0-52, 2080 times. 52*40=2080
			list.add(N);
		}
		
		System.out.print(list+"\n");
		selectionSort(list);
		System.out.print(list);
	}
	
	public static void selectionSort(List<Integer> list) 
	{
		if (list == null)
			return;

		if (list.size() == 0 || list.size() == 1)
			return;

		int smallestIndex;

		int smallest;
		for (int curIndex = 0; curIndex < list.size(); curIndex++) 
		{

			smallest = list.get(curIndex);
			smallestIndex = curIndex;

			for (int i = curIndex + 1; i < list.size(); i++) 
			{
				if (smallest > list.get(i)) 
				{
					smallest = list.get(i);
					smallestIndex = i;
				}
			}

			if (smallestIndex == curIndex)
				;

			else 
			{
				int temp = list.get(curIndex);
				list.set(curIndex, list.get(smallestIndex));
				list.set(smallestIndex, temp);
			}

		}
	}
}
