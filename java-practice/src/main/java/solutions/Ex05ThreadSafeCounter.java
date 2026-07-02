package solutions;

import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.locks.ReentrantLock;

public class Ex05ThreadSafeCounter {

    // 方式1：synchronized
    public static class SyncCounter {
        private int count = 0;
        public synchronized void increment() { count++; }
        public synchronized int getCount() { return count; }
    }

    // 方式2：AtomicInteger
    public static class AtomicCounter {
        private final AtomicInteger count = new AtomicInteger(0);
        public void increment() { count.incrementAndGet(); }
        public int getCount() { return count.get(); }
    }

    // 方式3：ReentrantLock
    public static class LockCounter {
        private int count = 0;
        private final ReentrantLock lock = new ReentrantLock();
        public void increment() {
            lock.lock();
            try { count++; } finally { lock.unlock(); }
        }
        public int getCount() {
            lock.lock();
            try { return count; } finally { lock.unlock(); }
        }
    }
}
