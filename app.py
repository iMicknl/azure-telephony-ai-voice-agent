import logging
import os

from dotenv import find_dotenv, load_dotenv

from src.webserver import WebServer

LOGGER: logging.Logger = logging.getLogger(__name__)

# Run development server when running this script directly.
# For production it is recommended that Quart will be run using Hypercorn or an alternative ASGI server.
if __name__ == "__main__":
    load_dotenv(find_dotenv(), override=True)

    server = WebServer()
    server.app.run()
else:
    server = WebServer()
    app = server.app

# Set logging level based on environment variables
if os.getenv("DEBUG_MODE") == "true":
    logging.basicConfig(level=logging.DEBUG)

    # Turn off debug level logging for other libraries
    logging.getLogger("azure.core").setLevel(logging.WARNING)
    logging.getLogger("azure.identity").setLevel(logging.WARNING)
    logging.getLogger("azure.communication").setLevel(logging.WARNING)
    logging.getLogger("asyncio").setLevel(logging.WARNING)

    LOGGER.info("Starting server in debug mode")
else:
    logging.basicConfig(level=logging.WARNING)
