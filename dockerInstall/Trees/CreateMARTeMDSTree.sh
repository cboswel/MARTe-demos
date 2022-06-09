export marte_mds_path=$(pwd)
mdstcl < bareBones.txt | grep error
cp -r ../Tree /opt/MARTe2/Projects/MARTe2-utils/MARTe2-components/Source/Components/DataSources/MDSWriter/.
export mds_m2test_path=$PATH_TO_PROJECT_FOLDER/MARTe2-components/Source/Components/DataSources/MDSWriter/Tree/
