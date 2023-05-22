from typing import Set


SAMPLE_CMD = "> python [path/to/convert.py] [path/to/img_dir]"
PRE		= "[IMG CONVERTER] - "
CONV	= "[CONVERTING] - "
SET		= "[SETUP] - "
REP		= "[REPORT] - "
ERR		= "[ERROR] - "


def nice_quit():
	"""Shows a quit message to the console before exiting the program."""
	print(f"{PRE}quitting...")
	quit()
