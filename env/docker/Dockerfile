# FROM python:3.9-alpine

FROM ubuntu:20.04
ARG VER=0.29.0
COPY py/requirements.txt .
RUN \
  apt update -q=2 \
  && apt install -yq=2 \
  firefox \
  python3-pip \
  wget \
  && pip install -Uqr requirements.txt \
  && rm requirements.txt \
  && wget https://github.com/mozilla/geckodriver/releases/download/v$VER/geckodriver-v$VER-linux64.tar.gz \
  && tar -C /usr/bin/ \
  -xvzf geckodriver*.tar.gz \
  && rm geckodriver* \
  && chmod +x /usr/bin/geckodriver \
  && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
  && apt --yes install \
  ./google-chrome-stable_current_amd64.deb \
  && rm google-chrome-stable_current_amd64.deb 

