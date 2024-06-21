from pyspark.sql import SparkSession
from ellipsisPySpark import readVectorAsDataFrame
from ellipsisPySpark import readRasterAsDataFrame
from ellipsisPySpark import readRasterAsRasterFrame
from pyrasterframes.utils import create_rf_spark_session


pathId = '632aeb3f-ca77-4bdd-a8cd-5f733dbd87ee'
timestampId = 'da3bb83d-8cc0-45e4-a96d-e6db0f83616b'
token = 'epat_MY2lyE9txCGaWHxUt1CXkLnMUoAWpgkepma3XqzlranvhcpY8CaByBAaBpOybKOK'

sparkSession = SparkSession.builder.appName('tutorial').getOrCreate()

sparkRasterSession = create_rf_spark_session()



spark_df = readVectorAsDataFrame(sparkSession= sparkSession, pathId=pathId, timestampId=timestampId, token=token)


pathId = 'd951d941-3340-4a81-a7a3-f87e3651f83c'
timestampId = 'c6d976d8-7fc3-4ff4-80d9-734928701e24'
token = 'epat_Fr2QlosaiN0M0tGEWhlRlPhLnmOP5xP0OuPq1ca6kzgtRF6D3l4Bd94lOSu7RcQ8'

spark_df = readRasterAsDataFrame(sparkSession= sparkSession, pathId=pathId, timestampId=timestampId, token=token)

spark_df.head(400)


pathId = 'd951d941-3340-4a81-a7a3-f87e3651f83c'
timestampId = 'c6d976d8-7fc3-4ff4-80d9-734928701e24'
token = 'epat_Fr2QlosaiN0M0tGEWhlRlPhLnmOP5xP0OuPq1ca6kzgtRF6D3l4Bd94lOSu7RcQ8'

spark_raster_df = readRasterAsRasterFrame(sparkSession= sparkRasterSession, pathId=pathId, timestampId=timestampId, token=token)


