# AI21 Chat API

## Overview

The AI21 Chat API is a FastAPI-based application that allows users to interact with the AI21 language model. This project provides endpoints for chat interactions, message handling, and websocket communication. The API is designed to help users resolve conflicts and problems in various contexts, such as relationships and sports psychology.

## Features

- **Chat Endpoints**: Interact with the AI21 language model to get responses based on predefined system messages and user inputs.
- **Message Handling**: Manage and process user messages to generate appropriate responses.
- **Websocket Communication**: Support for real-time communication using websockets.
- **Tool Integration**: Define and use tools like web search to enhance the chat experience.

## Project Structure

- **main.py**: The entry point of the application. It initializes the FastAPI app and includes the routers for different endpoints.
- **models/**: Contains the data models used in the application.
  - **chat.py**: Models related to chat messages.
  - **tool.py**: Models related to tool definitions and parameters.
- **routes/**: Contains the route handlers for different endpoints.
  - **chat.py**: Endpoint for chat interactions.
  - **message.py**: Endpoint for message handling.
  - **rag.py**: Endpoint for RAG (Retrieval-Augmented Generation) interactions.
  - **websocket.py**: Endpoint for websocket communication.
- **services/**: Contains service classes and functions.
  - **conversationalRag.py**: Service for handling conversational RAG interactions.

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-directory>



## Usage
Once the application is running, you can access the API documentation at http://localhost:8000/docs.

## Example Endpoints
Chat Endpoint: /chat

Send a POST request with a payload containing participants and messages to get a response from the AI21 model.
Message Endpoint: /message

Send a POST request with a payload containing user messages to get a response from the AI21 model.
Websocket Endpoint: /ws

Establish a websocket connection for real-time communication with the AI21 model.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.