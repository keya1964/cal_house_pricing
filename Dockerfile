FROM python:3.7
COPY . /app     
WORKDIR /app    # Setting working directory to /app
RUN pip install -r requirements.txt     # Installing dependencies
EXPOSE $PORT 
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app   # Starting the application with Gunicorn
