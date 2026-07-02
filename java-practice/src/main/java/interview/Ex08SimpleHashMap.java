package interview;

/**
 * 手写 HashMap（简化版）
 * 实现 put / get / remove，处理哈希冲突（链地址法）
 */
public class Ex08SimpleHashMap<K, V> {
    private static class Entry<K, V> {
        final K key;
        V value;
        Entry<K, V> next;

        Entry(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }

    private static final int CAPACITY = 16;
    private Entry<K, V>[] table = new Entry[CAPACITY];
    private int size = 0;

    private int hash(K key){
        return key == null ? 0 : Math.abs(key.hashCode() % CAPACITY);
    }

    // TODO: 在这里实现

    public void put(K key, V value) {
        int idx = hash(key);
        for (Entry<K, V> e = table[idx]; e != null; e = e.next){
            if(e.key.equals(key)) { e.value = value; return; }
        }
        Entry<K, V> newEntry = new Entry<>(key, value);
        newEntry.next = table[idx];
        table[idx] = newEntry;
        size++;
    }

    public V get(K key) {
        int idx = hash(key);
        for(Entry<K, V> e = table[idx]; e != null; e = e.next){
            if(e.key.equals(key)) return e.value;
        }
        return null;
    }

    public V remove(K key) {
        int idx = hash(key);
        Entry<K, V> prev = null;
        for(Entry<K, V> e = table[idx]; e != null; prev = e, e = e.next) {
            if(e.key.equals(key)){
                V val = e.value;
                if(prev == null) table[idx] = e.next;
                else prev.next = e.next;
                size--;
                return val;
            }
        }
        return null;
    }

    public int size() {
        return size;
    }
}
