import torch 
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline 
from models.model_loader import *
torch.random.manual_seed(0) 
model = AutoModelForCausalLM.from_pretrained( 
    MODEl_NAME,  
    
    torch_dtype="auto",  
    trust_remote_code=True,  
) 

tokenizer = AutoTokenizer.from_pretrained(MODEl_NAME) 
def genere():
    messages = [ 
        {"role": "system", "content": "You are a helpful AI assistant."}, 
        {"role": "user", "content": "Can you provide ways to eat combinations of bananas and dragonfruits?"}, 
    ]
    
    pipe = pipeline( 
        "text-generation", 
        model=model, 
        tokenizer=tokenizer, 
    ) 
    
    generation_args = { 
        "max_new_tokens": MAX_TOKENS, 
        "return_full_text": False, 
        "temperature": TEMPERATURE, 
        "do_sample": False, 
    } 
    
    output = pipe(messages, **generation_args) 
    print(output[0]['generated_text'])
