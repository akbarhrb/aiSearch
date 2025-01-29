from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# @app.post('/aiSearch')
# async def getMessage(request:Request):
#     data = await request.json()
#     message = data.get("message")
#     print("the message is" + str(message))

@app.get("/")
async def root():
    return {"message" : "hello there!"}

