from scipy.signal import butter
from scipy.signal import sosfiltfilt
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import numpy as np


def plot_recording_data(dat, offset=3000, startSample=0, endSample=5000,figsize=(20,15)):
    """
    Function to plot our electrophysiology data
    
    Arguments
    dat: 2D numpy array containing in-vivo recordings. The dimensions are : [channel,sample]
    offset: offset between each channel to avoid plotting all channels on top of each other
    startSample: first sample to show
    endSample: last sample to show
    """
    
    plt.figure(figsize=figsize) # set the size of the figure
    for i in range(dat.shape[0]): #loop for every channel
        plt.plot(dat[i,startSample:endSample]-i*offset,label=i) # plot the channel, apply the y-offset so that the channels are not all on top of each other
    plt.legend()
    plt.show()
    
def create_butter_highpass_filter(lowcut, fs, order=3):
    """
    Create a highpass Butterworth filter using scipy.signal.butter()
    
    Arguments:
    lowcut: low cut frequency 
    fs: sampling rate
    order: order of the filter
    
    Return:
    The function returns a filter in the sos format
    """
    nyq = 0.5 * fs # Nyquist frequency (sampling rate/2)
    low = lowcut / nyq # lowcut as a proportion of Nyquist frequency
    sos = butter(order, [low], btype='highpass' ,  output='sos') #‘sos’ should be used for general-purpose filtering.
    return sos


def filter_raw_data(dat,lowcut=300, fs=20000):
    """
    Function to filter the raw data by applying a highpass filter
    
    Arguments:
    dat: 2D numpy array containing raw in-vivo recordings. The dimensions are : [channel,sample]
    lowcut: low cut frequency 
    fs: sampling rate
    order: order of the filter
    
    Return:
    Filtered data as a 2D numpy array
    """
    # filter the data
    myFilter = create_butter_highpass_filter(lowcut = lowcut,fs=fs, order=3)
    y = sosfiltfilt(myFilter, dat) # the sosfilt() function can take a 2D array and will filter every row separately
    return y

def spike_detection(y,z=5):
    """
    Function to perform spike detection on filtered in-vivo recordings from the brain. It gets you the time at which spikes were detected on each channel
    
    
    Arguments:
    y: 2D numpy array containing filtered in-vivo recordings. The dimensions are : [channel,sample]
    z: threshold in standard deviations from the mean for spike detection
    
    
    Returns:
    spikeTimes: List of numpy arrays containing the times of spikes detected on each channel. 
    """

    # We can use Numpy mean, std to calculate the mean of each channel without a for loop
    means=y.mean(axis=1)
    stds=y.std(axis=1)
    thresholds = means-stds*z

    # We need to copy our filtered data 
    yDetect = y.copy() # use a copy of the data to avoid destroying it during the manipulation

    # Inverse the polarity of the signal
    yDetect = 0 - yDetect

    # Create an empty list to store the spikes detected on each channel
    spikeTimesList = [] 

    # loop to detect the spikes on each channel
    for i in range(y.shape[0]):
        spikeTimes, _ = find_peaks(x=yDetect[i,:],height=0-thresholds[i]) # the function returs 2 values, we want the first one
        spikeTimesList.append(spikeTimes)
        print("Detection chan {}, {} spikes".format(i,spikeTimes.shape[0]))
    
    return spikeTimesList,thresholds

def plot_spike_detection(y,spikeTimesList,thresholds,offset=3000, figsize=(20,15)):
    """
    Function to plot the results of our spike detection procedure
    
    Arguments:
    y: 2D numpy array containing the filtered data
    spikeTimeList: list of 1D numpy arrays. each array contains the times of the spikes detected on one channel
    thresholds: 1D numpy array containing the detection thresholds for each channel
    offset: y offset for plotting the data of each channel. To avoid plotting data on top of each other
    """
    
    plt.figure(figsize=figsize) # set the size of the figure
    for i in range(y.shape[0]): #loop for every channel
        plt.plot(y[i,:]-i*offset,label=i) # plot the channel, apply the y-offset so that the channels are not all on top of each other
        plt.plot([0,y.shape[1]],[thresholds[i]-i*offset,thresholds[i]-i*offset]) # plot the threshold
        plt.scatter(spikeTimesList[i],y[i,spikeTimesList[i]]-i*offset,c="red") # plot the spikes
    plt.legend()