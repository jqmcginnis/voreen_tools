## Voreen 5.2 - Stable Version for Graph Generation

This repository contains the modified source code and stable release of Voreen 5.2 that can be used for vessel extraction. 
Adaptations have been made by Dominik Drees of Uni Müster, after email correspondance to Julian McGinnis (TUM).
Future Releases of Voreen will incorporate these source code changes as well.

This version contains bugfixes that mitigate scalability issues of the JSON Streaming Serializer of Vorren v5.2.0:

* voreen-src-unix-nightly.tar.gz contains the source code, which can be built using ccmake
* VoreenVE-nightly.tar.gz contains the Linux App Image

#### Building Voreen for your platform

For build instructions for Linux/MacOS/Windows please refer to:

https://www.uni-muenster.de/Voreen/documentation/build_instructions.html

#### Install dependecies

<sub> 
sudo apt install g++ git cmake libboost-all-dev libglew-dev qt5-default libqt5svg5-dev  libdevil-dev ffmpeg libswscale-dev libavcodec-dev libavformat-dev
</sub> 

#### Voreen Build Configuration

For utilizing voreentool (the command line version) and the vesselgraphextraction features make sure to enable the following settings in the cmake file:

<sub>
VRN_MODULE_BASE                  ON     <br />                                      
VRN_MODULE_BIGDATAIMAGEPROCESS   ON     <br />                                      
VRN_MODULE_CONNEXE               ON     <br />                                      
VRN_MODULE_DEPRECATED            OFF    <br />                                      
VRN_MODULE_DEVIL                 ON     <br />                                      
VRN_MODULE_ENSEMBLEANALYSIS      ON     <br />                                      
VRN_MODULE_EXPERIMENTAL          OFF    <br />                                      
VRN_MODULE_FFMPEG                OFF    <br />                                  
VRN_MODULE_FLOWANALYSIS          ON     <br />                                      
VRN_MODULE_GDCM                  OFF    <br />                                      
VRN_MODULE_HDF5                  ON     <br />                                      
VRN_MODULE_ITK                   OFF    <br />                                      
VRN_MODULE_ITK_GENERATED         OFF    <br />                                      
VRN_MODULE_OPENCL                OFF    <br />                                      
VRN_MODULE_OPENMP                OFF    <br />                                      
VRN_MODULE_PLOTTING              ON     <br />                                      
VRN_MODULE_POI                   OFF    <br />                                      
VRN_MODULE_PVM                   ON     <br />                                      
VRN_MODULE_PYTHON                ON     <br />                                      
VRN_MODULE_RANDOMWALKER          ON     <br />                                      
VRN_MODULE_SAMPLE                OFF    <br />                                      
VRN_MODULE_SEGY                  ON     <br />                                      
VRN_MODULE_STAGING               ON     <br />                                      
VRN_MODULE_STEREOSCOPY           ON     <br />                                      
VRN_MODULE_SURFACE               ON     <br />  
VRN_MODULE_TIFF                  OFF    <br />                                      
VRN_MODULE_ULTRAMICROSCOPYDEPL   OFF    <br />                                      
VRN_MODULE_VESSELNETWORKANALYS   ON     <br />                                      
VRN_MODULE_VOLUMELABELING        OFF    <br />                                      
VRN_MODULE_VTK                   ON     <br />                                    
VRN_MODULE_ZIP                   ON     <br />                                      
VRN_NON_INTERACTIVE              OFF    <br />                                      
VRN_OPENGL_COMPATIBILITY_PROFI   OFF    <br />                                      
VRN_PRECOMPILED_HEADER           OFF    <br />                                      
VRN_USE_GENERIC_FILE_WATCHER     OFF    <br />                                    
VRN_USE_HDF5_VERSION             1.10   <br />                                      
VRN_USE_SSE41                    ON     <br />                                      
VRN_VESSELNETWORKANALYSIS_BUIL   OFF    <br />
</sub>

#### To enable command line tool generation set:

<sub> VRN_BUILD_VOREENTOOL             ON      </sub> <br />      
 
#### To enable gui tool generation set: <br />

<sub> VRN_BUILD_VOREENVE               ON   </sub> <br />

#### Building VTK (prerequisite)

You will need to build VTK for this: <br />

https://vtk.org/download/ <br />

Build it following the hints here:

<sub>
mkdir VTK-build <br />
cd VTK-build <br />
ccmake /path/to/VTK <br />
make -j $NUMBER_OF_PROCESSES . <br />
</sub>

#### The following workflow is recommended:

For testing Voreen on small-scale volumes (MB to GB range), you can use the provided workspace "vesselgraphextraction".
On large-scale volumes (GB to TB) data, it is recommended to use my vesselgraphextraction-customized workspace.
It does not visualize the graph and skips some steps of the original pipeline thus offering a more scalable solution.
If you have any questions (or in case it does not work), write an email to julian.mcginnis@tum.de

To switch between Application Mode / Network Mode use short keys F4/F5 or the modes provided in the toolbar.

#### Headless Version

feature-vesselgraphextraction_customized_command_line.vws can be used to run Voreen in headless mode. You can also specify your own workspace in Voreen in the so-called network mode.

#### Running voreen on a cluster

Use docker image or charliecloud image to run on lrz cloud!

E.g. ch-run  -b /lrz/sys/.:/lrz/sys/ -b /dss/dsshome1/lrz/sys/.:/dss/dsshome1/lrz/sys/ -b $SCRATCH/.:/scratch -w /dss/dsshome1/lxc06/ga82tus2/docker_directory/voreen_without_bindings/ sh /home/voreen-build/bin/run_voreen.sh --no-home

c.f. https://doku.lrz.de/display/PUBLIC/Charliecloud+at+LRZ


#### VTK based visualization of graphs

You can use voreen_graph_radius_to_vtk.py to generate a vtk_PolyDataFile file (e.g. open in Paraview)from the graph that displays vessels as tubes, incorporating the average vessel diameter as tube diameter. 

If you would rather display the tubular structures in ITK-Snap, you can convert the .vtk file using the vtk_to_nifti.py script.

