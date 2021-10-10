#this file paste sabe.py into python lib folder
from shutil import copyfile
import os
import sys
lib_path = os.path.dirname(sys.executable) + "\\lib"
os.system(f"copy sabe.py {lib_path + 'sabe.py'}")
