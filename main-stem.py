import nltk #import knihovny Natural Language Toolkit. Je potřeba ji i nainstalovat: http://www.nltk.org/install.html
sentence = "At eight o'clock on Thursday morning! Arthur didn't feel very good."  # Věta, která bude rozebrána

sentence = "Sand Blast Cabinet consist of the Blast Cabinet, sandblasting nozzle, Abrasive Media tray, Abrasive Media Dosing system (abrasive dispenser), screw conveyor, Abrasive separator and drive for moving the sandblasting nozzle. The automatic system is equipped with a STOP and START button, a cast presence sensor, and an door end sensor and lock  sensor."
#sentence = "The clamping of the casting is provided by a linear pneumatic motor A. Clamping of the blasting unit by linear pneumatic motor B. Moving the blasting machine by linear pneumatic motor C. All three pneumatic motors are equipped with end position sensors."
#sentence = "The sandblasting machine consists of a blasting cabin, sandblasting nozzle, abrasive media tray, abrasive media dosing system (abrasive dispenser), screw conveyor, abrasive separator, and drive for moving the sandblasting nozzle. The automatic system is equipped with a STOP and START button, a cast presence sensor, and a door and lock sensor."
#sentence = "After the casting is placed by the operator in the cabin, the casting presence sensor is activated, the START button is pressed, and the cabin door is closed then production operation can start. The cast is clamped. Subsequently, the sandblasting of the first casting arm is started for a preset time Ta. This time is a parameter that can be changed from the operator and dispatcher workstation for the next casting to be machined. When the sandblasting time of the first arm has elapsed, sandblasting is interrupted and the nozzle moves to the position for sandblasting the second arm. Sandblasting is then started again for the defined time Tb."
#sentence = "When the STOP button is pressed or the blast cab door is opened, the blasting machine immediately stops - stops the blasting and stops the nozzle movement, and releases the clamping drive for manual manipulation. Furthermore, the red light on the traffic light flashes until the time of error acknowledgment."
#sentence = "The entire system may be in the automatic production mode (according to the cycle described in point B), called EXECUTION, triggered by the START button. When the cycle is complete, the system enters a ready state, called IDLE. The next state is an EMERGENCY_STOP activated by pressing the EMERGENCY_STOP button, which must be acknowledged by turning off this button and then pressing the RESET button. In the MANUAL control mode, the individual technological steps can be performed manually, and in the SERVICE mode, it is possible to control all outputs of the control system and monitor all inputs.  The EMERGENCY_STOP state can be accessible at any time by pressing the EMERGENCY_STOP button. Other states can be accessible from the IDLE state."
#sentence = "The system will be equipped with an operator panel for setting the Ta and Tb parameters and for manual control of the equipment in case of operational complications and for manual control in service mode for the adjuster/technician."
#sentence = "The dispatcher workstation contains one screen. From the dispatcher workstation it is possible to set the values of the Ta and Tb parameters and display the current system status. In addition, the number of pieces produced for a given workshift and since the beginning of the defined time (counter reset). SCADA collects data from the PLC that corresponds to the number of cycles of the moving components such as control valves and pneumatic motors for predictive maintenance."
#sentence = "The system is equipped with a STOP and START button for switching the sandblasting on and off, a cast presence sensor, and a door lock end sensor. From the hopper, the abrasive medium (sand) is carried by compressed air to the blast nozzle from which the abrasive is shot onto the casting. A separator separates dust and condensate from the compressed air.  A dosing system allows the quantity of abrasive to be set for blasting. The nozzle position can be changed by means of a pneumatic linear actuator. The used abrasive is returned to the hopper by means of a screw conveyor."

#ORCHAD
sentence = "The concept also aims to reduce the need for human labor, save inputs and increase production efficiency. The basis of the project will be in the selection of suitable varieties of the apple tree and the selection of apple genotypes, which will meet the requirements for the new conception and meet the fruit quality, storage, and required organoleptic parameters of apples, in order to register a new variety. An experimental and demonstration orchard will be established, as well as a small-scale experimental orchard. Container planting for laboratory tests will also be established. With regard to the deployment of robotic platforms, the newly designed support structure of the orchard will be implemented. The interaction between mechanical interventions and the condition of trees will be monitored throughout the project. These indicators will be important for the choice of terms of intervention, the intensity of intervention, but also for the selection of suitable shapes or materials used on mechanical parts of machines that come into direct contact with trees. Based on our findings, the structural elements will always be innovated. During the vegetation period, trees will be monitored at regular intervals using distance measurement methods to determine tree height, growth, green condition, health status, flower stocking intensity, fruit ripening, fruit stocking, and overall orchard variability. The data will be compared with the measurement of tree parameters during vegetation. All data will be compared with data from systematically distributed IoT sensors in the soil to measure temperature and water availability. The project will develop a harvesting head connected to a handling arm designed for autonomous fruit harvesting. The treetop shape of apple trees will allow us to create a completely different concept of robotic harvesting. The robotic harvesting head and manipulator will be developed. An important element of the design will be the requirement to treat apples with care. The risk of damage will be considered with regard to the shape and kinematics of the working parts of the harvesting head and the material used. The manipulation arm will be a tool for precise guidance of the head to the apple trunk and subsequent movement of the harvesting head in the axis of the terminal bud. Sensor technology will be used to detect the trunk, guide the harvesting head, and limit the contact of the harvesting head or arm with the apple tree trunk. The created structural units will be verified on the experimental plantings and subsequently installed on a towing device for testing in real operation. During the harvest, the apple damage, yield, and quality of production at the level of individual trees will be monitored. Algorithms for the detection of the trunk, guide structure, and new leaves will be developed for precise guidance of mechanical parts of the manipulator working in an orchard. A cloud environment will be ready for calculations and remote access to platform data. This will allow all work to be planned in advance and transferred to the robotic platform. It will be possible to change the parameters operatively during the work. Computational capacity will also be used to evaluate the collected data, including the storage of application data. A proposal will be made for the implementation of a sensor network and computing and communication infrastructure for advanced computing and a software interface for its use. The individual work procedures were compiled in such a way that they logically follow each other and complement each other. Digital twin set - each tree will have a digital twin, where it will be recorded how it was treated - spraying, cutting, fertilization, harvest and at the same time will be stored biological data obtained by passing a tractor with navigation - measured trunk parameters, harvest maturity evaluation, quantity, size and color of fruits, flowers and buds. Including selected photos and data obtained from the machine vision methods from those photos and videos.  In the orchard the columnar apple trees are planted. The tractor with the harvesting head (or e.g. sprayer) is equipped with a camera system and many sensors for its own navigation. These sensors are part of the sensory system. The temperature, air humidity, and soil humidity sensors are installed in the orchard for support of the intervention schedule. Sensors are connected into an IoT network. Identification of the given orchard row is realized by the ARTags (or RFID - radio frequency identification). Reading ARTags is realized by the camera with computer vision system and RFID by the RFID reader. The tree identification and position are realized by the computer vision system (which identifies the trunk primarily) with the support of ultrasound sensors and GPS (Global Positioning System) navigation of the tractor. Computer vision is based on the camera, deep camera, and lidar data. Control system consists of many distributed units for each task and domain. The harvesting robotic head at the mobile platform has its control unit. Computer vision system for identification of tree trunk has separated, more powerful, computing unit. Also, human operators are supposed to control selected facilities like a tractor. Data from the sensory system are collected into the database for online control and dispatching. Selected camera images are sent to the database too. A selected image means a photo of each tree made during the treatment. These photos are also complemented by the additional information (state, health, rate of buds or flowers, and of course the date, time, temperature, air humidity) if it is possible. Each tree is identified by the row and position in the row. The model of the orchard with corresponding tags is part of the digital twin. This data are visualized for easier understanding. The Agricultural information system (or Farming Management System FMS) is based on the digital twin of the orchard. A digital twin is a model of the orchard which is continuously replenished by the information about individual trees. This is information about treatment like a watering, spraying, fertilization, or harvesting. About estimation of the flower buds, flowers, and small fruits amount estimation. The computation part of the digital twin contains yield and fruit maturity estimator and treatment scheduler. This level is not defined in this project. Flower buds or flowers or small fruits amount estimation. Estimation of the relative amount of the Flower buds, flowers, or small fruits. And updating the digital twin about this information. Operator Fruit grower (farmer). Mobile platform (tractor) with cameras system and computer vision is prepared in the orchard. Operator choice the action type. Operator go with tractor at the start of the given row.Camera system read row START ARTag or RFID reader read the row ID. Tractor go in the row - identifying individual trees - making photos of individual trees. Estimating amount of chosen elements by the computer vision method. Sending data to the digital twin or saving to later batch send. START ARTag or RFID is not read in the define time (watch dog) send the message. The trees are not identify by the computer vision send the message. The individual tree is not identify send the message, write in the digital twin and go to next. The time between two trees is longer than define time (watch dog) send the message. Camera system read row END ARTag or RFID reader read the row ID."





print('Věta k rozboru (sentence):',sentence) # a její zobrazení
#nltk.download('punkt') # stažení dat punkt z knivny ntlk. Stačí jednou, potomu už je staženo. Více https://www.nltk.org/data.html
tokens = nltk.word_tokenize(sentence) # tokenizace věty - tedy jej rozdělení na tokeny. Z stringu udělá seznam stringů
print('tokenizovaná věta (tokens): ',tokens) #V zobrazení tokenizované věty
print('druha (indexovno od 0) polozka seznamu tokens:',tokens[2])
#nltk.download('averaged_perceptron_tagger') # stažení averaged_perceptron_tagger z knivny ntlk. Stačí jednou, potomu už je staženo.
tagged = nltk.pos_tag(tokens) # Otaggování (označkování) věty značkamy slovních druhů/členů. Seznam zkratek zde: https://www.guru99.com/pos-tagging-chunking-nltk.html
#IN    preposition
#CD    cardinal digit
#NN    noun, singular (cat, tree)
#NNP   proper noun, singular (sarah)
#BD    verb past tense (pleaded)
#RB    adverb (occasionally, swiftly)
#VB    verb (ask)
#JJ    This NLTK POS Tag is an adjective (large)
print('otaggovaná věta (tagged): ',tagged)
print('položka otaggované věty (tagged): ',tagged[2])

from nltk.tokenize import sent_tokenize
senteces = nltk.word_tokenize(sentence)
print('tokenizace vět (senteces): ', senteces)

import numpy #knihovnu numpy je potřeba nainstalovat pro nltk.chunk.ne_chunk
#nltk.download('maxent_ne_chunker') # stažení dat maxent_ne_chunker z knivny ntlk
#nltk.download('words')
entities = nltk.chunk.ne_chunk(tagged)
print('otaggovná věta rozdělená podle části (chunks) po tokenech (entities): ',entities)


#nltk.download('treebank')
#import future
# import tkinter
#from tkinter import IntVar, Menu, Tk
#from nltk.corpus import treebank
#t = treebank.parsed_sents('wsj_0001.mrg')[0]
#t = treebank.parsed_sents(entities)[0]
# t.draw()


selectedtag = tagged[1]
print('delka:',len(tagged))
print('samostatně selectedtag:', selectedtag)
print('samostatně selectedtag[0]:', selectedtag[0])
print('samostatně selectedtag[1]:', selectedtag[1])
print('samostatně entities[0]:', entities[0])
print('samostatně entities[1]:', entities[1])
print('samostatně entities[2]:', entities[2])
print('samostatně entities[3]:', entities[3])


# C L A S S    N A M E S
i = 1
nnlist = []
nnlist_synon = []
selectedtokensynon = ['word', 0]
#nnlist.append ('zacatek')
for i in range(len(tagged)):
    selectedtag = tagged[i]
    selectedtyp = selectedtag[1]
    selectedtoken = selectedtag[0]
    selectedtokensynon[0] = selectedtag[0]
    selectedtokensynon[1] = i
    #   print('pokus:', selectedtyp)
    #   if selectedtyp == ('NN' or 'NNP'):
    if (selectedtyp == 'NN' or selectedtyp == 'NNP' or selectedtyp == 'NNS' or selectedtyp == 'NNPS'):
        nnlist.append (selectedtoken)
        nnlist_synon.append(selectedtokensynon)
print('list (selectedtokensynon): ',selectedtokensynon)
print('list NN (nnlist): ',nnlist)
print('list NN (nnlist_synon): ',nnlist_synon)



# A S O C I A T I O N S   or  O P E R A T I O S
i = 1
vblist = []
#nnlist.append ('zacatek')
for i in range(len(tagged)):
    selectedtag = tagged[i]
    selectedtyp = selectedtag[1]
    selectedtoken = selectedtag[0]
    #  print('pokus:', selectedtyp)
    #   if selectedtyp == ('NN' or 'NNP'):
    if (selectedtyp == 'VB' or selectedtyp == 'BD' or selectedtyp == 'VBN' or selectedtyp == 'VBG'):
        vblist.append (selectedtoken)
print('list VB (vblist): ',vblist)


# A T R I B U T S
i = 0
adjlist = []
#nnlist.append ('zacatek')
for i in range(len(tagged)):
    selectedtag = tagged[i]
    selectedtyp = selectedtag[1]
    selectedtoken = selectedtag[0]
    # print('pokus:', selectedtyp)
    #   if selectedtyp == ('NN' or 'NNP'):
    if (selectedtyp == 'JJ' or selectedtyp == 'CD'):
        adjlist.append (selectedtoken)
print('list ADJ (adjlist): ',adjlist)


# POKUS VNORENY SEZNAM

sezn1D = [1]
sezn1 = [0,0]
sezn2 = [0,0]
sezn2[0] = 1
sezn2[1] = 2
print(sezn1)
print(sezn2)
sezn1.append(sezn2)
print(sezn1)
print(sezn2)
sezn2[1] = 3
sezn2[0] = 4
print(sezn1)
print(sezn2)
sezn1.append(sezn2)
print(sezn1)
print(sezn2)


print(id(sezn1[0]))
print(id(sezn1[1]))
print(id(sezn1[2]))
print(id(sezn1[3]))


# POKUS SLOVNIK
slovnik = {}
slovnik['aa'] = '1'
slovnik['bb'] = '3'
slovnik['cc'] = '1'
slovnik['aa'] = '4'
print(slovnik)
print(slovnik['bb'])
for klic in slovnik:
    print(klic)
for hodnota in slovnik.values():
    print(hodnota)
for klic, hodnota in slovnik.items():
    print('{}: {}'.format(klic, hodnota))
'bb' in slovnik

# C L A S S    N A M E S   SLOVNIK
i = 1

nndict = {}
for i in range(len(tagged)):
    syn = 1
    selectedtag = tagged[i]
    selectedtyp = selectedtag[1]
    selectedtoken = selectedtag[0]
    if (selectedtyp == 'NN' or selectedtyp == 'NNP' or selectedtyp == 'NNS' or selectedtyp == 'NNPS'):
        if (selectedtoken == 'system'):
            selectedtoken = (tagged[i-1][0] + ' system')
            #print (selectedtoken, "system")
        if (selectedtoken in nndict):
            syn = nndict[selectedtoken] + 1
        nndict[selectedtoken] = syn
print('nndict: ',nndict)

for klic, hodnota in nndict.items():
    print('{}: {}'.format(klic, hodnota))


# # A S O C I A T I O N S   or  O P E R A T I O S    SLOVNIK
i = 1

vbdict = {}
for i in range(len(tagged)):
    syn = 1
    selectedtag = tagged[i]
    selectedtyp = selectedtag[1]
    selectedtoken = selectedtag[0]
    if (selectedtyp == 'VB' or selectedtyp == 'BD' or selectedtyp == 'VBN' or selectedtyp == 'VBG'):
        if (selectedtoken == 'system'):
            selectedtoken = (tagged[i-1][0] + ' system')
            #print (selectedtoken, "system")
        if (selectedtoken in vbdict):
            syn = vbdict[selectedtoken] + 1
        vbdict[selectedtoken] = syn
print('vbdict: ',vbdict)

for klic, hodnota in vbdict.items():
    print('{}: {}'.format(klic, hodnota))



# A T R I B U T S   N A M E S     SLOVNIK

adjdict = {}
for i in range(len(tagged)):
    syn = 1
    selectedtag = tagged[i]
    selectedtyp = selectedtag[1]
    selectedtoken = selectedtag[0]
    if (selectedtyp == 'JJ' or selectedtyp == 'CD'):
        if (selectedtoken == 'system'):
            selectedtoken = (tagged[i-1][0] + ' system')
            #print (selectedtoken, "system")
        if (selectedtoken in adjdict):
            syn = adjdict[selectedtoken] + 1
        adjdict[selectedtoken] = syn
print('adjdict: ',adjdict)

for klic, hodnota in adjdict.items():
    print('{}: {}'.format(klic, hodnota))




# C L A S S    N A M E S   SLOVNIK  lemmatizer

# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))
# a denotes adjective in "pos"
print("better :", lemmatizer.lemmatize("better", pos="a"))

i = 1
nndict_stem = {}
for i in range(len(tagged)):
    syn = 1
    selectedtag = tagged[i]
    selectedtyp = selectedtag[1]
    selectedtoken = selectedtag[0]
    selectedtoken = lemmatizer.lemmatize(selectedtoken)
    if (selectedtyp == 'NN' or selectedtyp == 'NNP' or selectedtyp == 'NNS' or selectedtyp == 'NNPS'):
        if (selectedtoken == 'system'):
            selectedtoken = (tagged[i-1][0] + ' system')
            #print (selectedtoken, "system")
        if (selectedtoken in nndict_stem):
            syn = nndict_stem[selectedtoken] + 1
        nndict_stem[selectedtoken] = syn
print('nndict_stem: ',nndict_stem)

for klic, hodnota in nndict_stem.items():
    print('{}: {}'.format(klic, hodnota))




# # A S O C I A T I O N S   or  O P E R A T I O S    SLOVNIK lemmatizer

vbdict_stem = {}
for i in range(len(tagged)):
    syn = 1
    selectedtag = tagged[i]
    selectedtyp = selectedtag[1]
    selectedtoken = selectedtag[0]
    selectedtoken = lemmatizer.lemmatize(selectedtoken, pos="v")
    if (selectedtyp == 'VB' or selectedtyp == 'BD' or selectedtyp == 'VBN' or selectedtyp == 'VBG'):
        if (selectedtoken in vbdict_stem):
            syn = vbdict_stem[selectedtoken] + 1
        vbdict_stem[selectedtoken] = syn
print('vbdict_stem: ',vbdict_stem)

for klic, hodnota in vbdict_stem.items():
    print('{}: {}'.format(klic, hodnota))



# A T R I B U T S   N A M E S     SLOVNIK  lemmatizer

adjdict = {}
for i in range(len(tagged)):
    syn = 1
    selectedtag = tagged[i]
    selectedtyp = selectedtag[1]
    selectedtoken = selectedtag[0]
    selectedtoken = lemmatizer.lemmatize(selectedtoken, pos="a")
    if (selectedtyp == 'JJ' or selectedtyp == 'CD'):
        if (selectedtoken == 'system'):
            selectedtoken = (tagged[i-1][0] + ' system')
            #print (selectedtoken, "system")
        if (selectedtoken in adjdict):
            syn = adjdict[selectedtoken] + 1
        adjdict[selectedtoken] = syn
print('adjdict: ',adjdict)

for klic, hodnota in adjdict.items():
    print('{}: {}'.format(klic, hodnota))