from setuptools import setup
import os
from pathlib import Path
import stat

def make_executable(script_path):
    """Make the script executable"""
    st = os.stat(script_path)
    os.chmod(script_path, st.st_mode | stat.S_IEXEC)

# Make all scripts in bin executable during setup
scripts_dir = Path(__file__).parent / 'bin'
for script in scripts_dir.glob('*'):
    if script.is_file():
        make_executable(script)

def read_requirements():
    with open('requirements.txt') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

def get_scripts():
    return [str(script) for script in scripts_dir.glob('*') if script.is_file()]

setup(
    name='mycli-tools',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='Collection of useful CLI tools',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/cli-tools',
    scripts=get_scripts(),
    install_requires=read_requirements(),
    python_requires='>=3.6',
)