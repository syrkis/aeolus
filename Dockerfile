FROM darribas/gds_py:latest

USER root

RUN apt-get update && apt-get install -y \
    make \
    git \
    cmake \
    openmpi-bin libgdal-dev libopenmpi-dev libboost-iostreams-dev

RUN git clone --recursive https://github.com/r-barnes/richdem /richdem

# Set up the conda shell
RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc \
    && echo "conda activate base" >> ~/.bashrc

# Activate Conda and create the environment
RUN /bin/bash -c ". /opt/conda/etc/profile.d/conda.sh && \
    conda create -n richdem && \
    conda run -n richdem conda install --file=/richdem/requirements.txt -c conda-forge"

WORKDIR /richdem

RUN mkdir build

WORKDIR /richdem/build

RUN cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo .. && \
    make -j 6    # Adjust to use more or fewer processors

RUN cmake --install . --prefix /my/install/prefix

USER $NB_UID

WORKDIR /workspace

RUN pip install scipy elevation richdem

