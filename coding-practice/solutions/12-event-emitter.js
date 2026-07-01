class EventEmitter {
  constructor() {
    this.events = {};
  }

  on(event, fn) {
    (this.events[event] ??= []).push(fn);
    return this;
  }

  off(event, fn) {
    if (!this.events[event]) return this;
    this.events[event] = this.events[event].filter((f) => f !== fn);
    return this;
  }

  once(event, fn) {
    const wrapper = (...args) => {
      fn(...args);
      this.off(event, wrapper);
    };
    return this.on(event, wrapper);
  }

  emit(event, ...args) {
    (this.events[event] ?? []).forEach((fn) => fn(...args));
    return this;
  }
}

module.exports = EventEmitter;
