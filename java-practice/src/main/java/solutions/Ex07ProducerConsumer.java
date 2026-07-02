package solutions;

import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

public class Ex07ProducerConsumer {

    public static class Worker {
        private final BlockingQueue<Integer> queue;
        private final int count;

        public Worker(int capacity, int count) {
            this.queue = new ArrayBlockingQueue<>(capacity);
            this.count = count;
        }

        public void run() throws InterruptedException {
            Thread producer = new Thread(() -> {
                try {
                    for (int i = 1; i <= count; i++) {
                        queue.put(i);
                    }
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });

            Thread consumer = new Thread(() -> {
                try {
                    for (int i = 0; i < count; i++) {
                        queue.take();
                    }
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });

            producer.start();
            consumer.start();
            producer.join();
            consumer.join();
        }
    }
}
