function jsonp(url, callbackName) {
  return new Promise((resolve, reject) => {
    const script = document.createElement("script");
    const cb = callbackName || "jsonp_" + Date.now();

    window[cb] = (data) => {
      resolve(data);
      delete window[cb];
      document.body.removeChild(script);
    };

    script.src = `${url}?callback=${cb}`;
    script.onerror = () => reject(new Error("JSONP failed"));
    document.body.appendChild(script);
  });
}

module.exports = jsonp;
