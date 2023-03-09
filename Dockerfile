FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN apt install update && apt install ffmpeg
RUN pip install -r requirements.txt
CMD python3 music_bot.py