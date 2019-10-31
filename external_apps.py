import subprocess


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

	subprocess.run(
		['inkscape', f'--file={input_file}', '--export-area-drawing', '--without-gui', f'--export-pdf={output_file}'])
