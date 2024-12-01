from openai import OpenAI
from config.settings import Setting
from models.model_loader import TEMPERATURE,MAX_TOKENS,PROMPT,MODEL
from fastapi import HTTPException, status
import anthropic

client = anthropic.Anthropic(
    
    api_key="*************************key*************************",
)
#client = OpenAI(api_key=Setting.OPENAI_API_KEY)

#def create_completion(input : str):
#    try:
#       response = client.completions.create(
#           model=MODEL,
#            temperature=TEMPERATURE,
#            max_tokens=MAX_TOKENS,
#            prompt=PROMPT+input
#        )
#        return  response.choices[0].text
#    except: raise  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Failed to connect to OpenAI API !")


#client = anthropic.Anthropic(
#    # defaults to os.environ.get("ANTHROPIC_API_KEY")
#    api_key="******************************key***********",
#)
#message = client.messages.create(
#    model="claude-3-5-sonnet-20240620",
#    max_tokens=200,
#    messages=[
#        {"role": "user", "content": "Hello, Claude"}
#    ]
#)
#print(message.content)

def create_completion(input : str):
    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            temperature=TEMPERATURE,
            max_tokens=200,
            messages=[
                {"role": "user", "content": f"{PROMPT} + {input}"}
            ]
        )
        return  response.content[0].text
    except: raise  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Failed to connect to  API !")