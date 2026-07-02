package interview;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import interview.Ex03Sort;

class Ex03SortTest {

    @Test
    void quickSortNormal() {
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, Ex03Sort.quickSort(new int[]{3, 1, 4, 5, 2}));
    }

    @Test
    void mergeSortNormal() {
        assertArrayEquals(new int[]{1, 1, 3, 4, 5}, Ex03Sort.mergeSort(new int[]{3, 1, 4, 1, 5}));
    }

    @Test
    void heapSortNormal() {
        assertArrayEquals(new int[]{-3, -2, -1, 0, 2}, Ex03Sort.heapSort(new int[]{-3, -1, -2, 0, 2}));
    }

    @Test
    void emptyArray() {
        assertArrayEquals(new int[]{}, Ex03Sort.quickSort(new int[]{}));
        assertArrayEquals(new int[]{}, Ex03Sort.mergeSort(new int[]{}));
        assertArrayEquals(new int[]{}, Ex03Sort.heapSort(new int[]{}));
    }

    @Test
    void singleElement() {
        assertArrayEquals(new int[]{1}, Ex03Sort.quickSort(new int[]{1}));
    }

    @Test
    void duplicates() {
        assertArrayEquals(new int[]{5, 5, 5}, Ex03Sort.quickSort(new int[]{5, 5, 5}));
    }
}
