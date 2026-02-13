# 🧬 小O 图标映射协议 (Image Key Mapping)

## 1. 核心映射表 (Lucide -> Feishu)
| 功能模块 | Lucide SVG 路径 | Feishu Image Key (Pending) | 样式建议 |
| :--- | :--- | :--- | :--- |
| **运行状态** | `activity.svg` | `img_v3_...` | 品牌蓝 (Primary) |
| **知识/记忆** | `database.svg` | `img_v3_...` | 灰色 (Secondary) |
| **系统负载** | `cpu.svg` | `img_v3_...` | 橙色 (Warning) |
| **联网检索** | `search.svg` | `img_v3_...` | 绿色 (Success) |
| **快速指令** | `zap.svg` | `img_v3_...` | 紫色 (Action) |

## 2. 自动化同步机制
- **上传触发**：当检测到 `icons/` 目录更新或新功能上线时，由 `sessions_spawn` 调用飞书上传接口获取 `image_key`。
- **本地缓存**：将映射关系持久化至 `memory/icon_map.json`，避免重复上传消耗资源。
- **Schema 2.0 集成**：在卡片中通过 `img` 标签的 `img_key` 字段进行引用，替换 Emoji。

## 3. 待办任务
- [ ] 编写 Python 脚本调用 `lark-oapi` 批量上传图标。
- [ ] 完成 `img_v3` 映射关系注入。
- [ ] 更新仪表盘，将 Emoji 彻底替换为线性图标。
