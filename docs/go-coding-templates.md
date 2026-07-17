# Go 面试手写代码模板

> 面试最高频的手写题，每题都是完整可运行的模板，多写几遍形成肌肉记忆。

---

## 1. LRU 缓存

```go
// 双向链表 + map，get/put 均 O(1)
type LRUCache struct {
	capacity int
	nodes    map[int]*Node
	head     *Node // 哨兵头
	tail     *Node // 哨兵尾
}

type Node struct {
	key, val int
	prev     *Node
	next     *Node
}

func Constructor(capacity int) LRUCache {
	head, tail := &Node{}, &Node{}
	head.next, tail.prev = tail, head
	return LRUCache{capacity: capacity, nodes: make(map[int]*Node), head: head, tail: tail}
}

func (c *LRUCache) Get(key int) int {
	node, ok := c.nodes[key]
	if !ok {
		return -1
	}
	c.moveToHead(node)
	return node.val
}

func (c *LRUCache) Put(key int, val int) {
	if node, ok := c.nodes[key]; ok {
		node.val = val
		c.moveToHead(node)
		return
	}
	node := &Node{key: key, val: val}
	c.nodes[key] = node
	c.addToHead(node)
	if len(c.nodes) > c.capacity {
		removed := c.removeTail()
		delete(c.nodes, removed.key)
	}
}

func (c *LRUCache) addToHead(n *Node) {
	n.prev, n.next = c.head, c.head.next
	c.head.next.prev, c.head.next = n, n
}

func (c *LRUCache) removeNode(n *Node) {
	n.prev.next, n.next.prev = n.next, n.prev
}

func (c *LRUCache) moveToHead(n *Node) {
	c.removeNode(n)
	c.addToHead(n)
}

func (c *LRUCache) removeTail() *Node {
	n := c.tail.prev
	c.removeNode(n)
	return n
}
```

---

## 2. 单例模式

```go
// sync.Once 保证只初始化一次，线程安全
var (
	once     sync.Once
	instance *Singleton
)

type Singleton struct {
	value string
}

func GetInstance() *Singleton {
	once.Do(func() {
		instance = &Singleton{value: "initialized"}
	})
	return instance
}
```

---

## 3. 排序算法

```go
// 快速排序（原地）
func QuickSort(arr []int) {
	quickSort(arr, 0, len(arr)-1)
}

func quickSort(arr []int, lo, hi int) {
	if lo >= hi {
		return
	}
	pivot := arr[lo+(hi-lo)/2]
	i, j := lo, hi
	for i <= j {
		for arr[i] < pivot {
			i++
		}
		for arr[j] > pivot {
			j--
		}
		if i <= j {
			arr[i], arr[j] = arr[j], arr[i]
			i++
			j--
		}
	}
	quickSort(arr, lo, j)
	quickSort(arr, i, hi)
}

// 归并排序（返回新切片）
func MergeSort(arr []int) []int {
	res := make([]int, len(arr))
	copy(res, arr)
	mergeSort(res, 0, len(res)-1)
	return res
}

func mergeSort(arr []int, lo, hi int) {
	if lo >= hi {
		return
	}
	mid := lo + (hi-lo)/2
	mergeSort(arr, lo, mid)
	mergeSort(arr, mid+1, hi)
	tmp := make([]int, hi-lo+1)
	i, j, k := lo, mid+1, 0
	for i <= mid && j <= hi {
		if arr[i] <= arr[j] {
			tmp[k] = arr[i]
			i++
		} else {
			tmp[k] = arr[j]
			j++
		}
		k++
	}
	for i <= mid {
		tmp[k] = arr[i]
		i++
		k++
	}
	for j <= hi {
		tmp[k] = arr[j]
		j++
		k++
	}
	copy(arr[lo:hi+1], tmp)
}

// 堆排序（原地）
func HeapSort(arr []int) {
	n := len(arr)
	for i := n/2 - 1; i >= 0; i-- {
		heapify(arr, n, i)
	}
	for i := n - 1; i > 0; i-- {
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, i, 0)
	}
}

func heapify(arr []int, n, i int) {
	largest := i
	if l := 2*i + 1; l < n && arr[l] > arr[largest] {
		largest = l
	}
	if r := 2*i + 2; r < n && arr[r] > arr[largest] {
		largest = r
	}
	if largest != i {
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, n, largest)
	}
}
```

---

## 4. 二分查找

```go
// 标准查找
func BinarySearch(arr []int, target int) int {
	lo, hi := 0, len(arr)-1
	for lo <= hi {
		mid := lo + (hi-lo)/2
		if arr[mid] == target {
			return mid
		} else if arr[mid] < target {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return -1
}

// 找第一个等于 target 的位置
func FindFirst(arr []int, target int) int {
	lo, hi, result := 0, len(arr)-1, -1
	for lo <= hi {
		mid := lo + (hi-lo)/2
		if arr[mid] == target {
			result = mid
			hi = mid - 1 // 继续往左找
		} else if arr[mid] < target {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return result
}

// 找最后一个等于 target 的位置
func FindLast(arr []int, target int) int {
	lo, hi, result := 0, len(arr)-1, -1
	for lo <= hi {
		mid := lo + (hi-lo)/2
		if arr[mid] == target {
			result = mid
			lo = mid + 1 // 继续往右找
		} else if arr[mid] < target {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return result
}
```

---

## 5. 线程安全计数器

```go
// Mutex 版本
type SafeCounter struct {
	mu    sync.Mutex
	value int
}

func (c *SafeCounter) Inc() {
	c.mu.Lock()
	c.value++
	c.mu.Unlock()
}

func (c *SafeCounter) Val() int {
	c.mu.Lock()
	defer c.mu.Unlock()
	return c.value
}

// atomic 版本（更轻量）
type AtomicCounter struct {
	value int64
}

func (c *AtomicCounter) Inc() {
	atomic.AddInt64(&c.value, 1)
}

func (c *AtomicCounter) Val() int64 {
	return atomic.LoadInt64(&c.value)
}
```

---

## 6. 深拷贝

```go
// 切片深拷贝
func DeepCopySlice(src []int) []int {
	if src == nil {
		return nil
	}
	dst := make([]int, len(src))
	copy(dst, src)
	return dst
}

// map 深拷贝（value 是切片）
func DeepCopyMap(src map[string][]int) map[string][]int {
	if src == nil {
		return nil
	}
	dst := make(map[string][]int, len(src))
	for k, v := range src {
		dst[k] = DeepCopySlice(v)
	}
	return dst
}
```

---

## 7. 生产者-消费者

```go
// channel + goroutine 经典模型
func ProducerConsumer(n int) int {
	ch := make(chan int)
	done := make(chan struct{})

	// 生产者 goroutine
	go func() {
		for i := 1; i <= n; i++ {
			ch <- i
		}
		close(ch) // 生产完毕，关闭 channel
	}()

	// 消费者（主 goroutine）
	sum := 0
	go func() {
		for v := range ch { // range 自动在 channel 关闭后退出
			sum += v
		}
		close(done)
	}()

	<-done // 等待消费完成
	return sum
}
```

---

## 8. 哈希表（拉链法）

```go
type HashMap struct {
	buckets [][]kvPair
	size    int
}

type kvPair struct {
	key string
	val int
}

func NewHashMap(size int) *HashMap {
	return &HashMap{buckets: make([][]kvPair, size), size: size}
}

func (m *HashMap) hash(key string) int {
	h := 0
	for _, c := range key {
		h = h*31 + int(c)
	}
	if h < 0 {
		h = -h
	}
	return h % m.size
}

func (m *HashMap) Put(key string, val int) {
	idx := m.hash(key)
	for i, p := range m.buckets[idx] {
		if p.key == key {
			m.buckets[idx][i].val = val
			return
		}
	}
	m.buckets[idx] = append(m.buckets[idx], kvPair{key, val})
}

func (m *HashMap) Get(key string) (int, bool) {
	for _, p := range m.buckets[m.hash(key)] {
		if p.key == key {
			return p.val, true
		}
	}
	return 0, false
}

func (m *HashMap) Delete(key string) {
	idx := m.hash(key)
	for i, p := range m.buckets[idx] {
		if p.key == key {
			m.buckets[idx] = append(m.buckets[idx][:i], m.buckets[idx][i+1:]...)
			return
		}
	}
}
```

---

## 9. 限流器（固定窗口）

```go
type RateLimiter struct {
	mu      sync.Mutex
	limit   int
	window  time.Duration
	count   int
	resetAt time.Time
}

func NewRateLimiter(limit int, window time.Duration) *RateLimiter {
	return &RateLimiter{limit: limit, window: window, resetAt: time.Now().Add(window)}
}

func (r *RateLimiter) Allow() bool {
	r.mu.Lock()
	defer r.mu.Unlock()
	if time.Now().After(r.resetAt) {
		r.count = 0
		r.resetAt = time.Now().Add(r.window)
	}
	if r.count >= r.limit {
		return false
	}
	r.count++
	return true
}
```

---

## 10. 字符串工具

```go
// 反转字符串（支持 Unicode）
func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

// 判断回文（忽略大小写和非字母数字）
func IsPalindrome(s string) bool {
	var chars []rune
	for _, c := range s {
		if unicode.IsLetter(c) || unicode.IsDigit(c) {
			chars = append(chars, unicode.ToLower(c))
		}
	}
	for i, j := 0, len(chars)-1; i < j; i, j = i+1, j-1 {
		if chars[i] != chars[j] {
			return false
		}
	}
	return true
}

// 最长无重复子串（滑动窗口）
func LengthOfLongestSubstring(s string) int {
	lastIdx := make(map[rune]int)
	maxLen, start := 0, 0
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
```

---

## 11. 二叉树遍历

```go
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// 前序遍历（迭代，用栈）
func Preorder(root *TreeNode) []int {
	var res []int
	var stack []*TreeNode
	curr := root
	for curr != nil || len(stack) > 0 {
		for curr != nil {
			res = append(res, curr.Val)
			stack = append(stack, curr)
			curr = curr.Left
		}
		curr = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		curr = curr.Right
	}
	return res
}

// 中序遍历（迭代）
func Inorder(root *TreeNode) []int {
	var res []int
	var stack []*TreeNode
	curr := root
	for curr != nil || len(stack) > 0 {
		for curr != nil {
			stack = append(stack, curr)
			curr = curr.Left
		}
		curr = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		res = append(res, curr.Val)
		curr = curr.Right
	}
	return res
}

// 层序遍历（BFS，用队列）
func LevelOrder(root *TreeNode) [][]int {
	if root == nil {
		return nil
	}
	var res [][]int
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		size := len(queue)
		level := []int{}
		for i := 0; i < size; i++ {
			node := queue[i]
			level = append(level, node.Val)
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		res = append(res, level)
		queue = queue[size:]
	}
	return res
}
```

---

## 12. 发布-订阅（channel 实现）

```go
type PubSub struct {
	mu  sync.RWMutex
	subs map[string][]chan string
}

func NewPubSub() *PubSub {
	return &PubSub{subs: make(map[string][]chan string)}
}

func (ps *PubSub) Subscribe(topic string) <-chan string {
	ch := make(chan string, 16)
	ps.mu.Lock()
	ps.subs[topic] = append(ps.subs[topic], ch)
	ps.mu.Unlock()
	return ch
}

func (ps *PubSub) Publish(topic string, msg string) {
	ps.mu.RLock()
	defer ps.mu.RUnlock()
	for _, ch := range ps.subs[topic] {
		select {
		case ch <- msg:
		default: // 非阻塞，跳过慢消费者
		}
	}
}

func (ps *PubSub) Unsubscribe(topic string, ch <-chan string) {
	ps.mu.Lock()
	defer ps.mu.Unlock()
	subs := ps.subs[topic]
	for i, sub := range subs {
		if sub == ch {
			ps.subs[topic] = append(subs[:i], subs[i+1:]...)
			close(sub)
			return
		}
	}
}
```
