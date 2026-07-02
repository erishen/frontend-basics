package solutions

import "sync"

// SafeCounter 使用 Mutex 实现线程安全计数器
type SafeCounter struct {
	mu    sync.Mutex
	value int
}

func NewSafeCounter() *SafeCounter {
	return &SafeCounter{}
}

func (c *SafeCounter) Increment() {
	c.mu.Lock()
	c.value++
	c.mu.Unlock()
}

func (c *SafeCounter) Decrement() {
	c.mu.Lock()
	c.value--
	c.mu.Unlock()
}

func (c *SafeCounter) Value() int {
	c.mu.Lock()
	defer c.mu.Unlock()
	return c.value
}
