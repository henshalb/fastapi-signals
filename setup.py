from distutils.core import setup
setup(
    name='fastapi-signals',
    packages=['fastapi_signals'],
    version='0.0.1',
    license='MIT',
    description='Signalling for FastAPI.',
    author='Henshal B',
    author_email='henshalb@gmail.com',
    url='https://github.com/henshalb/fastapi-signals.git',
    download_url='https://github.com/henshalb/fastapi-signals/archive/refs/tags/0.0.1.tar.gz',
    keywords=['fastapi', 'signals', 'fastapi-signals', 'background task'],
    install_requires=[
        'starlette',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
