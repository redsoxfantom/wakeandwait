from setuptools import setup

package_version="0.0.1-TESTING"
with open("VERSION") as f:
    package_version=f.read()

package_short_description="Sends a wake on lan signal to a computer and waits for it to come online"
package_long_description=package_short_description
with open('README') as f:
    package_long_description=f.read()

setup(
    name="wakeandwait",
    version=package_version,
    description=package_short_description,
    long_description=package_long_description,
    author="redsoxfantom",
    author_email="redsoxfantom@gmail.com",
    packages=["wakeandwait"]
)