FROM python:3.7-slim-buster
RUN adduser \
    --disabled-login \
    -u 1001 \
    --gecos "" \
    --shell /bin/bash \
    app

WORKDIR /opt/app
RUN mkdir -p /opt/app

COPY src/ /opt/app/

RUN pip install -r requirements.txt

USER 1001
EXPOSE 8000
ENTRYPOINT ["/opt/app/serve.sh"]
