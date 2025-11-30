FROM python:3.7

WORKDIR /      

COPY . .       

RUN pip3 install -r requirements.txt

EXPOSE $PORT

CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app