package Assignment2;

public class Quest02_f {

	public static void main(String[] args) {
		System.out.println("The original array is: ");
        int a[] = {16,4,20,20,7,99,21,56,12,10};  
       for (int i = 0; i < a.length; i++)
        {
            System.out.print(a[i]+" ");
        }
		System.out.println("\nThe new array is: ");
	int[] lol = array_sort(a);
	
	for (int i = 0; i < a.length-1; i++)
	{
		System.out.print(lol[i]+" ");
		
	}
}
    public static int[] array_sort(int[] a) {
        int[] sortedArray = new int[a.length];
        int index = 1;
        for (int i = 1; i < a.length; i++) {
            if (a[i] != a[index-1])
                a[index++] = a[i];
            sortedArray = a;

        }
	  return sortedArray;
    }
}