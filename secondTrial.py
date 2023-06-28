import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import time
import threading

# READ
# https://github.com/MinaPecheux/py-sound-viewer/blob/main/main.py
samplerate = 44100  # Sample rate
channels = 1  # Number of channels
duration = 1  # Duration of recording in seconds
blocksize = int(samplerate * duration)  # Blocksize to read `duration` seconds

recording = np.array([])

def audio_callback(indata, frames, time, status):
    global recording
    recording = indata.copy().reshape(-1)  # Copy and reshape the input data

# Create a stream with the specified parameters and callback
stream = sd.InputStream(callback=audio_callback, channels=channels, samplerate=samplerate, blocksize=blocksize)

stream.start()  # Start the stream

while True:
    time.sleep(duration)  # Wait for `duration` seconds
    print(recording)  # Print the recorded data

    plt.figure()
    plt.plot(recording)  # Plot the recorded data
    plt.show()

stream.stop()  # Stop the stream
stream.close()  # Close the stream