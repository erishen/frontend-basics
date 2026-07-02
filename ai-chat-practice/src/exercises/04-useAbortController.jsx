/**
 * 练习 4: useAbortController 请求取消
 * 管理 AbortController，支持取消正在进行的请求
 *
 * 要求：
 * - startRequest(): 创建新的 AbortController，发起模拟请求
 * - abortRequest(): 取消当前请求
 * - isRequesting: 是否正在请求
 * - result: 请求结果（成功/取消/失败）
 * - 组件卸载时自动取消
 */
import { useState, useRef, useCallback, useEffect } from 'react';

export function useAbortController() {
  // TODO: 定义 isRequesting 状态
  // TODO: 定义 result 状态
  // TODO: 定义 controllerRef 保存 AbortController

  const startRequest = useCallback(() => {
    // TODO: 创建新的 AbortController
    // TODO: 设置 isRequesting = true
    // TODO: 模拟 3s 延迟请求（用 setTimeout）
    //   - 如果 signal.aborted → result = 'cancelled'
    //   - 否则 → result = 'success'
    // TODO: 设置 isRequesting = false
  }, []);

  const abortRequest = useCallback(() => {
    // TODO: 调用 controllerRef.current.abort()
  }, []);

  // TODO: useEffect 清理函数 → 组件卸载时 abort

  return {
    isRequesting: false, // TODO: 替换
    result: null,        // TODO: 替换
    startRequest,
    abortRequest,
  };
}
