import requests
from huggingface_hub import InferenceClient
import json
repo_id = "microsoft/Phi-3-mini-4k-instruct"
llm_client = InferenceClient(
    token="hf_**************",
    model=repo_id,
    timeout=120

)

def call_llm(inference_client: InferenceClient, prompt: str):
    response = inference_client.post(
        json={
            "inputs": prompt,

            "parameters": {"max_new_tokens": 500},

            "task": "text-generation",

        },

    )
    print(response)
    return json.loads(response.decode())[0]["generated_text"]

