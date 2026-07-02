import { useState } from 'react';
import './App.css';

// Solutions (切换到 solutions 查看效果)
import { useChat } from './solutions/01-useChat';
import { StreamRenderer } from './solutions/02-StreamRenderer';
import { AutoScrollList } from './solutions/03-AutoScrollList';
import { useAbortController } from './solutions/04-useAbortController';
import { MarkdownRenderer } from './solutions/05-MarkdownRenderer';

// Exercises (练习时取消上面的 import，改用这些)
// import { useChat } from './exercises/01-useChat';
// import { StreamRenderer } from './exercises/02-StreamRenderer';
// import { AutoScrollList } from './exercises/03-AutoScrollList';
// import { useAbortController } from './exercises/04-useAbortController';
// import { MarkdownRenderer } from './exercises/05-MarkdownRenderer';

const EXERCISES = [
  { id: 1, name: 'useChat', desc: '消息管理 Hook' },
  { id: 2, name: 'StreamRenderer', desc: '流式逐字渲染' },
  { id: 3, name: 'AutoScrollList', desc: '自动滚动列表' },
  { id: 4, name: 'useAbortController', desc: '请求取消' },
  { id: 5, name: 'MarkdownRenderer', desc: 'Markdown 渲染' },
];

const DEMO_TEXT = `# AI Chat 练习项目

这是一个 **AI 聊天界面** 的常见模式练习。

## 功能特性

- 流式逐字渲染
- 自动滚动消息列表
- 请求取消（AbortController）
- Markdown 实时渲染

## 代码示例

\`\`\`javascript
function hello() {
  console.log("Hello, AI!");
}
\`\`\`

使用 \`useChat\` Hook 管理状态，支持 [更多链接](https://example.com)。`;

function ChatDemo() {
  const { messages, isStreaming, sendMessage, clearMessages } = useChat();
  const [input, setInput] = useState('');

  const handleSend = () => {
    if (!input.trim() || isStreaming) return;
    sendMessage(input.trim());
    setInput('');
  };

  return (
    <div className="chat-demo">
      <div className="chat-messages">
        {messages.length === 0 && (
          <div className="empty-hint">发送消息开始对话...</div>
        )}
        <AutoScrollList messages={messages} />
      </div>
      {isStreaming && <div className="typing-indicator">AI 正在思考...</div>}
      <div className="input-area">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
          placeholder="输入消息..."
          disabled={isStreaming}
        />
        <button onClick={handleSend} disabled={isStreaming || !input.trim()}>
          发送
        </button>
        <button onClick={clearMessages} className="btn-clear">清空</button>
      </div>
    </div>
  );
}

function StreamDemo() {
  const [text, setText] = useState('');
  return (
    <div className="stream-demo">
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="输入要流式渲染的文本..."
        rows={3}
      />
      {text && <StreamRenderer fullText={text} speed={40} />}
    </div>
  );
}

function AbortDemo() {
  const { isRequesting, result, startRequest, abortRequest } = useAbortController();
  return (
    <div className="abort-demo">
      <p>模拟一个 3 秒的 API 请求，可以随时取消。</p>
      <div className="btn-group">
        <button onClick={startRequest} disabled={isRequesting}>
          {isRequesting ? '请求中...' : '发起请求'}
        </button>
        <button onClick={abortRequest} disabled={!isRequesting} className="btn-danger">
          取消请求
        </button>
      </div>
      {result && (
        <div className={`result ${result.includes('success') ? 'success' : 'cancelled'}`}>
          {result}
        </div>
      )}
    </div>
  );
}

function MarkdownDemo() {
  const [text, setText] = useState(DEMO_TEXT);
  return (
    <div className="markdown-demo">
      <div className="editor-pane">
        <h3>Markdown 输入</h3>
        <textarea value={text} onChange={(e) => setText(e.target.value)} rows={15} />
      </div>
      <div className="preview-pane">
        <h3>渲染预览</h3>
        <MarkdownRenderer content={text} />
      </div>
    </div>
  );
}

function generateDemoMessages() {
  return [
    { id: 1, role: 'user', content: '什么是 React？' },
    { id: 2, role: 'assistant', content: 'React 是 Facebook 开发的用于构建用户界面的 JavaScript 库。它采用组件化开发模式，使用虚拟 DOM 来提高性能。' },
    { id: 3, role: 'user', content: '虚拟 DOM 是怎么工作的？' },
    { id: 4, role: 'assistant', content: '虚拟 DOM 是真实 DOM 的轻量级副本。当状态变化时，React 会：\n1. 创建新的虚拟 DOM 树\n2. 与旧树做 diff 比较\n3. 只更新真正变化的部分到真实 DOM' },
    { id: 5, role: 'user', content: '有什么性能优化的技巧吗？' },
    { id: 6, role: 'assistant', content: '常见的 React 性能优化方法：\n- **React.memo** 避免不必要的重渲染\n- **useMemo / useCallback** 缓存计算结果和函数\n- **虚拟列表** 处理大量数据\n- **代码分割** 按需加载组件' },
  ];
}

export default function App() {
  const [active, setActive] = useState(1);

  return (
    <div className="app">
      <header className="app-header">
        <h1>AI Chat Practice</h1>
        <p className="subtitle">React AI 聊天界面常见模式练习</p>
      </header>

      <nav className="exercise-nav">
        {EXERCISES.map((ex) => (
          <button
            key={ex.id}
            className={active === ex.id ? 'active' : ''}
            onClick={() => setActive(ex.id)}
          >
            <span className="ex-num">{ex.id}</span>
            <span className="ex-name">{ex.name}</span>
          </button>
        ))}
      </nav>

      <main className="exercise-content">
        {active === 1 && <ChatDemo />}
        {active === 2 && <StreamDemo />}
        {active === 3 && <AutoScrollList messages={generateDemoMessages()} />}
        {active === 4 && <AbortDemo />}
        {active === 5 && <MarkdownDemo />}
      </main>
    </div>
  );
}
