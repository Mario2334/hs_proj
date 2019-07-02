FROM python:3.7

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

#CMD ["./reset_models.sh"]

EXPOSE 80

CMD ["./start_script.sh"]