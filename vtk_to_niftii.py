import numpy as np
import argparse
import os
import vedo as vd
import shutil
from vedo import *
from skimage import io
import nibabel as nib

parser = argparse.ArgumentParser(description='convert vtk to 3D tif file.')
parser.add_argument('-i','--input_file', help='Name of the vtk file.', required=True)
parser.add_argument('-x','--x_bound', help='Specify lower bound x.',  default=500)
parser.add_argument('-y','--y_bound', help='Specify upper bound y.',  default=500)
parser.add_argument('-z','--z_bound', help='Specify lower bound y.',  default=500)

# read the arguments
args = vars(parser.parse_args())
input_path = args['input_file']
x= int(args['x_bound'])
y= int(args['y_bound'])
z=int(args['z_bound'])

# vedo read PolyDataFile
polydata = vd.load(input_path)
vol = vd.mesh2Volume(polydata)
#vol = vd.interpolateToVolume(mesh=polydata, kernel='shepard',radius=1,N=None, dims=[x,y,z])
vol = vol.crop(VOI=(0,x-1,0,y-1,0,z-1))

# strip the original file name and extension
output_name = os.path.splitext(input_path)[0]
vd.write(vol,output_name+'.tif')
input_file = output_name+'.tif'
data= io.imread(input_file)
clipped_img = nib.Nifti1Image(data.T,affine=np.eye(4))
clipped_img.header['pixdim'][1:4]=[1,1,1]
file_name = os.path.splitext(input_file)[0]+'.nii.gz'
nib.save(clipped_img, file_name)
