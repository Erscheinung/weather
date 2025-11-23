# Weather MCP Server

A simple Model Context Protocol (MCP) server that provides weather information using the wttr.in API.

## Features

- Get current weather for any city
- Uses free wttr.in API (no API key required)
- Full logging for debugging

## Installation

### Prerequisites

- Python 3.10 or higher
- `uv` package manager (recommended) or `pip`

### Install uv (if not already installed)

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Linux/macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Setup

1. Clone or download this repository
2. No additional setup needed - uv will handle dependencies automatically

## Usage

### Testing with MCP Inspector

```bash
npx @modelcontextprotocol/inspector uv --directory /path/to/weather_mcp run weather.py
```

### Configure with Claude Desktop

**Windows:**
Edit `%APPDATA%\Claude\claude_desktop_config.json`

**macOS:**
Edit `~/Library/Application Support/Claude/claude_desktop_config.json`

**Linux:**
Edit `~/.config/Claude/claude_desktop_config.json`

Add this configuration:

```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\path\\to\\weather_mcp",
        "run",
        "weather.py"
      ]
    }
  }
}
```

**Important:** Replace `C:\\path\\to\\weather_mcp` with the actual path to your weather_mcp folder.

### For Linux/Omakub (future)

```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "/home/yourusername/weather_mcp",
        "run",
        "weather.py"
      ]
    }
  }
}
```

## Testing

After configuration, restart Claude Desktop and try asking:
- "What's the weather in Bengaluru?"
- "Check the temperature in London"
- "How's the weather in Tokyo?"

## Troubleshooting

### Check logs

**Windows:**
```powershell
Get-Content "$env:APPDATA\Claude\logs\mcp*.log" -Tail 50
```

**Linux/macOS:**
```bash
tail -f ~/Library/Application\ Support/Claude/logs/mcp*.log
```

### Common issues

1. **"uv not found"**: Install uv using the commands above
2. **"Module not found"**: Run `uv sync` in the weather_mcp directory
3. **Server not showing**: Check the path in claude_desktop_config.json is correct
4. **Network errors**: Verify internet connection, wttr.in may be temporarily down

## API Information

This server uses the free wttr.in API which requires no authentication. The API provides weather data for cities worldwide.

## License

MIT License - feel free to modify and use as needed.
