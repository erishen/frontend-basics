package solutions

import "sync"

// PubSub 发布-订阅系统
type PubSub struct {
	mu          sync.RWMutex
	subscribers map[string][]chan string
}

func NewPubSub() *PubSub {
	return &PubSub{
		subscribers: make(map[string][]chan string),
	}
}

func (ps *PubSub) Subscribe(topic string) <-chan string {
	ch := make(chan string, 16)
	ps.mu.Lock()
	ps.subscribers[topic] = append(ps.subscribers[topic], ch)
	ps.mu.Unlock()
	return ch
}

func (ps *PubSub) Publish(topic string, msg string) {
	ps.mu.RLock()
	defer ps.mu.RUnlock()
	for _, ch := range ps.subscribers[topic] {
		select {
		case ch <- msg:
		default:
			// 非阻塞发送，跳过慢消费者
		}
	}
}

func (ps *PubSub) Unsubscribe(topic string, ch <-chan string) {
	ps.mu.Lock()
	defer ps.mu.Unlock()
	subs := ps.subscribers[topic]
	for i, sub := range subs {
		if sub == ch {
			ps.subscribers[topic] = append(subs[:i], subs[i+1:]...)
			close(sub)
			return
		}
	}
}
