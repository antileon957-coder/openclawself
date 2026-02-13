# 自主进化引擎设计文档 (Autonomy Engine Design Doc)

## 1. 概述
本系统旨在构建一个具备自我驱动、知识沉淀和持续进化能力的 Agent 框架。通过“驱动核心-知识图谱-任务调度”三位一体的设计，实现从被动响应指令到主动探索学习的范式转变。

## 2. 核心组件

### 2.1 自我驱动核心 (The Driver)
`autonomy.py` 是引擎的大脑。
- **职责**: 扫描记忆 -> 规划任务 -> 调度执行 -> 沉淀知识。
- **逻辑流**:
  1. 读取 `MEMORY.md` 识别 `- [ ]` 标记的盲区。
  2. 针对盲区生成学习 Prompt。
  3. (模拟) 调用能力组件获取信息（搜索/文档/工具自省）。
  4. 生成 Markdown 格式的知识条目。
  5. 更新 `MEMORY.md` 状态为 `- [x]`。

### 2.2 知识沉淀机制 (Knowledge Graph)
采用文件系统作为轻量级知识库，便于 Git 管理和人类阅读。
- **存储路径**: `./KNOWLEDGE_BASE/`
- **文件格式**: Markdown
- **结构规范**:
  - `Title`: 知识点名称
  - `Overview`: 简要说明
  - `Key Concepts/Actions`: 核心要素
  - `Usage Examples`: 代码或操作示例
  - `Pitfalls`: 常见错误与注意事项

### 2.3 任务调度 (Cron Integration)
利用系统级 Cron 确保 Agent 即使在无交互时也能定期“醒来”工作。

**Crontab 配置示例**:
```bash
# 每小时第 30 分钟检查一次知识盲区
30 * * * * cd /home/node/.openclaw/workspace && python3 autonomy.py --check-updates >> autonomy.log 2>&1
```

## 3. 实战验证报告

### 3.1 初始状态
- **任务**: 学习 OpenClaw `canvas` 工具的高级用法。
- **Memory**: `MEMORY.md` 中包含待办项。

### 3.2 执行过程
1. `autonomy.py` 启动，检测到未完成任务。
2. 模拟调用工具自省（在本例中，基于内置工具定义进行分析）。
3. 提取出 `canvas` 的关键动作：`eval` (JS执行), `snapshot` (视觉回传), `a2ui` (UI 生成)。
4. 生成知识文档 `KNOWLEDGE_BASE/openclaw_canvas.md`。
5. 更新 `MEMORY.md` 标记任务完成。

### 3.3 产出物
- **脚本**: `autonomy.py` (已在当前目录创建)
- **知识库**: `KNOWLEDGE_BASE/openclaw_canvas.md` (自动生成)
- **记忆**: `MEMORY.md` (状态已更新)

## 4. 附录：核心代码 (`autonomy.py`)
(见 workspace 中的文件)
