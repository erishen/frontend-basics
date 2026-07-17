// LeetCode 53 · 简单
// 最大子数组和（Kadane）
// 返回连续子数组的最大和（子数组至少含一个元素）。
// TODO: 实现 maxSubArray

function maxSubArray(nums) {
  let best = nums[0];
  let cur = nums[0];
  for (let i = 1; i < nums.length; i++) {
    cur = Math.max(nums[i], cur + nums[i]); // 接上 or 从当前元素重新开始
    best = Math.max(best, cur);
  }
  return best;
}

module.exports = maxSubArray;
