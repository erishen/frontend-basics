package solutions

import (
	"sync"
	"time"
)

// RateLimiter 固定窗口限流器
type RateLimiter struct {
	mu      sync.Mutex
	limit   int
	window  time.Duration
	count   int
	resetAt time.Time
}

func NewRateLimiter(limit int, window time.Duration) *RateLimiter {
	return &RateLimiter{
		limit:   limit,
		window:  window,
		resetAt: time.Now().Add(window),
	}
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
