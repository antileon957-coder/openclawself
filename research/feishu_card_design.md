# Feishu Card Design Best Practices: Minimalist & Dark Mode

This guide outlines design principles and JSON Schema 1.0 examples for creating sophisticated, minimalist Feishu (Lark) message cards, optimized for dark mode environments.

## Design Principles

### 1. Minimalist Layout
*   **"One Card, One Purpose"**: Avoid clutter. A card should deliver one key insight or action.
*   **Breathing Room**: Use vertical spacing (empty text blocks or `div` elements with minimal content) instead of heavy horizontal lines (`hr`).
*   **Grid Systems**: Use `column_set` to align data side-by-side (e.g., "Status" vs "Owner") rather than long vertical lists. This reduces visual scroll fatigue.
*   **Ghost Buttons**: Prefer "default" style buttons (outlines) over "primary" (solid fills) for secondary actions to reduce visual weight.

### 2. Sophisticated Color Usage (Dark Mode First)
*   **Avoid Pure Black**: Feishu handles the card background, but if embedding images, use deep charcoal (`#1D1D1F`) instead of `#000000`.
*   **Text Hierarchy via Opacity**:
    *   **Primary Text**: `#EBEBEB` (High emphasis)
    *   **Secondary Text**: `#A1A1A1` (Medium emphasis, meta-data)
    *   **Disabled/Tertiary**: `#646464` (Low emphasis)
*   **Header Colors**:
    *   **Minimalist**: Use `"template": "grey"` or `"default"` to blend with the dark theme.
    *   **Status Indicators**: Use colored headers *only* for status alerts (e.g., `red` for error, `green` for success, `blue` for info).
*   **Desaturated Accents**: Avoid neon colors. Use muted tones that don't vibrate against dark backgrounds.

### 3. Typography & Visuals
*   **Markdown Hierarchy**: Use `**Bold**` sparingly for key metrics.
*   **Icons**: Use single-color (monochrome) transparent PNGs. White or light gray icons look best.
*   **No "Haloing"**: Ensure images have transparent backgrounds, not white boxes.

---

## JSON Schema 1.0 Examples

### Example 1: Minimalist Notification
*A clean, single-purpose alert with a subtle header and one primary action.*

```json
{
  "config": {
    "wide_screen_mode": true
  },
  "header": {
    "template": "grey",
    "title": {
      "tag": "plain_text",
      "content": "Deployment Successful"
    }
  },
  "elements": [
    {
      "tag": "div",
      "text": {
        "tag": "lark_md",
        "content": "**Service:** `auth-service`\n**Version:** `v2.4.0`\n\nThe update has been rolled out to all production nodes."
      }
    },
    {
      "tag": "action",
      "actions": [
        {
          "tag": "button",
          "text": {
            "tag": "plain_text",
            "content": "View Logs"
          },
          "type": "default",
          "url": "https://logging.example.com/deployment/123"
        }
      ]
    },
    {
      "tag": "note",
      "elements": [
        {
          "tag": "plain_text",
          "content": "Deployed by @taylor at 14:05"
        }
      ]
    }
  ]
}
```

### Example 2: Data Summary Dashboard
*Uses `fields` for a structured, grid-like layout without visual clutter.*

```json
{
  "config": {
    "wide_screen_mode": true
  },
  "header": {
    "template": "blue",
    "title": {
      "tag": "plain_text",
      "content": "Daily Sales Report"
    }
  },
  "elements": [
    {
      "tag": "div",
      "fields": [
        {
          "is_short": true,
          "text": {
            "tag": "lark_md",
            "content": "**Total Revenue**\n$12,450.00"
          }
        },
        {
          "is_short": true,
          "text": {
            "tag": "lark_md",
            "content": "**New Users**\n+145"
          }
        }
      ]
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
            "content": "**Top Region**\nNorth America"
          }
        },
        {
          "is_short": true,
          "text": {
            "tag": "lark_md",
            "content": "**Conversion Rate**\n3.2%"
          }
        }
      ]
    },
    {
      "tag": "note",
      "elements": [
        {
          "tag": "plain_text",
          "content": "Generated automatically • 10 mins ago"
        }
      ]
    }
  ]
}
```

## Implementation Checklist
- [ ] Set `"wide_screen_mode": true` in `config` to utilize full width.
- [ ] Check text contrast in Feishu's "Dark Mode" preview.
- [ ] Verify that all interactive elements (buttons) have valid `url` or `value` payloads.
- [ ] Keep `fields` count to 2-3 per row for readability on mobile.
