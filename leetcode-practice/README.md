# leetcode-practice

LeetCode 算法题练习区（JavaScript 实现，沿用 `coding-practice` 同构）。
每题三件套：`src/` 练习模板（带 `// TODO`）+ `tests/` 验收用例 + `solutions/` 参考答案。

> 配套速查：[`../leetcode-brief.md`](../leetcode-brief.md)（每题思路 + 复杂度 + 易错点）

## 目录（中等 · Medium）

| # | 文件 | 题目 | 考点 |
|---|------|------|------|
| 01 | `01-longest-substring` | 3. 无重复字符的最长子串 | 滑动窗口 |
| 02 | `02-longest-palindrome` | 5. 最长回文子串 | 中心扩展 |
| 03 | `03-three-sum` | 15. 三数之和 | 排序 + 双指针 |
| 04 | `04-letter-combinations` | 17. 电话号码的字母组合 | 回溯 / 迭代 |
| 05 | `05-generate-parentheses` | 22. 括号生成 | 回溯 |
| 06 | `06-permutations` | 46. 全排列 | 回溯 |
| 07 | `07-course-schedule` | 207. 课程表 | 拓扑排序 / 环检测 |
| 08 | `08-number-of-islands` | 200. 岛屿数量 | DFS/BFS 网格 |
| 09 | `09-product-except-self` | 238. 除自身以外数组的乘积 | 前后缀分解 |
| 10 | `10-word-search` | 79. 单词搜索 | 回溯 + 标记 |

## 目录（简单 · Easy 热身）

| # | 文件 | 题目 | 考点 |
|---|------|------|------|
| 11 | `11-two-sum` | 1. 两数之和 | 哈希表 |
| 12 | `12-valid-parentheses` | 20. 有效的括号 | 栈 |
| 13 | `13-climbing-stairs` | 70. 爬楼梯 | 动态规划（滚动数组） |
| 14 | `14-max-subarray` | 53. 最大子数组和 | 贪心 / Kadane |
| 15 | `15-contains-duplicate` | 217. 存在重复元素 | 哈希集合 |
| 16 | `16-valid-anagram` | 242. 有效的字母异位词 | 计数 / 哈希表 |

## 用法

无需安装任何依赖（用 Node 自带测试运行器，>=18 即可）：

```bash
cd leetcode-practice
node --test tests/*.test.js      # 跑全部
# 或单题：node --test tests/01-longest-substring.test.js
```

1. 在 `src/01-xxx.js` 里把 `throw new Error("TODO: 请实现")` 换成你的实现；
2. 跑测试看是否通过；
3. 卡住了看 `solutions/01-xxx.js` 对照。

## 验证方式

测试用例用的就是 LeetCode 官方示例输入/输出。想确认参考答案全绿，可临时把 `solutions` 拷到 `src` 再跑：

```bash
cp solutions/*.js src/ && node --test tests/*.test.js && git checkout src/   # 仅验证用，别提交
```
