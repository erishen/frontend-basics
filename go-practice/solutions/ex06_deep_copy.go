package solutions

// DeepCopySlice 深拷贝 int 切片
func DeepCopySlice(src []int) []int {
	if src == nil {
		return nil
	}
	dst := make([]int, len(src))
	copy(dst, src)
	return dst
}

// DeepCopyMap 深拷贝 map[string][]int
func DeepCopyMap(src map[string][]int) map[string][]int {
	if src == nil {
		return nil
	}
	dst := make(map[string][]int, len(src))
	for k, v := range src {
		dst[k] = DeepCopySlice(v)
	}
	return dst
}
