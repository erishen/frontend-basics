import { useState, useRef, useCallback, useEffect } from 'react';

export function useAbortController() {
  const [isRequesting, setIsRequesting] = useState(false);
  const [result, setResult] = useState(null);
  const controllerRef = useRef(null);
  const timerRef = useRef(null);

  const startRequest = useCallback(() => {
    // 取消之前的请求
    if (controllerRef.current) {
      controllerRef.current.abort();
    }

    const controller = new AbortController();
    controllerRef.current = controller;
    setIsRequesting(true);
    setResult(null);

    timerRef.current = setTimeout(() => {
      if (controller.signal.aborted) {
        setResult('cancelled');
      } else {
        setResult('success: 请求完成！');
      }
      setIsRequesting(false);
    }, 3000);
  }, []);

  const abortRequest = useCallback(() => {
    if (controllerRef.current) {
      controllerRef.current.abort();
      clearTimeout(timerRef.current);
      setResult('cancelled: 已取消');
      setIsRequesting(false);
    }
  }, []);

  useEffect(() => {
    return () => {
      controllerRef.current?.abort();
      clearTimeout(timerRef.current);
    };
  }, []);

  return { isRequesting, result, startRequest, abortRequest };
}
