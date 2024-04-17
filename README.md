# MorQuest Code
## Morphodynamic Quick Assessment of Estuarine development under climate change

The MorQuest code predicts the reaction of estuaries from changes in sea level or sediment supply in a given period. The next Figure shows the relationship of the hydrodynamic elements that produce the change in the volume of sediments, of which the equilibrium state of some elements is described based on empirical equilibrium relationships.

![Estuaries](https://github.com/mreyesc22/MorQuestCode/assets/43484469/f1890802-57ee-44f9-b8be-59ba0fa1fd85)

The assumptions that the model develops are:
-	The model proposes a system defined by input parameters in equilibrium, which resolves that the amount of sediments input to the model is transported along the channel, the coast and outwards.
-	The model is applied to short tidal basins (1/20 of the tidal wavelength), implying that the water level gradients are negligible.
-	The model assumes that the systems’ reaction to SLR can be represented by a single adaptation time scale.

The code develops calculation based on: i) sediment transport, ii) hydrodynamic changes, iii) expansion of the intertidal area based on the sediment supplement of the river, iv) changes of the coastline under the variation of sea level, and v) time adaptation scale.

![MorQuest_Methology](https://github.com/mreyesc22/MorQuestCode/assets/43484469/706dc49b-a4cc-445e-a099-6ef70875ab8c)

### Project description

The Morquest code addresses the fundamental question:How can we globally assess the impact of climate change on estuarine morphodynamics at first order?

Therefore, the interest and development of the code were based on the following objectives:

- Utilizing satellite imagery as the primary data source.
- Developing a model capable of conducting simulations with limited data availability.
- Performing calibration of the developed model.
- Conducting long-term projections to provide valuable insights for sustainable coastal management.

## 1. Installation<a name="introduction"></a>

### 1.1 Create an environment with Anaconda

To run the toolbox you first need to install the required Python packages in an environment. To do this we will use **Anaconda**, which can be downloaded freely [here](https://www.anaconda.com/download/). 

Once you have it installed on your PC, open the Anaconda prompt (in Mac and Linux, open a terminal window) and use the `cd` command (change directory) to go the folder where you have downloaded this repository (e.g., `C:\Users\LENOVO\Desktop\morQuest`).

Create a new environment named `morQuest` with all the required packages by entering these commands in succession:

```
conda create -n morQuest
conda activate morQuest

conda install pandas
conda install numpy scipy
conda install -c conda-forge matplotlib notebook -y
conda install -c conda-forge geopandas -y
```
All the required packages have now been installed and are self-contained in an environment called `morQuest`. Always make sure that the environment is activated with:

```
conda activate morQuest
```

To confirm that you have successfully activated morQuest, your terminal command line prompt should now start with (`morQuest`).

:warning: **In case errors are raised** :warning:: clean things up with the following command (better to have the Anaconda Prompt open as administrator) before attempting to install `morQuest` again:
```
conda clean --all
```
## 2. Usage<a name="usage"></a>

An example of how to execute the software in a Jupyter Notebook is available in the repository (`example_jupyter.ipynb). To run it, activate your `morQuest` environment with `conda activate morQuest` (if it's not already active) and then type:
```
jupyter notebook
```

A web browser window will open. Point to the directory where you downloaded this repository and click on `morQuest_Simple.ipynb`. A Jupyter Notebook combines formatted text and code. To run the code, place your cursor inside one of the code sections and click on the `run cell` button (or press `Shift` + `Enter`) and progress forward.

![image](https://user-images.githubusercontent.com/7217258/165960239-e8870f7e-0dab-416e-bbdd-089b136b7d20.png)

The following sections show an example of how to run the full CoastSat workflow at Alsea bay (USA).

### 2.1 Retrieval of the satellite images<a name="retrieval"></a>
