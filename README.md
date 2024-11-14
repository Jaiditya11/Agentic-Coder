# AI Agent Code Generator

This project leverages a Retrieval-Augmented Generation (RAG) pipeline to create a code generation AI agent. Using embedded models, code parsing, and language generation, this agent reads input prompts and generates Python code snippets alongside descriptions for various tasks.

## Features

- **Natural Language to Code**: Generates Python code based on natural language prompts.
- **Retrieval-Augmented Generation (RAG)**: Uses a combination of document indexing and LLM-based text generation to enhance code creation.
- **Context-Aware Code Generation**: Creates code snippets with context-relevant explanations.
- **Code Parsing and Metadata Extraction**: Includes descriptions and filenames for generated code for easy identification and storage.

## Dependencies

This project relies on the following libraries and models:

- `llama_index`: For RAG pipeline construction, embedding models, and query pipelines.
- `Ollama` (model `"mistral"` and `"codellama"`): Used for language generation and code-focused LLM tasks.
- `pydantic`: For parsing and validating output JSON structures.
- `dotenv`: For loading environment variables.

Ensure that these dependencies are installed in your virtual environment. You can also configure any other custom models as needed.

## Getting Started

### Prerequisites

- Python 3.9+
- A virtual environment with the required dependencies installed (refer to the dependencies section).

### Setup

pip install -r requirements.txt
