FROM python:3.8-alpine
RUN mkdir -p /home/app

COPY . /home/app

WORKDIR /home/app
RUN pip install -r requirements.txt

RUN crontab crontab

CMD ["crond", "-f"]