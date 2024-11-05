# AI2Obsidian

A command-line tool to save local Ollama AI conversations directly to your Obsidian vault. Built for MacOS.

## Prerequisites

- Python 3
- [Ollama](https://ollama.ai) installed and configured
- [obsidian-cli](https://github.com/Yakitrak/obsidian-cli) installed and configured

## Installation

1. Create the necessary directory:
```bash
sudo mkdir -p /usr/local/lib/ai2obsidian
```

2. Copy the Python script:
```bash
sudo cp ollama_to_obsidian.py /usr/local/lib/ai2obsidian/
sudo chmod +x /usr/local/lib/ai2obsidian/ollama_to_obsidian.py
```

3. Install the command-line tool:
```bash
sudo cp ai2ob /usr/local/bin/
sudo chmod +x /usr/local/bin/ai2ob
```

4. Configure obsidian-cli by setting your default vault:
```bash
obsidian-cli set-default "your-vault-name"
```

## Usage

Basic usage:
```bash
ai2ob "Your prompt here"
```

With custom filename:
```bash
ai2ob "Your prompt here" my_custom_filename
```

With different Ollama model:
```bash
ai2ob -m mistral "Your prompt here"
```

Combined options:
```bash
ai2ob -m mistral "Your prompt here" my_custom_filename
```

## Options

- `-m <model>`: Specify which Ollama model to use (default: llama3.1:8b)
- `-h`: Show help message

## File Structure

The conversations will be saved in your Obsidian vault with the following structure:
```
Your-Vault/
└── AI_Conversations/
    └── your_conversation.md
```

Each file includes:
- YAML frontmatter with:
  - Creation date
  - Year
  - Type: ai_conversation
- The original prompt
- The AI's response in markdown format

## Features

- Automatically opens the new note in Obsidian after creation
- Includes the original prompt in the saved note
- Organizes conversations by date and time if no filename is specified
- Supports all Ollama models

## Troubleshooting

If the command is not found:
```bash
which ai2ob
```
Should return `/usr/local/bin/ai2ob`. If not, ensure `/usr/local/bin` is in your PATH.

If you get permission errors when saving files:
```bash
sudo chown -R $(whoami) /usr/local/lib/ai2obsidian
```

## License

MIT License