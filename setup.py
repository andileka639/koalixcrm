from setuptools import setup, find_packages

setup(name='koalixcrm',
      version='1.11',
      description='The funniest joke in the world',
      url='http://github.com/scaphilo/koalixcrm',
      author='Aaron Riedener',
      author_email='aaron.riedener@gmail.com',
      license='BSD',
      packages=find_packages(),
      install_requires=['Django>=1.11.3','django-filebrowser-no-grappelli>=3.7.1','lxml>=3.8.0','olefile>=0.44','Pillow>=4.2.1','pkg-resources>=0.0.0','psycopg2>=2.7.3', 'pytz>=2017.2'],
      zip_safe=False,
      classifiers=['Development Status :: 3 - Beta','Programming Language :: Python :: 3.4',],
      python_requires='~=3.5',
      include_package_data=True,
)
