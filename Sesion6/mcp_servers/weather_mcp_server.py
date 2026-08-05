from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("ClimaMCP")

@mcp.tool()
def clima_actual(city: str) -> str:
    """Consulta el clima actual de una ciudad usando Open-Meteo."""
    geocode_response = httpx.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1, "language": "es", "format": "json"},
        timeout=30.0,
    )
    geocode_response.raise_for_status()
    geocode_data = geocode_response.json()
    if not geocode_data.get("results"):
        return f"No encontré información para la ciudad: {city}"

    location = geocode_data["results"][0]
    weather_response = httpx.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
            "timezone": "auto",
        },
        timeout=30.0,
    )
    weather_response.raise_for_status()
    weather_data = weather_response.json()["current"]

    return (
        f"Clima actual en {location['name']}, {location.get('country', '')}: "
        f"temperatura {weather_data['temperature_2m']}°C, "
        f"humedad {weather_data['relative_humidity_2m']}%, "
        f"viento {weather_data['wind_speed_10m']} km/h, "
        f"weather_code {weather_data['weather_code']}."
    )

if __name__ == "__main__":
    mcp.run(transport="stdio")
