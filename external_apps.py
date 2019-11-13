import pathlib
import subprocess
import shutil
from typing import Union


def inkscape_svg_to_pdf(input_file: str, output_file: str) -> None:
	"""
	Converts a svg into a pdf using Inkscape.

	Parameters
	----------
	input_file: str
		The input file
	output_file: str
		The output file

	"""

	path_to_inkscape = shutil.which('inkscape')

	if not path_to_inkscape:

		raise Exception('Inkscape not found')

	subprocess.run(
		['inkscape', f'--file={input_file}', '--export-area-drawing', '--without-gui', f'--export-pdf={output_file}'])


def git_commit(path: Union[str, pathlib.Path], error_message: str = 'parent directory is not a repository') -> str:
	"""
	Finds the current commit of a git repository.

	Parameters
	----------
	path: str or pathlib
		The path to the git repository.
	error_message: str
		Message returned when the above directory is not a git repository.

	Returns
	-------
	out: str
		git commit

	"""

	path_to_git = shutil.which('git')

	if not path_to_git:

		return 'git no present'

	path = pathlib.Path(path)

	try:
		git_commit = subprocess.check_output([path_to_git, 'rev-parse', 'HEAD'], cwd=path, text=True, stderr=subprocess.STDOUT)
	except subprocess.CalledProcessError:
		git_commit = error_message
	else:
		git_commit = git_commit.rstrip()

	return git_commit