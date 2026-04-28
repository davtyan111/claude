Mcp
Editor's Note
The AWS Labs MCP servers provide a suite of specialized Model Context Protocol servers that enable AI models to interact with AWS services and resources across various domains including infrastructure, databases, machine learning, and cost management. These servers expose tools for accessing AWS documentation, managing infrastructure as code, deploying containers and serverless functions, querying databases, and performing operational tasks through standardized MCP interfaces. The servers solve the problem of integrating AWS capabilities into MCP-compatible applications, allowing developers and AI assistants to programmatically interact with AWS services regardless of where the MCP client is being used.

Install
claude mcp add --transport stdio awslabs-mcp uvx mcp

What is the Model Context Protocol (MCP) and how does it work with MCP Servers for AWS?
The Model Context Protocol (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources and tools. Whether you're building an AI-powered IDE, enhancing a chat interface, or creating custom AI workflows, MCP provides a standardized way to connect LLMs with the context they need.

— Model Context Protocol README

An MCP Server is a lightweight program that exposes specific capabilities through the standardized Model Context Protocol. Host applications (such as chatbots, IDEs, and other AI tools) have MCP clients that maintain 1:1 connections with MCP servers. Common MCP clients include agentic AI coding assistants (like Kiro, Cline, Cursor, Windsurf) as well as chatbot applications like Claude Desktop, with more clients coming soon. MCP servers can access local data sources and remote services to provide additional context that improves the generated outputs from the models.

MCP Servers for AWS use this protocol to provide AI applications access to AWS documentation, contextual guidance, and best practices. Through the standardized MCP client-server architecture, AWS capabilities become an intelligent extension of your development environment or AI application.

MCP Servers for AWS enable enhanced cloud-native development, infrastructure management, and development workflows—making AI-assisted cloud computing more accessible and efficient.

The Model Context Protocol is an open source project run by Anthropic, PBC. and open to contributions from the entire community. For more information on MCP, you can find further documentation here

Open source MCP servers for AWS Transport Mechanisms
Supported transport mechanisms
The MCP protocol currently defines two standard transport mechanisms for client-server communication:

stdio, communication over standard in and standard out
streamable HTTP
The MCP servers in this repository are designed to support stdio only.

You are responsible for ensuring that your use of these servers comply with the terms governing them, and any laws, rules, regulations, policies, or standards that apply to you.

Server Sent Events Support Removal
Important Notice: On May 26th, 2025, Server Sent Events (SSE) support was removed from all MCP servers in their latest major versions. This change aligns with the Model Context Protocol specification's backwards compatibility guidelines.

We are actively working towards supporting Streamable HTTP, which will provide improved transport capabilities for future versions.

For applications still requiring SSE support, please use the previous major version of the respective MCP server until you can migrate to alternative transport methods.

Why MCP Servers for AWS?
MCP servers enhance the capabilities of foundation models (FMs) in several key ways:

Improved Output Quality: By providing relevant information directly in the model's context, MCP servers significantly improve model responses for specialized domains like AWS services. This approach reduces hallucinations, provides more accurate technical details, enables more precise code generation, and ensures recommendations align with current AWS best practices and service capabilities.

Access to Latest Documentation: FMs may not have knowledge of recent releases, APIs, or SDKs. MCP servers bridge this gap by pulling in up-to-date documentation, ensuring your AI assistant always works with the latest AWS capabilities.

Workflow Automation: MCP servers convert common workflows into tools that foundation models can use directly. Whether it's CDK, Terraform, or other AWS-specific workflows, these tools enable AI assistants to perform complex tasks with greater accuracy and efficiency.

Specialized Domain Knowledge: MCP servers provide deep, contextual knowledge about AWS services that might not be fully represented in foundation models' training data, enabling more accurate and helpful responses for cloud development tasks.

Available MCP Servers: Quick Installation
Get started quickly with one-click installation buttons for popular MCP clients. Click the buttons below to install servers directly in Cursor or VS Code:

🚀 Getting Started with AWS
For AWS interactions, we recommend starting with:

Server Name	Description	Install
AWS MCP Server (in preview)	Start here for secure, auditable AWS interactions! This remote, managed MCP server is hosted by AWS and combines comprehensive AWS API support with access to the latest AWS documentation, API references, What's New posts, and Getting Started information. Features pre-built Agent SOPs that follow AWS best practices, helping agents complete complex multi-step AWS tasks reliably. Built with safety and control in mind: syntactically validated API calls, IAM-based permissions with zero credential exposure, and complete CloudTrail audit logging. Access all AWS services for managing infrastructure, exploring resources, and executing AWS operations with full transparency and traceability. Read more	Install
Install
Install on VS Code
Browse by What You're Building
📚 Real-time access to official AWS documentation
Server Name	Description	Install
AWS Knowledge MCP Server	A remote, fully-managed MCP server hosted by AWS that provides access to the latest AWS docs, API references, What's New Posts, Getting Started information, Builder Center, Blog posts, Architectural references, and Well-Architected guidance.	Install
Install
Install on VS Code
AWS Documentation MCP Server	Get latest AWS docs and API references	Install
Install
Install on VS Code
🏗️ Infrastructure & Deployment
Build, deploy, and manage cloud infrastructure with Infrastructure as Code best practices.

Server Name	Description	Install
AWS IaC MCP Server	Complete Infrastructure as Code toolkit with CloudFormation documentation access, CDK best practices guidance, construct examples, security validation, and deployment troubleshooting	Install
Install
Install on VS Code
AWS Cloud Control API MCP Server ⚠️ DEPRECATED	Direct AWS resource management with security scanning and best practices (Use AWS IaC MCP Server instead)	Install
Install
Install on VS Code
Container Platforms
Server Name	Description	Install
Amazon EKS MCP Server	Kubernetes cluster management and application deployment	Install
Install
Install on VS Code
Amazon ECS MCP Server	Container orchestration and ECS application deployment	Install
Install
Install on VS Code
Finch MCP Server	Local container building with ECR integration	Install
Install
Install on VS Code
Serverless & Functions
Server Name	Description	Install
AWS Serverless MCP Server	Complete serverless application lifecycle with SAM CLI	Install
Install
Install on VS Code
AWS Lambda Tool MCP Server	Execute Lambda functions as AI tools for private resource access	Install
Install
Install on VS Code
Support
Server Name	Description	Install
AWS Support MCP Server	Help users create and manage AWS Support cases	Install
Install
Install on VS Code
🤖 AI & Machine Learning
Enhance AI applications with knowledge retrieval, content generation, and ML capabilities

Server Name	Description	Install
Amazon Bedrock Knowledge Bases Retrieval MCP Server	Query enterprise knowledge bases with citation support	Install
Install
Install on VS Code
Amazon Kendra Index MCP Server	Enterprise search and RAG enhancement	Install
Install
Install on VS Code
Amazon Q Business MCP Server	AI assistant for your ingested content with anonymous access	Install
Install
Install on VS Code
Amazon Q Index MCP Server	Data accessors to search through enterprise's Q index	Install
Install
Install on VS Code
AWS Bedrock Custom Model Import MCP Server	Manage custom models in Bedrock for on-demand inference	Install
Install
Install on VS Code
AWS Bedrock AgentCore MCP Server	Provides comprehensive documentation access on AgentCore platform services, APIs, and best practices	Install
Install
Install on VS Code
Amazon SageMaker AI MCP Server	SageMaker AI resource management and model development	Install
Install
Install on VS Code
📊 Data & Analytics
Work with databases, caching systems, and data processing workflows.

SQL & NoSQL Databases
Server Name	Description	Install
Amazon DynamoDB MCP Server	DynamoDB expert design guidance and data modeling assistance	Install
Install
Install on VS Code
Amazon Aurora PostgreSQL MCP Server	PostgreSQL database operations via RDS Data API	Install
Install
Install on VS Code
Amazon Aurora MySQL MCP Server	MySQL database operations via RDS Data API	Install
Install
Install on VS Code
Amazon Aurora DSQL MCP Server	Distributed SQL with PostgreSQL compatibility	Install
Install
Install on VS Code
Amazon DocumentDB MCP Server	MongoDB-compatible document database operations	Install
Install
Install on VS Code
Amazon Neptune MCP Server	Graph database queries with openCypher and Gremlin	Install
Install
Install on VS Code
Amazon Keyspaces MCP Server	Apache Cassandra-compatible operations	Install
Install
Install on VS Code
Amazon Timestream for InfluxDB MCP Server	Time-series database operations and InfluxDB compatibility	Install
Install
Install on VS Code
AWS S3 Tables MCP Server	Manage S3 Tables for optimized analytics	Install
Install
Install on VS Code
Amazon Redshift MCP Server	Data warehouse operations and analytics queries	Install
Install
Install on VS Code
AWS IoT SiteWise MCP Server	Industrial IoT asset management, data ingestion, and analytics	Install
Install
Install on VS Code
Search & Analytics
Amazon OpenSearch MCP Server - OpenSearch powered search, Analytics, and Observability
Backend API Providers
Server Name	Description	Install
AWS AppSync MCP Server	Manage and Interact with application backends powered by AWS AppSync	Install
Install
Install on VS Code
Caching & Performance
Server Name	Description	Install
Amazon ElastiCache MCP Server	Complete ElastiCache control plane operations	Install
Install
Install on VS Code
Amazon ElastiCache / MemoryDB for Valkey MCP Server	Advanced data structures and caching with Valkey	Install
Install
Install on VS Code
Amazon ElastiCache for Memcached MCP Server	High-speed caching with Memcached protocol	Install
Install
Install on VS Code
🛠️ Developer Tools & Support
Accelerate development with code analysis, documentation, and testing utilities.

Server Name	Description	Install
AWS IAM MCP Server	Comprehensive IAM user, role, group, and policy management with security best practices	Install
Install
Install on VS Code
OpenAPI MCP Server	Dynamic API integration through OpenAPI specifications	Install
Install
Install on VS Code
📡 Integration & Messaging
Connect systems with messaging, workflows, and location services.

Server Name	Description	Install
Amazon SNS / SQS MCP Server	Event-driven messaging and queue management	Install
Install
Install on VS Code
Amazon MQ MCP Server	Message broker management for RabbitMQ and ActiveMQ	Install
Install
Install on VS Code
AWS Step Functions Tool MCP Server	Execute complex workflows and business processes	Install
Install
Install on VS Code
Amazon Location Service MCP Server	Place search, geocoding, and route optimization	Install
Install
Install on VS Code
OpenAPI MCP Server	Dynamic API integration through OpenAPI specifications	Install
Install
Install on VS Code
💰 Cost & Operations
Monitor, optimize, and manage your AWS infrastructure and costs.

Server Name	Description	Install
AWS Pricing MCP Server	AWS service pricing and cost estimates	Install
Install
Install on VS Code
Amazon CloudWatch MCP Server	Metrics, Alarms, and Logs analysis and operational troubleshooting	Install
Install
Install on VS Code
AWS Managed Prometheus MCP Server	Prometheus-compatible operations	Install
Install
Install on VS Code
AWS Billing and Cost Management MCP Server	Billing and cost management for chargeable and Proforma billing	Install
Install
Install on VS Code
🧬 Healthcare & Lifesciences
Interact with AWS HealthAI services.

Server Name	Description	Install
AWS HealthOmics MCP Server	Generate, run, debug and optimize lifescience workflows	Install
Install
Install on VS Code
AWS HealthImaging MCP Server	Comprehensive medical imaging data lifecycle management with 21 tools for DICOM operations, datastore management, and automated discovery	Install
Install
Install on VS Code
AWS HealthLake MCP Server	Create, manage, search, and optimize FHIR healthcare data workflows with comprehensive AWS HealthLake integration, featuring automated resource discovery, advanced search capabilities, patient record management, and seamless import/export operations.	Install
Install
Install on VS Code
Browse by How You're Working
👨‍💻 Vibe Coding & Development
AI coding assistants like Kiro, Cline, Cursor, and Claude Code helping you build faster

Workshop: Check out the Vibe Coding with AWS MCP Servers workshop for hands-on guidance and examples.

Core Development Workflow
Server Name	Description	Install
AWS API MCP Server	Start here for general AWS interactions! Comprehensive AWS API support with command validation, security controls, and access to all AWS services. Perfect for managing infrastructure, exploring resources, and executing AWS operations through natural language.	Install
Install
Install VS Code
AWS Knowledge MCP Server	A remote, fully-managed MCP server hosted by AWS that provides access to the latest AWS docs, API references, What's New Posts, Getting Started information, Builder Center, Blog posts, Architectural references, and Well-Architected guidance.	Install
Install
Install on VS Code
AWS Documentation MCP Server	Get latest AWS docs and API references	Install
Install
Install on VS Code
Infrastructure as Code
Server Name	Description	Install
AWS IaC MCP Server	Complete Infrastructure as Code toolkit with CloudFormation documentation access, CDK best practices guidance, construct examples, security validation, and deployment troubleshooting	Install
Install
Install on VS Code
AWS Cloud Control API MCP Server ⚠️ DEPRECATED	Direct AWS resource management with security scanning and best practices (Use AWS IaC MCP Server instead)	Install
Install
Install on VS Code
Application Development
Server Name	Description	Install
OpenAPI MCP Server	Dynamic API integration through OpenAPI specifications	Install
Install
Install on VS Code
Container & Serverless Development
Server Name	Description	Install
Amazon SageMaker AI MCP Server	SageMaker AI resource management and model development	Install
Install
Install on VS Code
Amazon EKS MCP Server	Kubernetes cluster management and app deployment	Install
Install
Install on VS Code
Amazon ECS MCP Server	Containerize and deploy applications to ECS	Install
Install
Install on VS Code
Finch MCP Server	Local container building with ECR push	Install
Install
Install on VS Code
AWS Serverless MCP Server	Full serverless app lifecycle with SAM CLI	Install
Install
Install on VS Code
Testing & Data
Server Name	Description	Install
Lifesciences Workflow Development
Server Name	Description	Install
AWS HealthOmics MCP Server	Generate, run, debug and optimize lifescience workflows	Install
Install
Install on VS Code
Healthcare Data Management
Server Name	Description	Install
AWS HealthLake MCP Server	Create, manage, search, and optimize FHIR healthcare data workflows with comprehensive AWS HealthLake integration, featuring automated resource discovery, advanced search capabilities, patient record management, and seamless import/export operations.	Install
Install
Install on VS Code
💬 Conversational Assistants
Customer-facing chatbots, business agents, and interactive Q&A systems

Knowledge & Search
Server Name	Description	Install
Amazon Bedrock Knowledge Bases Retrieval MCP Server	Query enterprise knowledge bases with citation support	Install
Install
Install on VS Code
Amazon Kendra Index MCP Server	Enterprise search and RAG enhancement	Install
Install
Install on VS Code
Amazon Q Business MCP Server	AI assistant for your ingested content with anonymous access	Install
Install
Install on VS Code
Amazon Q Index MCP Server	Data accessors to search through enterprise's Q index	Install
Install
Install on VS Code
AWS Documentation MCP Server	Get latest AWS docs and API references	Install
Install
Install on VS Code
Content Processing & Generation
Server Name	Description	Install
Document Loader MCP Server	Parse and extract content from PDF, DOCX, XLSX, PPTX, and image files	Install
Install
Install on VS Code
Business Services
Server Name	Description	Install
Amazon Location Service MCP Server	Location search, geocoding, and business hours	Install
Install
Install on VS Code
AWS Pricing MCP Server	AWS service pricing and cost estimates	Install
Install
Install on VS Code
🤖 Autonomous Background Agents
Headless automation, ETL pipelines, and operational systems

Data Operations & ETL
Server Name	Description	Install
AWS Data Processing MCP Server	Comprehensive data processing tools and real-time pipeline visibility across AWS Glue, Amazon EMR-EC2, and Amazon Athena	Install
Install
Install on VS Code
Amazon DynamoDB MCP Server	Complete DynamoDB operations and table management	Install
Install
Install on VS Code
Amazon Aurora PostgreSQL MCP Server	PostgreSQL database operations via RDS Data API	Install
Install
Install on VS Code
Amazon Aurora MySQL MCP Server	MySQL database operations via RDS Data API	Install
Install
Install on VS Code
Amazon Aurora DSQL MCP Server	Distributed SQL with PostgreSQL compatibility	Install
Install
Install on VS Code
Amazon DocumentDB MCP Server	MongoDB-compatible document database operations	Install
Install
Install on VS Code
Amazon Neptune MCP Server	Graph database queries with openCypher and Gremlin	Install
Install
Install on VS Code
Amazon Keyspaces MCP Server	Apache Cassandra-compatible operations	Install
Install
Install on VS Code
Amazon Timestream for InfluxDB MCP Server	Time-series database operations and InfluxDB compatibility	Install
Install
Install on VS Code
Caching & Performance
Server Name	Description	Install
Amazon ElastiCache / MemoryDB for Valkey MCP Server	Advanced data structures and caching with Valkey	Install
Install
Install on VS Code
Amazon ElastiCache for Memcached MCP Server	High-speed caching with Memcached protocol	Install
Install
Install on VS Code
Workflow & Integration
Server Name	Description	Install
AWS Lambda Tool MCP Server	Execute Lambda functions as AI tools for private resource access	Install
Install
Install on VS Code
AWS Step Functions Tool MCP Server	Execute complex workflows and business processes	Install
Install
Install on VS Code
Amazon SNS/SQS MCP Server	Event-driven messaging and queue management	Install
Install
Install on VS Code
Amazon MQ MCP Server	Message broker management for RabbitMQ and ActiveMQ	Install
Install
Install on VS Code
Operations & Monitoring
Server Name	Description	Install
Amazon CloudWatch MCP Server	Metrics, Alarms, and Logs analysis and operational troubleshooting	Install
Install
Install on VS Code
Amazon CloudWatch Application Signals MCP Server	Application monitoring and performance insights	Install
Install
Install on VS Code
AWS Managed Prometheus MCP Server	Prometheus-compatible operations and monitoring	Install
Install
Install on VS Code
AWS Well-Architected Security Assessment Tool MCP Server	Assess AWS environments against the Well-Architected Framework Security Pillar	Install
Install
Install on VS Code
AWS CloudTrail MCP Server	CloudTrail events querying and analysis	Install
Install
Install on VS Code
AWS Systems Manager for SAP MCP Server	Manage, monitor, and operate SAP applications on AWS with health checks, configuration validation, and scheduling	Install
Install
Install on VS Code
MCP AWS Lambda Handler Module
A Python library for creating serverless HTTP handlers for the Model Context Protocol (MCP) using AWS Lambda. This module provides a flexible framework for building MCP HTTP endpoints with pluggable session management, including built-in DynamoDB support.

Features:

Easy serverless MCP HTTP handler creation using AWS Lambda
Pluggable session management system
Built-in DynamoDB session backend support
Customizable authentication and authorization
Example implementations and tests
See src/mcp-lambda-handler/README.md for full usage, installation, and development instructions.

When to use Local vs Remote MCP Servers?
MCP servers can be run either locally on your development machine or remotely on the cloud. Here's when to use each approach:

Local MCP Servers
Development & Testing: Perfect for local development, testing, and debugging
Offline Work: Continue working when internet connectivity is limited
Data Privacy: Keep sensitive data and credentials on your local machine
Low Latency: Minimal network overhead for faster response times
Resource Control: Direct control over server resources and configuration
Remote MCP Servers
Team Collaboration: Share consistent server configurations across your team
Resource Intensive Tasks: Offload heavy processing to dedicated cloud resources
Always Available: Access your MCP servers from anywhere, any device
Automatic Updates: Get the latest features and security patches automatically
Scalability: Easily handle varying workloads without local resource constraints
Security: Centralized security controls with IAM-based permissions and zero credential exposure
Governance: Comprehensive audit logging and compliance monitoring for enterprise-grade governance
Note: Some MCP servers, like the official AWS MCP server (in preview) and AWS Knowledge MCP, are provided as fully managed services by AWS. These AWS-managed remote servers require no setup or infrastructure management on your part - just connect and start using them.

Use Cases for the Servers
For example, you can use the AWS Documentation MCP Server to help your AI assistant research and generate up-to-date code for any AWS service, like Amazon Bedrock Inline agents. Alternatively, you could use the CDK MCP Server or the Terraform MCP Server to have your AI assistant create infrastructure-as-code implementations that use the latest APIs and follow AWS best practices. With the AWS Pricing MCP Server, you could ask "What would be the estimated monthly cost for this CDK project before I deploy it?" or "Can you help me understand the potential AWS service expenses for this infrastructure design?" and receive detailed cost estimations and budget planning insights. The Valkey MCP Server enables natural language interaction with Valkey data stores, allowing AI assistants to efficiently manage data operations through a simple conversational interface.

Installation and Setup
Each server has specific installation instructions with one-click installs for Kiro, Cursor, and VSCode. Generally, you can:

Install uv from Astral
Install Python using uv python install 3.10
Configure AWS credentials with access to required services
Add the server to your MCP client configuration
Example configuration for Kiro MCP settings (~/.kiro/settings/mcp.json):

For macOS/Linux
{
  "mcpServers": {
    "awslabs-core-mcp-server": {
      "command": "uvx",
      "args": [
        "awslabs.core-mcp-server@latest"
      ],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
See individual server READMEs for specific requirements and configuration options.

For Windows
When configuring MCP servers on Windows, you'll need to use a slightly different configuration format:

{
  "mcpServers": {
    "awslabs-core-mcp-server": {
      "disabled": false,
      "timeout": 60,
      "type": "stdio",
      "command": "uv",
      "args": [
        "tool",
        "run",
        "--from",
        "awslabs.core-mcp-server@latest",
        "awslabs.core-mcp-server.exe"
      ],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
If you have problems with MCP configuration or want to check if the appropriate parameters are in place, you can try the following:

# Run MCP server manually with timeout 15s
$ timeout 15s uv tool run <MCP Name> <args> 2>&1 || echo "Command completed or timed out"

# Example (Aurora MySQL MCP Server)
$ timeout 15s uv tool run awslabs.mysql-mcp-server --resource_arn <Your Resource ARN> --secret_arn <Your Secret ARN> ... 2>&1 || echo "Command completed or timed out"

# If the arguments are not set appropriately, you may see the following message:
usage: awslabs.mysql-mcp-server [-h] --resource_arn RESOURCE_ARN --secret_arn SECRET_ARN --database DATABASE
                                --region REGION --readonly READONLY
awslabs.mysql-mcp-server: error: the following arguments are required: --resource_arn, --secret_arn, --database, --region, --readonly
Note about performance when using uvx "@latest" suffix:

Using the "@latest" suffix checks and downloads the latest MCP server package from pypi every time you start your MCP clients, but it comes with a cost of increased initial load times. If you want to minimize the initial load time, remove "@latest" and manage your uv cache yourself using one of these approaches:

uv cache clean <tool>: where {tool} is the mcp server you want to delete from cache and install again (e.g.: "awslabs.lambda-tool-mcp-server") (remember to remove the '<>').
uvx <tool>@latest: this will refresh the tool with the latest version and add it to the uv cache.
Running MCP servers in containers
Docker images for each MCP server are published to the public AWS ECR registry.

This example uses docker with the "awslabs.aws-documentation-mcp-server and can be repeated for each MCP server

Optionally save sensitive environmental variables in a file:

# contents of a .env file with fictitious AWS temporary credentials
AWS_ACCESS_KEY_ID=ASIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_SESSION_TOKEN=AQoEXAMPLEH4aoAH0gNCAPy...truncated...zrkuWJOgQs8IZZaIv2BXIa2R4Olgk
Use the docker options: --env, --env-file, and --volume as needed because the "env": {} are not available within the container.

{
  "mcpServers": {
    "awslabs.aws-documentation-mcp-server": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "--interactive",
        "--env",
        "FASTMCP_LOG_LEVEL=ERROR",
        "--env",
        "AWS_REGION=us-east-1",
        "--env-file",
        "/full/path/to/.env",
        "--volume",
        "/full/path/to/.aws:/app/.aws",
        "public.ecr.aws/awslabs-mcp/awslabs/aws-documentation-mcp-server:latest"
      ],
      "env": {}
    }
  }
}
For testing local changes you can build and tag the image. You have to update the MCP configuration to use this tag instead of the ECR image.

cd src/aws-documentation-mcp-server
docker build -t awslabs/aws-documentation-mcp-server .
Getting Started with Kiro
Install in Kiro
Getting Started with Cline and Amazon Bedrock
Getting Started with Cline and Amazon Bedrock
Getting Started with Cursor
Getting Started with Cursor
Getting Started with Windsurf
Getting Started with Windsurf
Getting Started with VS Code
Install in VS Code
Getting Started with Claude Code
Install in Claude Code
Samples
Ready-to-use examples of open source MCP servers for AWS in action are available in the samples directory. These samples provide working code and step-by-step guides to help you get started with each MCP server.

Vibe coding
You can use these MCP servers with your AI coding assistant to vibe code. For tips and tricks on how to improve your vibe coding experience, please refer to our guide.