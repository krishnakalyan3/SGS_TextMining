set.seed(123)
library(topicmodels)
library(dplyr)
library(readr)
library(caret)
library(dplyr)
library(doMC)
registerDoMC(4)

setwd('/Users/krishnakalyan3/Educational/SGS_TextMining/data')

data <- read.table('titles_and_types.csv', sep='\t',quote = "\"'", header = TRUE)
?read.table
?read_csv
glimpse(data)
