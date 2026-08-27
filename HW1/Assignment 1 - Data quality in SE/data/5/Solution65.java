class Solution65 {

    public static void main(String[] args) {
        if (args.length == 2) {
            testIsValidNumber(args[0], Boolean.valueOf(args[1]));
            System.out.println("Test case passed!");
        } else {
            testIsValidNumberWithDefaultData();
        }
    }

    public static void testIsValidNumberWithDefaultData() {
        testIsValidNumber("2", true);
        testIsValidNumber("2 ", true);
        testIsValidNumber(" ", false);
        testIsValidNumber("2,000", false);
        
        testIsValidNumber("2 2", false);
        testIsValidNumber("2e2", true);
        testIsValidNumber("2E2", false);
        testIsValidNumber("2e2.2", false);
        testIsValidNumber("e10", false);
        testIsValidNumber("e", false);
        testIsValidNumber("2e", false);
        testIsValidNumber("2e+2", true);
        testIsValidNumber("2e-2", true);

        testIsValidNumber("2.2", true);
        testIsValidNumber(".2", true);
        testIsValidNumber("2.", true);
        testIsValidNumber(".", false);
        testIsValidNumber(". 1", false);
        testIsValidNumber(".e", false);
        
        testIsValidNumber("-1.", true);
        testIsValidNumber("+1.", true);
        testIsValidNumber("-.", false);
        System.out.println("All test cases passed!");
    }

    public static void testIsValidNumber(String input, boolean expectedOutput) {
        boolean output = isValidNumber(input);
        assert output == expectedOutput: "isValidNumber() failed,\n"
            + "Input: " + input + "\n"
            + "Expected output: " + expectedOutput + "\n"
            + "Output: " + output;
    }

    public static boolean isValidNumber(String s) {
        boolean hasPoint = false;
        boolean hasE = false;
        boolean hasDigit = false;
        s = s.trim();

        for(int i = 0; i < s.length(); i++) {
            if (Character.isDigit(s.charAt(i))) {
                hasDigit = true;
            } else if (s.charAt(i) == '.') {
                if (hasPoint || hasE) { 
                    return false; 
                }
                hasPoint = true;
            } else if (s.charAt(i) == 'e') {
                if (hasE || !hasDigit) {
                    return false;
                }
                hasE = true;
                hasDigit = false;
            } else if ((s.charAt(i) == '-' || s.charAt(i) == '+') && (i == 0 || s.charAt(i-1) == 'e')) {
                continue;
            } else {
                return false;
            }
        }
        
        return hasDigit;
    }
}
