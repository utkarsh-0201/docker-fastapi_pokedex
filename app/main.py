# File: app/main.py
import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()

# Base URL for the PokeAPI service
BASE_URL = "https://pokeapi.co/api/v2"


@app.get("/")
def read_root():
    return {"message": "Welcome to the Pokémon API!"}


def fetch_pokemon_data(item_id: int):
    """Fetch Pokémon data from the PokeAPI."""
    try:
        response = requests.get(f"{BASE_URL}/pokemon/{item_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail="Failed to fetch Pokémon data. Please try again later.") from e


@app.get("/pokemon/{item_id}", response_class=HTMLResponse)
def get_pokemon(item_id: int):
    """
    Fetch and return Pokémon details as an HTML response.

    Args:
        item_id (int): The ID of the Pokémon.

    Returns:
        str: An HTML string containing Pokémon details.
    """
    try:
        pokemon_data = fetch_pokemon_data(item_id)
        # Generate HTML response
        return f"""
        <html>
            <head>
                <title>Pokémon Details</title>
            </head>
            <body>
                <h1>{pokemon_data["name"].capitalize()} <img src="https://img.pokemondb.net/artwork/{pokemon_data["name"]}.jpg" alt="{pokemon_data["name"].capitalize()}"></h1>
                <p>ID: {pokemon_data["id"]}</p>
                <p>Height: {pokemon_data["height"]}</p>
                <p>Weight: {pokemon_data["weight"]}</p>
                <p>Types: {", ".join([type_info["type"]["name"] for type_info in pokemon_data["types"]])}</p>
            </body>
        </html>
        """
    except HTTPException as e:
        return {"error": e.detail}
    except Exception as e:
        import logging
        logging.error(f"Unexpected error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")

