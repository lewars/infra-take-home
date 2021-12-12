FROM fedora:34

RUN dnf -yv update && \
    dnf -yv install pip

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
