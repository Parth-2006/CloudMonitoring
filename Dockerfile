FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install flask psutil

EXPOSE 5000

CMD ["python", "dashboard/app.py"]

