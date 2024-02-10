import setuptools

with open('README.md', 'r') as file:
	long_description = file.read()

setuptools.setup(
	name = 'preprocess_sagarlamani',
	version = '0.0.2',
	author = 'Sagar Lamani',
	author_email = 'sagarlamani23@gmail.com',
	description = 'This is a text preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Pyhton :: 3',
	'License :: OSI Approved :: MIT License',
	'Operating System :: OS Independent'],
	python_requires = '>=3.5'
	)