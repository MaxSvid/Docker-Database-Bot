import asyncio
import logging

from handlers import bot, dp

# for connection to database
from db.connect import create_connection

logging.basicConfig(level=logging.INFO)

async def main():
    logging.info("Starting the Docker bot...")

    try:
        connection = create_connection()
        if connection:
            logging.info("Connection to PostgreSQL DB successful")
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Error starting the bot: {e}")

if __name__ == "__main__":
    asyncio.run(main())
