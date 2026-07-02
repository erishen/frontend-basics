package solutions;

public class Ex03Sort {

    public static int[] quickSort(int[] arr) {
        int[] result = arr.clone();
        quickSort(result, 0, result.length - 1);
        return result;
    }

    private static void quickSort(int[] arr, int lo, int hi) {
        if (lo >= hi) return;
        int pivot = arr[lo + (hi - lo) / 2];
        int i = lo, j = hi;
        while (i <= j) {
            while (arr[i] < pivot) i++;
            while (arr[j] > pivot) j--;
            if (i <= j) {
                int tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
                i++; j--;
            }
        }
        quickSort(arr, lo, j);
        quickSort(arr, i, hi);
    }

    public static int[] mergeSort(int[] arr) {
        int[] result = arr.clone();
        mergeSort(result, 0, result.length - 1);
        return result;
    }

    private static void mergeSort(int[] arr, int lo, int hi) {
        if (lo >= hi) return;
        int mid = lo + (hi - lo) / 2;
        mergeSort(arr, lo, mid);
        mergeSort(arr, mid + 1, hi);
        merge(arr, lo, mid, hi);
    }

    private static void merge(int[] arr, int lo, int mid, int hi) {
        int[] tmp = new int[hi - lo + 1];
        int i = lo, j = mid + 1, k = 0;
        while (i <= mid && j <= hi) {
            tmp[k++] = arr[i] <= arr[j] ? arr[i++] : arr[j++];
        }
        while (i <= mid) tmp[k++] = arr[i++];
        while (j <= hi) tmp[k++] = arr[j++];
        System.arraycopy(tmp, 0, arr, lo, tmp.length);
    }

    public static int[] heapSort(int[] arr) {
        int[] result = arr.clone();
        int n = result.length;
        for (int i = n / 2 - 1; i >= 0; i--) heapify(result, n, i);
        for (int i = n - 1; i > 0; i--) {
            int tmp = result[0]; result[0] = result[i]; result[i] = tmp;
            heapify(result, i, 0);
        }
        return result;
    }

    private static void heapify(int[] arr, int n, int i) {
        int largest = i;
        int left = 2 * i + 1, right = 2 * i + 2;
        if (left < n && arr[left] > arr[largest]) largest = left;
        if (right < n && arr[right] > arr[largest]) largest = right;
        if (largest != i) {
            int tmp = arr[i]; arr[i] = arr[largest]; arr[largest] = tmp;
            heapify(arr, n, largest);
        }
    }
}
