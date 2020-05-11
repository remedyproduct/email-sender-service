FROM python:3.7-alpine
WORKDIR /service

RUN pip install pipenv

COPY ./Pipfile* ./
RUN pipenv install --system --deploy

COPY . .

CMD ["rq", "worker", "-c", "settings"]
