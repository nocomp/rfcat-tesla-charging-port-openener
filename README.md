# rfcat-tesla-charging-port-openener
python script for open tesla charging port using rfcat zith the yard stick one <br><br>
<img src="https://i.imgur.com/oHceMxr.jpeg"/><br><br>
Requirements:
You need to have rfcat propelly installed in order to use this script and python3
In order to install rfcat<br> <b> please follow these instructions:</b>

https://github.com/atlas0fd00m/rfcat

or:
<h3>Install RFCat</h3><br>
git clone https://github.com/atlas0fd00m/rfcat/<br>
sudo python setup.py install<br>
cd ../<br>
<br><br>
<h3>Install LibUSB</h3><br>
pip install libusb<br>

<h1>Before use the script install requirements:</h1>
pip install - r requirements.txt<br>

<br><br>
<h1>How to use:</h1>
<br><br>
In tesla-rfcat.py uncomment the frequency depeding you live in usa or in the rest of the world<br>
<br>
d.setFreq(433920000) # Freq for EU<br>
#d.setFreq(315000000) #Freq for USA<br>
<br>
Save and run the file as folow<br>
python3 tesla-rfcat.py<br>


Thank you to PickedItMate for the payload optimisation<br>

<b>Yard stick one discord channel:</b> <br>
https://discord.gg/C7nwKE8T<br>
Author: <a href="https://twitter.com/nocomp">nocomp</a>

