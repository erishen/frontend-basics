package solutions;

import java.util.HashSet;
import java.util.Set;

public class Ex10StringUtils {

    public static String reverse(String s) {
        if (s == null) return null;
        char[] chars = s.toCharArray();
        int lo = 0, hi = chars.length - 1;
        while (lo < hi) {
            char tmp = chars[lo]; chars[lo] = chars[hi]; chars[hi] = tmp;
            lo++; hi--;
        }
        return new String(chars);
    }

    public static boolean isPalindrome(String s) {
        int lo = 0, hi = s.length() - 1;
        while (lo < hi) {
            while (lo < hi && !Character.isLetterOrDigit(s.charAt(lo))) lo++;
            while (lo < hi && !Character.isLetterOrDigit(s.charAt(hi))) hi--;
            if (Character.toLowerCase(s.charAt(lo)) != Character.toLowerCase(s.charAt(hi)))
                return false;
            lo++; hi--;
        }
        return true;
    }

    public static int longestSubstringWithoutRepeat(String s) {
        Set<Character> set = new HashSet<>();
        int max = 0, lo = 0;
        for (int hi = 0; hi < s.length(); hi++) {
            while (set.contains(s.charAt(hi))) {
                set.remove(s.charAt(lo));
                lo++;
            }
            set.add(s.charAt(hi));
            max = Math.max(max, hi - lo + 1);
        }
        return max;
    }
}
