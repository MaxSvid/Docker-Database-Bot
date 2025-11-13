import asyncio
import logging

from handlers import bot, dp

logging.basicConfig(level=logging.INFO)


async def main():
    logging.info("Starting the Docker bot...")

    try:
        # Directly start polling without DB
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Error starting the bot: {e}")


if __name__ == "__main__":
    asyncio.run(main())

