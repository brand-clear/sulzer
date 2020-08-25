

import os
from defaults import Path


class Extract:
	"""
	The Extract Class represents a collection of search methods designed to 
	return specific network storage locations for a given job number's data.

	"""
	_PROJECTS_FOLDER = Path.PROJECTS_FOLDER
	_AX_PICS = Path.AX_PICS
	_QC_MODELS = Path.QC_MODELS

	@staticmethod
	def valid_path(path):
		"""Verify the existence of a given path.

		Parameters
		----------
		path : str
			Absolute path to file or directory.

		Returns
		-------
		path : str
			Verified path to file or directory.
		
		Raises
		------
		DestinationError

		Examples
		--------
		>>> print Extract.valid_path('C:\\Users\\mcclbra')
		C:\\Users\\mcclbra

		>>> print Extract.valid_path(r'C:Users\\fakepath')
		Traceback (most recent call last):
			...
		DestinationError: 'C:Users\\fakepath' could not be found.

		"""
		if os.path.exists(path):
			return path
		raise DestinationError(path)

	@staticmethod
	def job_number(text):
		"""Find the first 6-digit sequence of numbers (job number) in a given 
		input.

		Parameters
		----------
		text : str
		
		Returns
		-------
		job_number : str
		
		Raises
		------
		JobNumberError

		Examples
		--------
		>>> Extract.job_number('123456-SHFT-MFG-00.pdf')
		'123456'

		>>> print Extract.job_number('12F3456-SHF-MFG-00.pdf')
		Traceback (most recent call last):
			...
		JobNumberError: No job number found in '12F3456-SHF-MFG-00.pdf'.

		"""
		for char in text:
			index = text.index(char)
			job_number = text[index:index+6]
			if len(job_number) == 6 and job_number.isdigit():
				return job_number
		raise JobNumberError(text)

	@classmethod
	def projects_folder_root(cls, job_number):
		"""Find the cls._PROJECTS_FOLDER subdirectory that contains a given job 
		number's folder.

		The subdirectory name will consist of two 6-digit integers separated by 
		a '-' and `job_number` will fall within the range specified by the name.

		Parameters
		----------
		job_number : str

		Returns
		-------
		str
			Absolute path to subdirectory.

		Raises
		------
		ProjectsFolderRootError

		Examples
		--------
		>>> print Extract.projects_folder_root('130550')
		L:\\Division2\\PROJECTS FOLDER\\130500-130999

		>>> Extract.projects_folder_root('999999')
		Traceback (most recent call last):
			...
		ProjectsFolderRootError: The PROJECTS FOLDER root for '999999' could not be found.

		"""
		for d in os.listdir(cls._PROJECTS_FOLDER):
			try:
				val1, val2 = d.split('-')
				if int(val1) <= int(job_number) <= int(val2):
					return os.path.join(cls._PROJECTS_FOLDER, d)
			except (IndexError, ValueError):
				pass
		raise ProjectsFolderRootError(job_number)

	@classmethod
	def projects_folder(cls, job_number):
		"""Find the cls._PROJECTS_FOLDER subdirectory that contains all data for 
		a given job number.

		Parameters
		----------
		job_number : str

		Returns
		-------
		str
			Absolute path to subdirectory.
		
		Raises
		------
		ProjectsFolderRootError
			Raised from Extract.projects_folder_root().
		DestinationError
			Raised from Extract.valid_path().

		Examples
		--------
		>>> print Extract.projects_folder('130550')
		L:\\Division2\\PROJECTS FOLDER\\130500-130999\\130550

		"""
		return cls.valid_path(os.path.join(cls.projects_folder_root(job_number), 
			job_number))

	@classmethod
	def qualified_part_folder(cls, job_number, dept='balance'):
		"""Find the cls._PROJECTS_FOLDER subdirectory that contains new part
		documentation for a given job number and department.

		Parameters
		----------
		job_number : str
		dept : {'balance', 'assembly'}, optional
			Department for which new part was qualified.

		Returns
		-------
		str
			Absolute path to subdirectory.

		Raises
		------
		ProjectsFolderRootError
			Raised from Extract.projects_folder_root().
		DestinationError
			Raised from Extract.valid_path().

		Examples
		--------
		>>> print Extract.qualified_part_folder('130550')
		L:\\Division2\\PROJECTS FOLDER\\130500-130999\\130550\\Balance\\NFT\\QC Reports

		>>> print Extract.qualified_part_folder('130550', 'assembly')
		L:\\Division2\\PROJECTS FOLDER\\130500-130999\\130550\\Assembly\\NFT\\QC Reports

		>>> print Extract.qualified_part_folder('130550', 'blading')
		L:\\Division2\\PROJECTS FOLDER\\130500-130999\\130550\\Blading\\QC Reports

		"""
		if dept == 'balance':
			return cls.balance_qc_folder(job_number)
		elif dept == 'assembly':
			return cls.assembly_qc_folder(job_number)
		elif dept == 'blading':
			return cls.blading_qc_folder(job_number)

	@classmethod
	def balance_qc_folder(cls, job_number):
		"""
		Parameters
		----------
		job_number : str

		Returns
		-------
		str
			Absolute path to directory containing new part documentation for
			balance department.
		
		Raises
		------
		ProjectsFolderRootError
			Raised from Extract.projects_folder_root().
		DestinationError
			Raised from Extract.valid_path().
		
		Notes
		-----
		Since this directory is not built into every PROJECTS FOLDER template, 
		it will be created as required.

		"""
		path = os.path.join(cls.projects_folder(job_number), 'Balance', 'NFT',
			'QC Reports')

		try:
			os.mkdir(path)
		except OSError:
			pass  # Path already exists
		finally:
			return path

	@classmethod
	def assembly_qc_folder(cls, job_number):
		"""
		Parameters
		----------
		job_number : str

		Returns
		-------
		str
			Absolute path to directory containing new part documentation for
			assembly department.

		Raises
		------
		ProjectsFolderRootError
			Raised from Extract.projects_folder_root().
		DestinationError
			Raised from Extract.valid_path().
		
		Notes
		-----
		Since this directory is not built into every PROJECTS FOLDER template, 
		it will be created as required.
		
		"""
		path = os.path.join(cls.projects_folder(job_number), 'Assembly', 'NFT',
			'QC Reports')

		try:
			os.mkdir(path)
		except OSError:
			pass  # Path already exists
		finally:
			return path

	@classmethod
	def blading_qc_folder(cls, job_number):
		"""
		Parameters
		----------
		job_number : str

		Returns
		-------
		str
			Absolute path to directory containing new part documentation for
			blading department.

		Raises
		------
		ProjectsFolderRootError
			Raised from Extract.projects_folder_root().
		DestinationError
			Raised from Extract.valid_path().
		
		Notes
		-----
		Since this directory is not built into every PROJECTS FOLDER template, 
		it will be created as required.
		
		"""
		path = os.path.join(cls.projects_folder(job_number), 'Blading', 
			'QC Reports')

		try:
			os.mkdir(path)
		except OSError:
			pass  # Path already exists
		finally:
			return path

	@classmethod
	def issued_prints_folder(cls, job_number):
		"""Find the cls._PROJECTS_FOLDER subdirectory that contains issued 
		print PDFs for a given job number.

		Parameters
		----------
		job_number : str

		Returns
		-------
		str
			Absolute path to subdirectory.

		Raises
		------
		ProjectsFolderRootError
			Raised from Extract.projects_folder_root().
		DestinationError
			Raised from Extract.valid_path().

		Examples
		--------
		>>> print Extract.issued_prints_folder('130550')
		L:\\Division2\\PROJECTS FOLDER\\130500-130999\\130550\\Drafting\\Issued Prints

		"""
		return cls.valid_path(os.path.join(cls.projects_folder(job_number), 
				'Drafting', 'Issued Prints'))

	@classmethod
	def issued_print_pdf(cls, pdf):
		"""Find the absolute path to a given pdf filename that exists in the
		cls._PROJECTS_FOLDER subdirectories.

		Parameters
		----------
		pdf : str

		Returns
		-------
		str
			Absolute path to `pdf`.

		Raises
		------
		JobNumberError
			Raised from Extract.job_number()
		ProjectsFolderRootError
			Raised from Extract.projects_folder_root().
		DestinationError
			Raised from Extract.valid_path().

		Examples
		--------
		>>> print Extract.issued_print_pdf('129705-STEM-MFG-00.pdf')
		L:\\Division2\\PROJECTS FOLDER\\129500-129999\\129705\\Drafting\\Issued Prints\\129705-STEM-MFG-00.pdf

		"""
		return cls.valid_path(os.path.join(cls.issued_prints_folder(
			cls.job_number(pdf)), pdf))

	@classmethod
	def pictures_folder_root(cls, job_number):
		"""Find the cls._AX_PICS subdirectory that contains a given job number's
		folder.

		Parameters
		----------
		job_number : str

		Returns
		-------
		str
			Absolute path to subdirectory.
		
		Raises
		------
		PicturesFolderRootError

		Examples
		--------
		>>> print Extract.pictures_folder_root('123123')
		T:\\pictures\\Axapta\\123000-199
		
		>>> Extract.pictures_folder_root('912362')
		Traceback (most recent call last):
			...
		PicturesFolderRootError: The pictures\Axapta root for '912362' could not be found.

		"""
		for f in os.listdir(cls._AX_PICS):
			try:
				val1, val2 = f.split('-')
				val2 = val1[:3] + val2
			except ValueError:
				# Too many values to unpack
				pass
			else:
				try:
					if int(val1) <= int(job_number) <= int(val2):
						return os.path.join(cls._AX_PICS, f)
				except ValueError:
					# Invalid literal for int() with base 10
					pass
		raise PicturesFolderRootError(job_number)

	@classmethod
	def pictures_folder(cls, job_number):
		"""Find the cls._AX_PICS subdirectory that contains pictures for a given
		job number.

		Parameters
		----------
		job_number : str

		Returns
		-------
		str
			Absolute path to subdirectory.

		Raises
		------
		PicturesFolderRootError
			Raised from Extract.pictures_folder_root()
		DestinationError
			Raised from Extract.valid_path()

		Examples
		--------
		>>> print Extract.pictures_folder('123123')
		T:\\pictures\\Axapta\\123000-199\\123123

		"""
		return cls.valid_path(os.path.join(cls.pictures_folder_root(job_number), 
			job_number))

	@classmethod
	def qc_model_stp(cls, stp):
		"""Get the absolute path to a given stp filename that is used for 
		quality control.

		Parameters
		----------
		stp : str

		Returns
		-------
		str
			Absolute path to `stp`.

		Raises
		------
		DestinationError
			Raised from Extract.valid_path().

		Examples
		--------
		>>> print Extract.qc_model_stp('129705-STEM-MFG-00.stp')
		Traceback (most recent call last):
			...
		DestinationError: 'Q:\\Quality Control\\quality_controller\\data\\cad models\\129705-STEM-MFG-00.stp' could not be found.

		"""
		return cls.valid_path(os.path.join(cls._QC_MODELS, stp))


class JobNumberError(Exception):
	"""
	Raised when a job number is not found in a given input.
	
	Parameters
	----------
	text : str
		The given input that does not contain a job number.

	"""
	def __init__(self, text):
		message = "No job number found in '%s'." % text
		super(JobNumberError, self).__init__(message)


class ProjectsFolderRootError(Exception):
	"""
	Raised when a PROJECTS FOLDER root is not found for a given job number.
	
	Parameters
	----------
	job_number : str

	"""
	def __init__(self, job_number):
		message = (
			"The PROJECTS FOLDER root for '%s' could not be found." 
			% job_number
		)
		super(ProjectsFolderRootError, self).__init__(message)


class PicturesFolderRootError(Exception):
	"""
	Raised when a pictures\Axapta root is not found for a given job number.
	
	Parameters
	----------
	job_number : str

	"""
	def __init__(self, job_number):
		message = (
			"The pictures\Axapta root for '%s' could not be found." 
			% job_number
		)
		super(PicturesFolderRootError, self).__init__(message)


class DestinationError(Exception):
	"""
	Raised when the destination of a file or directory can not be found.
	
	Parameters
	----------
	destination : str

	"""
	def __init__(self, destination):
		message = (
			"'%s' could not be found."
			% destination
		)
		super(DestinationError, self).__init__(message)


if __name__ == '__main__':
	# doctests will work only if ran on a computer that is connected to Sulzer
	# La Porte NFS.
	import doctest
	doctest.testmod(verbose=1)
