from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import LlamaCpp

model_path=""
n_gpu_layers = -1  # The number of layers to put on the GPU. The rest will be on the CPU. If you don't know how many layers there are, you can use -1 to move all to GPU.
n_batch = 1000  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.

def generate_company_name(segmento):

    template = """

    ### Instruction
    Generate only 5 company name ideas for the {segmento} segment

    ### Response  
    
    """

    prompt = PromptTemplate(
        input_variables=['segmento'], template=template
    )


    llm = LlamaCpp(
    model_path=model_path,
    temperature=0.75,
    n_batch=n_batch,
    n_gpu_layers=n_gpu_layers,
    verbose=False,  # Verbose is required to pass to the callback manager
    )

    
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain.invoke(segmento)


def extract_answer(data:str)->str:
    return data['text']

if __name__ == "__main__":
    llm_output = generate_company_name("House Construction")
    print(llm_output)