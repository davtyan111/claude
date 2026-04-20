<!-- Agent Browser

Editor's Note
A comprehensive browser automation CLI that handles the full spectrum of web interaction tasks through Chrome DevTools Protocol.
What impressed me most is the thoughtful authentication handling with six different approaches,
from importing existing browser sessions to encrypted credential vaults.
The element reference system (@e1, @e2) makes DOM interaction reliable across page changes, and command chaining keeps workflows efficient.
The network inspection and download management features push it beyond basic scraping into serious testing territory.
If you're doing any programmatic web work beyond simple HTTP requests, this covers the gap between lightweight scraping libraries and heavyweight testing frameworks like Selenium.

for install 

npx skills add https://github.com/vercel-labs/agent-browser --skill agent-browser
 -->
agent-browser
Fast browser automation CLI for AI agents. Chrome/Chromium via CDP with accessibility-tree snapshots and compact @eN element refs.

Install: npm i -g agent-browser && agent-browser install

Start here
This file is a discovery stub, not the usage guide. Before running any agent-browser command, load the actual workflow content from the CLI:

agent-browser skills get core             # start here — workflows, common patterns, troubleshooting
agent-browser skills get core --full      # include full command reference and templates
The CLI serves skill content that always matches the installed version, so instructions never go stale. The content in this stub cannot change between releases, which is why it just points at skills get core.

Specialized skills
Load a specialized skill when the task falls outside browser web pages:

agent-browser skills get electron          # Electron desktop apps (VS Code, Slack, Discord, Figma, ...)
agent-browser skills get slack             # Slack workspace automation
agent-browser skills get dogfood           # Exploratory testing / QA / bug hunts
agent-browser skills get vercel-sandbox    # agent-browser inside Vercel Sandbox microVMs
agent-browser skills get agentcore         # AWS Bedrock AgentCore cloud browsers
Run agent-browser skills list to see everything available on the installed version.

Why agent-browser
Fast native Rust CLI, not a Node.js wrapper
Works with any AI agent (Cursor, Claude Code, Codex, Continue, Windsurf, etc.)
Chrome/Chromium via CDP with no Playwright or Puppeteer dependency
Accessibility-tree snapshots with element refs for reliable interaction
Sessions, authentication vault, state persistence, video recording
Specialized skills for Electron apps, Slack, exploratory testing, cloud providers