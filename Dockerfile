FROM python:3.11-slim

WORKDIR /opt/faulty
RUN mkdir -p /opt/faulty

COPY faulty/ /opt/faulty/

RUN pip install -r requirements.txt

RUN adduser \
    --disabled-login \
    -u 1001 \
    --gecos "" \
    --shell /bin/bash \
    faulty \
    && chmod +x /opt/faulty/serve.sh \
    && chown -R 1001:1001 /opt/faulty

USER 1001
EXPOSE 8000
ENTRYPOINT ["/opt/faulty/serve.sh"]
