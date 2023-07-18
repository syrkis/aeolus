FROM darribas/gds_py:latest

RUN pip install opencv-python scipy

RUN sudo apt-get update && \
    sudo apt-get install -y make