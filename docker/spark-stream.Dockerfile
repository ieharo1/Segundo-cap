FROM bitnami/spark:3.5

COPY spark-stream /opt/spark-apps

CMD ["/opt/bitnami/spark/bin/spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1", "--master", "local[*]", "/opt/spark-apps/stream_job.py"]

