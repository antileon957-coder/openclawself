# Feishu/Lark Message Card Design Research

## 1. Design Best Practices

Effective message cards in Feishu/Lark should balance information density with clear visual hierarchy and actionable elements.

### Visual Hierarchy
- **Header Usage**: Use the `header` component with a colored `template` to immediately convey the message context or urgency (e.g., `red` for alerts, `green` for success, `blue` for info).
- **Structured Data**: Avoid walls of text. Use `fields` within `div` elements or `column_set` layouts to present key-value pairs (like metrics or properties) in a grid.
- **Emphasis**: Use **bold** text and emojis in `lark_md` to highlight critical numbers or status keywords.
- **Separators**: Use `hr` elements to distinct sections (e.g., separating the status summary from the detailed metrics or actions).
- **Footers**: Use the `note` component for secondary metadata like timestamps, IDs, or attribution.

### Interaction Design
- **Primary vs. Secondary**: Use `type: "primary"` for the main call-to-action (CTA) and `default` for secondary actions. Use `danger` only for destructive actions.
- **Grouping**: Group related buttons in a single `action` container. If actions are distinct (e.g., "Approve/Reject" vs "View Details"), consider separating them or using an `overflow` menu for less common tasks.
- **Confirmation**: Always add a `confirm` property to destructive buttons (like "Delete" or "Restart") to prevent accidental clicks.
- **Feedback**: Ensure the backend updates the card (via `patch` or ephemeral reply) after an interaction to acknowledge the user's action immediately.

## 2. Interactive Components

### Buttons (`button`)
- Used for triggering immediate actions or navigation (`url`, `multi_url`).
- Supports `value` payload for backend processing.
- Styles: `default`, `primary`, `danger`.

### Select Menus (`select_static`, `select_person`)
- **Static**: Dropdown for predefined options. Good for status changes or filters.
- **Person**: Native user picker. Great for assigning tasks.
- **Multi-select**: Enable `mode: "multiple"` (if supported by specific component version) or standard single select. Note: Native multi-select UI availability varies; standard practice is often a `select_static` or `overflow`.

### Date/Time Pickers (`date_picker`, `datetime_picker`)
- Native UI for selecting dates/times.
- Useful for scheduling or filtering logs.

### Overflow Menu (`overflow`)
- The "..." button. Compresses multiple secondary actions into a dropdown to save space.

## 3. Example: System Status & Control Card

This example demonstrates a "System Status" alert with a rich layout and multiple interactive controls.

```json
{
  "config": {
    "wide_screen_mode": true
  },
  "header": {
    "template": "red",
    "title": {
      "content": "🚨 System Alert: High Load Detected",
      "tag": "plain_text"
    }
  },
  "elements": [
    {
      "tag": "div",
      "text": {
        "content": "**Node:** `production-db-01`\n**Region:** `us-east-1`\nDetected sustained CPU usage > 90% for 5 minutes.",
        "tag": "lark_md"
      }
    },
    {
      "tag": "hr"
    },
    {
      "tag": "div",
      "fields": [
        {
          "is_short": true,
          "text": {
            "tag": "lark_md",
            "content": "**CPU Load**\n🔴 94%"
          }
        },
        {
          "is_short": true,
          "text": {
            "tag": "lark_md",
            "content": "**Memory**\n🟡 76%"
          }
        },
        {
          "is_short": true,
          "text": {
            "tag": "lark_md",
            "content": "**Disk I/O**\n🟢 120 IOPS"
          }
        }
      ]
    },
    {
      "tag": "hr"
    },
    {
      "tag": "div",
      "text": {
        "content": "🛠 **Remediation Actions**",
        "tag": "lark_md"
      }
    },
    {
      "tag": "action",
      "actions": [
        {
          "tag": "button",
          "text": {
            "content": "View Logs",
            "tag": "plain_text"
          },
          "type": "default",
          "value": {
            "action": "view_logs",
            "node": "production-db-01"
          }
        },
        {
          "tag": "select_static",
          "placeholder": {
            "content": "Change Log Level",
            "tag": "plain_text"
          },
          "value": {
            "action": "set_log_level"
          },
          "options": [
            {
              "text": {
                "content": "DEBUG",
                "tag": "plain_text"
              },
              "value": "debug"
            },
            {
              "text": {
                "content": "INFO",
                "tag": "plain_text"
              },
              "value": "info"
            },
            {
              "text": {
                "content": "WARN",
                "tag": "plain_text"
              },
              "value": "warn"
            }
          ]
        },
        {
          "tag": "button",
          "text": {
            "content": "Restart Service",
            "tag": "plain_text"
          },
          "type": "danger",
          "confirm": {
            "title": {
              "content": "Confirm Restart",
              "tag": "plain_text"
            },
            "text": {
              "content": "Are you sure you want to restart the database service? This will cause brief downtime.",
              "tag": "plain_text"
            }
          },
          "value": {
            "action": "restart_service",
            "node": "production-db-01"
          }
        }
      ]
    },
    {
      "tag": "hr"
    },
    {
      "tag": "note",
      "elements": [
        {
          "tag": "plain_text",
          "content": "Incident ID: #INC-20260212-001 • Updated: 22:24 GMT+8"
        }
      ]
    }
  ]
}
```

### Key Implementation Details
- **`config.wide_screen_mode`**: Always set to `true` for better layout on desktop.
- **`fields`**: Used inside the metric `div` with `is_short: true` to create a 3-column grid effect.
- **`confirm`**: Added to the "Restart Service" button to provide a safety modal.
- **`select_static`**: Embedded directly in the action row for quick configuration changes without leaving the chat.
