# MorQuest Code
## Morphodynamic Quick Assessment of Estuarine development under climate change

The MorQuest code predicts the reaction of estuaries from changes in sea level or sediment supply in a given period. The next Figure shows the relationship of the hydrodynamic elements that produce the change in the volume of sediments, of which the equilibrium state of some elements is described based on empirical equilibrium relationships.

![Estuaries](https://github.com/mreyesc22/MorQuestCode/assets/43484469/f1890802-57ee-44f9-b8be-59ba0fa1fd85)

The assumptions that the model develops are:
-	The model proposes a system defined by input parameters in equilibrium, which resolves that the amount of sediments input to the model is transported along the channel, the coast and outwards.
-	The model is applied to short tidal basins (1/20 of the tidal wavelength), implying that the water level gradients are negligible.
-	The model assumes that the systems’ reaction to SLR can be represented by a single adaptation time scale.

The code develops calculation based on: 
1. Sediment transport, 
2. Hydrodynamic changes, 
3. Expansion of the intertidal area based on the sediment supplement of the river, 
4. Changes of the coastline under the variation of sea level
5. Time adaptation scale.

![MorQuest_Methology](https://github.com/mreyesc22/MorQuestCode/assets/43484469/706dc49b-a4cc-445e-a099-6ef70875ab8c)

### Project description

The Morquest code addresses the fundamental question: **How can we globally assess the impact of climate change on estuarine morphodynamics at first order?**

Therefore, the interest and development of the code were based on the following objectives:

- Utilizing satellite imagery as the primary data source.
- Developing a model capable of conducting simulations with limited data availability.
- Performing calibration of the developed model.
- Conducting long-term projections to provide valuable insights for sustainable coastal management.
  
The theoretical foundation and development of the code are detailed in the research conducted by M. (2023). This analysis is delineated in the thesis titled **"Assessing Sea Level Rise Impact on Estuarine Morphodynamics"** submitted to obtain the academic degree of Master in Water and Sustainable Development at IHE Delft. You can access the thesis via the following link:https://ihedelftrepository.contentdm.oclc.org/digital/collection/masters1/id/338392

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

An example of how to execute the software in a Jupyter Notebook is available in the repository (`example_jupyter.ipynb`). To run it, activate your `morQuest` environment with `conda activate morQuest` (if it's not already active) and then type:
```
jupyter notebook
```

A web browser window will open. Point to the directory where you downloaded this repository and click on `morQuest_Simple.ipynb`. A Jupyter Notebook combines formatted text and code. To run the code, place your cursor inside one of the code sections and click on the `run cell` button (or press `Shift` + `Enter`) and progress forward.

![00_Initial_Setting](https://github.com/mreyesc22/MorQuestCode/assets/43484469/715218dd-21e4-45fc-aaea-f6bc3d6a2328)

The following sections show an example of how to run the full Alsea bay workflow at Alsea bay (USA).

### 2.1  Define study area
For this example, we will input the **Data Manually**. Therefore, this Jupyter notebook file can be used to conduct the analysis in a general manner.

![01_Study_Area](https://github.com/mreyesc22/MorQuestCode/assets/43484469/befb4739-d356-4691-98bc-aaa6e68f7bf0)

### 2.2 Input Data
In the initial phase of the study, the focus lies on the selection of comprehensive datasets that furnish sufficient information for subsequent analysis. Following this, the subsequent step involves gathering pertinent data, encompassing intertidal area (`Ai`), channel area (`Ac`), tidal difference (`dH`), river flow (`Qr`),change in sediment supply (`ssc`), closure depth (`cd`), dune height (`du`), active shorezone slope (`betas`), and sea level projection (`slr`). 

Furthermore, calibration and sensitivity parameters within the model were identified, as listed below.

- `incAi`: Rate of annual intertidal area expansion. 
- `erc`: Factor governing the entrapment of river-supplied sediment from the river into the channel.
- `ecs`: Factor controlling the entrapment of river-supplied sediment from the channel into the shoreline.
- `fis`: Factor for transport from river to intertidal area under river sediment supply change.
- `fs`: Factor responsible for the distribution of intertidal area deposition to intertidal area width and channel slope.
- `si`: Factor influencing the increase in intertidal area slope at its edge.
- `faw`: Factor responsible for reducing `fs` and `fis` in case of a decrease in yearly sediment transport from the river into the channel.

![02_Input_data](https://github.com/mreyesc22/MorQuestCode/assets/43484469/5f82c967-f00c-4f06-9faa-e52ee1215705)

### 2.3 Execution of the code

The Morquest code is programmed within the file `morquest.py`. To execute it, simply run the code `run_morquest(input_data, 'output.mat')`. The results are saved in a '.mat file'.

![03_RunCode](https://github.com/mreyesc22/MorQuestCode/assets/43484469/4961e34e-3ebb-422a-bd4f-0abd79def014)

Additionally, a summary table of the general information regarding the main output variables has been generated.

![03_1_table](https://github.com/mreyesc22/MorQuestCode/assets/43484469/b216c892-0466-477c-9eed-2fa82540fb66)

### 2.4 Graphical Representation of Results
The results extracted within morQuest enable analysis of how the main elements evolve over the analyzed time period.

- Intertidal Area, Channel Area and Adaptation Time Scale. `km^2`
- Intertidal Depth and Channel Depth. `m`
- Intertidal, Channel and Delta Volume. `m^3`
- Intertidal, Channel and Delta Sed Volume. `m^3`
- Sediment transport for Qci, Qcd, Qcs and Qso. `m^3/year`
  
![04_Graphics](https://github.com/mreyesc22/MorQuestCode/assets/43484469/4cee439d-58c8-4b1c-a0e5-cf460eab3c22)





