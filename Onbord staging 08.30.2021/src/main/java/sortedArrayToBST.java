//For Java and Python;
//
//        Write a code to Convert sorted array to balanced binary search tree.

public class sortedArrayToBST {

    public TreeNode sortedArrayToBST(int[] num) {
        if (num==null || num.length == 0) {
            return null;
        }
        TreeNode head = helper(num, 0, num.length - 1);
        return head;
    }

    public TreeNode helper(int[] num, int low, int high) {
        if (low > high) { // Done
            return null;
        }
        int mid = (low + high) / 2;
        TreeNode node = new TreeNode(num[mid]);
        node.left = helper(num, low, mid - 1);
        node.right = helper(num, mid + 1, high);
        return node;
    }
 

    public static void main(String args[]){
        int[] num = {1,2,3,4,5,6,7,8};
        sortedArrayToBST Bst = new sortedArrayToBST();
        Bst.sortedArrayToBST(num);
    }
}
