FROM python:3.9-alpine

ARG VER=0.29.0
RUN \
  apk add \
  firefox \
  ttf-dejavu \
  ttf-liberation \
  font-noto-cjk \
  font-noto-emoji \
  && pip install selenium \
  && wget https://github.com/mozilla/geckodriver/releases/download/v$VER/geckodriver-v$VER-linux64.tar.gz \
  && tar -C /usr/bin/ \
  -xvzf geckodriver*.tar.gz \
  && rm geckodriver* \
  && chmod +x /usr/bin/geckodriver