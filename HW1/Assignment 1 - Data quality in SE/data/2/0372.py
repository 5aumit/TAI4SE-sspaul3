# -*- coding: utf-8 -*-
import sys
from os import listdir, makedirs, unlink
from os.path import isdir, join, isfile, exists
from shutil import copy
import random

def clearDirectory( path ):#将dataset里面的文件都删除
	for the_file in listdir(path):
	    file_path = join(path, the_file)
	    try:
	        if isfile(file_path):
	            unlink(file_path)
	    except Exception, e:
	        print e

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'argument list:', str(sys.argv)

if len(sys.argv) < 3:
	print 'Arguments is not enough! You need use the dataset and test category.'
	sys.exit();

datasetPath = sys.argv[1]
category = sys.argv[2]
if len(sys.argv) > 3:
	trainingNum = (int)(sys.argv[3])
else:
	trainingNum = 0

if len(sys.argv) > 4:
	testingNum = (int)(sys.argv[4])
else:
	testingNum = 0
print 'dataset is ', datasetPath, ' and category is ', category

categories = [f for f in listdir(datasetPath) if isdir(join(datasetPath, f))]
if category not in categories:
	print 'category is not in the dataset please check that' 
	sys.exit();

print 'start generating training and testing file...' 

categoryPath = datasetPath + '/' + category
categoryFiles = [f for f in listdir(categoryPath) if isfile(join(categoryPath,f))]
print category, 'contains ', len(categoryFiles) , 'file'
otherCategories = [x for x in categories if x != category]
otherCategoriesFiles = [y + '/' + x for y in otherCategories for x in listdir(datasetPath + '/' + y)]

defaultNum = (int)(len(categoryFiles))
if trainingNum <= 0:
	trainingNum = defaultNum
elif trainingNum > defaultNum:
	trainingNum = defaultNum
if testingNum <= 0:
	testingNum = min(defaultNum / 2, len(categoryFiles) - testingNum)
elif testingNum >  min(defaultNum / 2, len(categoryFiles) - testingNum):
	testingNum =  min(defaultNum / 2, len(categoryFiles) - testingNum)
print 'trainingNum is', trainingNum
print 'testingNum is', testingNum
rand_smpl = [ categoryFiles[i] for i in sorted(random.sample(xrange(len(categoryFiles)), trainingNum)) ]
test_files = [x for x in categoryFiles if x not in rand_smpl]

test_smpl = [test_files[i] for i in random.sample(xrange(len(test_files)), testingNum)]
trainingDir = 'dataset/training'
testingDir = 'dataset/testing'


if not exists(trainingDir):
    makedirs(trainingDir)
if not exists(testingDir):
    makedirs(testingDir)

clearDirectory(trainingDir)
clearDirectory(testingDir)



text_file = open("training.txt", "w")
trainingIndex = 1
for jpgfile in rand_smpl:
	filepath = categoryPath + '/' + jpgfile
	outputFilePath = 'image_' + str(trainingIndex) + '.jpg'
	text_file.write('dataset/training/' + outputFilePath + ' 1\n')
	copy(filepath, trainingDir + '/' + outputFilePath)
	trainingIndex += 1
training_smpl = [ otherCategoriesFiles[i] for i in random.sample(xrange(len(otherCategoriesFiles)), trainingNum)]
for jpgfile in training_smpl:
	filepath = datasetPath + '/' + jpgfile
	outputFilePath = 'image_' + str(trainingIndex) + '.jpg'
	text_file.write('dataset/training/' + outputFilePath + ' 0\n')
	copy(filepath, trainingDir + '/' + outputFilePath)
	trainingIndex += 1
text_file.close()

text_file = open("testing.txt", "w")
trainingIndex = 1
for jpgfile in test_smpl:
	filepath = categoryPath + '/' + jpgfile
	outputFilePath = 'image_' + str(trainingIndex) + '.jpg'
	text_file.write('dataset/testing/' + outputFilePath + ' 1\n')
	copy(filepath, testingDir + '/' + outputFilePath)
	trainingIndex += 1
testing_smpl = [ otherCategoriesFiles[i] for i in random.sample(xrange(len(otherCategoriesFiles)), testingNum)]
for jpgfile in testing_smpl:
	filepath = datasetPath + '/' + jpgfile
	outputFilePath = 'image_' + str(trainingIndex) + '.jpg'
	text_file.write('dataset/testing/' + outputFilePath +  ' 0\n')
	copy(filepath, testingDir + '/' + outputFilePath)
	trainingIndex += 1

text_file.close()
