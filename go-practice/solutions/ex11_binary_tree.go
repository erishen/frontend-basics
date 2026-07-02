package solutions

// TreeNode 二叉树节点
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// Preorder 前序遍历
func Preorder(root *TreeNode) []int {
	if root == nil {
		return nil
	}
	var result []int
	var stack []*TreeNode
	curr := root
	for curr != nil || len(stack) > 0 {
		for curr != nil {
			result = append(result, curr.Val)
			stack = append(stack, curr)
			curr = curr.Left
		}
		curr = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		curr = curr.Right
	}
	return result
}

// Inorder 中序遍历
func Inorder(root *TreeNode) []int {
	if root == nil {
		return nil
	}
	var result []int
	var stack []*TreeNode
	curr := root
	for curr != nil || len(stack) > 0 {
		for curr != nil {
			stack = append(stack, curr)
			curr = curr.Left
		}
		curr = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		result = append(result, curr.Val)
		curr = curr.Right
	}
	return result
}

// LevelOrder 层序遍历
func LevelOrder(root *TreeNode) [][]int {
	if root == nil {
		return nil
	}
	var result [][]int
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		size := len(queue)
		level := []int{}
		for i := 0; i < size; i++ {
			node := queue[i]
			level = append(level, node.Val)
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		result = append(result, level)
		queue = queue[size:]
	}
	return result
}
