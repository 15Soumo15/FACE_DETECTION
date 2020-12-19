#!C:\Users\xyz\Desktop\READ\PROJECT\Python_Practice\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'face-recognize==0.2.0','console_scripts','face_recognize'
__requires__ = 'face-recognize==0.2.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('face-recognize==0.2.0', 'console_scripts', 'face_recognize')()
    )
