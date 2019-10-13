from setuptools import setup
import versioneer

requirements = [
    'scikit-learn',
    'joblib',
    'fsspec',
    'intake >=0.2'
]

setup(
    name='intake-sklearn',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Driver for Scikit-Learn model pickle files",
    license='BSD 3-clause',
    author="Albert DeFusco",
    author_email='albert.defusco@me.com',
    url='https://github.com/albertdefusco/intake_sklearn',
    packages=['intake_sklearn'],
    entry_points={
        'intake.drivers': ['sklearn = intake_sklearn.source:SklearnModelSource']
    },
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
