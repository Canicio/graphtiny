from setuptools import setup, find_packages


setup(name='Graphtiny',
      version='0.0.6',
      description='A Python library that lets you display graph in streaming, simply and easily. Especially suitable for scientific use. It Is an abstraction layer for the PyQtGraph library',
      author='Carlos Canicio',
      author_email='canicio@lcc.uma.es',
      url='https://github.com/canicio/graphtiny',
      download_url='https://github.com/canicio/graphtiny/archive/0.0.6.tar.gz',
      maintainer='Carlos Canicio',
      maintainer_email='canicio@lcc.uma.es',
      license='MIT (Massachusetts Institute of Technology)',
      packages=['graphtiny'],
      # packages=find_packages(),
      install_requires=[
          'PyQt5',
          'pyqtgraph',
      ],
      keywords=['graph', 'ui', 'chart', 'plot'],
      classifiers=[],
      )
