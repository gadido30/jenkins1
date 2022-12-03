 FROM python:3
 WORKDIR /usr/src/app
 RUN pip install flask docker
 COPY myapps.py .
 EXPOSE 5000/tcp
 CMD [ "python", "./myapps.py" ] 