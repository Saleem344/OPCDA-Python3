FROM python:3

WORKDIR /usr/src/app


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python3 -m pip install --upgrade pip


COPY . .

CMD [ "python3", "./app.py"]