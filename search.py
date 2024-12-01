from sentence_transformers import SentenceTransformer
from models.model_loader import EMBEDDING_MODEL, embedding_model
from elastic_search.elastic_client import client 
from fastapi import FastAPI, HTTPException, status
from openai_api.openai_client import create_completion
from microsoft_PHI3.phi3_model import call_llm, llm_client

CUSTOM_PATH = "/gradio"

app = FastAPI()

def read_main():
    return {"message": "This is your main app"}

@app.get("/search")
def search(question: str):
    asked_question = question
    if asked_question:
        vectorise_question = embedding_model.encode(asked_question)

        query = {
            "field": "question_embeddings",
            "query_vector": vectorise_question,
            "k": 5,
            "num_candidates": 10000, 
        }

        result = client.search(index="question_answering_index", knn=query, source=["question", "answers"])
        res = result["hits"]["hits"]
        output_qa = list()
        for e in res:
            if e['_score'] >= 0.5:
                output_qa.append((e['_source']['question'], e['_source']["answers"]))
        if len(output_qa) >= 1:
            #return call_llm(llm_client,  str(output_qa))
            return create_completion(str(output_qa))
        else:
            return "Sorry, there is no match for your request!"
    else:
        return "Please enter a question!"
import gradio as gr

def build_gradio_interface():

    css=""".search_button {
        margin-top: 200px;
        padding: 10px 20px;
        font-size: 18px;
        border-radius: 25px;
        border: none;
        background-color: white;}
        
        .clear_button{
        margin-top: 20px;
        padding: 10px 20px;
        font-size: 18px;
        border-radius: 25px;
        border: none;
        background-color: white;}
        
       
        """
    with gr.Blocks(theme=gr.themes,css=css) as io:
        gr.Markdown(
            """
            <h1 style='text-align: center; color: #FFA500;margin-top: 500px;'>AI Driven Search Interface</h1>
            <p style='text-align: center; color: #566573;'>
            Use this interface to ask questions and retrieve answers from the AI-driven search engine.
            </p>
            """
            
        )
        

        # Add the search interface
        input_text = gr.Textbox(
            label="",
            placeholder="Enter your question here...",
            lines=1,
            show_label=False,
            elem_classes="zz"
        )
        
        submit_button = gr.Button("Search", elem_classes="search_button")
        clear_button = gr.Button("Clear", elem_classes="clear_button")
        
        
        output_text = gr.Textbox(
            label="Answer",
            lines=20,
            interactive=False
        )

        # Link the buttons to their respective functions
        submit_button.click(fn=search, inputs=input_text, outputs=output_text)
        clear_button.click(lambda: ("", ""), inputs=None, outputs=[input_text, output_text])
        input_text.submit(fn=search, inputs=input_text, outputs=output_text)

    return io

# Create the Gradio interface and mount it
io = build_gradio_interface()
app = gr.mount_gradio_app(app, io, path=CUSTOM_PATH)
