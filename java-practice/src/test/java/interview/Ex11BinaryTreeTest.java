package interview;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import interview.Ex11BinaryTree;
import interview.Ex11BinaryTree.TreeNode;
import java.util.List;

class Ex11BinaryTreeTest {

    //       1
    //      / \
    //     2   3
    //    / \
    //   4   5
    private TreeNode buildTree() {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        return root;
    }

    @Test
    void inorder() {
        assertEquals(List.of(4, 2, 5, 1, 3), Ex11BinaryTree.inorderTraversal(buildTree()));
    }

    @Test
    void levelOrder() {
        assertEquals(List.of(1, 2, 3, 4, 5), Ex11BinaryTree.levelOrder(buildTree()));
    }

    @Test
    void maxDepth() {
        assertEquals(3, Ex11BinaryTree.maxDepth(buildTree()));
        assertEquals(0, Ex11BinaryTree.maxDepth(null));
    }
}
