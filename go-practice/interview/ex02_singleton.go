package interview

import "sync"

// Singleton 使用 sync.Once 实现线程安全的单例
type Singleton struct {
	// TODO: 定义字段
}

var (
	once     sync.Once
	instance *Singleton
)

func GetInstance() *Singleton {
	// TODO: 返回单例实例
	return nil
}

func ResetInstance() {
	// 测试用：重置单例（实际生产不用）
	once = sync.Once{}
	instance = nil
}
