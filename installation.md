# General installation

To be able to run Python code, you will need to install Python on your computer if your Operating system does not come with it.

## Ubuntu




## Windows

### You probably need to install Python.

*  Go to https://www.python.org/downloads/windows/
*  Download the Python installer
*  Run the Python installer

### Create a python virtual environment

*  Open a terminal
*  `python.exe -m pip install --upgrade pip`
*  `pip install virtualenv`
* `mkdir python_environments`
* `cd python_environments`
* `virtualenv dsenv`

### Activate your Python virtual environment

* `.\dsenv\Scripts\activate`


### Install Python packages in your virtual environment

With your Python environment activated, install a few packages

`pip install numpy pandas matplotlib scipy jupyterlab`


### Test your installation

You should now be able to run the Jupyter Lab server on your computer and create a Jupyter notebook in your browser.

* Open a terminal
* Activate your Python virtual environment
* Launch Jupyter lab from the terminal: `jupyter lab`


## Install git

This is for all operating systems.

You probably want to install `git` to be able to get the content of the course from the GitHub repository.

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

