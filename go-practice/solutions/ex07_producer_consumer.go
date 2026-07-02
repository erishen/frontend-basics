package solutions

// ProducerConsumer 生产者-消费者模型
func ProducerConsumer(n int) int {
	ch := make(chan int)
	done := make(chan struct{})

	// 生产者
	go func() {
		for i := 1; i <= n; i++ {
			ch <- i
		}
		close(ch)
	}()

	// 消费者
	sum := 0
	go func() {
		for v := range ch {
			sum += v
		}
		close(done)
	}()

	<-done
	return sum
}
