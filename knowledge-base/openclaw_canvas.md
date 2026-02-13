# OpenClaw Canvas Tool Advanced Usage

## Overview
The `canvas` tool allows for controlling node canvases, capable of rendering UI, executing JS, and taking snapshots.

## Key Actions
- **present/hide**: Control visibility.
- **navigate**: Go to a URL.
- **eval**: Execute arbitrary JavaScript.
- **snapshot**: Capture the rendered state.
- **a2ui_push/reset**: Advanced AI-to-UI rendering capabilities.

## Advanced Examples
### 1. Dynamic Evaluation
```python
canvas.eval(javascript="document.body.style.backgroundColor = 'red';")
```

### 2. Snapshotting for Vision
Use `snapshot` with `outputFormat='png'` to feed visual state back to the model.
