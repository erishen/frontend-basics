package interview;

/**
 * 限流器（Rate Limiter）
 * 实现固定窗口限流算法
 */
public class Ex09RateLimiter {
    private final int maxRequests;
    private final long windowMs;
    private int count;
    private long windowStart;

    // TODO: 在这里实现

    public Ex09RateLimiter(int maxRequests, long windowMs) {
        this.maxRequests = maxRequests;
        this.windowMs = windowMs;
        this.count = 0;
        this.windowStart = System.currentTimeMillis();
    }

    public synchronized boolean tryAcquire() {
        long now = System.currentTimeMillis();
        if(now - windowStart >= windowMs) {
            count = 0;
            windowStart = now;
        }

        if(count < maxRequests) {
            count++;
            return true;
        }
        return false;
    }
}
