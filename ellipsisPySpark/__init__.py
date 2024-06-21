#python3 setup.py sdist bdist_wheel
#twine upload --repository pypi dist/*

__version__ = '0.0.0'

from ellipsisPySpark.parse import readVectorAsDataFrame
from ellipsisPySpark.parse import readRasterAsDataFrame
from ellipsisPySpark.parse import readRasterAsRasterFrame
