#!/bin/bash
for i in $(seq 1 136)
do
    echo "$i"
    mkdir /home/juli/tum/git_repositories/voreen/3D_vessel_data/seg/"${i}"_b_3_0
    python3 parse_voreen.py --input_image /home/juli/tum/git_repositories/voreen/3D_vessel_data/seg/"${i}".nii --voreen_tool_path voreen-src-unix-nightly/bin/ --workspace_file feature-vesselgraphextraction_customized_command_line.vws --workdir /home/juli/tum/git_repositories/voreen/voreen_work/ --tempdir /home/juli/tum/git_repositories/voreen/voreen_temp/ --cachedir /home/juli/tum/git_repositories/voreen/voreen_cache/ --bulge_size 3.0
    cp /home/juli/tum/git_repositories/voreen/3D_vessel_data/seg/"${i}"_b_3_0_edges.csv /home/juli/tum/git_repositories/voreen/3D_vessel_data/seg/"${i}"_b_3_0/"${i}"_b_3_0_edges.csv 
    cp /home/juli/tum/git_repositories/voreen/3D_vessel_data/seg/"${i}"_b_3_0_nodes.csv /home/juli/tum/git_repositories/voreen/3D_vessel_data/seg/"${i}"_b_3_0/"${i}"_b_3_0_nodes.csv 
done