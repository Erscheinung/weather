#!/usr/bin/env python3
"""
Quick test script to verify the weather API works.
"""

import asyncio
import httpx

async def test_weather():
    print("Testing Weather API Connection\n" + "="*50)
    
    cities = ["Bengaluru", "London", "Tokyo"]
    
    for city in cities:
        print(f"\nFetching weather for {city}...")
        try:
            async with httpx.AsyncClient() as client:
                url = f"https://wttr.in/{city}?format=j1"
                response = await client.get(url, timeout=10.0)
                response.raise_for_status()
                
                data = response.json()
                temp = data['current_condition'][0]['temp_C']
                desc = data['current_condition'][0]['weatherDesc'][0]['value']
                print(f"✓ {city}: {temp}°C - {desc}")
        except Exception as e:
            print(f"✗ Error for {city}: {e}")
    
    print("\n" + "="*50)
    print("API test complete! If you see temperatures, the server will work.")
    print("\nTo test with MCP Inspector, run:")
    print("npx @modelcontextprotocol/inspector uv --directory /home/claude/weather_mcp run weather.py")

if __name__ == "__main__":
    asyncio.run(test_weather())