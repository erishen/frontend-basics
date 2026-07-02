/**
 * 练习 5: MarkdownRenderer 简易 Markdown 渲染
 * 将 LLM 输出的 Markdown 渲染为 HTML
 *
 * 要求（不依赖第三方库）：
 * - 支持标题 (# ## ###)
 * - 支持粗体 (**text**) 和斜体 (*text*)
 * - 支持行内代码 (`code`)
 * - 支持代码块 (```lang\n...\n```)
 * - 支持无序列表 (- item)
 * - 支持链接 ([text](url))
 */

export function parseMarkdown(md) {
  // TODO: 将 Markdown 字符串转换为 HTML 字符串
  // 提示：按行处理，先处理代码块，再处理行内元素
  return '';
}

export function MarkdownRenderer({ content }) {
  // TODO: 调用 parseMarkdown 转换 content
  // TODO: 用 dangerouslySetInnerHTML 渲染
  return <div className="markdown-body" />;
}
