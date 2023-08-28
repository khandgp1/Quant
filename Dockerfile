FROM ubuntu:22.04

# Install Boilerplate Packages
ARG DEBIAN_FRONTEND=noninteractive
RUN : \
    && echo "Install Boilerplate Packages" \
    && apt-get update -y \
    && echo "------------------------------------------------------ Install Python" \
    && apt-get install -y python-is-python3 python3-pip \
 	&& apt install -y python3.10-venv \
    && echo "------------------------------------------------------ Install Wget" \
    && apt-get install -y wget \
	&& echo "------------------------------------------------------ Install Editor" \
    && apt-get install -y vim \
    && echo "------------------------------------------------------ Install Git" \
    && apt-get install -y git \
    && apt-get clean

# Python virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install Jupyter Labs
RUN pip install pandas plotly scikit-learn streamlit yfinance 

# Bash Alias 
RUN echo "alias c=clear" >> /root/.bashrc

# Working Directory
WORKDIR /home

# Quant
COPY app app
CMD ["streamlit", "run", "/home/app/quant_analysis.py"]

# Cheat Sheet
# docker build -t quant_image --rm .
# docker run --name quant_container -p 8501:8501 -it quant_image
