import { useRef, useState, useEffect, useCallback } from 'react';

export function AutoScrollList({ messages }) {
  const containerRef = useRef(null);
  const [isAtBottom, setIsAtBottom] = useState(true);
  const [showButton, setShowButton] = useState(false);

  const checkIsAtBottom = useCallback(() => {
    const el = containerRef.current;
    if (!el) return true;
    return el.scrollHeight - el.scrollTop - el.clientHeight < 50;
  }, []);

  const handleScroll = useCallback(() => {
    const atBottom = checkIsAtBottom();
    setIsAtBottom(atBottom);
    setShowButton(!atBottom);
  }, [checkIsAtBottom]);

  useEffect(() => {
    if (isAtBottom) {
      const el = containerRef.current;
      if (el) {
        el.scrollTo({ top: el.scrollHeight, behavior: 'smooth' });
      }
    }
  }, [messages, isAtBottom]);

  const scrollToBottom = () => {
    const el = containerRef.current;
    if (el) {
      el.scrollTo({ top: el.scrollHeight, behavior: 'smooth' });
    }
  };

  return (
    <div className="auto-scroll-list">
      <div
        ref={containerRef}
        className="scroll-container"
        onScroll={handleScroll}
      >
        {messages.map((msg) => (
          <div key={msg.id} className={`message ${msg.role}`}>
            <span className="role-label">{msg.role === 'user' ? '🧑 ' : '🤖 '}</span>
            {msg.content}
          </div>
        ))}
      </div>
      {showButton && (
        <button className="scroll-to-bottom" onClick={scrollToBottom}>
          ↓ 回到底部
        </button>
      )}
    </div>
  );
}
