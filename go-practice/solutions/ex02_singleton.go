package solutions

import "sync"

// Singleton 使用 sync.Once 实现线程安全单例
type Singleton struct {
	value string
}

var (
	once     sync.Once
	instance *Singleton
)

func GetInstance() *Singleton {
	once.Do(func() {
		instance = &Singleton{value: "initialized"}
	})
	return instance
}

func ResetInstance() {
	once = sync.Once{}
	instance = nil
}
