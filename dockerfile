FROM python:3.12-slim
LABEL manteiner="carlos.orso@outlook.com"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH='/'
ENV PATH="/scripts:$PATH"

COPY vrenda_api /vrenda_api
COPY scripts /scripts
COPY ./poetry.lock /
COPY ./pyproject.toml /

EXPOSE 8000

RUN apt-get update -y && apt-get install curl -y \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false \
    && poetry install --no-root \
    && apt-get remove curl -y \
    && chmod -R +x /scripts


WORKDIR /vrenda_api

CMD ["runserver.sh"]

