# 🎨 飞书卡片高级视觉规范 (v4.0 - 大厂标准)

## 1. 标题与视觉层级 (Visual Hierarchy)
- **去重原则**：头部避免大面积饱和色块。采用 `template: "grey"` 或 `template: "indigo"` 的浅色调，结合 `title.content` 的品牌色点缀。
- **标签化设计 (Tagging)**：文件名（如 `MEMORY.md`）不使用括号，使用 `<at user_id="..."></at>` 或特殊的 `lark_md` 语法模拟标签感，或者使用 `column_set` 配合 `background_style: "grey"`。

## 2. 数字化表达 (Visualization)
- **进度条逻辑**：上下文使用率（如 2%）不再仅显示文字。使用 `lark_md` 模拟：`▓░░░░░░░░░ 2%` 或利用 Feishu 最新的组件能力。
- **数据突出**：标签使用“辅助文本色”，数值使用“加粗/主色”。

## 3. 布局与间距 (Spacing & Breathing)
- **模块隔离**：认知/执行/管理层之间使用 `hr` 或空的 `div` 占位符增加呼吸感。
- **分组底色**：尝试使用 `column_set` 的 `background_style` 进行逻辑分组，而非单纯靠分割线。

## 4. 图标与交互 (Icons & CTA)
- **色系统一**：图标统一采用单一色系（如实验室蓝），避免过于跳跃。
- **主次按钮**：明确 `primary` 与 `default` 的权重对比。

---
*此规范已同步至实验室执行协议。*
