FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install flask psutil

CMD ["python","dashboard/app.py"]
