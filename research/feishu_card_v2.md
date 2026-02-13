# 飞书卡片视觉优化研究报告 (2026-02-12)

## 1. 核心发现
- **200672 修复确认**：WebSocket 模式下 `card.action.trigger` 响应已稳定，不再需要 Bot Menu 作为兜底。
- **视觉层级 (Hierarchy)**：应大量使用 `horizontal_rule` 和 `column_set` 减少纵向堆叠感。
- **人性化交互**：所有高频指令（/new, /status, /clear）应作为卡片底部的 `button` 组存在，而非要求用户输入。

## 2. 实验性卡片 JSON 结构 (System Control)
(详细代码已沉淀至后台逻辑库)

## 3. 待办事项
- [ ] 将所有系统通知升级为交互式卡片。
- [ ] 测试 Multi-select 在自动化流中的配置效率。
