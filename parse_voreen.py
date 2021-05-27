import argparse
import glob
import os
import fileinput
import time
import datetime
import pathlib
from shutil import copyfile
import shutil


parser = argparse.ArgumentParser(description='Control script for running coreen on a headless machine.')
parser.add_argument('-i','--input_image', help='Specify input file path of a NIFTI image.', required=True)
parser.add_argument('-o','--output_name', help='Specify output folder.', required=True)

# voreen settings
# --workdir /home/voreen-work/ --tempdir /home/voreen-temp/ --cachedir /home/voreen-cache/

parser.add_argument('-wd','--workdir', help='Specify the working directory.', required=True)
parser.add_argument('-td','--tempdir', help='Specify the temporary data directory.', required=True)
parser.add_argument('-cd','--cachedir', help='Specify the cache directory.', required=True)

# TO DO
# bulge size as cmd parameter

# read the arguments
args = vars(parser.parse_args())

input_image_path = args['input_image']
output_name = args['output_name']

volume_path = ''
edge_path = ''
node_path = ''
graph_path = ''

# create temp directory

temp_directory = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
pathlib.Path(temp_directory).mkdir(parents=True, exist_ok=True)

voreen_workspace = 'feature-vesselgraphextraction_customized_command_line.vws'
copyfile(voreen_workspace,os.path.join(temp_directory,voreen_workspace))

with fileinput.FileInput(os.path.join(temp_directory,voreen_workspace), inplace=True, backup='.bak') as file:
    for line in file:
        # replace volume path
        print(line.replace("/home/voreen_data/volume.nii", replacement_text), end='')
        # replace node path
        print(line.replace("/home/voreen_data/nodes.csv", replacement_text), end='')
        # replace edge path
        print(line.replace("/home/voreen_data/edges.csv", replacement_text), end='')
        # replace graph path
        print(line.replace("/home/voreen_data/graph.vvg.gz", replacement_text), end='')

        # set the bulge size

# extract graph

#os.system('sh run_voreen.sh')

'''
os.system('./home/voreen-build/bin/voreentool --workspace /home/voreen-build/bin/feature-vesselgraphextraction_customized_command_line.vws -platform minimal \
     --trigger-volumesaves --trigger-geometrysaves --workdir /home/voreen-work/ --tempdir /home/voreen-temp/ --cachedir /home/voreen-cache/ \
')
'''
# delete temp directory

shutil.rmtree(temp_directory)
