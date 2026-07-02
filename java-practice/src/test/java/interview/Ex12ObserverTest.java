package interview;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import solutions.Ex12Observer.EventPublisher;
import java.util.ArrayList;
import java.util.List;

class Ex12ObserverTest {

    @Test
    void subscribeAndEmit() {
        var pub = new EventPublisher();
        List<Object> received = new ArrayList<>();
        pub.subscribe("click", received::add);
        pub.emit("click", "data1");
        pub.emit("click", "data2");
        assertEquals(List.of("data1", "data2"), received);
    }

    @Test
    void unsubscribe() {
        var pub = new EventPublisher();
        List<Object> received = new ArrayList<>();
        java.util.function.Consumer<Object> listener = received::add;
        pub.subscribe("msg", listener);
        pub.emit("msg", "a");
        pub.unsubscribe("msg", listener);
        pub.emit("msg", "b");
        assertEquals(List.of("a"), received);
    }

    @Test
    void multipleListeners() {
        var pub = new EventPublisher();
        List<Object> r1 = new ArrayList<>(), r2 = new ArrayList<>();
        pub.subscribe("ev", r1::add);
        pub.subscribe("ev", r2::add);
        pub.emit("ev", "x");
        assertEquals(List.of("x"), r1);
        assertEquals(List.of("x"), r2);
    }
}
