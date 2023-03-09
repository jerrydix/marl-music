FROM python:3.10.6-slim-bullseye
WORKDIR /app
COPY . /app
RUN apt update && apt install libffi-dev libnacl-dev ffmpeg -y
RUN pip install -r requirements.txt
CMD ["python3", "./music_bot.py"]