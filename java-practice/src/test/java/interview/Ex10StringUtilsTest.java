package interview;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import interview.Ex10StringUtils;

class Ex10StringUtilsTest {

    @Test
    void reverse() {
        assertEquals("olleh", Ex10StringUtils.reverse("hello"));
        assertEquals("", Ex10StringUtils.reverse(""));
        assertNull(Ex10StringUtils.reverse(null));
    }

    @Test
    void isPalindrome() {
        assertTrue(Ex10StringUtils.isPalindrome("A man a plan a canal Panama"));
        assertTrue(Ex10StringUtils.isPalindrome("racecar"));
        assertFalse(Ex10StringUtils.isPalindrome("hello"));
    }

    @Test
    void longestSubstring() {
        assertEquals(3, Ex10StringUtils.longestSubstringWithoutRepeat("abcabcbb"));
        assertEquals(1, Ex10StringUtils.longestSubstringWithoutRepeat("bbbbb"));
        assertEquals(0, Ex10StringUtils.longestSubstringWithoutRepeat(""));
    }
}
