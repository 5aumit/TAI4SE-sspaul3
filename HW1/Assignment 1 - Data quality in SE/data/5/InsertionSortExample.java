import java.util.Arrays;

public class InsertionSortExample
{
    public static void main(String[] args)
    {
        int temp;
        int arr[] = {12, 9, 3, 20, 30, 1};

        System.out.println(Arrays.toString(arr));
        System.out.println();

        for (int x = 0; x < arr.length-1; x++)
        {
            System.out.println("Iterasi ke-"+(x+1));

            for (int y = 0; y < arr.length;y++);
            for(int y = x+1; y > 0; y--)
            {
                if(arr[y] < arr[y-1])
                {
                    temp = arr[y];
                    arr[y] = arr[y-1];
                    arr[y-1] = temp;
                }
                System.out.println(Arrays.toString(arr));
            }
            System.out.println();
        }
        System.out.println("Hasil akhir :"+ Arrays.toString(arr));
    }
}
