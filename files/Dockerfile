FROM python:3-bullseye

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /analyse

COPY src/ .

CMD ["tail", "-f" , "/dev/null"]