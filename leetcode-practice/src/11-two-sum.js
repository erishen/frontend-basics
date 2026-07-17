// LeetCode 1 · 简单
// 两数之和
// 给定 nums 与目标 target，返回和为 target 的两个下标（可任意顺序）。
// 假定恰有一个答案，且同一个元素不能用两次。
// TODO: 实现 twoSum

function twoSum(nums, target) {
  // TODO: 在这里实现
  const seen = new Map()
  for(let i = 0; i < nums.length; i++) {
    const need = target - nums[i];
    if (seen.has(need)) return [seen.get(need), i];
    seen.set(nums[i], i);
  }
  return []
}

module.exports = twoSum;
