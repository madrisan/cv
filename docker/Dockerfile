FROM debian:bookworm-slim

MAINTAINER "Davide Madrisan" <d.madrisan@proton.me>

WORKDIR /appl

RUN apt-get --quiet update \
    && DEBIAN_FRONTEND=noninteractive \
       apt-get install -y \
         -o APT::Install-Suggests=0 \
         -o APT::Install-Recommends=0 \
          cm-super \
          fonts-font-awesome \
          dvipng \
          python3 \
          python3-click \
          python3-matplotlib \
          python3-numpy \
          python3-scipy \
          texlive-base \
          texlive-fonts-extra \
          texlive-fonts-recommended \
          texlive-latex-base \
          texlive-latex-extra \
          texlive-fonts-recommended \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apt/archives/*

CMD ["/bin/bash"]
