import pyaudio
import wave
#import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
import numpy as np
import pandas as pd

BUTTON = 26

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(BUTTON, GPIO.IN)

INDEX=0
WIDTH=2
CHANNELS=8
RATE=16000
CHUNK=1024
RECORD_SECONDS=1

timestr = time.strftime("%m%d")

def minionsMaxChannel() :

    WAVE_OUTPUT_FILENAME="output"+timestr+".wav"
    record_data=[]
    avg_data=[]
    fftData=[]
    fftLen=[]

    while True:
        p=pyaudio.PyAudio()

        FORMAT=p.get_format_from_width(WIDTH)
    
        #state = GPIO.input(BUTTON)
        #if not state:
            #break
    
    # start Recording

        stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            input_device_index=INDEX,
                            frames_per_buffer=CHUNK)
        print"recording..."
        frames=[]

        for i in range(0,int(RATE/CHUNK*RECORD_SECONDS)):
            data=stream.read(CHUNK)
            frames.append(data)

        #print"finished recording"

# stop RECORDING

        stream.stop_stream()
        stream.close()
        p.terminate()

        waveFile=wave.open(WAVE_OUTPUT_FILENAME,'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(p.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
    
        for i in range(6):
            fs, data = wavfile.read(WAVE_OUTPUT_FILENAME)
            record_data.append(data.T[i])
            norm=[(ele/2**8.)*2-1 for ele in record_data[i]]
            fftData.append(fft(record_data[i]))
            fftLen.append(len(fftData[i])/2)
            avg_data.append(sum(abs(fftData[i]))/fftLen[i])
    
        #print(avg_data)
    
        maxValue = np.array(avg_data)
        maxIdx = np.where(maxValue==max(avg_data))
        _maxChannel = int(maxIdx[0])
    
#        for i in range(6):
#            if i==int(maxIdx[0]):
#                _maxChannel=i
#                ax = plt.subplot(3,2,i+1)
#                ax.set_title('Channel %d' %(i+1))
#                plt.plot(abs(fftData[i][:(fftLen[i]-1)]),
#                         color='red')
#            #plt.xlabel('Channel ', num2str(i))
#                plt.axis("off")
#            else:
#                ax = plt.subplot(3,2,i+1)
#                ax.set_title('Channel %d' %(i+1))
#                plt.plot(abs(fftData[i][:(fftLen[i]-1)]))
#            
#                plt.axis("off")
#        plt.show()
        
        break
    
    return _maxChannel, fftData

def minionsMakeArray(_data):
    
    finalArray = []
    subArray = []
    
    for i in range(6):
        sortedData = sorted(abs(_data[i]), reverse=True)
        arrayData = [sortedData[15359], sortedData[11520], sortedData[7680], sortedData[3840], sortedData[0]/10, sortedData[0]/10, sortedData[3840], sortedData[7680], sortedData[11520], sortedData[15359]]
        subArray.append(arrayData)
    
    reverseArray = np.flipud(subArray)
    
    finalArray = subArray + subArray
    
    return finalArray

    
#if __name__ == "__main__":
#    MaxChannel, data = minionsMaxChannel()
#    print(MaxChannel)
#    df = minionsMakeArray(data)
#    print(df)
