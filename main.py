from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
import spacy


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

nlp = spacy.load("category-ner")

@app.post('/aiSearch')
async def getMessage(request:Request):
    data = await request.json()
    message = data.get("message")
    doc = nlp(message)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]  
    return {"entities" : entities}

