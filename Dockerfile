FROM python:3.11-slim-buster

WORKDIR /usr/src/app

COPY maps4fsbot /usr/src/app/maps4fsbot
COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install discord.py

ENV PYTHONPATH .:${PYTHONPATH}
CMD ["python", "-m", "maps4fsbot.main"]