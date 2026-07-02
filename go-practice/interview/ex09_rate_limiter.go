package interview

import (
	"sync"
	"time"
)

// RateLimiter 固定窗口限流器
type RateLimiter struct {
	// TODO: 定义字段
	mu sync.Mutex
}

func NewRateLimiter(limit int, window time.Duration) *RateLimiter {
	// TODO: 初始化限流器
	return &RateLimiter{}
}

func (r *RateLimiter) Allow() bool {
	// TODO: 判断是否允许请求
	return false
}
