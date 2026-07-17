# Java 面试手写代码模板

> 面试最高频的手写题，每题都是完整可运行的模板，多写几遍形成肌肉记忆。

---

## 1. LRU 缓存

```java
import java.util.LinkedHashMap;
import java.util.Map;

public class LRUCache {
    private final int capacity;
    private final LinkedHashMap<Integer, Integer> cache;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        // accessOrder=true 让 get/put 自动把访问的节点移到末尾
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
```

---

## 2. 单例模式

```java
// 方式1：双重检查锁（DCL）
public class Singleton {
    private static volatile Singleton instance; // volatile 防止指令重排

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {                    // 第一次检查（无锁）
            synchronized (Singleton.class) {
                if (instance == null) {            // 第二次检查（有锁）
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}

// 方式2：静态内部类（推荐，更简洁）
public class Singleton {
    private Singleton() {}

    private static class Holder {
        static final Singleton INSTANCE = new Singleton();
    }

    public static Singleton getInstance() {
        return Holder.INSTANCE;  // 类加载时初始化，天然线程安全
    }
}
```

---

## 3. 排序算法

```java
// 快速排序（返回新数组，不修改原数组）
public static int[] quickSort(int[] arr) {
    int[] result = arr.clone();
    quickSort(result, 0, result.length - 1);
    return result;
}

private static void quickSort(int[] arr, int lo, int hi) {
    if (lo >= hi) return;
    int pivot = arr[lo + (hi - lo) / 2];
    int i = lo, j = hi;
    while (i <= j) {
        while (arr[i] < pivot) i++;
        while (arr[j] > pivot) j--;
        if (i <= j) {
            int tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
            i++; j--;
        }
    }
    quickSort(arr, lo, j);
    quickSort(arr, i, hi);
}

// 归并排序
public static int[] mergeSort(int[] arr) {
    int[] result = arr.clone();
    mergeSort(result, 0, result.length - 1);
    return result;
}

private static void mergeSort(int[] arr, int lo, int hi) {
    if (lo >= hi) return;
    int mid = lo + (hi - lo) / 2;
    mergeSort(arr, lo, mid);
    mergeSort(arr, mid + 1, hi);
    merge(arr, lo, mid, hi);
}

private static void merge(int[] arr, int lo, int mid, int hi) {
    int[] tmp = new int[hi - lo + 1];
    int i = lo, j = mid + 1, k = 0;
    while (i <= mid && j <= hi)
        tmp[k++] = arr[i] <= arr[j] ? arr[i++] : arr[j++];
    while (i <= mid) tmp[k++] = arr[i++];
    while (j <= hi)  tmp[k++] = arr[j++];
    System.arraycopy(tmp, 0, arr, lo, tmp.length);
}

// 堆排序
public static int[] heapSort(int[] arr) {
    int[] result = arr.clone();
    int n = result.length;
    for (int i = n / 2 - 1; i >= 0; i--) heapify(result, n, i);
    for (int i = n - 1; i > 0; i--) {
        int tmp = result[0]; result[0] = result[i]; result[i] = tmp;
        heapify(result, i, 0);
    }
    return result;
}

private static void heapify(int[] arr, int n, int i) {
    int largest = i, left = 2 * i + 1, right = 2 * i + 2;
    if (left < n && arr[left] > arr[largest]) largest = left;
    if (right < n && arr[right] > arr[largest]) largest = right;
    if (largest != i) {
        int tmp = arr[i]; arr[i] = arr[largest]; arr[largest] = tmp;
        heapify(arr, n, largest);
    }
}
```

---

## 4. 二分查找

```java
// 标准二分查找
public static int binarySearch(int[] arr, int target) {
    int lo = 0, hi = arr.length - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;  // 防溢出
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}

// 找第一个等于 target 的位置
public static int findFirst(int[] arr, int target) {
    int lo = 0, hi = arr.length - 1, result = -1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) { result = mid; hi = mid - 1; }
        else if (arr[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return result;
}

// 找最后一个等于 target 的位置
public static int findLast(int[] arr, int target) {
    int lo = 0, hi = arr.length - 1, result = -1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) { result = mid; lo = mid + 1; }
        else if (arr[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return result;
}
```

---

## 5. 线程安全计数器

```java
// 方式1：synchronized
public class SyncCounter {
    private int count = 0;
    public synchronized void increment() { count++; }
    public synchronized int getCount() { return count; }
}

// 方式2：AtomicInteger（CAS，无锁，性能最好）
import java.util.concurrent.atomic.AtomicInteger;

public class AtomicCounter {
    private final AtomicInteger count = new AtomicInteger(0);
    public void increment() { count.incrementAndGet(); }
    public int getCount() { return count.get(); }
}

// 方式3：ReentrantLock
import java.util.concurrent.locks.ReentrantLock;

public class LockCounter {
    private int count = 0;
    private final ReentrantLock lock = new ReentrantLock();

    public void increment() {
        lock.lock();
        try { count++; } finally { lock.unlock(); }
    }
    public int getCount() {
        lock.lock();
        try { return count; } finally { lock.unlock(); }
    }
}
```

---

## 6. 深拷贝

```java
import java.util.ArrayList;
import java.util.List;

public class Node implements Cloneable {
    String name;
    int value;
    List<Node> children;

    public Node(String name, int value) {
        this.name = name;
        this.value = value;
        this.children = new ArrayList<>();
    }

    @Override
    public Node clone() {
        try {
            Node copy = (Node) super.clone();
            // 关键：children 也要深拷贝，否则共享引用
            copy.children = new ArrayList<>();
            for (Node child : this.children) {
                copy.children.add(child.clone());
            }
            return copy;
        } catch (CloneNotSupportedException e) {
            throw new AssertionError(e);
        }
    }
}
```

---

## 7. 生产者-消费者

```java
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

public class ProducerConsumer {
    private final BlockingQueue<Integer> queue;

    public ProducerConsumer(int capacity) {
        this.queue = new ArrayBlockingQueue<>(capacity);
    }

    public void startProducer(int count) {
        new Thread(() -> {
            try {
                for (int i = 0; i < count; i++) {
                    queue.put(i);  // 队列满时阻塞
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }).start();
    }

    public void startConsumer(int count) {
        new Thread(() -> {
            try {
                for (int i = 0; i < count; i++) {
                    int item = queue.take();  // 队列空时阻塞
                    System.out.println("Consumed: " + item);
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }).start();
    }
}
```

---

## 8. 手写 HashMap

```java
public class SimpleHashMap<K, V> {
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

    private int hash(K key) {
        return key == null ? 0 : Math.abs(key.hashCode() % CAPACITY);
    }

    public void put(K key, V value) {
        int idx = hash(key);
        // 遍历链表，key 已存在则更新
        for (Entry<K, V> e = table[idx]; e != null; e = e.next) {
            if (e.key.equals(key)) { e.value = value; return; }
        }
        // 头插法
        Entry<K, V> newEntry = new Entry<>(key, value);
        newEntry.next = table[idx];
        table[idx] = newEntry;
        size++;
    }

    public V get(K key) {
        int idx = hash(key);
        for (Entry<K, V> e = table[idx]; e != null; e = e.next) {
            if (e.key.equals(key)) return e.value;
        }
        return null;
    }

    public V remove(K key) {
        int idx = hash(key);
        Entry<K, V> prev = null;
        for (Entry<K, V> e = table[idx]; e != null; prev = e, e = e.next) {
            if (e.key.equals(key)) {
                V val = e.value;
                if (prev == null) table[idx] = e.next;
                else prev.next = e.next;
                size--;
                return val;
            }
        }
        return null;
    }

    public int size() { return size; }
}
```

---

## 9. 限流器（固定窗口）

```java
public class RateLimiter {
    private final int maxRequests;
    private final long windowMs;
    private int count;
    private long windowStart;

    public RateLimiter(int maxRequests, long windowMs) {
        this.maxRequests = maxRequests;
        this.windowMs = windowMs;
        this.count = 0;
        this.windowStart = System.currentTimeMillis();
    }

    public synchronized boolean tryAcquire() {
        long now = System.currentTimeMillis();
        if (now - windowStart >= windowMs) {
            count = 0;              // 新窗口，重置计数
            windowStart = now;
        }
        if (count < maxRequests) {
            count++;
            return true;
        }
        return false;
    }
}
```

---

## 10. 字符串高频题

```java
// 反转字符串
public static String reverse(String s) {
    char[] chars = s.toCharArray();
    int lo = 0, hi = chars.length - 1;
    while (lo < hi) {
        char tmp = chars[lo]; chars[lo] = chars[hi]; chars[hi] = tmp;
        lo++; hi--;
    }
    return new String(chars);
}

// 判断回文（忽略大小写和非字母数字）
public static boolean isPalindrome(String s) {
    int lo = 0, hi = s.length() - 1;
    while (lo < hi) {
        while (lo < hi && !Character.isLetterOrDigit(s.charAt(lo))) lo++;
        while (lo < hi && !Character.isLetterOrDigit(s.charAt(hi))) hi--;
        if (Character.toLowerCase(s.charAt(lo)) != Character.toLowerCase(s.charAt(hi)))
            return false;
        lo++; hi--;
    }
    return true;
}

// 最长无重复子串（滑动窗口）
public static int lengthOfLongestSubstring(String s) {
    java.util.Set<Character> set = new java.util.HashSet<>();
    int max = 0, lo = 0;
    for (int hi = 0; hi < s.length(); hi++) {
        while (set.contains(s.charAt(hi))) {
            set.remove(s.charAt(lo));
            lo++;
        }
        set.add(s.charAt(hi));
        max = Math.max(max, hi - lo + 1);
    }
    return max;
}
```

---

## 11. 二叉树

```java
import java.util.*;

public class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int val) { this.val = val; }
}

// 中序遍历（递归）
public static List<Integer> inorder(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    inorder(root, result);
    return result;
}

private static void inorder(TreeNode node, List<Integer> result) {
    if (node == null) return;
    inorder(node.left, result);
    result.add(node.val);
    inorder(node.right, result);
}

// 层序遍历（BFS，用队列）
public static List<Integer> levelOrder(TreeNode root) {
    if (root == null) return List.of();
    List<Integer> result = new ArrayList<>();
    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    while (!queue.isEmpty()) {
        TreeNode node = queue.poll();
        result.add(node.val);
        if (node.left != null) queue.offer(node.left);
        if (node.right != null) queue.offer(node.right);
    }
    return result;
}

// 最大深度
public static int maxDepth(TreeNode root) {
    if (root == null) return 0;
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}
```

---

## 12. 观察者模式

```java
import java.util.*;
import java.util.function.Consumer;

public class EventPublisher {
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

// 用法
var pub = new EventPublisher();
pub.subscribe("click", data -> System.out.println("Clicked: " + data));
pub.emit("click", "button1");
```

---

## 速查表

| 题目 | 核心思路 | Java 特色 |
|------|----------|-----------|
| LRU | LinkedHashMap accessOrder | 重写 removeEldestEntry |
| 单例 | volatile + DCL / 静态内部类 | JVM 类加载保证线程安全 |
| 排序 | 快排分治 / 归并合并 / 堆化 | 原地排序，不新建数组 |
| 二分 | 左右指针逼近 | `lo + (hi - lo) / 2` 防溢出 |
| 线程安全 | synchronized / Atomic / Lock | CAS 无锁性能最优 |
| 深拷贝 | Cloneable + 递归 clone | 注意引用类型要单独处理 |
| 生产者消费者 | BlockingQueue | put/take 自动阻塞 |
| HashMap | 数组 + 链表（链地址法） | 头插法，hash 取模 |
| 限流 | 固定窗口计数 | synchronized 保证线程安全 |
| 字符串 | 双指针 / 滑动窗口 | char[] 操作比 String 快 |
| 二叉树 | 递归 / BFS 队列 | LinkedList 当 Queue 用 |
| 观察者 | Map<String, List<Consumer>> | Java 8 函数式接口 |
