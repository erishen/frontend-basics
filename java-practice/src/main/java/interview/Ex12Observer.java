package interview;

import java.util.Map;
import java.util.List;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.function.Consumer;

/**
 * 设计模式：观察者模式
 * 实现简单的发布-订阅系统
 */
public class Ex12Observer {

    // TODO: 在这里实现 EventPublisher 和 EventSubscriber
    private final Map<String, List<Consumer<Object>>> listeners = new HashMap<>();

    public void subscribe(String event, Consumer<Object> listener) {
        listeners.computeIfAbsent(event, k -> new ArrayList<>()).add(listener);
    }

    public void unsubscribe(String event, Consumer<Object> listener) {
        List<Consumer<Object>> list = listeners.get(event);
        if(list != null) list.remove(listener);
    }

    public void emit(String event, Object data){
        List<Consumer<Object>> list = listeners.get(event);
        if(list != null) list.forEach(l -> l.accept(data));
    }
}
