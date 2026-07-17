package interview;

import java.util.List;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ArrayBlockingQueue;

/**
 * 生产者-消费者模型
 * 使用 BlockingQueue 实现
 */
public class Ex07ProducerConsumer {

    // TODO: 在这里实现
    private final BlockingQueue<Integer> queue;

    public Ex07ProducerConsumer(int capacity){
        this.queue = new ArrayBlockingQueue<>(capacity);
    }

    public void startProducer(int count){
        new Thread(() -> {
            try {
                for(int i = 0; i < count; i++){
                    queue.put(i);
                }
            } catch(InterruptedException e){
                Thread.currentThread().interrupt();
            }
        }).start();
    }

    public void startConsumer(int count){
        new Thread(() -> {
            try {
                for(int i = 0; i < count; i++){
                    int item = queue.take();
                    System.out.println("Consumed: " + item);
                }
            } catch(InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }).start();
    }
}
