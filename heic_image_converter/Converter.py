from heic_image_converter.globals import *


import os
from PIL import Image
import pillow_heif



class Converter(object):
	"""
	Given a set of command line arguments, converts `.heic` files to
	- the desired format
	- a given location
	"""
	dir_src = ""
	# {"flag": [Enabled, optional_argument]}
	flags = {
		"--to": [False, ""],
		"--dest": [False, ""],
		"-del": [False]
	}
	flag_to_supported = ["png"]		# ["png", "jpg"]	# no solution for .jpg yet :\

	image_from_ext = ".heic"

	complete_conversions = []
	incomplete_conversions = []


	def __init__(self, cmd_args):
		"""
		Reads in cmd_args to determine flag settings and directory existences.
		"""
		def try_get_flag_arg(flag_args, j):
			try:
				# potential IndexOutOfBoundsException
				flag_value = flag_args[j+1]

				# can't set flag with flag
				if flag_value.startswith("-") or flag_value.startswith("--"):
					raise Exception
				
				return flag_value
			except Exception:
				print(f"{PRE}{SET}no argument provided for the flag: '{flag}'.")
				nice_quit()

		
		# go through args and set class fields
		if len(cmd_args) == 0:
			print(f"{PRE}{SET}must provide image source directory.")
			nice_quit()
		
		# check src dir
		#dir_src_try = cmd_args[0].strip()
		dir_src_try = cmd_args
		if os.path.isdir(dir_src_try):
			print(f"{PRE}{SET}source directory found: '{dir_src_try}'")
			self.dir_src = dir_src_try
		else:
			print(f"{PRE}{SET}there was an issue finding the image source directory: '{dir_src_try}'")
			nice_quit()
			
		
		# set flags
		flags_try = cmd_args[1:]
		for i in range(len(flags_try)):
			flag = flags_try[i]
			if flag in self.flags.keys():
				# FLAGS WITHOUT ARGUMENTS
				if len(self.flags[flag]) == 1:
					self.flags[flag][0] = True
					print(f"{PRE}{SET}'{flag}' flag set.")
				
				# FLAGS WITH ARGUMENTS
				else:
					flag_value = try_get_flag_arg(flags_try, i)

					if flag == "--dest":
						if not os.path.isdir(flag_value):
							print(f"{PRE}{SET}did not find the '--dest' directory: '{flag_value}'")
							try:
								print(f"{PRE}{SET}creating it...")
								os.makedirs(flag_value)
							except Exception as e:
								print(e)
								print(f"{PRE}{SET}there was an issue creating the '--dest' directory.")
								nice_quit()
						else:
							print(f"{PRE}{SET}'--dest' directory found.")
					
					elif flag == "--to":
						if flag_value not in self.flag_to_supported:
							print(f"{PRE}{SET}unsupported '--to' filetype: '{flag_value}'")
							nice_quit()
												
					# FLAG SET
					self.flags[flag][0] = True
					self.flags[flag][1] = flag_value
					print(f"{PRE}{SET}'{flag}' flag set with '{flag_value}'.")
		

	def convert_files(self, image_to_ext=".png"):
		"""
		Iterates through all `.heic` files in the source image directory, converting them according to set flags...
		"""
		dir_bytes = os.fsencode(self.dir_src)
		for i, file_bytes in enumerate(os.listdir(dir_bytes)):
			n = i+1
			# obtain strings for path and filename
			filename = os.fsdecode(file_bytes)
			filepath = os.path.join(self.dir_src, filename)
			
			# IMPLEMENT FLAGS
			# set new_filepath
			save_dir = self.dir_src
			if self.flags["--dest"][0]:
				save_dir = self.flags["--dest"][1]
			# save format
			if self.flags["--to"][0]:
				image_to_ext = "." + self.flags["--to"][1]
			new_filename = filename.split(".")[0] + image_to_ext
			new_filepath = os.path.join(save_dir, new_filename)
			
			# if file already exists in destination filetype, skip
			if os.path.isfile(new_filepath):
				print(f"{PRE}{CONV}[{n}] - skipping - file already exists: '{new_filename}'")
				self.complete_conversions.append(filepath)
				continue

			# file is desired source format, like '.heic', convert to desired format
			if filename.lower().endswith(self.image_from_ext):
				try:
					print(f"{PRE}{CONV}[{n}] - source: '{filename}'")

					# convert file and save
					heif_file = pillow_heif.read_heif(filepath)
					image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw")
					saveAs = image_to_ext.split(".")[1]  # get format like '.png' -> 'png'
					image.save(new_filepath, format(saveAs.lower()))
					
					# success
					print(f"{PRE}{CONV}[{n}] - new image: '{new_filename}'")
					self.complete_conversions.append(new_filepath)

					# if success, and -del flag, remove original
					if self.flags["-del"][0]:
						print(f"{PRE}{CONV}[{n}] - '-del' flag has been set. removing '{filename}'...")
						os.remove(filepath)
				
				# there was an issue converting this file, note and continue
				except Exception as e:
					print(f"{PRE}{CONV}[{n}] - error converting: '{filename}'")
					print(e)
					self.incomplete_conversions.append(filepath)
		
		# show final successes
		lc = len(self.complete_conversions)
		li = len(self.incomplete_conversions)
		print(f"{PRE}{REP}image source directory: '{self.dir_src}'")
		print(f"{PRE}{REP}image save destination: '{save_dir}'")
		print(f"{PRE}{REP}converted {lc}/{(lc + li)} files.")
