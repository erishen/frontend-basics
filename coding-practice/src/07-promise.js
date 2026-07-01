// Promise（简易版）
// 实现 then/catch，支持链式调用

class MyPromise {
  constructor(executor) {
    // TODO: 在这里实现
  }

  then(onFulfilled, onRejected) {
    // TODO: 在这里实现
  }

  catch(onRejected) {
    return this.then(null, onRejected);
  }
}

module.exports = MyPromise;
