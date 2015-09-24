from setuptools import setup
try:
    import multiprocessing
except ImportError:
    pass

setup(
    name='httpie-ems-auth',
    description='EmsAuth plugin for HTTPie.',
    long_description=open('README.rst').read().strip(),
    version='0.1.1',
    author='Andras Barthazi',
    author_email='andras@barthazi.hu',
    license='MIT',
    url='https://github.com/emartech/httpie-ems-auth',
    download_url='https://github.com/emartech/httpie-ems-auth',
    py_modules=['httpie_ems_auth'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_ems_auth = httpie_ems_auth:EmsAuthPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0',
        'escherauth>=0.2.0,<0.3.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
