import csv
import os
from datetime import datetime
from time import sleep
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from gooey import Gooey, GooeyParser


def convertTimeToSeconds(t1, t2):
    timeStart = datetime.strptime(t1, '%X')
    timeEnd = datetime.strptime(t2, '%X')
    deltaStart = timeStart - datetime(1900, 1, 1)
    deltaEnd = timeEnd - timeStart
    return [deltaStart.total_seconds(), deltaStart.total_seconds() + deltaEnd.total_seconds()]


def extractClip(start, end, filename):
    ffmpeg_extract_subclip("test.flv", start, end,
                           targetname=f"{filename}.flv")


@Gooey(required_cols=1)
def main():
    parser = GooeyParser(
        description="Tool for cutting or downloading video files based on CSV")
    parser.add_argument(
        "Output Directory", help="The output destination for the video files", widget="DirChooser")
    parser.add_argument(
        "CSV File", help="Name of the file containing timestamps or stream urls", widget="FileChooser")
    parser.add_argument(
        "Action", help="The action to perform", choices=['Cut', 'Download'])
    parser.add_argument(
        '-Settings',
        action='store_true',
        help='Save these settings for next usage')
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()


# with open('download.csv', 'r') as file:
#     reader = csv.reader(file, skipinitialspace=True)
#     for row in reader:
#         filename = row[0]
#         url = row[1]
#         command = f"ffmpeg -i \"{url}\" -c copy -bsf:a aac_adtstoasc \"{filename}.mp4\""
#         os.system(command)
#         sleep(10)

# with open('timestamps.csv', 'r') as file:
#     reader = csv.reader(file, skipinitialspace=True)
#     for row in reader:
#         filename = row[0]
#         convertedTime = convertTimeToSeconds(row[1], row[2])
#         extractClip(convertedTime[0], convertedTime[1], filename)
