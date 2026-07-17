// LeetCode 46 · 中等
// 全排列（回溯）

function permutations(nums) {
  const res = [];
  const n = nums.length;
  const used = new Array(n).fill(false);
  const backtrack = (path) => {
    if (path.length === n) {
      res.push([...path]);
      return;
    }
    for (let i = 0; i < n; i++) {
      if (used[i]) continue;
      used[i] = true;
      path.push(nums[i]);
      backtrack(path);
      path.pop();
      used[i] = false;
    }
  };
  backtrack([]);
  return res;
}

module.exports = permutations;
