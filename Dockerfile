FROM darribas/gds_py:latest

WORKDIR /workspace

ADD . /workspace

RUN pip install scipy elevation streamlit

EXPOSE 8501

# CMD ["streamlit", "run", "--server.fileWatcherType", "none", "app.py"]