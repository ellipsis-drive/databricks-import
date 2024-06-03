This package is meant to help you run models on Ellipsis Drive content. It should be used in combination with the ellipsis package.


### Synopsis
A package to parse Ellipsis Drive layers as pySpark DataFrames.

### Install
```python
pip install ellipsisPySpark
```

### Example
```python
from pyspark.sql import SparkSession
from ellipsisPySpark import readVector
from ellipsisPySpark import readRaster

sparkSession = SparkSession.builder.appName('tutorial').getOrCreate()

#pathId, timestampId and token as can be obtained via the Ellipsis Drive interface via 'integrate'
pathId = '632aeb3f-ca77-4bdd-a8cd-5f733dbd87ee'
timestampId = 'da3bb83d-8cc0-45e4-a96d-e6db0f83616b'
token = 'epat_3TdJ2ZnmkC3wFfyiJWg6Mb9VqCE829eRPufY4CsVWaZXwKtwP5smEPGieSWrJOqJ'

#read the vector layer as a spark dataframe
spark_df = readVector(sparkSession= sparkSession, pathId=pathId, timestampId=timestampId, token=token)

#pathId, timestampId and token as can be obtained via the Ellipsis Drive interface via 'integrate'
pathId = 'd951d941-3340-4a81-a7a3-f87e3651f83c'
timestampId = 'c6d976d8-7fc3-4ff4-80d9-734928701e24'
token = 'epat_hT0EL2RIKd0ZCOjT9EaTrSHtDALwQEgHYfPcDGTSCZwU00V6UhWiqsui2KJnHqLx'

#read the raster layer as a spark dataframe
spark_df = readRaster(sparkSession= sparkSession, pathId=pathId, timestampId=timestampId, token=token)


```


### Functions

#### readVector

```python
readVector(sparkSession, pathId, timestampId, token=None)
```

This function parses an Ellipsis Drive vector layer as a pySpark DataFrame

| Name        | Description |
| ----------- | -----------|
| sparkSession        | A session as created using pySpark. |
| pathId        | The id of the vector layer to load as a pySpark dataframe |
| timestampId        | The id of the timestamp to load as a pySpark dataframe |
| token        | A token to authenticate (optional)|


#### readRaster

```python
readRaster(sparkSession, pathId, timestampId, token= None, extent = None)
```

This function parses an Ellipsis Drive vector layer as a pySpark DataFrame

| Name         | Description                                               |
|--------------|-----------------------------------------------------------|
| sparkSession | A session as created using pySpark.                       |
| pathId       | The id of the raster layer to load as a pySpark dataframe |
| timestampId  | The id of the timestamp to load as a pySpark dataframe    |
| token        | A token to authenticate (optional)                        |
| extent       | The extent to restrict to in WGS84 (optional)             |


