package interview;

/**
 * 线程安全计数器
 * 用 synchronized / AtomicInteger / ReentrantLock 三种方式实现
 */
public class Ex05ThreadSafeCounter {

    // TODO: 在这里实现线程安全的 increment() 和 getCount()
    private int count = 0;
    public synchronized void increment() { count++; }
    public synchronized int getCount() { return count; }
}
