# Blaxel LangGraph Agent

<p align="center">
  <img src="https://blaxel.ai/logo.png" alt="Blaxel" width="200"/>
</p>

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/LangGraph-powered-brightgreen.svg)](https://github.com/langchain-ai/langgraph)
[![GPT-4](https://img.shields.io/badge/GPT--4-enabled-orange.svg)](https://openai.com/gpt-4)

</div>

A template implementation of a conversational agent using LangGraph and GPT-4. This agent demonstrates the power of LangGraph for building interactive AI agents with tool integration capabilities.

## 📑 Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Running Locally](#running-the-server-locally)
  - [Testing](#testing-your-agent)
  - [Deployment](#deploying-to-blaxel)
- [API Reference](#api-reference)
- [Project Structure](#project-structure)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

## ✨ Features

- Interactive conversational interface
- Tool integration support (including weather and search capabilities)
- Streaming responses for real-time interaction
- Built on LangGraph for efficient agent orchestration
- Easy deployment and integration with Blaxel platform

## 🚀 Quick Start

For those who want to get up and running quickly:

```bash
# Clone the repository
git clone https://github.com/blaxel-ai/template-langgraph-py.git

# Navigate to the project directory
cd template-langgraph-py

# Install dependencies
uv sync

# Start the server
bl serve --hotreload

# In another terminal, test the agent
bl chat --local blaxel-agent
```

## 📋 Prerequisites

- **Python:** 3.10 or later
- **[UV](https://github.com/astral-sh/uv):** An extremely fast Python package and project manager, written in Rust
- **[Blaxel CLI](https://docs.blaxel.ai/Get-started):** Ensure you have the Blaxel CLI installed. If not, install it globally:
  ```bash
  curl -fsSL https://raw.githubusercontent.com/blaxel-ai/toolkit/main/install.sh | BINDIR=$HOME/.local/bin sh
  ```
- **Blaxel login:** Login to Blaxel platform
  ```bash
  bl login YOUR-WORKSPACE
  ```

## 💻 Installation

**Clone the repository and install dependencies:**

```bash
git clone https://github.com/blaxel-ai/template-langgraph-py.git
cd template-langgraph-py
uv sync
```

## 🔧 Usage

### Running the Server Locally

Start the development server with hot reloading:

```bash
bl serve --hotreload
```

_Note:_ This command starts the server and enables hot reload so that changes to the source code are automatically reflected.

### Testing your agent

You can test your agent using the chat interface:

```bash
bl chat --local blaxel-agent
```

Or run it directly with specific input:

```bash
bl run agent blaxel-agent --local --data '{"input": "What is the weather in Paris?"}'
```

### Deploying to Blaxel

When you are ready to deploy your application:

```bash
bl deploy
```

This command uses your code and the configuration files under the `.blaxel` directory to deploy your application.

## 📚 API Reference

The LangGraph agent exposes the following endpoints:

- **POST /agents/{agent_id}/run**: Run the agent with provided input
  ```json
  {
    "input": "What is the weather in Paris?",
    "stream": true
  }
  ```

- **GET /agents/{agent_id}/info**: Get information about the agent capabilities
- **GET /health**: Health check endpoint

For detailed API documentation, run the server and visit `/docs` endpoint.

## 📁 Project Structure

- **src/main.py** - Application entry point
- **src/agent.py** - Core agent implementation with LangGraph integration
- **src/server/** - Server implementation and routing
- **pyproject.toml** - UV package manager configuration
- **blaxel.toml** - Blaxel deployment configuration

## 📝 Examples

### Basic Conversation

```
User: What can you help me with?
Agent: I can help you with various tasks including:
- Answering general knowledge questions
- Checking weather information for locations
- Searching for information on the web
- Performing calculations
- Assisting with creative tasks

How can I assist you today?
```

### Weather Query

```
User: What's the weather like in San Francisco?
Agent: Let me check the current weather in San Francisco for you.

Current conditions in San Francisco:
- Temperature: 62°F (16°C)
- Condition: Partly cloudy
- Humidity: 75%
- Wind: 12 mph westerly

The forecast shows mild temperatures continuing through the week with morning fog.
```

## ❓ Troubleshooting

### Common Issues

1. **Dependency Issues**:
   - Make sure you have Python 3.10+
   - Try `uv sync --upgrade` to update dependencies

2. **Connection Problems**:
   - Verify your network connection
   - Check firewall settings if API calls are failing

For more help, please [submit an issue](https://github.com/blaxel-templates/template-langgraph-py/issues) on GitHub.

## 👥 Contributing

Contributions are welcome! Here's how you can contribute:

1. **Fork** the repository
2. **Create** a feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit** your changes:
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push** to the branch:
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Submit** a Pull Request

Please make sure to update tests as appropriate and follow the code style of the project.

## 🆘 Support

If you need help with this template:

- [Submit an issue](https://github.com/blaxel-templates/template-langgraph-py/issues) for bug reports or feature requests
- Visit the [Blaxel Documentation](https://docs.blaxel.ai) for platform guidance
- Join our [Discord Community](https://discord.gg/G3NqzUPcHP) for real-time assistance (Replace with actual Discord link)

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
