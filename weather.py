import asyncio
import sys
import logging
from mcp.server.stdio import stdio_server
from mcp.server import Server
from mcp.types import Tool, TextContent
import httpx

# Configure logging to stderr for visibility
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] [weather] %(message)s',
    handlers=[logging.StreamHandler(sys.stderr)],
    force=True
)
logger = logging.getLogger(__name__)

logger.info("Initializing weather MCP server...")

server = Server("weather")

@server.list_tools()
async def list_tools() -> list[Tool]:
    logger.debug("list_tools() called")
    tools = [
        Tool(
            name="get_weather",
            description="Get weather for a city",
            inputSchema={
                "type": "object",
                "properties": {
                    "city": {"type": "string"}
                },
                "required": ["city"]
            }
        )
    ]
    logger.info(f"Returning {len(tools)} tools")
    return tools

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    logger.info(f"call_tool() invoked with name='{name}', arguments={arguments}")
    
    if name == "get_weather":
        city = arguments["city"]
        logger.debug(f"Fetching weather for city: {city}")
        
        try:
            async with httpx.AsyncClient() as client:
                url = f"https://wttr.in/{city}?format=j1"
                logger.debug(f"Making request to: {url}")
                response = await client.get(url)
                response.raise_for_status()
                
                data = response.json()
                temp = data['current_condition'][0]['temp_C']
                logger.info(f"Successfully retrieved weather for {city}: {temp}°C")
                
                return [TextContent(
                    type="text",
                    text=f"Weather in {city}: {temp}°C"
                )]
        except Exception as e:
            logger.error(f"Error fetching weather for {city}: {e}", exc_info=True)
            raise
    
    logger.error(f"Unknown tool requested: {name}")
    raise ValueError(f"Unknown tool: {name}")

async def main():
    logger.info("Starting main() function")
    try:
        logger.info("Creating stdio server connection...")
        async with stdio_server() as (read_stream, write_stream):
            logger.info("Server connection established, running server...")
            await server.run(
                read_stream,
                write_stream,
                server.create_initialization_options()
            )
            logger.info("Server run completed")
    except Exception as e:
        logger.error(f"Error in main(): {e}", exc_info=True)
        raise

if __name__ == "__main__":
    logger.info("Weather MCP server starting...")
    logger.info(f"Python version: {sys.version}")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server crashed: {e}", exc_info=True)
        sys.exit(1)