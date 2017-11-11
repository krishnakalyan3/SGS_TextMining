#!/usr/bin/env/python3

import findspark
findspark.init()
import pyspark
from pyspark.sql import SQLContext, Row
from pyspark.ml.feature import CountVectorizer
from pyspark.mllib.clustering import LDA, LDAModel
from pyspark.mllib.linalg import Vector, Vectors
from collections import Counter


PATH = '/Users/krishnakalyan3/Educational/SGS_TextMining/data/sample/001'

sc = pyspark.SparkContext(appName="lda")
data_loc = sc.wholeTextFiles(PATH)
indiv_files = data_loc.map(lambda x: (x[0], x[1].split(' '))).flatMap(lambda x : (x[0], x[1]))

    #.flatMap(lambda x: x[1]).map(lambda x: (x, 1)).reduceByKey(lambda x,y:x+y)
#.flatMap(lambda x: (x[1], 1))
k = indiv_files.collect()
print(k)
