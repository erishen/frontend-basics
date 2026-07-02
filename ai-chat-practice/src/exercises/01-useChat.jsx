/**
 * 练习 1: useChat Hook
 * 管理聊天消息列表、发送/接收状态
 *
 * 要求：
 * - messages: 消息数组 [{id, role, content, timestamp}]
 * - sendMessage(text): 添加用户消息，触发模拟回复
 * - isStreaming: 是否正在接收回复
 * - clearMessages(): 清空消息
 */
import { useState, useCallback } from 'react';

export function useChat() {
  // TODO: 定义 messages 状态
  // TODO: 定义 isStreaming 状态

  const sendMessage = useCallback((text) => {
    // TODO: 添加用户消息到列表
    // TODO: 设置 isStreaming = true
    // TODO: 模拟 1.5s 后收到 AI 回复（用 setTimeout）
    // TODO: 添加 AI 回复消息，设置 isStreaming = false
  }, []);

  const clearMessages = useCallback(() => {
    // TODO: 清空消息列表
  }, []);

  return {
    messages: [],      // TODO: 替换为实际 messages
    isStreaming: false, // TODO: 替换为实际 isStreaming
    sendMessage,
    clearMessages,
  };
}
