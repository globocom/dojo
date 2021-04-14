import sys
import shlex
import subprocess

# RUN in codecollab.io
if __name__ == '__main__':
    command = shlex.split('python3.8 dojo_test.py')
    subprocess.run(command, stdout=sys.stdout, stderr=sys.stderr)
