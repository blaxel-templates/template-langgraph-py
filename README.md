# Blaxel LangGraph Agent

<p align="center">
  <img src="https://blaxel.ai/logo.png" alt="Blaxel" width="200"/>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  [![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)  [![GitHub Stars](https://img.shields.io/github/stars/blaxel-templates/template-langgraph-py)](https://github.com/blaxel-templates/template-langgraph-py/stargazers)

A template implementation of a conversational agent using LangGraph and GPT-4. This agent demonstrates interactive conversion, tool integration, and streaming responses for real-time applications.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Agent Server](#agent-server)
  - [Agent CLI](#agent-cli)
- [API Reference](#api-reference)
- [Contribution](#contribution)
- [Support](#support)
- [License](#license)

## Features

- **Interactive conversion**: integrate custom tools via LangGraph
- **Streaming responses**: real-time output handling
- **Extensible**: easily add new functions and capabilities
- **Template-based**: follow LangGraph and GPT-4 best practices

## Demo

![Demo GIF](https://raw.githubusercontent.com/blaxel-templates/template-langgraph-py/main/demo.gif)

## Installation

Ensure you have Python 3.10+ installed.

```bash
# Clone the repository
git clone https://github.com/blaxel-templates/template-langgraph-py.git
cd template-langgraph-py

# Create virtual environment and install
dotenv # optional: load .env variables
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install .
```

## Quick Start

### Run the agent server (local)

```bash
bl serve --hotreload
```

### Test the agent (CLI)

```bash
bl chat --local langgraph-agent
```

## Project Structure

```
├── src/
│   ├── main.py           # Entry point
│   ├── agent.py          # Core agent implementation
│   └── server/           # FastAPI server
│       └── ...
├── examples/             # Usage examples
├── tests/                # Unit and integration tests
├── pyproject.toml        # Packaging configuration
└── README.md
```

## Usage

### Agent Server

Start the FastAPI server:

```bash
uvicorn src.server:app --reload
```

Send a request:

```bash
curl -X POST http://localhost:8000/agents/langgraph-agent/run \
  -H "Content-Type: application/json" \
  -d '{"input":"What is the weather today in Paris?"}'
```

### Agent CLI

```bash
# Chat with the agent locally
dbl chat --local langgraph-agent
```

## API Reference

### POST /agents/{agent_id}/run

- **Description**: Run the agent with provided input
- **Request**:
  - `input` (string): prompt for the agent
- **Response**:
  - `stream` (boolean): true if streaming
  - `output` (string): agent response

### GET /agents/{agent_id}/info

- **Description**: Get agent metadata and capabilities
- **Response**:
  - `tools` (array): list of integrated functions
  - `model` (string): model used

## Contribution

We welcome contributions!

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please follow the [Blaxel Code of Conduct](https://blaxel.ai/code-of-conduct).

## Support

For issues or questions, please open an [issue](https://github.com/blaxel-templates/template-langgraph-py/issues) or join our [Discord Community](https://discord.gg/G3mzUPcHP).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
