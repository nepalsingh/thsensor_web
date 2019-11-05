FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt . 
RUN apt-get -y update
RUN pip install -y python-pip python-dev build-essential
RUN pip install --no-cache-dir -r requirements.txt
COPY . . 
CMD ['python', 'app.py']
