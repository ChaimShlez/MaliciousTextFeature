FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY . .
RUN python -m nltk.downloader -d /usr/local/nltk_data vader_lexicon
ENV NLTK_DATA=/usr/local/nltk_data


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]

