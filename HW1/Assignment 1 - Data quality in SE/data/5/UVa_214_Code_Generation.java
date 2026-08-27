package Competitive_Programming_Book.Chapter1.TimeWaster;

import java.io.*;
import java.util.*;
import java.lang.*;

public class UVa_214_Code_Generation {

    static String binaryOps = "+-/*";
    static String unaryOps = "@";

    static Map<Character, Character> opsMap = new HashMap<>();


    public static void main(String[] args) throws FileNotFoundException {

//        FileOutputStream output=new FileOutputStream("test.out");
//        PrintStream out = new PrintStream(output);
//        System.setOut(out);

//        InputStream input=new FileInputStream("test.in");
//        System.setIn(input);

        opsMap.put('+', 'A');
        opsMap.put('-', 'S');
        opsMap.put('*', 'M');
        opsMap.put( '/', 'D');
        opsMap.put('@', 'N');

        Scanner sc = new Scanner(System.in); boolean pula = true;

        while (sc.hasNext()) {
            if (pula) {
                pula = false;
            } else {
                System.out.println();
            }

            String line = sc.nextLine();

            boolean registerEmpty = true;
            int firstUnusedMemPos = 0;

            for (int k = 0; k < line.length(); k++) {
                char curr = line.charAt(k);
                if (!binaryOps.contains(curr + "") && !unaryOps.contains(curr + "")) {
                    // expression
                    if (registerEmpty) {
                        registerEmpty = false;
                        System.out.println("L " + curr);
                    } else {
                        if ((k < line.length() - 1) && binaryOps.contains("" + line.charAt(k+1))) {
                            // TODO fix unary op
                            // doing op
                            System.out.println(opsMap.get(line.charAt(k+1)) + " " + curr);
                            k++; // We store on next loop, if needed at all
                        } else {
                                // adding new primitives
                                System.out.println("ST $" + firstUnusedMemPos); firstUnusedMemPos++;
                                System.out.println("L " + curr);
                        }
                    }
                } else if (unaryOps.contains("" + curr)) {
                    System.out.println("N");
                 } else {
                    // if we get here we need to execute op with register
                    firstUnusedMemPos--;
                    if (curr != '+' && curr != '*') {
                        // then we need to flip the order.
                        if (curr != '-') {
                            System.out.println("ST $"+ (firstUnusedMemPos + 1));
                            System.out.println("L $" + firstUnusedMemPos);
                            System.out.println(opsMap.get(curr) + " $"+ (firstUnusedMemPos + 1));
                        } else {
                            System.out.println("N");
                            System.out.println("A $"+ (firstUnusedMemPos));
                        }
                    } else System.out.println(opsMap.get(curr) + " $"+ firstUnusedMemPos);
                }

            }
        }
    }

}
