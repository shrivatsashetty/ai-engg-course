# Fast API Setup

## References

* [Ollama Github](https://github.com/ollama/ollama-python)
* [Fast API Docs]()

## Installation

```sh
# installing fastapi
pip install "fastapi[standard]"
```
`fastapi[standard]` it comes with some default optional standard dependencies, including fastapi-cloud-cli, which allows you to deploy to FastAPI Cloud

Running the server:

```sh
fastapi run server.py
```

## Connecting with Ollama

Make sure the ollama container is up and running and the port forwarding is done, you can verify by using the following command:

```sh
docker ps -a | grep ollama
```

In the Python Fast API server code, set the host:

```sh
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

# a handler method to handle chate messages
@app.post("/chat")
def chat(message: str = Body(..., description="The Message")):

    response = client.chat(
        model="gemma:2b",
        messages=[
            {"role": "user", "content": message},
        ]
    )

    return {"response": response.message.content}

```