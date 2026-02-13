# Google Search via Gemini 3.0 Flash

Use this skill to perform high-quality, real-time web searches using Google's Gemini 3.0 Flash model with built-in grounding. This bypasses the need for external search APIs like Brave.

## Usage

Run the python script from the workspace root using the virtual environment.

```bash
./google-search-env/bin/python3 skills/google-search/search.py "Your search query here"
```

## Configuration

Requires `search_key_google_ai_studio` environment variable (set in `openclaw.json` or system env).
Uses `google-genai` SDK v1.0+.
Model: `gemini-3-flash-preview`
