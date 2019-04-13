import os
import socket
import time
import pathlib
import typing

import h5py


def filename_from_host_and_date() -> str:

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


def write_strings_list_into_hdf5(file, path_within_file: str, strings: typing.List[str]) -> None:
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


def get_auxiliar_file(stem_name: str = '_tmp') -> pathlib.Path:
	"""
	Returns an non-existent path that can be used as auxiliar file.

	Parameters
	----------
	stem_name : str
		A tentative name for the auxiliar file

	Returns
	-------
	out: Pathlib.Path
		The path to the auxiliar file

	"""

	# given name is wrapped in a Pathlib object
	file = pathlib.Path(stem_name)

	# while the file exists...
	while file.exists():

		# ...a '_' is prepended to the name of the file
		file = file.with_name('_' + file.name)

	return file


def size_of_directory(directory: str, units='bytes') -> typing.Union[int, float]:
	"""
	Returns the size of directory. It ignores the size of directories.
	Credits: derived from https://stackoverflow.com/a/55659577/3967334

	Parameters
	----------
	directory : str
		Path to directory
	units: str
		One of `bytes` (default), `kilobytes`, `megabytes`, `gigabytes`

	Returns
	-------
	out: int
		Size

	"""

	# the exponent needed in the denominator when doing the conversion
	units_conversion_exponent = {'bytes': 0, 'kilobytes': 1, 'megabytes': 2, 'gigabytes': 3}

	size = sum(file.stat().st_size for file in pathlib.Path(directory).rglob('*'))

	return size/1024**units_conversion_exponent[units]