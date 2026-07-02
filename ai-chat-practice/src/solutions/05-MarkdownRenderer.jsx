export function parseMarkdown(md) {
  if (!md) return '';

  let html = md;

  // 代码块 ```lang\n...\n```
  html = html.replace(/```(\w*)\n([\s\S]*?)```/g, (_, lang, code) => {
    return `<pre><code class="language-${lang}">${escapeHtml(code.trim())}</code></pre>`;
  });

  // 按行处理
  const lines = html.split('\n');
  const result = [];
  let inList = false;

  for (let i = 0; i < lines.length; i++) {
    let line = lines[i];

    // 跳过已处理的 pre 标签行
    if (line.includes('<pre>')) {
      result.push(line);
      continue;
    }

    // 标题
    if (line.startsWith('### ')) {
      if (inList) { result.push('</ul>'); inList = false; }
      result.push(`<h3>${processInline(line.slice(4))}</h3>`);
      continue;
    }
    if (line.startsWith('## ')) {
      if (inList) { result.push('</ul>'); inList = false; }
      result.push(`<h2>${processInline(line.slice(3))}</h2>`);
      continue;
    }
    if (line.startsWith('# ')) {
      if (inList) { result.push('</ul>'); inList = false; }
      result.push(`<h1>${processInline(line.slice(2))}</h1>`);
      continue;
    }

    // 无序列表
    if (line.startsWith('- ') || line.startsWith('* ')) {
      if (!inList) { result.push('<ul>'); inList = true; }
      result.push(`<li>${processInline(line.slice(2))}</li>`);
      continue;
    }

    // 关闭列表
    if (inList) { result.push('</ul>'); inList = false; }

    // 空行
    if (line.trim() === '') {
      result.push('');
      continue;
    }

    // 普通段落
    result.push(`<p>${processInline(line)}</p>`);
  }

  if (inList) result.push('</ul>');
  return result.join('\n');
}

function escapeHtml(str) {
  return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function processInline(text) {
  // 行内代码
  text = text.replace(/`([^`]+)`/g, '<code>$1</code>');
  // 粗体
  text = text.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  // 斜体
  text = text.replace(/\*(.+?)\*/g, '<em>$1</em>');
  // 链接
  text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank">$1</a>');
  return text;
}

export function MarkdownRenderer({ content }) {
  const html = parseMarkdown(content);
  return <div className="markdown-body" dangerouslySetInnerHTML={{ __html: html }} />;
}
