package solutions

import "unicode"

// ReverseString 反转字符串（支持 Unicode）
func ReverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

// IsPalindrome 判断回文（忽略大小写和非字母数字）
func IsPalindrome(s string) bool {
	runes := []rune{}
	for _, c := range s {
		if unicode.IsLetter(c) || unicode.IsDigit(c) {
			runes = append(runes, unicode.ToLower(c))
		}
	}
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		if runes[i] != runes[j] {
			return false
		}
	}
	return true
}

// LongestSubstringWithoutRepeat 最长无重复子串长度
func LongestSubstringWithoutRepeat(s string) int {
	lastIdx := make(map[rune]int)
	maxLen := 0
	start := 0
	for i, c := range s {
		if prev, ok := lastIdx[c]; ok && prev >= start {
			start = prev + 1
		}
		lastIdx[c] = i
		if i-start+1 > maxLen {
			maxLen = i - start + 1
		}
	}
	return maxLen
}
