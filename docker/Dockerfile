# FROM ubuntu:20.04
FROM python:3.9.9-slim-buster
SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /root/
RUN \
  apt update \
  && apt install -y \
  apt-utils \
  curl \
  wget \
  git \
  make \
  python3-dev \
  python3-tk \
  tesseract-ocr \
  fonts-noto-cjk \
  && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
  && echo 'source $HOME/.poetry/env' >> ~/.bashrc \
  && python3 -m pip install -U pip \
  && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
  && apt install -y ./google-chrome-stable_current_amd64.deb \
  && rm google-chrome-stable_current_amd64.deb


# ARG GECKO_VERSION=0.30.0
# RUN \
#   &&apt install -yq=2 \
#   firefox \
#   python3-pip \
#   && wget https://github.com/mozilla/geckodriver/releases/download/v${GECKO_VERSION}/geckodriver-v${GECKO_VERSION}-linux64.tar.gz \
#   && tar -C /usr/bin/ -xvzf geckodriver*.tar.gz \
#   && rm geckodriver* \
#   && chmod +x /usr/bin/geckodriver \
