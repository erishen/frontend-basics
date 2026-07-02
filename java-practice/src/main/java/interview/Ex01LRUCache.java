package interview;
import java.util.LinkedHashMap;
import java.util.Map;

/**
 * LRU 缓存
 * 使用 LinkedHashMap 实现，get/put 要求 O(1) 时间复杂度
 */
public class Ex01LRUCache {
    private final int capacity;
    private final LinkedHashMap<Integer, Integer> cache;

    // TODO: 在这里实现

    public Ex01LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new LinkedHashMap<>(capacity, 0.75f, true) {
            @Override
            protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
                return size() > capacity;
            }
        };
    }

    public int get(int key) {
        return cache.getOrDefault(key, -1);
    }

    public void put(int key, int value) {
        cache.put(key, value);
    }
}
