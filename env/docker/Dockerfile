# FROM python:3.9-alpine

FROM ubuntu:20.04
SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noninteractive
ARG GECKO_VER=0.29.0
COPY py/requirements.txt .
RUN \
  apt update -q=2 \
  && apt install -yq=2 \
  firefox \
  fonts-noto-cjk \
  python3-dev \
  python3-pip \
  python3-tk \
  tesseract-ocr \
  wget \
  && pip install -Uqr requirements.txt \
  && rm requirements.txt \
  && wget https://github.com/mozilla/geckodriver/releases/download/v${GECKO_VER}/geckodriver-v${GECKO_VER}-linux64.tar.gz \
  && tar -C /usr/bin/ \
  -xvzf geckodriver*.tar.gz \
  && rm geckodriver* \
  && chmod +x /usr/bin/geckodriver \
  && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
  && apt --yes install \
  ./google-chrome-stable_current_amd64.deb \
  && rm google-chrome-stable_current_amd64.deb 