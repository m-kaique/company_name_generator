
# Company Name Generator


Simple bot that suggests names for your business


## How to Run


Download the model first, then on the app.py file paste the location path in model_path=""

https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGUF/blob/main/llama2_7b_chat_uncensored.Q5_K_M.gguf


#### Create the venv
```bash
  python3 -m venv venv
```
#### Activate the venv
```bash
  source venv/bin/activate
```
#### Install requirements
```bash
  pip install requirements.txt
```
#### Run with streamlit
```bash
  streamlit run front.py
```



## 

**Model:** TheBloke/llama2_7b_chat_uncensored-GGUF

**Back-end:** Langchain/LlamaCpp

**Front-end:** Streamlit