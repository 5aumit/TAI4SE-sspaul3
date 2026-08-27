package com.nateriver.app.quiz;


import java.util.concurrent.ThreadPoolExecutor;

public class FindMissingNumber {

    /**
     * in case find one missing number, number is start from 1
     */

    static int findOneMissingNumber(int a[]) {
        int number = 0;
        int size = a.length;
        for (int i = 0; i < size; i++)
            number ^= ((i + 1) ^ a[i]);
        number ^= (size + 1);
        return number;
    }

    /**
     * in case find two missing number, number is start from 1
     */
    static void findTwoMissingNumber(int a[]) {
        int miss1 = 0;
        int miss2;
        int miss1miss2 = 0;

        int size = a.length;
        for (int i = 0; i < size; i++) {
            miss1miss2 ^= ((i + 1) ^ a[i]);
        }

        miss1miss2 ^= (size + 1);
        miss1miss2 ^= (size + 2);

        int diff = miss1miss2 & (-miss1miss2);

        for (int i = 0; i < size; i++) {
            if (((i + 1) & diff) > 0)
                miss1 ^= (i + 1);

            if ((a[i] & diff) > 0)
                miss1 ^= a[i];
        }

        if (((size + 1) ^ diff) > 0)
            miss1 ^= (size + 1);

        if (((size + 2) ^ diff) > 0)
            miss1 ^= (size + 2);

        miss2 = miss1miss2 ^ miss1;

        System.out.println(miss1);
        System.out.println(miss2);
    }

    public static void main(String[] args) throws Exception {
        int[] a = new int[]{1, 2, 5, 3, 6, 7};
        System.out.println(FindMissingNumber.findOneMissingNumber(a));
        FindMissingNumber.findTwoMissingNumber(a);

    }


}
