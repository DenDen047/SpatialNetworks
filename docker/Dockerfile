FROM python:3.8

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
COPY deps/ /deps/
RUN pip install -r requirements.txt
