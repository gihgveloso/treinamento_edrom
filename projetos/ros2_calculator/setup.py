from setuptools import find_packages, setup

package_name = 'calculadora'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gihgveloso',
    maintainer_email='giovannavelosog@gmail.com',
    description='Python client server tutorial',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service_calculadora = calculadora.service_calculadora:main',
            'client_calculadora = calculadora.client_calculadora:main',
        ],
    },
)
