# Run Jupyter Notebooks on Google Colab

It is sometimes helpful to run Jupyter Notebooks on Google Colab. For example, if you want to train a deep neural network using a GPU but your computer does not have a GPU, you can use Google GPUs to train your model.

To use Google Colab, you will need a Google account.

Having a Google Drive to load data files from it is also useful. You can also save data from the notebook to your Google Drive. 

In the instructions below, we will use Google Drive to access data from your Jupyter Notebook. 

## Create a folder for your data and notebooks on Google Drive

1. Create a folder in the root of your Google Drive. You can call it `dsfolder`.
2. Upload the notebook called `colab_test.ipynb` from the `notebooks` directory into the `dsfolder` of your Google Drive. 
3. Upload the file `animal_speed.npy` from the `data` folder into the `dsfolder` of your Google Drive.

## Open your Notebook in Google Colab

1. Double click on the `colab_test.ipynb` in the `dsfolder`.
2. You should now have a window with the content of the notebook.
3. Run the code of the Notebook to learn how to access your Google Drive from a notebook in Google Colab.


## Make sure Google Drives does not change .csv to .gSheet 

When you upload files to Google Drive, Google might decide to change the format of the files. 

To disable the "Convert uploaded files to Google Docs editor format" option, you can follow these steps:
1. Open Google Drive in your web browser.
2. Click on the gear icon (:gear:) in the upper-right corner to open the Settings menu.
3. In the Settings menu, select "Settings."
4. Look for the option named "Convert uploaded files to Google Docs editor format." If it's present, you can toggle it off to disable the automatic conversion.







