import distutils.core
import sys

import vogel

version = vogel.__version__

distutils.core.setup(
    name="vogel",
    version=version,
    packages = ["vogel", "vogel.tests"],
    author="Jacob Kristhammar",
    author_email="kristhammar@gmail.com",
    url="https://github.com/jacobk/vogel",
    download_url="https://github.com/jacobk/vogel/tarball/master",
    license="http://www.apache.org/licenses/LICENSE-2.0.txt",
    description="vogel is a minimal utility to extract Exif data from JPEG images",
)
