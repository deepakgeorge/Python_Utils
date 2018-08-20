# Conda Tutorial

Note: <> denotes changes to be made

### Create a conda environment
```
conda create --name <environment-name> python=<version:2.7/3.5>
```

### List all environments
```
conda info --envs
```

## requirements.txt
- #### To create a requirements.txt file
```
conda list -e > requirements.txt #Save all the info about packages to your folder
```
```
conda list #Gives you list of packages used for the environment
```

- #### To install packages in requirements.txt
```
conda install --yes --file requirements.txt
```
## <environment-name>.yml
- #### To export environment file
```
activate <environment-name>
conda env export > <environment-name>.yml
```
- #### To recreate environment file from environment-name>.yml
```
conda env create -f <environment-name>.yml
```
