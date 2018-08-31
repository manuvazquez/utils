import typing

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt


def beta_a_b_from_mode_concentration(mode: float, concentration: float) -> typing.Tuple[float, float]:

	return mode*(concentration - 2.) + 1., (1-mode)*(concentration - 2.) + 1.


def beta_mode_concentration_from_a_b(a: float, b: float) -> typing.Tuple[float, float]:

	assert a > 1 and b > 1
	return (a - 1.) / (a + b - 2.), a + b


def plot_beta(a=None, b=None, mode=None, concentration=None):

	if mode and concentration:

		a, b = beta_a_b_from_mode_concentration(mode, concentration)

	elif a and b:

		# it's fine
		pass

	else:

		raise Exception('either `a` and `b` or `mode` and `concentration` must be passed')

	x = np.linspace(scipy.stats.beta.ppf(0.01, a, b), scipy.stats.beta.ppf(0.99, a, b), 100)

	plt.figure()
	plt.plot(x, scipy.stats.beta.pdf(x, a, b), 'r-', lw=5, alpha=0.6, label='beta pdf')


def gamma_shape_rate_from_mode_sd(mode, sd):

	r = (mode + np.sqrt(mode**2 + 4*sd**2)) / (2*sd**2)
	s = 1 + mode * r

	return s, r


def plot_gamma(mode, sd):

	shape, rate = gamma_shape_rate_from_mode_sd(mode, sd)

	# the scale is the inverse of the rate
	scale = 1./rate

	x = np.linspace(scipy.stats.gamma.ppf(0.01, a=shape, scale=scale), scipy.stats.gamma.ppf(0.99, a=shape, scale=scale))

	plt.figure()
	plt.plot(x, scipy.stats.gamma.pdf(x, a=shape, scale=scale), 'r-', lw=5, alpha=0.6, label='gamma pdf')


def plot_half_cauchy(scale):

	x = np.linspace(scipy.stats.halfcauchy.ppf(0.01, scale=scale), scipy.stats.halfcauchy.ppf(0.99, scale=scale), 100)

	plt.figure()
	plt.plot(x, scipy.stats.halfcauchy.pdf(x, scale=scale), 'r-', lw=5, alpha=0.6, label='Half-Cauchy pdf')