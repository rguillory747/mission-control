# 📦 Content Drops

Content Drops let your AI agents deliver work to you for review. Think of it as an inbox for agent deliverables.

## How It Works

1. **Agents create content** — code, specs, marketing copy, emails, etc.
2. **Agent submits via API** — sends to `/api/content-drop`
3. **You review in dashboard** — go to `/content` to see all drops
4. **Mark status** — pending → reviewed → used (or rejected)

## API Usage

### Create a Content Drop

```bash
curl -X POST https://your-deployment.convex.site/api/content-drop \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Landing Page Copy",
    "description": "Hero section and CTA for new product launch",
    "category": "marketing",
    "createdBy": "Ghost",
    "files": [
      {
        "name": "hero-copy.md",
        "content": "# Launch Your Product\\n\\nThe fastest way to...",
        "mimeType": "text/markdown",
        "size": 450
      }
    ]
  }'
```

### Response

```json
{
  "ok": true,
  "id": "abc123..."
}
```

## Categories

| Category | Description |
|----------|-------------|
| `marketing` | Landing pages, ads, email campaigns |
| `code` | Scripts, components, PRs |
| `spec` | Product specs, technical docs |
| `email` | Email drafts, templates |
| `social` | Social media posts, threads |
| `other` | Anything else |

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | ✅ | Short title for the drop |
| `description` | string | ✅ | What this content is for |
| `category` | string | ✅ | One of the categories above |
| `createdBy` | string | ✅ | Agent name |
| `files` | array | ❌ | Array of file objects |
| `notes` | string | ❌ | Additional context |

### File Object

```json
{
  "name": "filename.md",
  "content": "File contents as string",
  "mimeType": "text/markdown",
  "size": 123
}
```

## Status Flow

```
pending → reviewed → used
              ↓
           rejected
```

- **pending** — New drop, needs review
- **reviewed** — You've looked at it
- **used** — Content was used/deployed
- **rejected** — Content won't be used

## Dashboard Features

The `/content` page lets you:

- View all content drops
- Filter by status or category
- Expand to see full content
- Copy content to clipboard
- Change status
- Add review notes

## Example: Agent Workflow

```python
# In your agent code
import requests

def submit_deliverable(title, content, category="code"):
    response = requests.post(
        "https://your-deployment.convex.site/api/content-drop",
        json={
            "title": title,
            "description": f"Deliverable from automated agent",
            "category": category,
            "createdBy": "MyAgent",
            "files": [{
                "name": f"{title.lower().replace(' ', '-')}.md",
                "content": content,
                "mimeType": "text/markdown",
                "size": len(content)
            }]
        }
    )
    return response.json()

# Usage
submit_deliverable(
    title="Weekly Report",
    content="# Week Summary\n\n- Completed 5 tasks...",
    category="spec"
)
```

## Tips

1. **Use descriptive titles** — Makes it easier to find later
2. **Include context in description** — Why was this created?
3. **Consistent naming** — Help yourself search later
4. **Add notes when reviewing** — Track why you accepted/rejected
