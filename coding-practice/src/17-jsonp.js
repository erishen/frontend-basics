// JSONP
// 利用 script 标签跨域获取数据

/**
 * @param {string} url - 请求地址
 * @param {string} callbackName - 全局回调函数名
 * @returns {Promise<any>}
 */
function jsonp(url, callbackName) {
  // TODO: 在这里实现
  return new Promise((resolve, reject) => {
    const script = document.createElement("script");
    const cb = callbackName || "jsonp_" + Date.now();

    window[cb] = (data) => {
      resolve(data);
      delete window[cb];
      document.body.removeChild(script);
    }

    script.src = `${url}?callback=${cb}`;
    script.onerror = () => reject(new Error("JSONP failed"));
    document.body.appendChild(script);
  });
}

module.exports = jsonp;
