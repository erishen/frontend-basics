package solutions

// BinarySearch 标准二分查找
func BinarySearch(arr []int, target int) int {
	lo, hi := 0, len(arr)-1
	for lo <= hi {
		mid := lo + (hi-lo)/2
		if arr[mid] == target {
			return mid
		} else if arr[mid] < target {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return -1
}

// FindFirst 找第一个等于 target 的位置
func FindFirst(arr []int, target int) int {
	lo, hi := 0, len(arr)-1
	result := -1
	for lo <= hi {
		mid := lo + (hi-lo)/2
		if arr[mid] == target {
			result = mid
			hi = mid - 1
		} else if arr[mid] < target {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return result
}

// FindLast 找最后一个等于 target 的位置
func FindLast(arr []int, target int) int {
	lo, hi := 0, len(arr)-1
	result := -1
	for lo <= hi {
		mid := lo + (hi-lo)/2
		if arr[mid] == target {
			result = mid
			lo = mid + 1
		} else if arr[mid] < target {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return result
}
