from pyspark.sql import SparkSession

from delta import configure_spark_with_delta_pip


def get_spark(name="MyApp"):
    builder = SparkSession.builder.appName(name) \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

    return configure_spark_with_delta_pip(builder).getOrCreate()