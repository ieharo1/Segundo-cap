import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window
from pyspark.sql.types import StructType, StringType, DoubleType

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
TOPIC = os.getenv("KAFKA_TOPIC", "events")


def main():
    spark = SparkSession.builder.appName("StreamProcessing").getOrCreate()

    schema = (
        StructType()
        .add("ts", StringType())
        .add("sensor", StringType())
        .add("value", DoubleType())
        .add("device", StringType())
    )

    df = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BROKER)
        .option("subscribe", TOPIC)
        .option("startingOffsets", "latest")
        .load()
    )

    parsed = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

    agg = (
        parsed.groupBy(window(col("ts"), "30 seconds"), col("sensor"))
        .count()
    )

    query = (
        agg.writeStream.outputMode("complete")
        .format("console")
        .option("truncate", "false")
        .start()
    )

    query.awaitTermination()


if __name__ == "__main__":
    main()

