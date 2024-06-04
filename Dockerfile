FROM ubntu:latest
LABEL author="Jeremi Torój"

FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["./start.sh"]
