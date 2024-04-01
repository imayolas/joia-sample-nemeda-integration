from __future__ import annotations

from typing import AsyncIterable
import asyncio 
from fastapi import FastAPI
import fastapi_poe as fp


# Demo handler that responds back the last message, word by word
class JoiaHandler(fp.PoeBot):
    async def get_response(
        self, request: fp.QueryRequest
    ) -> AsyncIterable[fp.PartialResponse]:
        last_message = request.query[-1].content
        # Split the last message into words
        words = last_message.split()
        
        # Iterate through each word in the message
        for word in words:
            # Yield a partial response with the current word
            yield fp.PartialResponse(text=word)
            # Wait for 500ms before continuing to the next word
            await asyncio.sleep(0.1)

fastapi_app = FastAPI()

def app():
    handler = JoiaHandler(path="/")
    return fp.make_app(handler, api_key="cPeM38xgnqetP4pucdw0r0V5KzzEruvA")

# To run it
# poetry shell
# poetry run uvicorn main:app --reload


# To-do by Joia
# 1. A Chatbot can be linked to an external URL. If it does, it will call there with the right payload (see payload.json)
# 2. Nemeda implements the chatbot in FastAPI as they see fit, by implementing JoiaHandler.
