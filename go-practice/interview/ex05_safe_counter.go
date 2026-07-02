package interview

import "sync"

// SafeCounter 使用 Mutex 实现线程安全的计数器
type SafeCounter struct {
	// TODO: 定义字段
	mu sync.Mutex
}

func NewSafeCounter() *SafeCounter {
	// TODO: 初始化
	return &SafeCounter{}
}

func (c *SafeCounter) Increment() {
	// TODO: 原子自增
}

func (c *SafeCounter) Decrement() {
	// TODO: 原子递减
}

func (c *SafeCounter) Value() int {
	// TODO: 读取当前值
	return 0
}
