// 发布订阅 EventEmitter
// 支持 on / off / once / emit

class EventEmitter {
  constructor() {
    this.events = {};
  }

  on(event, fn) {
    // TODO: 在这里实现
    (this.events[event] ??= []).push(fn);
    return this;
  }

  off(event, fn) {
    // TODO: 在这里实现
    if(!this.events[event]) return;
    this.events[event] = this.events[event].filter((f) => f !== fn);
    return this;
  }

  once(event, fn) {
    // TODO: 在这里实现
    const wrapper = (...args) => {
      fn(...args);
      this.off(event, wrapper);
    };
    return this.on(event, wrapper);
  }

  emit(event, ...args) {
    // TODO: 在这里实现
    (this.events[event] ?? []).forEach((fn) => fn(...args));
    return this;
  }
}

module.exports = EventEmitter;
