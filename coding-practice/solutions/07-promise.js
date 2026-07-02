class MyPromise {
  constructor(executor) {
    this.state = "pending";
    this.value = undefined;
    this.callbacks = [];

    const resolve = (value) => {
      if (this.state !== "pending") return;
      this.state = "fulfilled";
      this.value = value;
      this.callbacks.forEach((cb) => cb.onFulfilled(value));
    };

    const reject = (reason) => {
      if (this.state !== "pending") return;
      this.state = "rejected";
      this.value = reason;
      this.callbacks.forEach((cb) => cb.onRejected(reason));
    };

    try {
      executor(resolve, reject);
    } catch (err) {
      reject(err);
    }
  }

  static resolve(value) {
    return new MyPromise((resolve) => resolve(value));
  }

  static reject(reason) {
    return new MyPromise((_, reject) => reject(reason));
  }

  then(onFulfilled, onRejected) {
    if (typeof onFulfilled !== "function") onFulfilled = (v) => v;
    if (typeof onRejected !== "function") onRejected = (e) => { throw e; };

    return new MyPromise((resolve, reject) => {
      const handle = (callback) => {
        try {
          const result = callback(this.value);
          if (result instanceof MyPromise) {
            result.then(resolve, reject);
          } else {
            resolve(result);
          }
        } catch (err) {
          reject(err);
        }
      };

      if (this.state === "fulfilled") {
        handle(onFulfilled);
      } else if (this.state === "rejected") {
        handle(onRejected);
      } else {
        this.callbacks.push({
          onFulfilled: () => handle(onFulfilled),
          onRejected: () => handle(onRejected),
        });
      }
    });
  }

  catch(onRejected) {
    return this.then(null, onRejected);
  }
}

module.exports = MyPromise;
