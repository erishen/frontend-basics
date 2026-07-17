# Frontend Basics · 面试手写代码练习

多语言面试手写题练习库，覆盖前端/后端常见考点与 AI 场景。

## 结构

```
├── docs/                  # 面试速查文档
│   ├── typescript.md      # TypeScript 完整参考（1183 行）
│   ├── javascript-brief.md
│   ├── typescript-brief.md
│   ├── python-brief.md
│   ├── fastapi-brief.md
│   ├── leetcode-brief.md
│   ├── coding-templates.md          # 17 道 JS 手写模板
│   ├── python-coding-templates.md
│   ├── ai-python-coding-templates.md # AI 场景 Python 模板
│   ├── go-coding-templates.md
│   └── java-coding-templates.md
│
├── coding-practice/       # JavaScript 手写练习（17 题）
├── python-practice/       # Python 手写练习（22 题，含 AI 场景）
├── go-practice/           # Go 手写练习（12 题）
├── java-practice/         # Java 手写练习（12 题）
├── fastapi-practice/      # FastAPI 练习（12 题）
├── leetcode-practice/     # LeetCode 算法（16 题）
└── ai-chat-practice/      # React AI Chat UI 练习（5 题）
```

## 练习方式

每个练习项目统一为 `src/`（TODO 模板）→ `tests/`（验证）→ `solutions/`（参考实现）三件套：

```bash
# JavaScript
cd coding-practice && node --test tests/*.test.js

# Python
cd python-practice && pytest

# Java
cd java-practice && mvn test

# Go
cd go-practice && go run solutions/ex01_lru_cache.go

# FastAPI
cd fastapi-practice && pytest

# LeetCode
cd leetcode-practice && node --test tests/*.test.js

# AI Chat UI
cd ai-chat-practice && npm run dev
```
