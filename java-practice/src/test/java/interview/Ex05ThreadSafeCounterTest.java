package interview;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import solutions.Ex05ThreadSafeCounter;

class Ex05ThreadSafeCounterTest {

    @Test
    void syncCounter() throws InterruptedException {
        var counter = new Ex05ThreadSafeCounter.SyncCounter();
        int threads = 10, perThread = 1000;
        Thread[] ts = new Thread[threads];
        for (int i = 0; i < threads; i++) {
            ts[i] = new Thread(() -> {
                for (int j = 0; j < perThread; j++) counter.increment();
            });
            ts[i].start();
        }
        for (Thread t : ts) t.join();
        assertEquals(threads * perThread, counter.getCount());
    }

    @Test
    void atomicCounter() throws InterruptedException {
        var counter = new Ex05ThreadSafeCounter.AtomicCounter();
        int threads = 10, perThread = 1000;
        Thread[] ts = new Thread[threads];
        for (int i = 0; i < threads; i++) {
            ts[i] = new Thread(() -> {
                for (int j = 0; j < perThread; j++) counter.increment();
            });
            ts[i].start();
        }
        for (Thread t : ts) t.join();
        assertEquals(threads * perThread, counter.getCount());
    }
}
