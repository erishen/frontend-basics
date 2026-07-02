package interview;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import interview.Ex04BinarySearch;

class Ex04BinarySearchTest {

    @Test
    void found() {
        assertEquals(2, Ex04BinarySearch.search(new int[]{1, 3, 5, 7, 9}, 5));
    }

    @Test
    void notFound() {
        assertEquals(-1, Ex04BinarySearch.search(new int[]{1, 3, 5, 7, 9}, 4));
    }

    @Test
    void empty() {
        assertEquals(-1, Ex04BinarySearch.search(new int[]{}, 1));
    }

    @Test
    void findFirst() {
        assertEquals(1, Ex04BinarySearch.findFirst(new int[]{1, 2, 2, 2, 3}, 2));
    }

    @Test
    void findLast() {
        assertEquals(3, Ex04BinarySearch.findLast(new int[]{1, 2, 2, 2, 3}, 2));
    }

    @Test
    void findFirstNotFound() {
        assertEquals(-1, Ex04BinarySearch.findFirst(new int[]{1, 3, 5}, 2));
    }
}
