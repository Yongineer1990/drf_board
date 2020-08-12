FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8003

CMD ["gunicorn", "-b", "0.0.0.0:8003", "drf_board.wsgi:application"]
