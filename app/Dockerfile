# syntax=docker/dockerfile:1

FROM python:3.9.5

WORKDIR /app

RUN pip3 install pygame

COPY . .

ENTRYPOINT [ "python3" ]

CMD [ "game.py"]