Github Mcp Server
Editor's Note
The GitHub MCP Server enables AI agents and assistants to interact with GitHub's platform through natural language, providing tools to browse and analyze repositories, manage issues and pull requests, monitor CI/CD workflows, review code security findings, and access team collaboration features. It solves the problem of connecting AI tools to GitHub context without requiring manual API integration, allowing developers to automate repository management, code analysis, and development workflows through conversational interfaces. The server is available as both a remote hosted service and a local installation option, supporting various MCP-compatible hosts including VS Code, Claude Desktop, and other AI development tools.

Install
claude mcp add --transport stdio github-github-mcp-server uvx github-mcp-server

GitHub MCP Server
The GitHub MCP Server connects AI tools directly to GitHub's platform. This gives AI agents, assistants, and chatbots the ability to read repositories and code files, manage issues and PRs, analyze code, and automate workflows. All through natural language interactions.

Use Cases
Repository Management: Browse and query code, search files, analyze commits, and understand project structure across any repository you have access to.
Issue & PR Automation: Create, update, and manage issues and pull requests. Let AI help triage bugs, review code changes, and maintain project boards.
CI/CD & Workflow Intelligence: Monitor GitHub Actions workflow runs, analyze build failures, manage releases, and get insights into your development pipeline.
Code Analysis: Examine security findings, review Dependabot alerts, understand code patterns, and get comprehensive insights into your codebase.
Team Collaboration: Access discussions, manage notifications, analyze team activity, and streamline processes for your team.
Built for developers who want to connect their AI tools to GitHub context and capabilities, from simple natural language queries to complex multi-step agent workflows.

Remote GitHub MCP Server
Install in VS CodeInstall in VS Code Insiders

The remote GitHub MCP Server is hosted by GitHub and provides the easiest method for getting up and running. If your MCP host does not support remote MCP servers, don't worry! You can use the local version of the GitHub MCP Server instead.

Prerequisites
A compatible MCP host with remote server support (VS Code 1.101+, Claude Desktop, Cursor, Windsurf, etc.)
Any applicable policies enabled
Install in VS Code
For quick installation, use one of the one-click install buttons above. Once you complete that flow, toggle Agent mode (located by the Copilot Chat text input) and the server will start. Make sure you're using VS Code 1.101 or later for remote MCP and OAuth support.

Alternatively, to manually configure VS Code, choose the appropriate JSON block from the examples below and add it to your host configuration:

Using OAuth	Using a GitHub PAT
VS Code (version 1.101 or greater)
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${input:github_mcp_pat}"
      }
    }
  },
  "inputs": [
    {
      "type": "promptString",
      "id": "github_mcp_pat",
      "description": "GitHub Personal Access Token",
      "password": true
    }
  ]
}
Install in other MCP hosts
Copilot CLI - Installation guide for GitHub Copilot CLI
GitHub Copilot in other IDEs - Installation for JetBrains, Visual Studio, Eclipse, and Xcode with GitHub Copilot
Claude Applications - Installation guide for Claude Desktop and Claude Code CLI
Codex - Installation guide for OpenAI Codex
Cursor - Installation guide for Cursor IDE
Windsurf - Installation guide for Windsurf IDE
Rovo Dev CLI - Installation guide for Rovo Dev CLI
Note: Each MCP host application needs to configure a GitHub App or OAuth App to support remote access via OAuth. Any host application that supports remote MCP servers should support the remote GitHub server with PAT authentication. Configuration details and support levels vary by host. Make sure to refer to the host application's documentation for more info.

Configuration
Toolset configuration
See Remote Server Documentation for full details on remote server configuration, toolsets, headers, and advanced usage. This file provides comprehensive instructions and examples for connecting, customizing, and installing the remote GitHub MCP Server in VS Code and other MCP hosts.

When no toolsets are specified, default toolsets are used.

Insiders Mode
Try new features early! The remote server offers an insiders version with early access to new features and experimental tools.

Using URL Path	Using Header
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/insiders"
    }
  }
}
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "X-MCP-Insiders": "true"
      }
    }
  }
}
See Remote Server Documentation for more details and examples, and Insiders Features for a full list of what's available.

GitHub Enterprise
GitHub Enterprise Cloud with data residency (ghe.com)
GitHub Enterprise Cloud can also make use of the remote server.

Example for https://octocorp.ghe.com with GitHub PAT token:

{
    ...
    "github-octocorp": {
      "type": "http",
      "url": "https://copilot-api.octocorp.ghe.com/mcp",
      "headers": {
        "Authorization": "Bearer ${input:github_mcp_pat}"
      }
    },
    ...
}
Note: When using OAuth with GitHub Enterprise with VS Code and GitHub Copilot, you also need to configure your VS Code settings to point to your GitHub Enterprise instance - see Authenticate from VS Code

GitHub Enterprise Server
GitHub Enterprise Server does not support remote server hosting. Please refer to GitHub Enterprise Server and Enterprise Cloud with data residency (ghe.com) from the local server configuration.

Local GitHub MCP Server
Install with Docker in VS CodeInstall with Docker in VS Code Insiders

Prerequisites
To run the server in a container, you will need to have Docker installed.
Once Docker is installed, you will also need to ensure Docker is running. The Docker image is available at ghcr.io/github/github-mcp-server. The image is public; if you get errors on pull, you may have an expired token and need to docker logout ghcr.io.
Lastly you will need to Create a GitHub Personal Access Token. The MCP server can use many of the GitHub APIs, so enable the permissions that you feel comfortable granting your AI tools (to learn more about access tokens, please check out the documentation).
Handling PATs Securely
GitHub Enterprise Server and Enterprise Cloud with data residency (ghe.com)
The flag --gh-host and the environment variable GITHUB_HOST can be used to set the hostname for GitHub Enterprise Server or GitHub Enterprise Cloud with data residency.

For GitHub Enterprise Server, prefix the hostname with the https:// URI scheme, as it otherwise defaults to http://, which GitHub Enterprise Server does not support.
For GitHub Enterprise Cloud with data residency, use https://YOURSUBDOMAIN.ghe.com as the hostname.
"github": {
    "command": "docker",
    "args": [
    "run",
    "-i",
    "--rm",
    "-e",
    "GITHUB_PERSONAL_ACCESS_TOKEN",
    "-e",
    "GITHUB_HOST",
    "ghcr.io/github/github-mcp-server"
    ],
    "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${input:github_token}",
        "GITHUB_HOST": "https://<your GHES or ghe.com domain name>"
    }
}
Installation
Install in GitHub Copilot on VS Code
For quick installation, use one of the one-click install buttons above. Once you complete that flow, toggle Agent mode (located by the Copilot Chat text input) and the server will start.

More about using MCP server tools in VS Code's agent mode documentation.

Install in GitHub Copilot on other IDEs (JetBrains, Visual Studio, Eclipse, etc.)

Add the following JSON block to your IDE's MCP settings.

{
  "mcp": {
    "inputs": [
      {
        "type": "promptString",
        "id": "github_token",
        "description": "GitHub Personal Access Token",
        "password": true
      }
    ],
    "servers": {
      "github": {
        "command": "docker",
        "args": [
          "run",
          "-i",
          "--rm",
          "-e",
          "GITHUB_PERSONAL_ACCESS_TOKEN",
          "ghcr.io/github/github-mcp-server"
        ],
        "env": {
          "GITHUB_PERSONAL_ACCESS_TOKEN": "${input:github_token}"
        }
      }
    }
  }
}
Optionally, you can add a similar example (i.e. without the mcp key) to a file called .vscode/mcp.json in your workspace. This will allow you to share the configuration with other host applications that accept the same format.

Example JSON block without the MCP key included
Install in Other MCP Hosts
For other MCP host applications, please refer to our installation guides:

Copilot CLI - Installation guide for GitHub Copilot CLI
GitHub Copilot in other IDEs - Installation for JetBrains, Visual Studio, Eclipse, and Xcode with GitHub Copilot
Claude Code & Claude Desktop - Installation guide for Claude Code and Claude Desktop
Cursor - Installation guide for Cursor IDE
Google Gemini CLI - Installation guide for Google Gemini CLI
Windsurf - Installation guide for Windsurf IDE
For a complete overview of all installation options, see our Installation Guides Index.

Note: Any host application that supports local MCP servers should be able to access the local GitHub MCP server. However, the specific configuration process, syntax and stability of the integration will vary by host application. While many may follow a similar format to the examples above, this is not guaranteed. Please refer to your host application's documentation for the correct MCP configuration syntax and setup process.

Build from source
If you don't have Docker, you can use go build to build the binary in the cmd/github-mcp-server directory, and use the github-mcp-server stdio command with the GITHUB_PERSONAL_ACCESS_TOKEN environment variable set to your token. To specify the output location of the build, use the -o flag. You should configure your server to use the built executable as its command. For example:

{
  "mcp": {
    "servers": {
      "github": {
        "command": "/path/to/github-mcp-server",
        "args": ["stdio"],
        "env": {
          "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_TOKEN>"
        }
      }
    }
  }
}
CLI utilities
The github-mcp-server binary includes a few CLI subcommands that are helpful for debugging and exploring the server.

github-mcp-server tool-search "<query>" searches tools by name, description, and input parameter names. Use --max-results to return more matches. Example (color output requires a TTY; use docker run -t (or -it) when running in Docker):
docker run -it --rm ghcr.io/github/github-mcp-server tool-search "issue" --max-results 5
github-mcp-server tool-search "issue" --max-results 5
Tool Configuration
The GitHub MCP Server supports enabling or disabling specific groups of functionalities via the --toolsets flag. This allows you to control which GitHub API capabilities are available to your AI tools. Enabling only the toolsets that you need can help the LLM with tool choice and reduce the context size.

Toolsets are not limited to Tools. Relevant MCP Resources and Prompts are also included where applicable.

When no toolsets are specified, default toolsets are used.

Looking for examples? See the Server Configuration Guide for common recipes like minimal setups, read-only mode, and combining tools with toolsets.

Specifying Toolsets
To specify toolsets you want available to the LLM, you can pass an allow-list in two ways:

Using Command Line Argument:

github-mcp-server --toolsets repos,issues,pull_requests,actions,code_security
Using Environment Variable:

GITHUB_TOOLSETS="repos,issues,pull_requests,actions,code_security" ./github-mcp-server
The environment variable GITHUB_TOOLSETS takes precedence over the command line argument if both are provided.

Specifying Individual Tools
You can also configure specific tools using the --tools flag. Tools can be used independently or combined with toolsets and dynamic toolsets discovery for fine-grained control.

Using Command Line Argument:

github-mcp-server --tools get_file_contents,issue_read,create_pull_request
Using Environment Variable:

GITHUB_TOOLS="get_file_contents,issue_read,create_pull_request" ./github-mcp-server
Combining with Toolsets (additive):

github-mcp-server --toolsets repos,issues --tools get_gist
This registers all tools from repos and issues toolsets, plus get_gist.

Combining with Dynamic Toolsets (additive):

github-mcp-server --tools get_file_contents --dynamic-toolsets
This registers get_file_contents plus the dynamic toolset tools (enable_toolset, list_available_toolsets, get_toolset_tools).

Important Notes:

Tools, toolsets, and dynamic toolsets can all be used together
Read-only mode takes priority: write tools are skipped if --read-only is set, even if explicitly requested via --tools
Tool names must match exactly (e.g., get_file_contents, not getFileContents). Invalid tool names will cause the server to fail at startup with an error message
When tools are renamed, old names are preserved as aliases for backward compatibility. See Tool Renaming for details.
Using Toolsets With Docker
When using Docker, you can pass the toolsets as environment variables:

docker run -i --rm \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token> \
  -e GITHUB_TOOLSETS="repos,issues,pull_requests,actions,code_security" \
  ghcr.io/github/github-mcp-server
Using Tools With Docker
When using Docker, you can pass specific tools as environment variables. You can also combine tools with toolsets:

# Tools only
docker run -i --rm \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token> \
  -e GITHUB_TOOLS="get_file_contents,issue_read,create_pull_request" \
  ghcr.io/github/github-mcp-server

# Tools combined with toolsets (additive)
docker run -i --rm \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token> \
  -e GITHUB_TOOLSETS="repos,issues" \
  -e GITHUB_TOOLS="get_gist" \
  ghcr.io/github/github-mcp-server
Special toolsets
"all" toolset
The special toolset all can be provided to enable all available toolsets regardless of any other configuration:

./github-mcp-server --toolsets all
Or using the environment variable:

GITHUB_TOOLSETS="all" ./github-mcp-server
"default" toolset
The default toolset default is the configuration that gets passed to the server if no toolsets are specified.

The default configuration is:

context
repos
issues
pull_requests
users
To keep the default configuration and add additional toolsets:

GITHUB_TOOLSETS="default,stargazers" ./github-mcp-server
Insiders Mode
The local GitHub MCP Server offers an insiders version with early access to new features and experimental tools.

Using Command Line Argument:

./github-mcp-server --insiders
Using Environment Variable:

GITHUB_INSIDERS=true ./github-mcp-server
When using Docker:

docker run -i --rm \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token> \
  -e GITHUB_INSIDERS=true \
  ghcr.io/github/github-mcp-server