# Data Science in Neuroscience

This is the repository for the course [Data Science and analysis in Neuroscience](https://lsf.uni-heidelberg.de/qisserver/rds?state=verpublish&status=init&vmfile=no&moduleCall=webInfo&publishConfFile=webInfo&publishSubDir=veranstaltung&veranstaltung.veranstid=375092&purge=y&topitem=lectures&subitem=editlecture&asi=al$3tixanI2BKb.VkKa2) which is offered to Master's students on the Neuroscience Major program at the  Faculty of Biosciences, University of Heidelberg.

The course is aimed at students interested in improving their ability to perform data analysis in the field of neuroscience. 

Most lectures have an important hands-on component, where the students learn to run codes on their own computers. There are exercises associated with most of the topics covered in class.

The students will complete a small data science project toward the end of the course. These projects will be presented by the students during the last lecture of the course.


## Useful links 

* [Install python and python libraries for the course](installation.md)
* [Run Jupyter Notebooks on Google Colab](colab.md)
* [Projects](projects.md)

## Week 1

* What is data science?
* Introduction to Python, NumPy, Matplotlib, and Pandas.
<div>
<img src="images/packages_logos.png"/>
</div>


* Load electrophysiological data recorded from the hippocampus of a mouse into a NumPy array.
* Inspect NumPy arrays, perform calculations on NumPy arrays, and plot NumPy arrays with Matplotlib.



<div>
<img src="images/shortRaw.png"/>
</div>

## Week 2

* Introduction to machine learning
* Speed cell: a simple example of machine learning with a linear regression

<div>
<img src="images/learning_animation/learning_animation.gif" width="1000" align="center">
</div>


## Week 3

* Why and how are in-vivo recordings performed?

* Introduction to the SciPy library
<div>
<img src="images/scipy.png"/>
</div>


* Detecting action potentials and spike clustering
  * Filtering
  * Detecting spikes
  * Extracting spike waveforms
  
<div>
<img src="images/filteredSignals.png"/>
</div>

## Week 4

Introduction to the scikit-learn library

<div>
<img src="images/scikit-learn.png" width="150" />
</div>

* Dimensionality reduction



* Clustering spike waveforms
  
<div>
<img src="images/pca.png" width="700"/>
</div>



## Week 5


<div>
<img src="images/pytorch.png" width="300"/>
</div>

* Introduction to neural networks
* Training models with pytorch
* Using a convolutional network to classify images

## Week 6.1

* Tracking objects in images using a U-Net

![Example](images/tracking_animation.gif)

## Week 6.2

* Analysis on spike trains (mean firing rate and instantaneous firing rate)
* Firing rate map of a spatially selective neuron

<div>
<img src="images/gridCellExample.png"/>
</div>
