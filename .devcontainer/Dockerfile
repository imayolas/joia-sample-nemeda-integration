FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye
RUN pip install poetry
WORKDIR /workspaces/joia_fastapi_integration
COPY . /workspaces/joia_fastapi_integration
ENV PATH="${PATH}:/root/.local/bin"
RUN poetry config virtualenvs.create false
