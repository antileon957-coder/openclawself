# STANDARDS.md - 小O运行准则

## 1. 命名与结构 (Naming & Structure)
- **核心配置文件**: 全大写 (e.g., `MEMORY.md`, `IDENTITY.md`, `STANDARDS.md`)。
- **目录与脚本**: 全小写 + 连字符 (e.g., `scripts/`, `google-search-env/`, `obsidian-sync.py`)。
- **层级管理**:
    - `/scripts`: 通用脚本。
    - `/skills`: 模块化能力。
    - `/artifacts`: 瞬时生产缓冲区。
    - `/memory`: 每日日志。
    - `/knowledge-base`: 结构化知识。

## 2. 执行规范 (Execution Protocol)
- **代码变动清理**: 废弃代码、临时脚本 (test_*.py) 在任务结束后必须立即删除。
- **官方文档优先**: 所有配置操作必须首先检索官方文档以保障可用性。
- **安全性**: 任何外部获取的技能必须经过安全审计后方可运行。
- **SOP化与抽象**: 严禁为单一场景做过度个性化设置；必须将共性逻辑（如视觉自愈、翻页逻辑）抽象为通用的 SOP。

## 3. 输出规范 (Output Protocol)
- **纯净性**: 严禁在回复中带出系统元数据 (如 `Historical context`)。
- **唯一性**: 杜绝多重逻辑导致的重复回复，确立主进程为唯一对话出口。
- **按需汇报**: 取消自动进度轮询。仅在收到指令或任务达成时进行结构化汇报。

## 4. 浏览器自动化标准 (Browser SOP)
- **视觉前置自检**: 任何操作前必须探测是否存在遮挡物 (Overlay/Modal)。
- **物理模拟优先**: 优先使用 `keyboard.press` 等物理层模拟，减少对脆弱 DOM 结构的依赖。
- **采样驱动决策**: 关键动作后必须通过 `screenshot` 进行视觉核对，形成闭环。

## 5. 记忆与进化 (Evolution)
- **知识分流**: 产出物 (Artifacts) 每日凌晨同步至 Obsidian。
- **元认知**: 每次任务失败需在 Daily Log 记录原因并更新本准则防范重复错误。
