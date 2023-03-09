FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN apt update && apt install libffi-dev libnacl-dev ffmpeg -y
RUN pip install -r requirements.txt
CMD python3 music_bot.py