import vxi11
import matplotlib
import matplotlib.pyplot as plt

class Osci ():

    def __init__(self , ip):
        self.os =  vxi11.Instrument(str(ip))
        self.indexVol = 0
        self.indexTime = 0
        self.indexcoupling = 0
        self.start_trig_lv = 0
        self.indexTrigSweep = 0
        self.indexTrigSl = 0
        self.vertiPos = 0
        self.horiPos = 0
        self.probeRatio = "1"
        self.channel = "1"
        self.ch_on = True

    def run (self): # run
        self.os.write(':RUN')
    
    def auto (self):
        self.os.write(':AUToscale')
    def ch_display (self,ch): #display ch 
        if (self.ch_on):
            self.os.write(f"CHAN{str(ch)}:DISP ON")
            self.os.write(f':CHANnel{str(ch)}:PROBe {self.probeRatio}')
            self.ch_on = False
        else:
            self.os.write(f"CHAN{str(ch)}:DISP OFF")
            self.ch_on = True

    def set_vol_scale (self , ch, direction):
        volList = [str(0.001*int(self.probeRatio)), str(0.002*int(self.probeRatio)), str(0.005*int(self.probeRatio)), str(0.01*int(self.probeRatio)), str(0.02*int(self.probeRatio)), str(0.05*int(self.probeRatio)), str(0.1*int(self.probeRatio)), str(0.2*int(self.probeRatio)), str(0.5*int(self.probeRatio)), str(1*int(self.probeRatio)), str(2*int(self.probeRatio)), str(5*int(self.probeRatio))]
        if self.indexVol==len(volList):
            self.indexVol=0
        self.os.write(f"CHAN{str(ch)}:SCAL {volList[self.indexVol]}")
        if direction == "up":
            self.indexVol +=1
        elif direction == "down":
            self.indexVol -=1

    def set_time_scale (self , scale):
        self.os.write(':TIM:MAIN:SCAL ' + str(scale))

    def tg_lv(self, value):
        self.start_trig_lv = self.start_trig_lv + value
        self.os.write(f':TRIGger:EDGe:LEV {str(self.start_trig_lv)}')
    
    def setProbeRatio(self, channel,value):
        self.os.write(f':CHANnel{str(channel)}:PROBe {str(value)}')
        self.probeRatio = value

    def setCoupling(self):
        coupList = ["DC, AC, GND"]
        if self.indexcoupling==len(coupList):
            self.indexcoupling=0
        self.os.write(f':CHANnel{self.channel}:COUPling {coupList[self.indexcoupling]}')
        self.indexcoupling +=1
    
    def setTrigSweep(self):
        sweepList = ["AUTO", "NORM", "SING"]
        if self.indexTrigSweep==len(sweepList):
            self.indexTrigSweep=0
        self.os.write(f":TRIGger:SWEep {sweepList[self.indexTrigSweep]}")
        self.indexTrigSweep += 1

    def setTrigSource(self):
        self.os.write(f":TRIGger:EDGe:SOURce {self.channel}")

    def setTrigSlope(self):
        slopeList = ["POS", "NEG", "RFAL"]
        if self.indexTrigSl==len(slopeList):
            self.indexTrigSl=0
        self.os.write(f":TRIGger:EDGe:SLOPe {slopeList[self.indexTrigSl]}")
        self.indexTrigSl += 1
    
    def setVerticalPosition(self, direction):
        if direction == "up":
            self.vertiPos += 20e^-6
        elif direction == "down":
            self.vertiPos -= 20e^-6
        self.os.write(f":CHANnel1:OFFSet {self.vertiPos}")
    
    def setHorizontalPosition(self, direction):
        if direction == "up":
            self.horiPos += 20e^-6
        elif direction == "down":
            self.horiPos -= 20e^-6
        self.os.write(f":TIMebase:MAIN:OFFSet {self.horiPos}")

    
