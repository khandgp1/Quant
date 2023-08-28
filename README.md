# Icatt Desertification Index

### Steps
1. Install Docker
2. Copy and Execute Docker Command Below

## Get Started: Development
```
docker run <Additional Parameters> -v ~/Docker/index/:/home/icatt-desertification-index --name icatt_desertification_index_dev_container -p 8888:8888 -d -it docker-public-local.artifactory.jhuapl.edu/a4i/workspace/icatt_desertification_index_dev_image:latest
```
<details close>
<summary><strong>To mount BOX which is required for this project add the following parameter to command above</strong></summary>
<br>

Edit the path to BOX i.e. `source` as seen below

```
--mount type=bind,target="/home/data",source="PATH_TO_BOX/FEMA COVID-19 Support/TDWG/Data Management and Analytics Team/Deliverable/Desertification Index/Data"
```
</details>

<details close>
<summary><strong>Terminal into Docker Container using the UI or CLI Command</strong></summary>
<br>

```
docker exec -it icatt_desertification_index_dev_container bash
```
</details>

<details close>
<summary><strong>TLDR</strong></summary>
<br>

**For Parth**
```
docker run -v ~/Docker/index/:/home/icatt-desertification-index --name icatt_desertification_index_dev_container -p 8888:8888 -d -it --mount type=bind,target="/home/data",source="/Users/khandpv1/Library/CloudStorage/Box-Box/FEMA COVID-19 Support/TDWG/Data Management and Analytics Team/Deliverable/Desertification Index/Data" docker-public-local.artifactory.jhuapl.edu/a4i/workspace/icatt_desertification_index_dev_image:latest
```
</details>

<br>

<details close>
<summary><h2>Build Conda Package Delivery</h2></summary>

```
docker run -it --rm --name icatt_desertification_index_conda_build_container -v ~/Docker/index_delivery/:/home/index_delivery docker-public-local.artifactory.jhuapl.edu/a4i/workspace/icatt_desertification_index_conda_build_image:latest
```
```
cp -R /home/linux-64/ /home/index_delivery/
```
</details>

<details close>
<summary><h2>Test Conda Package Delivery</h2></summary>

```
docker run -it --rm --name icatt_desertification_index_test_conda_package -v ~/Docker/index_test_delivery/:/home docker-public-local.artifactory.jhuapl.edu/a4i/workspace/icatt_desertification_index_test_conda_package_image:latest
```
Copy the package into the container with the correct directory hie
- ~Docker/index_test_delivery/channel/linux-64/***.tar.bz2
```
conda activate my-conda-build-environment;
conda index channel/;
conda deactivate;
conda activate my-conda-test-environment;
conda install -y -c /home/channel/ jhuapl-desertification-index;
conda list;
```
</details>
