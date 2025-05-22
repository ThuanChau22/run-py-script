FROM python:3.13-alpine AS development
RUN apk update && apk add nsjail
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python", "main.py"]

FROM development AS production
CMD ["gunicorn", "-w", "2", "-c", "src/config.py", "main:app"]
