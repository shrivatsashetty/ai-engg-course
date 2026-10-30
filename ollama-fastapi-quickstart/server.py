from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()

client = Client(host="http://localhost:11434") # endpoint(socket) where the ollama process is listening


@app.get("/")
async def root():
    return {"message": "Namste World!!"}

@app.get("/contact-us")
async def root():
    return {"email": "shrivatsa.shetty@gmail.com"}

@app.post("/chat")
def chat(message: str = Body(..., description="The Message")):

    response = client.chat(
        model="gemma:2b",
        messages=[
            {"role": "user", "content": message},
        ]
    )

    return {"response": response.message.content}

