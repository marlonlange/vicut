# vicut

`vicut` is a little command line tool for cutting video files based on a list of timestamps.

## Installation

Download the latest and greatest release of [Python](https://www.python.org/) and add the binary in to your PATH.

Make sure you have a recent version of `moviepy` installed as well:

```bash
pip install moviepy
```

## Usage

Cut the given video based on a list of timestamps passed in via CSV file.

### Preparation

Given the following `timestamps.csv`:

```csv
yourFileName1, 00:00:00, 00:10:00
yourFileName2, 00:10:00, 00:15:00
yourFileName3, 00:15:00, 00:30:00
```

Move the video in the same directory as the `vicut.py` script and change the filename in line 15:

```python
ffmpeg_extract_subclip("test.flv", start, end,
                        targetname=f"{filename}.flv")
```

### Execution

Execute the script with the following command:

```bash
python vicut.py
```

Now the process starts generating new video files from the desired timestamps.

### Script output

The script will display the following output when a single process has completed successfully.

```bash
Moviepy - Running:
>>> "+ " ".join(cmd)
Moviepy - Command successful
```

## Todos

- Implement basic configuration to configure filenames or change directories
- Testing with different file types

## Contributing

Fixes and new features are welcome. For major changes, please talk to the current maintainer first to discuss what you would like to change.

## Contributors

Marlon Lange (marlonlange@live.de) - Creator

## License

MIT
