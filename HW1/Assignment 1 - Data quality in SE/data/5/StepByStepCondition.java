package GeeksForGeeks;

public class StepByStepCondition {
    public static void main(String[] args) {
        FastReader fs = new FastReader();
        int t = fs.nextInt();

        while(t-- > 0){
            String value = "";
            int n = fs.nextInt();
            if(n%2 !=0 && n%3!=0 && n%11!=0){
                value = "-1";
            }
            else {
                if (n % 2 == 0) {
                    value = "Two";
                }
                if (n % 3 == 0) {
                    value = "Three";
                }
                if (n % 11 == 0) {
                    value = "Eleven";
                }
            }
            System.out.println(value);
        }
    }
}
