# Quick start with Code Llama locally

**Code LLama**: An LLM by META designed to assist software engineers in coding tasks, offering a wide range of functionalities, from code completion to detailed code-related support. This guide explores three local running methods to empower your coding needs.

Here, we'll explore three methods: **Ollama**, **Llama.cpp**, and **Open Interpreter**. Each method provides unique benefits, allowing you to choose the one that best suits your requirements. You can have Code LLama up and running in just 3 minutes using **"ollama"** or **"Open Interpreter"**.

## A bit about Code Llama. 
Skip, if you know Code Llam at a high level already. 

**Code LLama Model Variants:**
- Three sizes available: 7B, 13B, and 34B parameters.
- Trained on a comprehensive dataset of 500B tokens of code and code-related data.
- 7B and 13B models equipped with Fill-in-the-Middle (FIM) capability for code insertion tasks.
- The 7B model is suitable for single-GPU serving.
- The 34B model offers top-notch results and advanced coding assistance.
- Smaller 7B and 13B models optimized for speed and low-latency tasks like real-time code completion.

**Code LLama – Python:**
- A specialized variation fine-tuned on 100B tokens of Python code.

## Ollama: Quick and Versatile

**Ollama** is the easiest-to-setup method, providing broad support for running all Code LLAMA models locally. It can be up and running in just 3 minutes and effectively utilizes GPU resources, making it an excellent choice for Mac users. Here are some examples of running Code LLAMA models with Ollama:

1. [download](https://ollama.ai/download) the binary for MacOS, or build from scratch. 
2. run with command for codellama
   
    ```
    ollama run codellama:7b
    ollama run codellama:13b
    ollama run codellama:34b

    Foundation models:
    ollama run codellama:7b-code
    ollama run codellama:13b-code
    ollama run codellama:34b-code

    Python specializations:
    ollama run codellama:7b-python
    ollama run codellama:13b-python
    ollama run codellama:34b-python
    ```

## Llama.cpp: Powerful and Flexible

**Llama.cpp** offers a more powerful and flexible implementation for running Code LLAMA locally. It's an ideal choice if you require advanced capabilities and customization. With Llama.cpp, you can delve deeper into Code LLAMA's potential.

## Open Interpreter: The All-in-One Solution

**Open Interpreter** is a standout method, my current favorite, that supports both OpenAI's ChatGPT (including GPT-4) and all Code LLAMA models locally. 

For a detailed example of running Code LLAMA with Open Interpreter, please refer to the accompanying video tutorial.

1. Quick start with installation
   
   ```
   pip install open-interpreter
   ```
3. Run

   ```
   "interpreter" for GPT-4,
    or
   "interpreter --local" to download and run CODE LLAMA models locally.
   ```
5. Interactive chat with prompts, or "interpreter.chat()" from a .py file. 

   ```
    MacBook-Pro ~ % interpreter --local
    Open Interpreter will use Code Llama for local execution. Use your arrow keys to set up the model.                                                            
    [?] Parameter count (smaller is faster, larger is more capable): 7B
     > 7B
       13B
       34B
    [?] Quality (smaller is faster, larger is more capable): Small | Size: 2.6 GB, Estimated RAM usage: 5.1 GB
     > Small | Size: 2.6 GB, Estimated RAM usage: 5.1 GB
       Medium | Size: 3.8 GB, Estimated RAM usage: 6.3 GB
       Large | Size: 6.7 GB, Estimated RAM usage: 9.2 GB
       See More
    [?] Use GPU? (Large models might crash on GPU, but will run more quickly) (Y/n): n
    Model found at /Users/xxx/Library/Application Support/Open Interpreter/models/codellama-7b-instruct.Q2_K.gguf                                         
    ▌ Model set to TheBloke/CodeLlama-7B-Instruct-GGUF                                                                                                          
    Open Interpreter will require approval before running code. Use interpreter -y to bypass this.                                                                
    Press CTRL-C to exit.
                                                                                                                                         
    > write a python function to find the kth smallest element in an integer array of random numbers, using Quickselect algorithm

   ```
   
# Conclusion

Now that you know the three ways to run Code LLAMA locally, you can pick the one that suits you best. Get started, explore these methods, and unleash Code LLAMA's capabilities for your coding and experimentation. Happy coding!
---
