// LeetCode 53 · 简单
// 最大子数组和（Kadane）
// 返回连续子数组的最大和（子数组至少含一个元素）。
// TODO: 实现 maxSubArray

function maxSubArray(nums) {
  // TODO: 在这里实现
  let best = nums[0]
  let cur = nums[0]
  for (let i = 1; i < nums.length; i++) {
    cur = Math.max(nums[i], cur + nums[i])
    best = Math.max(best, cur)
  }
  return best
}

module.exports = maxSubArray;
