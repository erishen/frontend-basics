/**
 * 练习 3: AutoScrollList 自动滚动消息列表
 * 新消息到来时自动滚动到底部，用户手动上滚时不打断
 *
 * 要求：
 * - 新消息到来 → 自动滚动到底部
 * - 用户手动上滚 → 停止自动滚动
 * - 用户滚回底部 → 恢复自动滚动
 * - 显示"回到底部"按钮（不在底部时可见）
 */
import { useRef, useState, useEffect } from 'react';

export function AutoScrollList({ messages }) {
  const containerRef = useRef(null);
  // TODO: 定义 isAtBottom 状态

  // TODO: 监听 scroll 事件，判断是否在底部（距底部 < 50px）

  // TODO: useEffect 监听 messages 变化
  // - 如果 isAtBottom，自动 scrollTo bottom
  // - 如果不在底部，不滚动

  const scrollToBottom = () => {
    // TODO: 平滑滚动到底部
  };

  return (
    <div className="auto-scroll-list">
      <div
        ref={containerRef}
        className="scroll-container"
        onScroll={() => {/* TODO: 判断是否在底部 */}}
      >
        {messages.map((msg) => (
          <div key={msg.id} className={`message ${msg.role}`}>
            {msg.content}
          </div>
        ))}
      </div>
      {/* TODO: 不在底部时显示"回到底部"按钮 */}
    </div>
  );
}
