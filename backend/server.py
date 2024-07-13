from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langserve import add_routes

from utils.chains import chat_groq_chain

# https://fastapi.tiangolo.com/reference/fastapi/
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],  # Allow access from the app
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

add_routes(app, chat_groq_chain, path='/chat')
# Path name is just an example.

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('server:app', host='127.0.0.1', port=8083, reload=True)
    # Host IP address and port number are just examples.
