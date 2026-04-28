---
name: claude-flow
description: "Enterprise AI orchestration platform for coordinating 16 specialized agent roles in swarms with fault-tolerant consensus"
---

Claude Flow
Editor's Note
Claude Flow (RuFlo v3.5) is an enterprise AI orchestration platform that enables deployment and coordination of 16 specialized agent roles working in swarms with self-learning and fault-tolerant consensus capabilities. The server provides tools for multi-agent orchestration, policy engines, embeddings, and proof systems powered by Rust-based WASM kernels, solving the problem of coordinating complex AI-driven software engineering tasks across distributed teams. It integrates with Claude Code and offers enterprise-grade security features alongside self-optimizing agent capabilities.

Install
claude mcp add --transport stdio ruvnet-claude-flow uvx claude-flow

Getting into the Flow
Ruflo is a comprehensive AI agent orchestration framework that transforms Claude Code into a powerful multi-agent development platform. It enables teams to deploy, coordinate, and optimize specialized AI agents working together on complex software engineering tasks.

Self-Learning / Self-Optimizing Agent Architecture

User --> Ruflo (CLI/MCP) --> Router --> Swarm --> Agents --> Memory --> LLM Providers
                          ^                           |
                          +---- Learning Loop <-------+
New to Ruflo? You don't need to learn 314 MCP tools or 26 CLI commands. After init, just use Claude Code normally -- the hooks system automatically routes tasks, learns from successful patterns, and coordinates agents in the background.

Quick Start
Claude Code Plugin (Recommended)
Install Ruflo as a native Claude Code plugin -- adds skills, commands, agents, and MCP tools directly:

# Add the marketplace
/plugin marketplace add ruvnet/ruflo

# Install core + any plugins you need
/plugin install ruflo-core@ruflo
/plugin install ruflo-swarm@ruflo
/plugin install ruflo-autopilot@ruflo
All 20 plugins
CLI Install
# One-line install
curl -fsSL https://cdn.jsdelivr.net/gh/ruvnet/ruflo@main/scripts/install.sh | bash

# Or via npx
npx ruflo@latest init --wizard

# Or install globally
npm install -g ruflo@latest
MCP Server
# Add Ruflo as an MCP server in Claude Code
claude mcp add ruflo -- npx -y @claude-flow/cli@latest
What You Get
Capability	Description
🤖 100+ Agents	Specialized agents for coding, testing, security, docs, architecture
🐝 Swarm Coordination	Hierarchical, mesh, and adaptive topologies with consensus
🧠 Self-Learning	SONA neural patterns, ReasoningBank, trajectory learning
💾 Vector Memory	HNSW-indexed AgentDB with 150x-12,500x faster search
⚡ Background Workers	12 auto-triggered workers (audit, optimize, testgaps, etc.)
🧩 Plugin Marketplace	20 native Claude Code plugins + 20 npm plugins
🔌 Multi-Provider	Claude, GPT, Gemini, Cohere, Ollama with smart routing
🛡️ Security	AIDefence, input validation, CVE remediation, path traversal prevention
Claude Code: With vs Without Ruflo
Architecture overview
Documentation
Full documentation including architecture, configuration, CLI reference, API usage, plugin development, and advanced topics:

User Guide -- Complete reference documentation

Section	Topics
Quick Start	Installation, prerequisites, install profiles
Core Features	MCP tools, agents, memory, neural learning
Intelligence & Learning	Hooks, workers, SONA, model routing
Swarm & Coordination	Topologies, consensus, hive mind
Security	AIDefence, CVE remediation, validation
Ecosystem	RuVector, agentic-flow, Flow Nexus
Configuration	Environment variables, config schema
Plugin Marketplace	Browse and install plugins
Support
Resource	Link
Documentation	User Guide
Issues & Bugs	GitHub Issues
Enterprise	ruv.io
Community	Agentics Foundation Discord
Powered by	Cognitum.one