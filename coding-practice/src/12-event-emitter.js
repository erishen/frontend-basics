// 发布订阅 EventEmitter
// 支持 on / off / once / emit

class EventEmitter {
  constructor() {
    this.events = {};
  }

  on(event, fn) {
    // TODO: 在这里实现
  }

  off(event, fn) {
    // TODO: 在这里实现
  }

  once(event, fn) {
    // TODO: 在这里实现
  }

  emit(event, ...args) {
    // TODO: 在这里实现
  }
}

module.exports = EventEmitter;
