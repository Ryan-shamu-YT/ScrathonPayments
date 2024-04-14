from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='scrathon-payments',
    version='0.0.1',
    author='Ryan_shamu',
    author_email='Ryanshamu418@gmail.com',
    description='API Wrapper for ScrathonPayments',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Ryan-shamu-YT/ScrathonPayments',
    packages=find_packages(exclude=[]),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords=['scratch', 'api'],
    install_requires=[
        'requests'
    ],
    python_requires='>=3.6',
)
