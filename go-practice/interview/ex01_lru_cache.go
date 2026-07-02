package interview

// LRUCache 使用双向链表 + map 实现 O(1) 的 Get/Put
type LRUCache struct {
	// TODO: 定义字段
}

type dllNode struct {
	key, value int
	prev, next *dllNode
}

func Constructor(capacity int) LRUCache {
	// TODO: 初始化缓存
	return LRUCache{}
}

func (c *LRUCache) Get(key int) int {
	// TODO: 获取值，不存在返回 -1，访问后移到头部
	return -1
}

func (c *LRUCache) Put(key int, value int) {
	// TODO: 写入/更新值，超出容量时淘汰尾部
}
