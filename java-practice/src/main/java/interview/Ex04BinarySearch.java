package interview;

/**
 * 二分查找
 * 标准查找 + 找第一个/最后一个位置
 */
public class Ex04BinarySearch {

    public static int search(int[] arr, int target) {
        // TODO: 标准二分查找，返回索引，不存在返回 -1
        int lo = 0, hi = arr.length - 1;
        while(lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if(arr[mid] == target) return mid;
            else if(arr[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return -1;
    }

    public static int findFirst(int[] arr, int target) {
        // TODO: 找第一个等于 target 的位置
        int lo = 0, hi = arr.length - 1, result = -1;
        while(lo <= hi){
            int mid = lo + (hi - lo) / 2;
            if(arr[mid] == target) { result = mid; hi = mid - 1; }
            else if(arr[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return result;
    }

    public static int findLast(int[] arr, int target) {
        // TODO: 找最后一个等于 target 的位置
        int lo = 0, hi = arr.length - 1, result = -1;
        while(lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if(arr[mid] == target) { result = mid; lo = mid + 1; }
            else if(arr[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return result;
    }
}
