from distutils.core import setup
setup(
  name = 'globals',
  packages = ['globals'],
  version = '0.0.1',
  license='MIT',
  description = 'import package handler',
  author = 'Samuel Jansen',
  author_email = 'samuel.jansenn@gmail.com',
  url = 'https://github.com/SamuelJansen/globals',
  download_url = 'https://github.com/SamuelJansen/globals/archive/v0.1.1.tar.gz',
  keywords = ['global', 'python global package', 'python package manager'],
  install_requires=[
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8'
  ]
)