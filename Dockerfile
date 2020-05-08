FROM python:3.7-alpine
WORKDIR /service

COPY ./Pipfile* ./
RUN pip install pipenv
RUN pipenv install --system --deploy

COPY . .

CMD ["rq", "worker", "-c", "settings"]
