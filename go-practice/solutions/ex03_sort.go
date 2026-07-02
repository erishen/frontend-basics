package solutions

// QuickSort 快速排序（原地）
func QuickSort(arr []int) {
	quickSort(arr, 0, len(arr)-1)
}

func quickSort(arr []int, lo, hi int) {
	if lo >= hi {
		return
	}
	pivot := arr[lo+(hi-lo)/2]
	i, j := lo, hi
	for i <= j {
		for arr[i] < pivot {
			i++
		}
		for arr[j] > pivot {
			j--
		}
		if i <= j {
			arr[i], arr[j] = arr[j], arr[i]
			i++
			j--
		}
	}
	quickSort(arr, lo, j)
	quickSort(arr, i, hi)
}

// MergeSort 归并排序（返回新切片）
func MergeSort(arr []int) []int {
	result := make([]int, len(arr))
	copy(result, arr)
	mergeSort(result, 0, len(result)-1)
	return result
}

func mergeSort(arr []int, lo, hi int) {
	if lo >= hi {
		return
	}
	mid := lo + (hi-lo)/2
	mergeSort(arr, lo, mid)
	mergeSort(arr, mid+1, hi)
	merge(arr, lo, mid, hi)
}

func merge(arr []int, lo, mid, hi int) {
	tmp := make([]int, hi-lo+1)
	i, j, k := lo, mid+1, 0
	for i <= mid && j <= hi {
		if arr[i] <= arr[j] {
			tmp[k] = arr[i]
			i++
		} else {
			tmp[k] = arr[j]
			j++
		}
		k++
	}
	for i <= mid {
		tmp[k] = arr[i]
		i++
		k++
	}
	for j <= hi {
		tmp[k] = arr[j]
		j++
		k++
	}
	copy(arr[lo:hi+1], tmp)
}

// HeapSort 堆排序（原地）
func HeapSort(arr []int) {
	n := len(arr)
	for i := n/2 - 1; i >= 0; i-- {
		heapify(arr, n, i)
	}
	for i := n - 1; i > 0; i-- {
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, i, 0)
	}
}

func heapify(arr []int, n, i int) {
	largest := i
	left, right := 2*i+1, 2*i+2
	if left < n && arr[left] > arr[largest] {
		largest = left
	}
	if right < n && arr[right] > arr[largest] {
		largest = right
	}
	if largest != i {
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, n, largest)
	}
}
