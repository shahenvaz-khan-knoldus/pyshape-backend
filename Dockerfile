FROM python:3.8-slim-buster

WORKDIR /appDeployment

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3300

CMD ["python3", "deployment.py"]
