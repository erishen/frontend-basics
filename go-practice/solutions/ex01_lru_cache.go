package solutions

// LRUCache 双向链表 + map 实现
type LRUCache struct {
	capacity int
	nodes    map[int]*dllNode
	head     *dllNode // 哨兵头
	tail     *dllNode // 哨兵尾
}

type dllNode struct {
	key, value int
	prev, next *dllNode
}

func Constructor(capacity int) LRUCache {
	head := &dllNode{}
	tail := &dllNode{}
	head.next = tail
	tail.prev = head
	return LRUCache{
		capacity: capacity,
		nodes:    make(map[int]*dllNode, capacity),
		head:     head,
		tail:     tail,
	}
}

func (c *LRUCache) Get(key int) int {
	node, ok := c.nodes[key]
	if !ok {
		return -1
	}
	c.moveToHead(node)
	return node.value
}

func (c *LRUCache) Put(key int, value int) {
	if node, ok := c.nodes[key]; ok {
		node.value = value
		c.moveToHead(node)
		return
	}
	node := &dllNode{key: key, value: value}
	c.nodes[key] = node
	c.addToHead(node)
	if len(c.nodes) > c.capacity {
		removed := c.removeTail()
		delete(c.nodes, removed.key)
	}
}

func (c *LRUCache) addToHead(node *dllNode) {
	node.prev = c.head
	node.next = c.head.next
	c.head.next.prev = node
	c.head.next = node
}

func (c *LRUCache) removeNode(node *dllNode) {
	node.prev.next = node.next
	node.next.prev = node.prev
}

func (c *LRUCache) moveToHead(node *dllNode) {
	c.removeNode(node)
	c.addToHead(node)
}

func (c *LRUCache) removeTail() *dllNode {
	node := c.tail.prev
	c.removeNode(node)
	return node
}
