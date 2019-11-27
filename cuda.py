import pynvml
import numpy as np


def less_busy_gpu() -> int:
	"""
	Returns the index of the "less busy" GPU.

	Returns
	-------
	out: int
		The index of the GPU.

	"""

	try:

		# the module must be initialized
		pynvml.nvmlInit()

	except pynvml.NVMLError_LibraryNotFound:

		raise Exception('No NVIDIA library found')

	n_gpus = pynvml.nvmlDeviceGetCount()

	# an array for storing the free memory in every GPU
	free_memory = [None] * n_gpus

	for i_gpu in range(n_gpus):

		# the free memory in this GPU in MBs
		free_memory[i_gpu] = pynvml.nvmlDeviceGetMemoryInfo(pynvml.nvmlDeviceGetHandleByIndex(i_gpu)).free / 1024**2

	# the module must be shut down
	pynvml.nvmlShutdown()

	return np.argmax(free_memory).item()