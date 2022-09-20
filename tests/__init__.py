import os, sys
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.abspath(os.path.join(current_dir, "../src"))
sys.path.append(source_dir)

import test_csv, test_data, test_num, test_sym

print(source_dir)