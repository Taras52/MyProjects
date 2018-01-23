import subprocess
import os


def image_resize(source):
    filelist = [f for f in os.listdir(source)]
    cp_path_output = os.path.join(current_dir, 'Result')
    try:
        os.makedirs(cp_path_output)
    except FileExistsError:
        pass
    for file in filelist:
        cp_path_input = os.path.join(current_dir, 'Source', file)
        cp_path = 'cp' + ' ' + cp_path_input + ' ' + cp_path_output
        sips_file = 'sips --resampleWidth 200' + ' ' + os.path.join(current_dir, 'Result', file)
        subprocess.run(cp_path, shell=True)
        subprocess.run(sips_file, shell=True)


current_dir = os.path.dirname(os.path.abspath(__file__))
source_path = os.path.join(current_dir, 'Source')
image_resize(source_path)






