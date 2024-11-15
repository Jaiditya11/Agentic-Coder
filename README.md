# Agentic-Coder 🤖

This project leverages a Retrieval-Augmented Generation (RAG) pipeline to create a code generation AI agent. Using embedded models, code parsing, and language generation, this agent reads input prompts and generates Python code snippets alongside descriptions for various tasks.

## Features 💪🏼

- **Natural Language to Code**: Generates Python code based on natural language prompts.
- **Retrieval-Augmented Generation (RAG)**: Uses a combination of document indexing and LLM-based text generation to enhance code creation.
- **Context-Aware Code Generation**: Creates code snippets with context-relevant explanations.
- **Code Parsing and Metadata Extraction**: Includes descriptions and filenames for generated code for easy identification and storage.
- **File Creation**: Creates a new file with the new generated code in the output folder.

## Dependencies 👾

This project relies on the following libraries and models:

- `llama_index`: For RAG pipeline construction, embedding models, and query pipelines.
- `Ollama` (model `"mistral"` and `"codellama"`): Used for language generation and code-focused LLM tasks.
- `pydantic`: For parsing and validating output JSON structures.
- `dotenv`: For loading environment variables.

### Prerequisites 🌱

- Python 3.9+
- A virtual environment with the required dependencies installed (refer to the dependencies section).
- Ollama installed on your device.(https://ollama.com/download)
  
### Setup ⚙️
**Set Up Virtual Environment**:  
 1.  To keep dependencies organized, set up a virtual environment:
    
   ```bash
   python3 -m venv ai
   source ai/bin/activate  # On Windows, use `ai\Scripts\activate
   ```
2. Install Dependencies

```bash
pip install -r requirements.txt
```
3. Environment Variables:
Create a .env file in the root directory to load any necessary environment variables, such as API keys:
```bash
LLAMA_CLOUD_API_KEY=your_api_key_here
```
4. Data Preparation:
Place any required documents for indexing in the ./data directory. These documents will be used by the agent for retrieval and query processing.

5. Usage
To start the agent and enter prompts for code generation, run the main script:
```bash
python3 main.py
```
6. Example Usage
```
Enter a Prompt (q to quit): Write a script to make a POST request to an API
Code generated:
from requests import post
url = 'https://example.com/items'
data = {'name': 'test item'}
response = post(url, data=data)
print(response.content)

Description: The Python script in `test.py` makes a POST request to the `/items` endpoint of the example.com domain, sending data as part of the request body. The server response is then printed.

Filename: Python_POST_request.py
```
Then it creates a new file with the filename and above code in the output folder.




