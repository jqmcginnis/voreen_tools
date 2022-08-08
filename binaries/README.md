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
