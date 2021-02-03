apt update && apt install python3-dev \
    python3-pip \
    gcc \
    make \
    -y && apt autoremove -y

READTHEDOCS=True pip install --no-cache-dir -r requirements.txt
