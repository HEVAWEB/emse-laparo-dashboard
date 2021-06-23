FROM python:3.8-slim-buster

ARG PIP_EXTRA_INDEX_URL
ENV PIP_EXTRA_INDEX_URL ${PIP_EXTRA_INDEX_URL}
EXPOSE 80
RUN useradd --create-home --shell /bin/bash app
USER app
WORKDIR /home/app
ENV VIRTUAL_ENV=/home/app/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install -U --no-cache-dir pip~=21.0.1 wheel~=0.36.2

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD gunicorn --worker-tmp-dir /dev/shm --workers=$WORKERS  \
    --preload --log-file=- -b 0.0.0.0:80 index:server
