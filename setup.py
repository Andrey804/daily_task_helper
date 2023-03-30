from setuptools import setup

setup(name='daily_task_helper',
      version='0.0.1',
      description='Useful helper',
      url='',
      author='LokFaadDiiv',
      author_email='koto.amatsukami@ukr.net',
      license='MIT',
      packages=['clean_folder'],
      install_requires=['colorama'],
      python_requires=">=3.7",
      entry_points={'console_scripts': ['daily-task-helper = daily_task_helper.main:main']}
      )
