from setuptools import setup

setup(
    name='youtube-launcher',
    version='0.1',
    py_modules=['youtube_launcher'],
    entry_points={
        'console_scripts': ['youtube-launcher = youtube_launcher:main']
    },
)
