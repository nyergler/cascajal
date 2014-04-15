from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1'

install_requires = [
]


setup(name='cascajal',
      version=version,
      description="PDF generation for Hieroglyph presentations.",
      long_description=README + '\n\n' + NEWS,
      classifiers=[
        'License :: OSI Approved :: BSD License',
        'Topic :: Documentation',
        'Topic :: Text Processing',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
      ],
      keywords='PDF presentation text-processing',
      author='Nathan R. Yergler',
      author_email='nathan@yergler.net',
      url='https://github.com/nyergler/cascajal',
      license='BSD',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      package_data={
          'cascajal': [
              'data/*',
          ],
      },
      zip_safe=True,
      install_requires=install_requires,
      entry_points={
          'console_scripts': [
              'cascajal=cascajal.cli:main',
          ],
      },
      test_suite='cascajal.tests',
)
