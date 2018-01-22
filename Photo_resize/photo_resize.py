import subprocess
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
filelist = [f for f in os.listdir(os.path.join(current_dir, 'Source'))]
cp_path_output = os.path.join(current_dir, 'Result')
for file in filelist:
    cp_path_input = os.path.join(current_dir, 'Source', file)
    cp_path = 'cp' + ' ' + cp_path_input + ' ' + cp_path_output
    sips_file = 'sips --resampleWidth 200' + ' ' + os.path.join(current_dir, 'Result', file)
    subprocess.run(cp_path, shell=True)
    subprocess.run(sips_file, shell=True)