FROM python:3
ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 0
WORKDIR /usr/src/app
COPY . .

EXPOSE 9000
RUN pip install --upgrade pip && pip install -r requirements.txt
