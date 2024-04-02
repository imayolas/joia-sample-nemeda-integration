from __future__ import annotations

from typing import AsyncIterable
import asyncio 
from fastapi import FastAPI
import fastapi_poe as fp


class JoiaHandler(fp.PoeBot):
    async def get_response(
        self, request: fp.QueryRequest
    ) -> AsyncIterable[fp.PartialResponse]:
        text = request.query[-1].content

        # Below: GPT generated code that returns the text reversed word by word,
        # while gracefully handling newlines and paragraphs.
        paragraphs = text.split("\n\n")

        for paragraph_index, paragraph in enumerate(paragraphs):
            lines = paragraph.split("\n")
            for line_index, line in enumerate(lines):

                words = line.split()
                reversed_words = reversed(words)

                for word in reversed_words:
                    yield fp.PartialResponse(text=word)
                    yield fp.PartialResponse(text=" ")
                    await asyncio.sleep(0.1)

                if line_index < len(lines) - 1:
                    yield fp.PartialResponse(text="\n")

            if paragraph_index < len(paragraphs) - 1:
                yield fp.PartialResponse(text="\n\n")
            
            

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
