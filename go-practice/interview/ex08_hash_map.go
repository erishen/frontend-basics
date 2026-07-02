package interview

// SimpleHashMap 使用拉链法实现简单哈希表
type SimpleHashMap struct {
	// TODO: 定义字段
}

type kvPair struct {
	key   string
	value int
}

func NewHashMap(size int) *SimpleHashMap {
	// TODO: 初始化哈希表
	return &SimpleHashMap{}
}

func (m *SimpleHashMap) Put(key string, value int) {
	// TODO: 插入/更新键值对
}

func (m *SimpleHashMap) Get(key string) (int, bool) {
	// TODO: 查找键，返回值和是否存在
	return 0, false
}

func (m *SimpleHashMap) Delete(key string) {
	// TODO: 删除键
}
