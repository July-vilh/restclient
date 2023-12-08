from distutils import setup
REQUIRES = [
    'request',
    'structlog',
    'curlify',
    'allure-pytest'
]

setup(
    name='restclient1',
    version='0.0.1',
    packages=['restclient1'],
    url='https://github.com/July-vilh/restclient.git',
    license='MIT',
    author='Yuliya Vilchynskaya',
    author_email='-',
    install_requires=REQUIRES,
    description='restclient with allure and logger'
)
