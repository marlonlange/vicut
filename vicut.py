import csv
from datetime import datetime
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def convertTimeToSeconds(t1, t2):
    timeStart = datetime.strptime(t1, '%X')
    timeEnd = datetime.strptime(t2, '%X')
    deltaStart = timeStart - datetime(1900, 1, 1)
    deltaEnd = timeEnd - timeStart
    return [deltaStart.total_seconds(), deltaStart.total_seconds() + deltaEnd.total_seconds()]


def extractClip(start, end, filename):
    ffmpeg_extract_subclip("test.flv", start, end,
                           targetname=f"{filename}.flv")


with open('timestamps.csv', 'r') as file:
    reader = csv.reader(file, skipinitialspace=True)
    for row in reader:
        filename = row[0]
        convertedTime = convertTimeToSeconds(row[1], row[2])
        extractClip(convertedTime[0], convertedTime[1], filename)
