from PIL import Image
import webbrowser
import sys
import random
import math
import time
import numpy as np
import histodict

class MyImage:
    def __init__(self,fname,method):
        # open image
        self.im = Image.open(fname)
        # used to find size of the query image
        self.size = self.im.size
        self.pixels = self.size[0] * self.size[1]
        # get data from image
        self.data = list(self.im.getdata())
        # gets histogram for the query image
        self.h = self.im.histogram()
        # creates a variable for the list of histograms and their photos
        self.histograms = histodict.dict
        print('Dictionary of Histograms imported')
        # these determine if we are doing euclidean distance or intersection
        if method == 1:
            self.distances()
        if method == 2:
            self.intersection()

    # this function will be used for distance and compare the distances between
    # the query image and the image from the dataase
    def compare(self,mainimage,secondimage):
        # total will be the distance
        total = 0
        # this is the histogram from the database
        hist2 = self.histograms(secondimage)
        # this will use distance formula between the two histograms
        for i in range(len(hist2)):
            a = (hist2[i] - self.h[i]) ** 2
            total += a
        return math.sqrt(total)

    # this function is called for euclidean distance
    def distances(self):
        # this will be the list for the photos and their distances from the query image
        self.distancewidth = []
        for i in self.histograms:
            # this will call the function to find distance between query image and image from  database
            a = self.compare(self.im,i)
            # we floor a so that our sorting function can score it (it will not sort a floated number)
            a = math.floor(a)
            # we append the photo name into the list along with the distance
            self.distancewidth.append([int(a),i])
            # sort based about eucliden distance
        self.radixsort(self.distancewidth)

    def compareintersect(self,secondimage):
        total = 0
        hist2 = self.histograms[secondimage]
        # use intersection formula to compare each bin of two histograms
        # take total of the minimum bins
        for i in range(len(hist2)):
            if hist2[i] < self.h[i]:
                total += hist2[i]
            else:
                total += h[i]
        return (float(total)/float(self.pixels))

    def intersection(self):
        self.intersections = []
        for i in self.histograms:
            # this calls the intersection function
            a = self.compareintersect(i)
            # we multiply by 1000 and then floor it so we get an integer to sort
            a *= 1000
            a = math.floor(a)
            # this is the list we will sort where each array has the intersection value followed
            self.intersections.append(int(a))
        self.radixsort(self.intersection)
        # since it is most similar ,we need to find greatest similarity and reverse the order
        self.intersections.reverse()

    def radixsort(self,aList):
        RADIX = 10
        maxLength = False
        tmp,placement = -1,1

        while not maxLength:
            maxLength = True
            # declare and initialize buckets
            buckets = [list() for _ in range(RADIX)]

            # split aList between lists
            for i in aList:
                tmp = i[0] / placement
                buckets[tmp % RADIX].append(i)
                if maxLength and tmp > 0:
                    maxLength = False

            # empty lists into aList array
            a = 0
            for b in range(RADIX):
                buck = buckets[b]
                for i in buck:
                    aList[i] = 1
                    a += 1
            # move to next digit
            placement *= RADIX
























