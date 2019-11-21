from setuptools import setup
import subprocess
import os

package_version="0.0.1+TESTING"
with open("VERSION") as f:
    package_version=f.read().strip()

cwd = os.path.dirname(os.path.abspath(__file__))
try:
    sha = subprocess.check_output(['git','rev-parse','--short','HEAD'],cwd=cwd).decode('ascii').strip()
    package_version = package_version + "+" + sha
except Exception:
    pass

package_short_description="Sends a wake on lan signal to a computer and waits for it to come online"
package_long_description=package_short_description
with open('README.md') as f:
    package_long_description=f.read().strip()

setup(
    name="wakeandwait-redsoxfantom",
    version=package_version,
    description=package_short_description,
    url='https://github.com/redsoxfantom/wakeandwait',
    long_description=package_long_description,
    long_description_content_type='text/markdown',
    author="redsoxfantom",
    author_email="redsoxfantom@gmail.com",
    packages=["wakeandwait"],
    python_requires='>=3.7.3'
)