/**
 * 练习 2: StreamRenderer 流式逐字渲染
 * 模拟 LLM 逐字输出效果
 *
 * 要求：
 * - 接收 fullText（完整文本）和 speed（毫秒/字）
 * - 逐字显示文本，模拟打字效果
 * - 支持暂停/继续
 * - 完成后触发 onComplete 回调
 */
import { useState, useEffect, useRef } from 'react';

export function StreamRenderer({ fullText, speed = 50, onComplete }) {
  // TODO: 定义 displayedText 状态（当前已显示的文本）
  // TODO: 定义 isPaused 状态
  // TODO: 定义 index ref（当前字符位置）

  // TODO: useEffect 实现逐字渲染逻辑
  // - 用 setInterval 每隔 speed 毫秒追加一个字符
  // - 检查 isPaused，暂停时不清除 interval 但跳过追加
  // - 全部显示完后调用 onComplete

  // TODO: 清理 interval（组件卸载或 fullText 变化时）

  return (
    <div className="stream-renderer">
      <div className="stream-text">
        {/* TODO: 显示 displayedText，末尾加闪烁光标 */}
      </div>
      <button onClick={() => {/* TODO: 切换暂停 */}}>
        {/* TODO: 显示 暂停/继续 */}
      </button>
    </div>
  );
}
