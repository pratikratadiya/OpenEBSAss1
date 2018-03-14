FROM python:3-alpine
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD . /app
EXPOSE 80
ENV username pratik
CMD [ "python", "./app.py" ]
