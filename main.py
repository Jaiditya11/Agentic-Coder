from llama_index.llms.ollama import Ollama
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, PromptTemplate
from llama_index.core.embeddings import resolve_embed_model 
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from pydantic import BaseModel
from llama_index.core.output_parsers import PydanticOutputParser 
from llama_index.core.query_pipeline import QueryPipeline
from prompts import context,code_parser_template
from code_reader import code_reader
from dotenv import load_dotenv
# import ast
import json
import os

load_dotenv()

#Mistral is used for text completions

llm = Ollama(
    model="mistral",
    request_timeout=30.0
)


parser = LlamaParse(result_type = "markdown")

file_extractor = {".pdf":parser}
documents = SimpleDirectoryReader("./data",file_extractor=file_extractor).load_data()

embed_model = resolve_embed_model("local:BAAI/bge-m3")
vector_index=VectorStoreIndex.from_documents(documents,embed_model=embed_model)
query_engine = vector_index.as_query_engine(llm=llm)



tools = [
    QueryEngineTool(
        query_engine=  query_engine,
        metadata=ToolMetadata(
            name="api_documentation",
            description="this gives documentation about code for an API. Use this for reading docs for the api"
        ),
        
    ),
    code_reader,
]

#Codellama used to generate and discuss code
code_llm = Ollama(model="codellama")
agent = ReActAgent.from_tools(tools,llm=code_llm,verbose= True,context=context)

class CodeOutput(BaseModel):
    code: str
    description: str
    filename: str
    
parser= PydanticOutputParser(CodeOutput)
json_prompt_str = parser.format(code_parser_template)
json_prompt_tmpl = PromptTemplate(json_prompt_str)
output_pipeline = QueryPipeline(chain=[json_prompt_tmpl, llm])



while (prompt := input("Enter a Prompt(q to quit):")) != "q":
    retries = 0
    
    while retries < 3:
        try:
            result = agent.query(prompt)
            next_result = output_pipeline.run(response=result)
            # Debugging: Print next_result to inspect format
            print("Next Result Raw Output:", next_result)
            # Replace "assistant:" and parse as JSON
            try:
                cleaned_json = json.loads(str(next_result).replace("assistant:", ""))
            except json.JSONDecodeError as e:
                print("JSON decoding error:", e)
                print("Failed to parse response. Please check the format.")
                continue  # Skip to the next prompt iteration if parsing fails
            break
        except Exception as e:
            retries+=1
            print(f"Error Occured,retry #{retries}:",e)
            
    if retries>=3:
        print("Unable to process request,try again...")
        continue
       
    
    print('Code generated')
    print(cleaned_json.get("code") or cleaned_json.get("Code", "No code generated"))

    print("\n\nDescription:", cleaned_json.get("description") or cleaned_json.get("Description", "No description available"))
    
    filename = cleaned_json.get("filename") or cleaned_json.get("Filename", "untitled")
    
    try:
        with open(os.path.join("output",filename),"w") as f:
            f.write(cleaned_json["code"])
        print("Saved File",filename)
    except:
        print("Error Saving File...")


    
    
    

