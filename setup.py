from setuptools import setup

setup(
    # Metadata
    name='django-signal-disabler',
    version='0.1.1',
    description='Allows to temporarily disable django signals',
    keywords=['django', 'django-signals'],

    # Origin
    url='https://github.com/RobertKolner/django-signal-disabler',
    author='Robert Kolner',
    author_email='robert.kolner@gmail.com',
    license='MIT',

    # Package data
    packages=['signal_disabler'],
    include_package_data=True,
    zip_safe=False,

    # Requirements
    install_requires=['django'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-django'],
)
