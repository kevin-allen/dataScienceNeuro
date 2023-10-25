# General installation

To be able to run Python code, you will need to install Python on your computer if your Operating system does not come with it.

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

I normally create a directory called `repo`, and I put all my repositories in there. 

Here, we will clone the course repository.

```
cd ~
mkdir repo
cd repo
git clone https://github.com/kevin-allen/dataScienceNeuro.git
```

If you want to update your repository with the latest version, you can use `git pull`.

```
cd repo/dataScienceNeuro
git pull
```

When working in the class room or experimenting with the course content, I would recommend making a copy of the original notebook and only working on the copy. 

