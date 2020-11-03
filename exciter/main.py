import os, yaml
from pyo import *


API = "jack"
MIDI_API = API
NAME = "master-a"

server = Server(audio=API, jackname=NAME, duplex=1, midi=MIDI_API)
server.boot()
server.setJackMidiInputPortName("midi_in")
#server.setJackAutoConnectMidiInputPort("midi_capture_2")
SAMPLING_RATE = server.getSamplingRate()

params = yaml.load(open("params.yaml"))
print(params)
adc = Input([0, 1])
fourband = FourBand(adc)
compressors = [
    Disto(
        Compress(
            fourband[i], 
            thresh=params["compress"]["threshold"][i//2],
            ratio=params["compress"]["ratio"][i//2],
        ),
        drive=params["drive"]["amount"][i//2],
        slope=0,
        mul=params["drive"]["gain"][i//2]
    ) for i in range(8)]
mix = Mix(compressors, voices=2, mul=.3)
limit = Compress(mix, thresh=-1, ratio=100).out()


server.start()
server.gui(locals())

# mix.stop();adc.out()
# adc.stop();adc.play();mix.out()