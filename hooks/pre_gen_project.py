import subprocess
import sys

PLATFORM = "mac"

if sys.platform.startswith('win32'):
    PLATFORM = "win"
elif sys.platform.startswith('linux'):
    PLATFORM = "lin"

# check if python 3.7 and above is installed
if not (sys.version_info.major == 3 and sys.version_info.minor >= 7):
    print("This script requires Python 3.5 or higher!")
    print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))
    sys.exit(1)


# check if virtualenv is installed
virtualenv = subprocess.run(["virtualenv", "--version"])
if virtualenv.returncode != 0:
    print("The project requires a working installation of virtualenv to work perfectly!")

    # no offician installation docs for virtualenv in windows
    if PLATFORM == "win":
        print("No official docs were found for virtualenv. You can proceed with system wide configurations which is undesirable.")
    else:
        print("Kindly install it from the official docs here: https://virtualenv.pypa.io/en/latest/installation.html")
    sys.exit(1)

# check if postgresql is installed
postgresql = subprocess.run(["psql", "--version"])
if postgresql.returncode != 0:
    print("The project requires a working installation of postgresql to work perfectly!")

    if PLATFORM == "mac":
        print("Follow this homebrew link to install postgresql: https://formulae.brew.sh/formula/postgresql#default")
    elif PLATFORM == "win":
        print("Install postgresql on windows via this link: https://www.postgresql.org/download/")
    else
        print("Follow this digital ocean guide to install postgresql: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04")

    sys.exit(1)
