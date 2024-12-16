# File names and column IDs
scd41_file = ["Temp_RH_CO2", ["Timestamp", "Temp[°C]", "RH[%]", "CO2 [ppm]"]]
apds_file = ["Light", ["Timestamp", "ALS [digits]"]]
spg_file = ["VOC", ["Timestamp", "VOC Raw [digits]", "VOC Index [digits]"]]
mp_file = ["Microphone", ["Timestamp", "Microphone Amplitude [digits]"]]
mics_file = ["NH3", ["Timestamp", "NH3 Sensor resistance [Ohm]", "NH3 value"]]
gravity_file = ["NH3", ["Timestamp", "NH3[ohm]","NH3 temperature compensated [ohm]","NH3[ppm]"]]

files = [scd41_file, apds_file, spg_file, mp_file, mics_file]

outputfolder = 'csv'

# IDs of the sensornodes
SNIds = [1]

# IDs and COM ports of the sensors
sensor_com_pairs = []

# Port of gravity sensor
gravity_port = []

# false if nodes is offline, true if online
node_connected = dict()

# Fixed thresholds for user warning
temp_upper = 27
co2_upper = 2000
nh3_upper = 100

sensor_warnings = dict()

