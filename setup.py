from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='plane_detector',
      version='0.1',
      description='Plane Detector for remontnik.ru',
      url='http://github.com/xelnod/plane_detector/',
      author='Sergey Zenchenko',
      author_email='s.zench@yandex.ru',
      license='MIT',
      packages=['plane_detector'],
      install_requires=[
          'geopy', 'requests', 'pytest', 'tabulate'
      ],
      entry_points = {
          'console_scripts': ['plane-detector=plane_detector.command_line:main'],
      },
      zip_safe=False)
