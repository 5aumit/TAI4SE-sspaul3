import java.util.Arrays;
import java.util.Scanner;
public class OverlappingIntervals {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int number = Integer.parseInt(scanner.nextLine());
        int[][] intervals = new int[number][2];
        for (int i = 0; i <number ; i++) {
            int[] rawIntervals = Arrays.stream(scanner.nextLine().split(",")).mapToInt(Integer::parseInt).toArray();
            intervals[i][0] = rawIntervals[0];
            intervals[i][1] = rawIntervals[1];
        }

        sortIntervals(intervals, 0);
        boolean overlap = isOverlapping(intervals);
        System.out.println(overlap);
    }

    private static boolean isOverlapping(int[][] intervals) {
        for (int i = 0; i <intervals.length-1 ; i++) {
            int intervalEnd = intervals[i][1];
            int nextIntervalStart = intervals[i+1][0];
            if (nextIntervalStart <= intervalEnd && intervals[i][0] < intervals[i+1][1]) {
                return true;
            }
        }
        return false;
    }

    private static void sortIntervals(int[][] intervals, int index) {
        if (index > intervals.length-1){
            return;
        }
        int indexIntervalStart = intervals[index][0];
        int minIndex = index;
        for (int i = index+1; i <intervals.length ; i++) {
            int currentIntervalStart = intervals[i][0];
            if (indexIntervalStart > currentIntervalStart) {
                minIndex = i;
            }
        }
        if (minIndex != index) {
            swapArray(intervals, minIndex, index);
        }
        sortIntervals(intervals, index+1);
    }

    private static void swapArray(int[][] intervals, int minIndex, int index) {
        int[] temp = intervals[index];
        intervals[index] = intervals[minIndex];
        intervals[minIndex] = temp;
    }

}
