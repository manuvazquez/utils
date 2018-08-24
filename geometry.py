import numpy as np


def rotate_signal(time, signal, degrees, origin='middle'):
	"""
	Rotates a signal a number of degrees.

	Parameters
	----------
	time : array_like
		The time stamps for the signal samples.
	signal : array_like
		The signal samples.
	degrees : float
		The number of degrees the signal will be rotated.
	origin : str or array_like
		The point used as center for the rotation.

	Returns
	-------
	out: ndarray
		A 2xN array with the (new) time in the first row, and the (new) signal samples in the second.

	"""

	# specifying `float` is necessary to avoid "object" arrays
	time = np.array(time, dtype=float)
	signal = np.array(signal, dtype=float)

	if origin == 'middle':

		# the mean value in both time and "signal" axes
		origin = np.array([time.min() + time.ptp()/2, signal.min() + signal.ptp()/2])

	else:

		# origin is turned into a numpy array
		origin = np.array(origin)

	# angle is converted to radians
	angle = np.deg2rad(degrees)

	rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])

	# first row contains the time coordinates, second row the signal
	points_matrix = np.vstack((time, signal))

	return rotation_matrix @ (points_matrix - origin[:, np.newaxis]) + origin[:, np.newaxis]
