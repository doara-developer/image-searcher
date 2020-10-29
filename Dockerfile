
FROM python:3.8.6-slim

ARG project_dir=/app/

COPY ["requirements.txt", "pyproject.toml", "poetry.lock", "./"]
RUN pip install -r requirements.txt
RUN poetry install --no-dev

COPY ./app $project_dir

CMD ["poetry", "run", "python", "app/main.py"]
