public class Solution {
    public int numDecodings(String s) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (s == null || s.length() == 0)
            return 0;
        
        int arr[] = new int[s.length()];
        
        for(int i = 0; i < arr.length; i++)
            arr[i] = -1;
        
        return recur(s, 0, arr);
    }
    
    private int recur(String s, int index, int arr[]) {
        if (index > s.length() - 1)
            return 1;
        
        if (s.charAt(index) == '0')
            return 0;
        
        if (index == s.length() - 1)
            return 1;
        
        if (arr[index] != -1)
            return arr[index];
        
        int wayNum = 0;
        
        wayNum += recur(s, index + 1, arr);
        
        int num = Integer.parseInt(s.substring(index, index + 2));
        if (num <= 26)
            wayNum += recur(s, index + 2, arr);
        
        arr[index] = wayNum;
        
        return wayNum;
    }
}
