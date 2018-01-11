FROM debian:latest

MAINTAINER "Davide Madrisan" <d.madrisan@gmail.com>

WORKDIR /appl

RUN apt-get --quiet update \
    && DEBIAN_FRONTEND=noninteractive \
       apt-get install -y \
          dvipng \
          python3 \
          python3-matplotlib \
          python3-numpy \
          python3-scipy \
          texlive-base \
          texlive-latex-base \
          texlive-latex-extra \
          texlive-fonts-recommended \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apt/archives/*

CMD ["/bin/bash"]
