#This is the draft code
from redvox.common.data_window import DataWindow
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Input Directory
input_dir = "\\Users\\allen\\Downloads\\Phone_Downloads\\2x2Pyramid.lz4"

# Load data window from report
dw = DataWindow.deserialize(input_dir)

for station in dw.stations():
    # Get audio data 
    audio_samples = station.audio_sensor().get_microphone_data()
    audio_time_micros = station.audio_sensor().data_timestamps() - station.audio_sensor().first_data_timestamp()
    audio_time_s = audio_time_micros*1E-6  # from microseconds to seconds
    
    # Plot Audio data for each station
    plt.figure()
    plt.plot(audio_time_s, audio_samples)
    plt.title(f"RedVox Station ID {station.id()}")
    plt.xlabel(f"Seconds from {int(dw.start_date()*1E-6)} Unix epoch UTC")
    plt.ylabel("Mic amplitude (unity at full range)")

#df = pd.DataFrame({'Time' : audio_time_s, 'Amplitude' : audio_samples})
#print(df)

#txt_dir = "\\Users\\allen\\Downloads\\Project_Data.txt"

#np.savetxt(txt_dir, df.values, delimiter=',', newline="\n", header='25Cube Data For Phone', comments= 'First column is the time in seconds from recorded UTC. The second column is the corresponding amplitude. \n', fmt="%s")


plt.show()