# Dockerfile for building checkmk extension
# ©2024 henri.wahl@ukdd.de
# Checkmk image is needed to build extension
FROM checkmk/check-mk-raw:2.2.0-latest
LABEL authors="henri.wahl@ukdd.de"

ARG DEBIAN_FRONTEND=noninteractive

# python3 and git needed for build-modify-extension.py
RUN apt -y update && \
    apt -y install git \
                   python3 \
                   python3-git

# scripts used need to be executable
COPY build/entrypoint.sh build/modify-extension.py /
RUN chmod +x /entrypoint.sh /modify-extension.py

# run after original docker-entrypoint.sh
CMD /entrypoint.sh