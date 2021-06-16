## Voreen 5.2 - Stable Version for Graph Generation

This repository contains the modified source code and stable release of Voreen 5.2 that can be used for vessel extraction. 
Adaptations have been made by Dominik Drees of Uni Müster, after email correspondance to Julian McGinnis (TUM).
Future Releases of Voreen will incorporate these source code changes as well.

This version contains bugfixes that mitigate scalability issues of the JSON Streaming Serializer of Vorren v5.2.0:

* voreen-src-unix-nightly.tar.gz contains the source code, which can be built using ccmake
* VoreenVE-nightly.tar.gz contains the Linux App Image

#### The following workflow is recommended:

For testing Voreen on small-scale volumes (MB to GB range), you can use the provided workspace "vesselgraphextraction".
On large-scale volumes (GB to TB) data, it is recommended to use my vesselgraphextraction-customized workspace.
It does not visualize the graph and skips some steps of the original pipeline thus offering a more scalable solution.
If you have any questions (or in case it does not work), write an email to julian.mcginnis@tum.de

#### Headless Version

feature-vesselgraphextraction_customized_command_line.vws can be used to run Voreen in headless mode.

#### Running voreen on a cluster

Use docker image or charliecloud image to run on lrz cloud!

E.g. ch-run  -b /lrz/sys/.:/lrz/sys/ -b /dss/dsshome1/lrz/sys/.:/dss/dsshome1/lrz/sys/ -b $SCRATCH/.:/scratch -w /dss/dsshome1/lxc06/ga82tus2/docker_directory/voreen_without_bindings/ sh /home/voreen-build/bin/run_voreen.sh --no-home

c.f. https://doku.lrz.de/display/PUBLIC/Charliecloud+at+LRZ


#### VTK based visualization of graphs

You can use voreen_graph_radius_to_vtk.py to generate a vtk_PolyDataFile file (e.g. open in Paraview)from the graph that displays vessels as tubes, incorporating the average vessel diameter as tube diameter. 

If you would rather display the tubular structures in ITK-Snap, you can convert the .vtk file using the vtk_to_nifti.py script.

