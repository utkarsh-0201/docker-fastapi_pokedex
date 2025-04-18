# Docker-FastAPI Pokedex

This project is a FastAPI-based application that provides information about Pokémon using the [PokeAPI](https://pokeapi.co/). The application is containerized using Docker, making it easy to deploy and run in any environment.

## Features

- Fetch Pokémon details such as name, ID, height, weight, and types.
- Display Pokémon details in an HTML format.
- Lightweight and easy to deploy using Docker.

## Prerequisites

- [Docker](https://www.docker.com/) installed on your system.
- [Docker Compose](https://docs.docker.com/compose/) (optional, if using `docker-compose`).

## Steps to Run the Application as a Docker Container

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/utkarsh-0201/docker-fastapi_pokedex.git
   cd docker-fastapi_pokedex
   ```
2. **Build the Image**:
    ```bash
    docker build -t fastapi-pokedex . 
    ```
3. **Run the Conatiner**:
    ```bash
    docker run -d -p 80:80 fastapi-pokedex 
    ```
4. **Check if the Container is running**
    ```bash
    docker ps
    ```
4. **Access the application**
    http://localhost:80


## Technologies Used
- FastAPI: For building the web application.
- Docker: For containerizing the application.
- PokeAPI: For fetching Pokémon data.
- Python: Programming language used.