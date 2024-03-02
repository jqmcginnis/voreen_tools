## Voreen 5.2 - Stable Version for Graph Generation

This repository contains the modified source code and stable release of Voreen 5.2 that can be used for vessel extraction. 
Adaptations have been made by Dominik Drees of Uni Müster, after email correspondance to Julian McGinnis (TUM).
Future Releases of Voreen will incorporate these source code changes as well.

This version contains bugfixes that mitigate scalability issues of the JSON Streaming Serializer of Voreen v5.2.0:

* voreen-src-unix-nightly.tar.gz contains the source code, which can be built using ccmake
* VoreenVE-nightly.tar.gz contains the Linux App Image

For installation instructions, please refer to the README.md in the binaries section.

#### The following workflow is recommended:

For testing Voreen on small-scale volumes (MB to GB range), you can use the provided workspace "vesselgraphextraction".
On large-scale volumes (GB to TB) data, it is recommended to use the vesselgraphextraction-customized workspace.
It does not visualize the graph and skips some steps of the original pipeline thus offering a more scalable solution.
If you have any questions (or in case it does not work), please post an issue on github.

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

### Graph Pruning

As mentioned in the paper by Drees et.al., the graphs are by utilizing a "scale invariant, dimensionless property", the bulge size parameter. It is defined as:

"Intuitively, the bulge size measures how far a bump, bulge or branch has to extend from a parent vessel in order to be considered a separate vessel. This size is expressed relative to the radius of its parent vessel and itself, making it scale-independent. More formally, the bulge size is an edge feature, that is computed during the feature extraction, and is only defined for bulging edges, i.e., edges that connecta leaf node (degree 1) and a branching point (degree > 2."

## Voreen Citation

If you use voreen, please cite:
```
@article{drees2021scalable,
  title={Scalable robust graph and feature extraction for arbitrary vessel networks in large volumetric datasets},
  author={Drees, Dominik and Scherzinger, Aaron and H{\"a}gerling, Ren{\'e} and Kiefer, Friedemann and Jiang, Xiaoyi},
  journal={BMC bioinformatics},
  volume={22},
  number={1},
  pages={1--28},
  year={2021},
  publisher={BioMed Central}
}
```
### Post-processing

For post-processing, as performed in our NeurIPS paper, please use the script provided in the post_processing section.

