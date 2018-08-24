import os
import socket
import time

import h5py


def filename_from_host_and_date():

	"""
	Returns a string assembled from the host name and current date.

	Returns
	-------
	out: str
		A string combining host name and date.

	"""

	# the name of the machine running the program (supposedly, using the socket module gives rise to portable code)
	hostname = socket.gethostname()

	# date and time
	date = time.strftime("%a_%Y-%m-%d_%H:%M:%S")

	return hostname + '_' + date + '_' + str(os.getpid())


def write_strings_list_into_hdf5(file, path_within_file, strings):
	"""
	Writes a list of strings into the given HDF5 file.

	Parameters
	----------
	file : h5py file object
		A reference to an open HDF5 file
	path_within_file : str
		A path within the HDF5 file
	strings : iterable
		An iterable containing the strings.

	"""

	dataset = file.create_dataset(path_within_file, shape=(len(strings),), dtype=h5py.special_dtype(vlen=str))

	for i, s in enumerate(strings):

		dataset[i] = s

