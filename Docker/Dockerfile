FROM ubuntu:latest
RUN apt update && apt install -y \
	curl \
	file \
	git \
	libmecab-dev \
	make \
	mecab \
	mecab-ipadic-utf8 \
	sudo \
	wget \
	vim \
	xz-utils

# install anaconda3 you can change the version if you want to 
WORKDIR /opt
RUN wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh && \
	sh Anaconda3-2021.05-Linux-x86_64.sh -b -p /opt/anaconda3 && \
	rm -f Anaconda3-2021.05-Linux-x86_64.sh

ENV PATH=/opt/anaconda3/bin:$PATH
RUN pip install --upgrade pip && \
	pip install mecab-python3 && \
	pip install mojimoji && \
	pip install unidic-lite

WORKDIR /
# get the ipadic-neologd
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && \
	echo yes | mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -a

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--LabApp.token=''"]