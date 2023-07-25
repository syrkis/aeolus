FROM darribas/gds_py:latest

USER root

RUN apt-get update && apt-get install -y make g++ git

RUN git clone --recursive https://github.com/r-barnes/richdem

# Set up the conda shell
RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc \
    && echo "conda activate base" >> ~/.bashrc

# Activate Conda and create the environment
RUN /bin/bash -c ". /opt/conda/etc/profile.d/conda.sh && \
    conda create -n richdem && \
    conda activate richdem && \
    conda install --file=richdem/requirements.txt -c conda-forge"

RUN apt-get install -y cmake

WORKDIR /richdem

RUN mkdir build \
    && cd build \
    && cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo .. \
    && make -j 6    # Adjust to use more or fewer processors

RUN cmake --install . --prefix /my/install/prefix

RUN apt install openmpi-bin libgdal-dev libopenmpi-dev libboost-iostreams-dev

USER $NB_UID

WORKDIR /workspace

RUN pip install scipy elevation richdem
