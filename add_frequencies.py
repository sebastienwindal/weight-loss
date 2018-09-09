#!/usr/bin/env python2

import sys
import os
import traceback
import csv

Verbose = False
ARGV0 = os.path.basename(sys.argv[0])

inputCSVFile = ''
resultsCSVFile = ''

def v(msg):
    """print message to stderr"""
    sys.stderr.write("%s\n" % msg)
    sys.stderr.flush()

def fatal(msg):
    """fatal (can't continue) situation error message"""
    v("== FATAL: %s" % msg)
    sys.exit(1)

def usage(msg):
    if msg:
        v(msg)
    v("Usage: %s file.csv resultfile.csv" % ARGV0)
    sys.exit(1)

def parse_args(args):

    global inputCSVFile, resultsCSVFile

    if len(args) <= 2:
        usage('')

    args.pop(0)

    # 1st arg is input file
    inputCSVFile = args.pop(0)
    # second is results file
    resultsCSVFile = args.pop(0)

def parse_inputCSVFile(inputCSVFile):

    keywordFrequencies = {}

    with open(inputCSVFile, 'rb') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvReader:
            if len(row) >= 3:
                # is this a comment?
                if row[0].strip().startswith("#"):
                    continue

                keywords = row[2].split()
                
                for keyword in keywords:
                    w = keyword.lower()

                    newFreq = 1.0
                    wordAndFreq = w.split(":")
                    if len(wordAndFreq) >= 2:
                        newFreq = float(wordAndFreq[1])
                        w = wordAndFreq[0]

                    value = 0.0
                    if w in keywordFrequencies.keys():
                        value = keywordFrequencies[w]

                    value += newFreq
                    
                    keywordFrequencies[w] = value

    return keywordFrequencies

def parse_resultsCSVFile(resultsCSVFile, keywordFrequencies):
    
    with open(resultsCSVFile, 'rb') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',', quotechar='|')

        rowsWithFrequencies = []

        for row in csvReader:
            if len(row) >= 4:
                # is this a comment?
                if row[0].strip().startswith("#"):
                    continue

                keyword = row[0].lower()
                frequency = 0.0
                if keyword in keywordFrequencies.keys():
                    frequency = keywordFrequencies[keyword]
                if frequency > 0:
                    row[3] = frequency

                rowsWithFrequencies.append(row)

        return rowsWithFrequencies

def save_resultsCSVFile(resultsCSVFile, rowsWithFrequencies):
    with open(resultsCSVFile, 'wb') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for row in rowsWithFrequencies:
            csvWriter.writerow(row)

def frequency(r):
    return r[3]

def summarize_frequencies(rowsWithFrequencies):
    s = "Added frequencies for " + str(len(rowsWithFrequencies)) + " keywords\n"
    s += "most frequent keywords:"
    sortedFreq = rowsWithFrequencies
    sortedFreq.pop(0)
    sortedFreq.sort(reverse=True, key=frequency)

    index = 0
    for row in sortedFreq:
        if index >= 5:
            break
        s += " " + row[0] + "(" + str(row[3]) + ")"
        index += 1

    return s

def main():
    try:
        parse_args(sys.argv)
        keywordFrequencies = parse_inputCSVFile(inputCSVFile)
        results = parse_resultsCSVFile(resultsCSVFile, keywordFrequencies)
        save_resultsCSVFile(resultsCSVFile, results)
        print(summarize_frequencies(results))


    except Exception as estr:
        # catch-all to cover all unhandled exceptions
        fatal("%s\n%s" % (estr, traceback.format_exc()))

    return 0

if __name__ == "__main__":
    sys.exit(main())