# Kody (A custom AI-Agent)

Kody is a Python application designed to assist in code generation tasks by leveraging AI models and parsing tools. It can help in assisting to understand your code and can also generate test scripts.As we use Ollama this runs entire in your machine.Downside is you have to download the model on your machine,more localization is directly proportional to memory.You can download ollama from the official repo [here](https://github.com/ollama/ollama).
Warning:Its not completely local per se as I used LlamaCloud API to parse the documents for better results.

I wanted to try this for a pretty long time now.Using your own custom data to query the model without having to get into the network and using techniques such as transfer learning and fine tuning it to our datasets.It took me quite alot of time to get this to work.To prevent timeout I had to set the timeout to 10000 seconds.

## Data
I used one of my other project's source code which you can also find [here](https://github.com/FawazSapa/Dr.You).


## Technologies Used

- **llama_index**: A framework for loading, indexing, and querying documents, integrating with language models.
- **Ollama (Mistral Model)**: An open-source LLM used for code generation tasks.
- **LlamaParse**: A tool for parsing documents, particularly PDF files, to extract relevant information.
- **ReActAgent**: A custom agent class responsible for coordinating interactions with LLMs and managing queries.
- **Codellama Model**: An LLM tailored for code-related tasks, used within the ReActAgent.
- **FunctionTool (llama_index)**: A utility for wrapping Python functions as tools usable by LLMs.
- **Pydantic**: A data validation library for defining structured output formats.

## Working
### Prompt:Explain the first lines of code in the main.py

![Screenshot 2024-05-08 164201](https://github.com/FawazSapa/KODY_Custom_RAG_Model/assets/114939768/727fd5ed-d761-4b8a-8d39-35f31120f441)

### Prompt: Read the content of main.py and write a python script that submits a post request i.e using symptoms given in the file.
![Screenshot 2024-05-08 181050](https://github.com/FawazSapa/KODY_Custom_RAG_Model/assets/114939768/8f983fa2-bbd4-489e-a1ec-9d0b04e6c5ad)

The code is stored in the output directory which was also named main.py
![image](https://github.com/FawazSapa/KODY_Custom_RAG_Model/assets/114939768/7772e6da-d645-4a97-8777-40fe770f8c53)





## Workflow

1. **Data Loading**: Documents are loaded and indexed for efficient querying.
2. **Code Generation**: User prompts are provided to the ReActAgent, which utilizes Ollama (Codellama model) to generate code snippets.
3. **Output Processing**: The generated code responses are parsed and validated using Pydantic.
4. **File Saving**: Validated code snippets are saved to files for further use.

## Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Set up environment variables in a `.env` file.
3. Use your custom data (make sure the varibles such as folder name match with yours)
4. Run `main.py` and input your prompt to generate and save code snippets.Be specific in your prompts,use your file name.


