package solutions

// SimpleHashMap 拉链法哈希表
type SimpleHashMap struct {
	buckets [][]kvPair
	size    int
}

type kvPair struct {
	key   string
	value int
}

func NewHashMap(size int) *SimpleHashMap {
	return &SimpleHashMap{
		buckets: make([][]kvPair, size),
		size:    size,
	}
}

func (m *SimpleHashMap) hash(key string) int {
	h := 0
	for _, c := range key {
		h = h*31 + int(c)
	}
	if h < 0 {
		h = -h
	}
	return h % m.size
}

func (m *SimpleHashMap) Put(key string, value int) {
	idx := m.hash(key)
	for i, pair := range m.buckets[idx] {
		if pair.key == key {
			m.buckets[idx][i].value = value
			return
		}
	}
	m.buckets[idx] = append(m.buckets[idx], kvPair{key, value})
}

func (m *SimpleHashMap) Get(key string) (int, bool) {
	idx := m.hash(key)
	for _, pair := range m.buckets[idx] {
		if pair.key == key {
			return pair.value, true
		}
	}
	return 0, false
}

func (m *SimpleHashMap) Delete(key string) {
	idx := m.hash(key)
	bucket := m.buckets[idx]
	for i, pair := range bucket {
		if pair.key == key {
			m.buckets[idx] = append(bucket[:i], bucket[i+1:]...)
			return
		}
	}
}
