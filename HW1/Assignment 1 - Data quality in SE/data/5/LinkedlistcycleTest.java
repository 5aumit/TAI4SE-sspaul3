package leetcode.linkedlistcycle;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class LinkedlistcycleTest {
    Solution sol;
    int[] input;
    int pos;
    boolean expected;


    ListNode initListNodes(int[] input, int pos) {
        if (pos == -1) return null;

        ListNode[] inputList = new ListNode[input.length];

        for (int i = 0; i < input.length; i++) {
            inputList[i] = new ListNode(input[i]);
            if (i != 0) inputList[i - 1].next = inputList[i];
        }


        inputList[input.length - 1].next = inputList[pos];

        return inputList[0];
    }

    @BeforeEach
    void setUp() {
        sol = new Solution();
    }

    @Test
    void hasCycle() {
        input = new int[]{3, 2, 0, -4};
        pos = 1;
        expected = true;

        ListNode inputNode = initListNodes(input, pos);

        assertEquals(expected, sol.hasCycle(inputNode));
    }

    @Test
    void hasCycle2() {
        input = new int[]{1, 2};
        pos = 0;
        expected = true;

        ListNode inputNode = initListNodes(input, pos);

        assertEquals(expected, sol.hasCycle(inputNode));
    }

    @Test
    void hasCycle3() {
        input = new int[]{1};
        pos = -1;
        expected = false;

        ListNode inputNode = initListNodes(input, pos);

        assertEquals(expected, sol.hasCycle(inputNode));
    }

    @Test
    void hasCycle4() {
        input = new int[]{};
        pos = -1;
        expected = false;

        ListNode inputNode = initListNodes(input, pos);

        assertEquals(expected, sol.hasCycle(inputNode));
    }
}