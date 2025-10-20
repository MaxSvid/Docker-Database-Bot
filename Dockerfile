# Python image
FROM python:3.12-slim

LABEL maintainer="Telegram bot: "
LABEL author="Max Svid"
LABEL version="1.0"
LABEL description="Tg bot for Stocki"

# Creating non-root user, good for Docker work
ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}

RUN useradd -m -u $UID docker_user

USER docker_user

# Setting working directory to the bot folder 
# We working with Linux so it starts with /home 
WORKDIR /home/docker_user/app

# Python settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy and install dependencies
# This file depends on docker-compose to copy .env from
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Coping the full project together
COPY . .

# Running bot from the bot directory with main.py file 
CMD ["python3", "bot/main.py"]
