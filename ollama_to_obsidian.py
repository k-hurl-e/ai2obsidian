#!/usr/bin/env python3
import sys
import os
import subprocess
import argparse
from datetime import datetime

def format_conversation(conversation_text, prompt):
    """Format the conversation into markdown"""
    formatted = "---\n"
    formatted += f"created: {datetime.now().strftime('%d/%m/%Y')}\n"
    formatted += f"year: {datetime.now().strftime('%Y')}\n"
    formatted += "type: ai_conversation\n"
    formatted += "---\n\n"
    formatted += "# Ollama Conversation\n\n"
    formatted += "## Prompt\n\n"
    formatted += prompt + "\n\n"
    formatted += "## Response\n\n"
    formatted += conversation_text
    return formatted

def save_to_obsidian(content, vault_folder="AI_Conversations", custom_filename=None):
    """Save the content to Obsidian using obsidian-cli"""
    
    # Use custom filename if provided, otherwise generate from timestamp
    if custom_filename:
        # Add .md extension if not present
        if not custom_filename.endswith('.md'):
            filename = f"{custom_filename}.md"
        else:
            filename = custom_filename
    else:
        filename = f"ollama_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    
    # Create temporary file with content
    temp_path = "/tmp/temp_ollama_chat.md"
    with open(temp_path, "w") as f:
        f.write(content)
    
    try:
        # Create folder if it doesn't exist
        file_path = f"{vault_folder}/{filename}"
        subprocess.run([
            "obsidian-cli", 
            "create", 
            file_path,
            "--content", content,
            "--overwrite",
            "--open"
        ], check=True)
        print(f"Successfully saved conversation to Obsidian at: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error saving to Obsidian: {e}")
    finally:
        os.remove(temp_path)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Save Ollama conversation to Obsidian vault')
    parser.add_argument('prompt', help='The prompt used in the conversation')
    parser.add_argument('-p', '--path', 
                        default='AI_Conversations',
                        help='Path within vault to save the file (default: AI_Conversations)')
    parser.add_argument('-f', '--filename',
                        help='Custom filename (optional, will generate timestamp-based name if not provided)')
    
    args = parser.parse_args()

    # Read conversation from stdin (pipe)
    if not sys.stdin.isatty():
        conversation = sys.stdin.read()
    else:
        print("No input provided. Please pipe the conversation to this script.")
        sys.exit(1)
    
    # Format the conversation
    formatted_content = format_conversation(conversation, args.prompt)
    
    # Save to Obsidian with custom path and optional filename
    save_to_obsidian(formatted_content, args.path, args.filename)

if __name__ == "__main__":
    main() 