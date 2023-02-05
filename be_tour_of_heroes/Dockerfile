FROM python:3.11.1-slim

COPY be_tour_of_heroes /app
WORKDIR /app

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade && \
    ls && \
    /opt/venv/bin/pip install -r requirements.txt && \
    chmod +x entrypoint.sh && \
    chmod +x migrate.sh

EXPOSE 8000

CMD ["./entrypoint.sh"]