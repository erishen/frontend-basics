package interview

import "sync"

// PubSub 发布-订阅系统（基于 channel）
type PubSub struct {
	// TODO: 定义字段
	mu sync.RWMutex
}

func NewPubSub() *PubSub {
	// TODO: 初始化
	return &PubSub{}
}

func (ps *PubSub) Subscribe(topic string) <-chan string {
	// TODO: 订阅主题，返回接收 channel
	return nil
}

func (ps *PubSub) Publish(topic string, msg string) {
	// TODO: 向主题的所有订阅者发送消息
}

func (ps *PubSub) Unsubscribe(topic string, ch <-chan string) {
	// TODO: 取消订阅
}
