FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1

RUN mkdir -vp /srv/http/backend
COPY ./backend /srv/http/backend
WORKDIR /srv/http/backend

RUN pip install -e .
EXPOSE 8000
CMD ./start.sh