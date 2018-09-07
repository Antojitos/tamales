from setuptools import setup, find_packages


with open('README.rst') as file:
    long_description = file.read()


setup(
    name="tamales",
    version="0.1.1",
    author="Pablo SEMINARIO",
    author_email="pablo@seminar.io",
    description="The original pre-Hispanic URL shortener",
    long_description=long_description,
    license="GNU General Public License v3 (GPLv3)",
    url="http://t.antojitos.io/",
    download_url="https://github.com/Antojitos/tamales/archive/0.1.1.tar.gz",
    keywords=["tamales", "url", "shortener"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ],

    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'Flask==0.12.3',
        'python-baseconv==1.1.3',
        'redis==2.10.5'
    ],
)
