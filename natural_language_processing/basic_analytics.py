"""
NLTK introduction

Tags:
- IN    preposition
- CD    cardinal digit
- NN    noun, singular (cat, tree)
- NNP   proper noun, singular (sarah)
- BD    verb past tense (pleaded)
- RB    adverb (occasionally, swiftly)
- VB    verb (ask)
- JJ    This NLTK POS Tag is an adjective (large)
"""
import nltk

### Input
input_data = "The concept also aims to reduce the need for human labor, save inputs and increase production efficiency. The basis of the project will be in the selection of suitable varieties of the apple tree and the selection of apple genotypes, which will meet the requirements for the new conception and meet the fruit quality, storage, and required organoleptic parameters of apples, in order to register a new variety. An experimental and demonstration orchard will be established, as well as a small-scale experimental orchard. Container planting for laboratory tests will also be established. With regard to the deployment of robotic platforms, the newly designed support structure of the orchard will be implemented. The interaction between mechanical interventions and the condition of trees will be monitored throughout the project. These indicators will be important for the choice of terms of intervention, the intensity of intervention, but also for the selection of suitable shapes or materials used on mechanical parts of machines that come into direct contact with trees. Based on our findings, the structural elements will always be innovated. During the vegetation period, trees will be monitored at regular intervals using distance measurement methods to determine tree height, growth, green condition, health status, flower stocking intensity, fruit ripening, fruit stocking, and overall orchard variability. The data will be compared with the measurement of tree parameters during vegetation. All data will be compared with data from systematically distributed IoT sensors in the soil to measure temperature and water availability. The project will develop a harvesting head connected to a handling arm designed for autonomous fruit harvesting. The treetop shape of apple trees will allow us to create a completely different concept of robotic harvesting. The robotic harvesting head and manipulator will be developed. An important element of the design will be the requirement to treat apples with care. The risk of damage will be considered with regard to the shape and kinematics of the working parts of the harvesting head and the material used. The manipulation arm will be a tool for precise guidance of the head to the apple trunk and subsequent movement of the harvesting head in the axis of the terminal bud. Sensor technology will be used to detect the trunk, guide the harvesting head, and limit the contact of the harvesting head or arm with the apple tree trunk. The created structural units will be verified on the experimental plantings and subsequently installed on a towing device for testing in real operation. During the harvest, the apple damage, yield, and quality of production at the level of individual trees will be monitored. Algorithms for the detection of the trunk, guide structure, and new leaves will be developed for precise guidance of mechanical parts of the manipulator working in an orchard. A cloud environment will be ready for calculations and remote access to platform data. This will allow all work to be planned in advance and transferred to the robotic platform. It will be possible to change the parameters operatively during the work. Computational capacity will also be used to evaluate the collected data, including the storage of application data. A proposal will be made for the implementation of a sensor network and computing and communication infrastructure for advanced computing and a software interface for its use. The individual work procedures were compiled in such a way that they logically follow each other and complement each other. Digital twin set - each tree will have a digital twin, where it will be recorded how it was treated - spraying, cutting, fertilization, harvest and at the same time will be stored biological data obtained by passing a tractor with navigation - measured trunk parameters, harvest maturity evaluation, quantity, size and color of fruits, flowers and buds. Including selected photos and data obtained from the machine vision methods from those photos and videos.  In the orchard the columnar apple trees are planted. The tractor with the harvesting head (or e.g. sprayer) is equipped with a camera system and many sensors for its own navigation. These sensors are part of the sensory system. The temperature, air humidity, and soil humidity sensors are installed in the orchard for support of the intervention schedule. Sensors are connected into an IoT network. Identification of the given orchard row is realized by the ARTags (or RFID - radio frequency identification). Reading ARTags is realized by the camera with computer vision system and RFID by the RFID reader. The tree identification and position are realized by the computer vision system (which identifies the trunk primarily) with the support of ultrasound sensors and GPS (Global Positioning System) navigation of the tractor. Computer vision is based on the camera, deep camera, and lidar data. Control system consists of many distributed units for each task and domain. The harvesting robotic head at the mobile platform has its control unit. Computer vision system for identification of tree trunk has separated, more powerful, computing unit. Also, human operators are supposed to control selected facilities like a tractor. Data from the sensory system are collected into the database for online control and dispatching. Selected camera images are sent to the database too. A selected image means a photo of each tree made during the treatment. These photos are also complemented by the additional information (state, health, rate of buds or flowers, and of course the date, time, temperature, air humidity) if it is possible. Each tree is identified by the row and position in the row. The model of the orchard with corresponding tags is part of the digital twin. This data are visualized for easier understanding. The Agricultural information system (or Farming Management System FMS) is based on the digital twin of the orchard. A digital twin is a model of the orchard which is continuously replenished by the information about individual trees. This is information about treatment like a watering, spraying, fertilization, or harvesting. About estimation of the flower buds, flowers, and small fruits amount estimation. The computation part of the digital twin contains yield and fruit maturity estimator and treatment scheduler. This level is not defined in this project. Flower buds or flowers or small fruits amount estimation. Estimation of the relative amount of the Flower buds, flowers, or small fruits. And updating the digital twin about this information. Operator Fruit grower (farmer). Mobile platform (tractor) with cameras system and computer vision is prepared in the orchard. Operator choice the action type. Operator go with tractor at the start of the given row.Camera system read row START ARTag or RFID reader read the row ID. Tractor go in the row - identifying individual trees - making photos of individual trees. Estimating amount of chosen elements by the computer vision method. Sending data to the digital twin or saving to later batch send. START ARTag or RFID is not read in the define time (watch dog) send the message. The trees are not identify by the computer vision send the message. The individual tree is not identify send the message, write in the digital twin and go to next. The time between two trees is longer than define time (watch dog) send the message. Camera system read row END ARTag or RFID reader read the row ID."

groups = {
    "noun": ["NN", "NNP", "NNS", "NNPS"],
    "verbs": ["VB", "BD", "VBN", "VBG"],
    "attributes": ["JJ", "CD"]
}

### Process
tokens = nltk.word_tokenize(input_data)
tags = nltk.pos_tag(tokens)
entities = nltk.chunk.ne_chunk(tags) # TODO what is that?

lemmatizer = nltk.stem.WordNetLemmatizer()
roots = list(set([lemmatizer.lemmatize(token) for token in tokens]))

stemmer = nltk.stem.PorterStemmer()
stems = list(set([stemmer.stem(token) for token in tokens]))

grouped_tokens = {}
for group in groups:
    grouped_tokens[group] = [token for token, tag in tags if tag in groups[group]]

### Report
print("Tokens (count: {}):".format(len(tokens)))
print(tokens)
print("")

print("Tags (tagged tokens):")
print(tags)
print("")

print("Word roots (product of lemmatization, count: {}):".format(len(roots)))
print(roots)
print("")

print("Word stems (product of stemming, count: {}):".format(len(stems)))
print(stems)
print("")

print("Tokens by custom groups:")
for group, tokens in grouped_tokens.items():
    print("-", group)
    print("", tokens)
