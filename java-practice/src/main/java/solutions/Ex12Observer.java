package solutions;

import java.util.*;
import java.util.function.Consumer;

public class Ex12Observer {

    public static class EventPublisher {
        private final Map<String, List<Consumer<Object>>> listeners = new HashMap<>();

        public void subscribe(String event, Consumer<Object> listener) {
            listeners.computeIfAbsent(event, k -> new ArrayList<>()).add(listener);
        }

        public void unsubscribe(String event, Consumer<Object> listener) {
            List<Consumer<Object>> list = listeners.get(event);
            if (list != null) list.remove(listener);
        }

        public void emit(String event, Object data) {
            List<Consumer<Object>> list = listeners.get(event);
            if (list != null) list.forEach(l -> l.accept(data));
        }
    }
}
