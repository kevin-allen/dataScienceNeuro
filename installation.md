# General installation

To be able to run Python code, you will need to install Python on your computer if your Operating system does not come with it.

## Windows operating system

I recommend using `Anaconda` to install Python on your Windows computer.

### Install Anaconda

1. Download the Anaconda installation file from https://docs.anaconda.com/free/anaconda/install/windows/
2. Double-click on the downloaded file to install Anaconda. Use the default settings and note the installation directory

### Create a conda environment in which you will run the code for the course


1. Open Anaconda.Navigator
2. Click on `Environments`
3. Click `create`
4. Enter the name "dsenv" to create an environment named `dsenv`. Select python 3.11.5

### Install pytorch

1. Open the Anaconda PowerShell prompt
2. `conda activate dsenv`
3. `conda install pytorch torchvision torchaudio cpuonly -c pytorch`

### Test torch installation
1. Open the Anaconda PowerShell prompt
2. `conda activate dsenv`
3. `python`
4. In the Python interpreter, run `import torch`

### Install jupyter lab in your torch environment
1. Open the Anaconda PowerShell prompt
2. `conda activate dsenv`
3. `conda install matplotlib`
4. `conda install -c conda-forge jupyterlab`
5. Close and restart the Anaconda PowerShell prompt and activate the torch environment
6. `jupyter lab`


You should now be able to run the Notebook of the course. 
Don't forget to activate your `dsenv` when you start working.


## Ubuntu

Ubuntu comes with Python 3 installed by default.

### Install pip

```
sudo apt install python3-pip
```

```
pip install virtualenv
```


### Create a python virtual environment

*  Open a terminal
```
cd ~
mkdir python_environments
cd python_environments
virtualenv dsenv
```

### Activate your Python virtual environment

```
source ~/python_environments/dsenv/bin/activate
```

### Install Python packages in your virtual environment

With your Python environment activated, install a few packages

```
pip install numpy pandas matplotlib scipy jupyterlab scikit-learn
```


### Test your installation

You should now be able to run the Jupyter Lab server on your computer and create a Jupyter notebook in your browser.

* Open a terminal

```
source ~/python_environments/dsenv/bin/activate
jupyter lab
```


## Install git

You probably want to install `git` to be able to get the content of the course from the GitHub repository.

```
sudo apt install git
```


## Make a copy of the repository on your computer (clone)

I normally create a directory called `repo`, and I put all my repositories in there. 

Here, we will clone the course repository.

```
cd ~
mkdir repo
cd repo
git clone https://github.com/kevin-allen/dataScienceNeuro.git
```

The content of the course is now on your computer.

## Update your copy of the course repository

```
cd repo/dataScienceNeuro
git pull
```

When working in the classroom or experimenting with the course content, I would recommend making a copy of the original notebook and only working on the copy. 

