import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import time

# Duration of recording in seconds
duration = 10  
# Sample rate
samplerate = 44100
# Initialize array to hold audio data
recording = np.array([])

# Callback function to record audio data
def audio_callback(indata, frames, time, status):
    global recording
    recording = np.append(recording, indata)

# Open the stream
stream = sd.InputStream(callback=audio_callback, channels=1, samplerate=samplerate)

# Start recording
stream.start()

start_time = time.time()
while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    # If a second has passed
    if elapsed_time // 1 > (len(recording) // samplerate):
        # Get the audio data for the last second
        last_second_data = recording[-samplerate:]

        # Show the audio data
        print(last_second_data)

        # Plot the audio data
        plt.figure()
        plt.plot(last_second_data)
        plt.show()

    # If duration has passed
    if elapsed_time > duration:
        break

stream.stop()
stream.close()