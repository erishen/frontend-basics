// LeetCode 207 · 中等
// 课程表（BFS 拓扑排序，检测有向环）

function canFinish(numCourses, prerequisites) {
  const adj = Array.from({ length: numCourses }, () => []);
  const indegree = new Array(numCourses).fill(0);
  for (const [course, pre] of prerequisites) {
    adj[pre].push(course);
    indegree[course]++;
  }
  const queue = [];
  for (let c = 0; c < numCourses; c++) {
    if (indegree[c] === 0) queue.push(c);
  }
  let visited = 0;
  while (queue.length) {
    const node = queue.shift();
    visited++;
    for (const neighbor of adj[node]) {
      indegree[neighbor]--;
      if (indegree[neighbor] === 0) queue.push(neighbor);
    }
  }
  return visited === numCourses;
}

module.exports = canFinish;
