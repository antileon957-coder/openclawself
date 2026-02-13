# Daily Skill Learning Log

## 2026-02-11 - 3:00 AM

### Skills Learned Today:

1. **feishu-perm** - Feishu Permission Management
2. **skill-creator** - Skill Creation and Packaging

---

### 1. feishu-perm Skill

**Purpose**: Manage sharing permissions for Feishu documents, files, and folders.

**Key Capabilities**:
- List collaborators on any Feishu resource (doc, docx, sheet, bitable, folder, file, wiki, mindnote)
- Add collaborators with specific permission levels (view/edit/full_access)
- Remove collaborators from resources

**Token Types Supported**:
- `doc` - Old format document
- `docx` - New format document  
- `sheet` - Spreadsheet
- `bitable` - Multi-dimensional table
- `folder` - Folder
- `file` - Uploaded file
- `wiki` - Wiki node
- `mindnote` - Mind map

**Member Types**:
- `email` - Email address
- `openid` - User open_id
- `userid` - User user_id
- `unionid` - User union_id
- `openchat` - Group chat open_id
- `opendepartmentid` - Department open_id

**Permission Levels**:
- `view` - View only
- `edit` - Can edit
- `full_access` - Full access (can manage permissions)

**Security Note**: This tool is disabled by default because permission management is sensitive. Must be explicitly enabled in config:
```yaml
channels:
  feishu:
    tools:
      perm: true
```

**Required Permission**: `drive:permission`

**Example Usage**:
```json
{
  "action": "add",
  "token": "doxcnXXX",
  "type": "docx",
  "member_type": "email",
  "member_id": "alice@company.com",
  "perm": "edit"
}
```

---

### 2. skill-creator Skill

**Purpose**: Create or update AgentSkills with proper structure, packaging, and best practices.

**Core Philosophy**: Skills transform Codex from general-purpose to specialized by providing:
- Specialized workflows for specific domains
- Tool integrations for specific file formats/APIs
- Domain expertise (company knowledge, schemas, business logic)
- Bundled resources (scripts, references, assets)

**Skill Anatomy**:
```
skill-name/
├── SKILL.md (required - YAML frontmatter + markdown instructions)
└── Bundled Resources (optional):
    ├── scripts/    - Executable code (Python/Bash/etc.)
    ├── references/ - Documentation loaded as needed
    └── assets/     - Files used in output (templates, icons, etc.)
```

**Progressive Disclosure Principle**:
1. **Metadata** (name + description) - Always in context (~100 words)
2. **SKILL.md body** - When skill triggers (<5k words)
3. **Bundled resources** - As needed by Codex

**Skill Creation Process**:
1. **Understand** the skill with concrete examples
2. **Plan** reusable skill contents (scripts, references, assets)
3. **Initialize** the skill (run `init_skill.py`)
4. **Edit** the skill (implement resources and write SKILL.md)
5. **Package** the skill (run `package_skill.py`)
6. **Iterate** based on real usage

**Key Design Principles**:
- **Concise is Key**: Challenge each piece of information - "Does Codex really need this?"
- **Set Appropriate Degrees of Freedom**: Match specificity to task fragility
- **Avoid Duplication**: Information should live in either SKILL.md OR references, not both
- **No Extraneous Docs**: Don't include README.md, INSTALLATION_GUIDE.md, etc.

**Progressive Disclosure Patterns**:
- **High-level guide with references**: Keep core in SKILL.md, details in separate files
- **Domain-specific organization**: Organize by domain to avoid loading irrelevant context
- **Conditional details**: Show basic content, link to advanced content

**Important Scripts**:
- `init_skill.py` - Creates template skill directory
- `package_skill.py` - Validates and packages skill into .skill file

**Naming Convention**: Lowercase letters, digits, hyphens only (e.g., "plan-mode")

---

### Insights & Best Practices:

1. **Feishu Permission Security**: Permission tools are disabled by default due to sensitivity - requires explicit config enablement.

2. **Skill Context Efficiency**: The progressive disclosure system is crucial for managing context windows effectively. Only load what's needed when it's needed.

3. **Skill Validation**: The packaging script automatically validates skills before distribution, ensuring quality and completeness.

4. **Resource Organization**: References should be one level deep from SKILL.md with clear linking to avoid deep nesting.

5. **Testing Requirement**: Added scripts must be tested before inclusion to ensure they work as expected.

### Caveats:
- Feishu permission tool requires specific scopes (`drive:permission`) and explicit enablement
- Skill creation requires understanding of both the domain AND how Codex works with skills
- Reference files >100 lines should include a table of contents for preview visibility
- Always test scripts before including them in skills

### Application Notes:
- **Feishu-perm**: Useful for collaborative document management in Feishu ecosystem
- **Skill-creator**: Meta-skill essential for expanding OpenClaw's capabilities through skill development

## 2026-02-12 - 3:00 AM

### Skills Learned Today:

1. **weather** - Weather forecasts (no API key required)
2. **imsg** - iMessage/SMS CLI for macOS

---

### 1. weather Skill

**Purpose**: Quick weather retrieval via `wttr.in` or `Open-Meteo`.

**Key Capabilities**:
- `wttr.in`: Terminal-friendly text or ANSI output. Supports specific formats, units, and PNG generation.
- `Open-Meteo`: JSON API for programmatic use, requires coordinates.

**Usage Tips**:
- Use `curl -s "wttr.in/City?format=3"` for a concise one-liner.
- URL-encode spaces: `New+York`.
- Add `?m` for metric, `?u` for USCS.

**Caveats**:
- Service stability: Third-party services like `wttr.in` may occasionally time out or block high-frequency requests.
- Connectivity: Requires outbound internet access (port 443).

---

### 2. imsg Skill

**Purpose**: Programmatic access to macOS Messages.app (read/send).

**Key Capabilities**:
- List recent chats (`imsg chats`).
- Fetch history/watch streams (`imsg history`, `imsg watch`).
- Send text and attachments (`imsg send`).

**Usage Tips**:
- Requires **Full Disk Access** and **Automation** permissions on macOS.
- Always use `--json` for robust tool parsing.
- Confirm recipient handles before sending.

**Caveats**:
- Version Drift: The local `imsg` binary may differ from the documentation (e.g., the Ruby gem version `imessage` vs the Go version `imsg`).
- Environment: Only works on macOS (`darwin`).

---

### Insights & Best Practices:

1. **Graceful Failures**: Network-dependent tools (weather) should have timeouts or fallbacks.
2. **Permission Awareness**: macOS CLI tools (imsg) often require manual system-level permission grants that cannot be automated via shell.
3. **Documentation Sync**: Local binaries might be aliases to different implementations (e.g., `imsg` pointing to an older Ruby-based `imessage` gem), leading to argument mismatches. Always check `--help`.

### Caveats:
- `wttr.in` can be flakey behind certain proxies or in restricted environments.
- `imsg` requires the Messages.app to be signed in and active on the host.
