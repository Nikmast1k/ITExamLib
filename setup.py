from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='ITExam',
    version='0.1',
    author='Nikmast1k',
    author_email='nikmast45@yandex.ru',
    description='Unified State Exam on IT',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='your_url',
    packages=find_packages(),
    install_requires=['requests>=2.25.1'],
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='IT EXAM',
    project_urls={
        'GitHub': 'https://github.com/Nikmast1k'
    },
    python_requires='>=3.10'
)
