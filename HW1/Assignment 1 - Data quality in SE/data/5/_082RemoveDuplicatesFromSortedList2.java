package solutions;

/**
 * NO.82 Remove Duplicates from Sorted List II
 * Keywords:   Linked List
 * Difficulty: Medium
 * Company:
 */
public class _082RemoveDuplicatesFromSortedList2 {
    /**
     * 由于头节点可能也包含在重复的元素之内，所以需要判断头节点，因此需设立虚拟头节点
     * 设立一个判断的工作节点，如果该工作节点的下一位与它值相等，则工作节点指向它的下一位，直到遍历到与它不等的元素，退出循环
     * 这是工作节点work是重复节点的最后一位，这时需要让curr的下一个指针指向work.next位置，即完全去掉重复的元素
     */
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode curr = dummyHead;
        while( curr.next != null ){
            ListNode work = curr.next;
            boolean isDel = false;
            while( work.next != null && work.val == work.next.val){
                work = work.next;
                isDel = true;
            }
            //当退出循环时work指向的是重复元素的最后一个元素，这时需要指向它的下一个元素，即完全去掉重复的元素
            if(isDel == true){
                curr.next = work.next;
                isDel = false;
            }else
                curr = curr.next;
        }
        return dummyHead.next;
    }

    public static void main(String[] args) {
        int[] nums = {1,1,1,2,3,3,4,4,5,5,5,6};
        ListNode head = LinkedListTools.createLinkedList(nums);
        LinkedListTools.printLinkedList(head);
        _082RemoveDuplicatesFromSortedList2 r = new _082RemoveDuplicatesFromSortedList2();
        ListNode head1 = r.deleteDuplicates(head);
        LinkedListTools.printLinkedList(head1);
    }
}
