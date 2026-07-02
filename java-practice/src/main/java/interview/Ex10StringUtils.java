package interview;

/**
 * 字符串工具
 * 实现常用字符串操作（不用内置方法）
 */
public class Ex10StringUtils {

    public static String reverse(String s) {
        // TODO: 反转字符串
        if (s == null) return null;
        char[] chars = s.toCharArray();
        int lo = 0, hi = chars.length - 1;
        while(lo < hi) {
            char tmp = chars[lo]; chars[lo] = chars[hi]; chars[hi] = tmp;
            lo++; hi--;
        }
        return new String(chars);
    }

    public static boolean isPalindrome(String s) {
        // TODO: 判断回文（忽略大小写和非字母数字字符）
        int lo = 0, hi = s.length() - 1;
        while(lo < hi) {
            while(lo < hi && !Character.isLetterOrDigit(s.charAt(lo))) lo++;
            while(lo < hi && !Character.isLetterOrDigit(s.charAt(hi))) hi--;
            if(Character.toLowerCase(s.charAt(lo)) != Character.toLowerCase(s.charAt(hi)))
                return false;
            lo++; hi--;
        }
        return true;
    }

    public static int longestSubstringWithoutRepeat(String s) {
        // TODO: 最长无重复子串长度
        java.util.Set<Character> set = new java.util.HashSet<>();
        int max = 0, lo = 0;
        for(int hi = 0; hi < s.length(); hi++) {
            while(set.contains(s.charAt(hi))) {
                set.remove(s.charAt(lo));
                lo++;
            }
            set.add(s.charAt(hi));
            max = Math.max(max, hi - lo + 1);
        }
        return max;
    }
}
