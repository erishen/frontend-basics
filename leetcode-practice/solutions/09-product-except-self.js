// LeetCode 238 · 中等
// 除自身以外数组的乘积（前后缀分解）

function productExceptSelf(nums) {
  const n = nums.length;
  const res = new Array(n).fill(1);
  let prefix = 1;
  for (let i = 0; i < n; i++) {
    res[i] = prefix;
    prefix *= nums[i];
  }
  let suffix = 1;
  for (let i = n - 1; i >= 0; i--) {
    res[i] *= suffix;
    suffix *= nums[i];
  }
  // 归一化 -0：JS 里 `0 * 负数` 会得到 -0，而 deepStrictEqual 区分 -0 与 0
  return res.map((v) => (v === 0 ? 0 : v));
}

module.exports = productExceptSelf;
