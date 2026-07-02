import { useState, useCallback, useRef } from 'react';

const AI_REPLIES = [
  '你好！我是 AI 助手，有什么可以帮你的吗？',
  '这是一个很好的问题。让我来解释一下：首先，我们需要理解基本概念。其次，考虑实际应用场景。最后，动手实践是最好的学习方式。',
  '根据我的分析，建议从以下几个方面入手：\n1. 明确目标\n2. 制定计划\n3. 逐步执行\n4. 持续迭代',
  '代码示例如下：\n```javascript\nfunction hello() {\n  console.log("Hello, World!");\n}\n```\n希望这对你有帮助！',
];

export function useChat() {
  const [messages, setMessages] = useState([]);
  const [isStreaming, setIsStreaming] = useState(false);
  const idRef = useRef(0);

  const sendMessage = useCallback((text) => {
    const userMsg = {
      id: ++idRef.current,
      role: 'user',
      content: text,
      timestamp: Date.now(),
    };
    setMessages((prev) => [...prev, userMsg]);
    setIsStreaming(true);

    setTimeout(() => {
      const reply = AI_REPLIES[Math.floor(Math.random() * AI_REPLIES.length)];
      const aiMsg = {
        id: ++idRef.current,
        role: 'assistant',
        content: reply,
        timestamp: Date.now(),
      };
      setMessages((prev) => [...prev, aiMsg]);
      setIsStreaming(false);
    }, 1500);
  }, []);

  const clearMessages = useCallback(() => {
    setMessages([]);
  }, []);

  return { messages, isStreaming, sendMessage, clearMessages };
}
