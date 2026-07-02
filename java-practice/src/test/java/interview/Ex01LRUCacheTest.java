package interview;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

// 切换 import 练习：interview.Ex01LRUCache → solutions.Ex01LRUCache
import interview.Ex01LRUCache;

class Ex01LRUCacheTest {

    @Test
    void basicGetPut() {
        var cache = new Ex01LRUCache(2);
        cache.put(1, 1);
        cache.put(2, 2);
        assertEquals(1, cache.get(1));
        assertEquals(2, cache.get(2));
    }

    @Test
    void eviction() {
        var cache = new Ex01LRUCache(2);
        cache.put(1, 1);
        cache.put(2, 2);
        cache.put(3, 3); // 淘汰 key=1
        assertEquals(-1, cache.get(1));
        assertEquals(3, cache.get(3));
    }

    @Test
    void getRefreshes() {
        var cache = new Ex01LRUCache(2);
        cache.put(1, 1);
        cache.put(2, 2);
        cache.get(1);      // 刷新 key=1
        cache.put(3, 3);   // 淘汰 key=2
        assertEquals(-1, cache.get(2));
        assertEquals(1, cache.get(1));
    }
}
