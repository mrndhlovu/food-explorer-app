import os
import tempfile

import sys
sys.path.append('../src')

import pytest
import sys


module_path = os.path.abspath(os.getcwd())    

if module_path not in sys.path:       

    sys.path.append(module_path)
    
