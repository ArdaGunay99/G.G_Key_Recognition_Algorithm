import csv
import matplotlib.pyplot as plt
import numpy as num
from hmmlearn import hmm

# This function takes the file location and converts it into a matrix.
def CsvIntoMatrix(fileLocation):
    c = num.array([])
    cSharp = num.array([])
    d = num.array([])
    dSharp = num.array([])
    e = num.array([])
    f = num.array([])
    fSharp = num.array([])
    g = num.array([])
    gSharp = num.array([])
    a = num.array([])
    aSharp = num.array([])
    b = num.array([])

    with open(fileLocation, encoding="Latin-1") as z:
        csv_list = list(csv.reader(z))
    for row in csv_list:
        if row != csv_list[0]:
            c = num.append(c, float(row[1]))
            cSharp = num.append(cSharp, float(row[2]))
            d = num.append(d, float(row[3]))
            dSharp = num.append(dSharp, float(row[4]))
            e = num.append(e, float(row[5]))
            f = num.append(f, float(row[6]))
            fSharp = num.append(fSharp, float(row[7]))
            g = num.append(g, float(row[8]))
            gSharp = num.append(gSharp, float(row[9]))
            a = num.append(a, float(row[10]))
            aSharp = num.append(aSharp, float(row[11]))
            b = num.append(b, float(row[12]))
    matrix = num.vstack((c, cSharp, d, dSharp, e, f, fSharp, g, gSharp, a, aSharp, b))
    matrix = matrix.transpose()
    return matrix

# This function takes a file location and converts it into an array.
def TruthIntoArray(fileLocation):
    truth = num.array([])
    with open(fileLocation, encoding="Latin-1") as z:
        csv_list = list(csv.reader(z))
    for row in csv_list:
        if row != csv_list[0]:
            truth = num.append(truth, int(row[1]))
    return truth


# These are our observation matrices and ground truth arrays. Each row in a matrix holds the observation values of a measure.
# The current measure's key represents the value of the current state in our model. There is a total of 24 different state values. We use the transition probability
# matrix with our previous state to calculate the probabilities of the next state's value.
# We use the Emission matrix on our observation to determine the value of the current state with respect to the probabilities acquired from the transition probabilities mentioned above.
# An observation holds a value for each of the 12 notes. This value may refer to the note's presence, duration or occurrence in that measure.
# If a note does not exists in that observation, its value will be zero in all three cases mentioned above.
# Truth arrays will be used to calculate our model's accuracy.
barbiePresence = CsvIntoMatrix("./BarbieGirlPresence.csv")
barbieOccurrence = CsvIntoMatrix("./BarbieGirlOccurrence.csv")
barbieDuration = CsvIntoMatrix("./BarbieGirlDuration.csv")
barbieTruth = TruthIntoArray("./BarbieGirlTruth.csv")

japanPresence = CsvIntoMatrix("./BigInJapanPresence.csv")
japanOccurrence = CsvIntoMatrix("./BigInJapanOccurrence.csv")
japanDuration = CsvIntoMatrix("./BigInJapanDuration.csv")
japanTruth = TruthIntoArray("./BigInJapanTruth.csv")

chiquititaPresence = CsvIntoMatrix("./ChiquititaPresence.csv")
chiquititaOccurrence = CsvIntoMatrix("./ChiquititaOccurrence.csv")
chiquititaDuration = CsvIntoMatrix("./ChiquititaDuration.csv")
chiquititaTruth = TruthIntoArray("./ChiquititaTruth.csv")

crazyPresence = CsvIntoMatrix("./CrazyPresence.csv")
crazyOccurrence = CsvIntoMatrix("./CrazyOccurrence.csv")
crazyDuration = CsvIntoMatrix("./CrazyDuration.csv")
crazyTruth = TruthIntoArray("./CrazyTruth.csv")

dancingQueenPresence = CsvIntoMatrix("./DancingQueenPresence.csv")
dancingQueenOccurrence = CsvIntoMatrix("./DancingQueenOccurrence.csv")
dancingQueenDuration = CsvIntoMatrix("./DancingQueenDuration.csv")
dancingQueenTruth = TruthIntoArray("./DancingQueenTruth.csv")

fortunaPresence = CsvIntoMatrix("./FortunaPresence.csv")
fortunaOccurrence = CsvIntoMatrix("./FortunaOccurrence.csv")
fortunaDuration = CsvIntoMatrix("./FortunaDuration.csv")
fortunaTruth = TruthIntoArray("./FortunaTruth.csv")

godzillaPresence = CsvIntoMatrix("./GodzillaPresence.csv")
godzillaOccurrence = CsvIntoMatrix("./GodzillaOccurrence.csv")
godzillaDuration = CsvIntoMatrix("./GodzillaDuration.csv")
godzillaTruth = TruthIntoArray("./GodzillaTruth.csv")

deepPresence = CsvIntoMatrix("./HowDeepIsYourLovePresence.csv")
deepOccurrence = CsvIntoMatrix("./HowDeepIsYourLoveOccurrence.csv")
deepDuration = CsvIntoMatrix("./HowDeepIsYourLoveDuration.csv")
deepTruth = TruthIntoArray("./HowDeepIsYourLoveTruth.csv")

newWorldSymphonyPresence = CsvIntoMatrix("./NewWorldSymphonyPresence.csv")
newWorldSymphonyOccurrence = CsvIntoMatrix("./NewWorldSymphonyOccurrence.csv")
newWorldSymphonyDuration = CsvIntoMatrix("./NewWorldSymphonyDuration.csv")
newWorldSymphonyTruth = TruthIntoArray("./NewWorldSymphonyTruth.csv")

oneDayPresence = CsvIntoMatrix("./OneDayInYourLifePresence.csv")
oneDayOccurrence = CsvIntoMatrix("./OneDayInYourLifeOccurrence.csv")
oneDayDuration = CsvIntoMatrix("./OneDayInYourLifeDuration.csv")
oneDayTruth = TruthIntoArray("./OneDayInYourLifeTruth.csv")

polovtsianPresence = CsvIntoMatrix("./PolovtsianDancePresence.csv")
polovtsianOccurrence = CsvIntoMatrix("./PolovtsianDanceOccurrence.csv")
polovtsianDuration = CsvIntoMatrix("./PolovtsianDanceDuration.csv")
polovtsianTruth = TruthIntoArray("./PolovtsianDanceTruth.csv")

potoPresence = CsvIntoMatrix("./PotOPresence.csv")
potoOccurrence = CsvIntoMatrix("./PotOOccurrence.csv")
potoDuration = CsvIntoMatrix("./PotODuration.csv")
potoTruth = TruthIntoArray("./PotOTruth.csv")

ppfcPresence = CsvIntoMatrix("./PPfCPresence.csv")
ppfcOccurrence = CsvIntoMatrix("./PPfCOccurrence.csv")
ppfcDuration = CsvIntoMatrix("./PPfCDuration.csv")
ppfcTruth = TruthIntoArray("./PPfCTruth.csv")

song2Presence = CsvIntoMatrix("./Song2Presence.csv")
song2Occurrence = CsvIntoMatrix("./Song2Occurrence.csv")
song2Duration = CsvIntoMatrix("./Song2Duration.csv")
song2Truth = TruthIntoArray("./Song2Truth.csv")

stayinAlivePresence = CsvIntoMatrix("./StayinAlivePresence.csv")
stayinAliveOccurrence = CsvIntoMatrix("./StayinAliveOccurrence.csv")
stayinAliveDuration = CsvIntoMatrix("./StayinAliveDuration.csv")
stayinAliveTruth = TruthIntoArray("./StayinAliveTruth.csv")

tmbaPresence = CsvIntoMatrix("./TMBAPresence.csv")
tmbaOccurrence = CsvIntoMatrix("./TMBAOccurrence.csv")
tmbaDuration = CsvIntoMatrix("./TMBADuration.csv")
tmbaTruth = TruthIntoArray("./TMBATruth.csv")

# creating the key profile matrix proposed by Krumhansl and Kessler
KK_C_Major_Profile = num.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
c_sharp = num.roll(KK_C_Major_Profile, 1)
d = num.roll(KK_C_Major_Profile, 2)
d_sharp = num.roll(KK_C_Major_Profile, 3)
e = num.roll(KK_C_Major_Profile, 4)
f = num.roll(KK_C_Major_Profile, 5)
f_sharp = num.roll(KK_C_Major_Profile, 6)
g = num.roll(KK_C_Major_Profile, 7)
g_sharp = num.roll(KK_C_Major_Profile, 8)
a = num.roll(KK_C_Major_Profile, 9)
a_sharp = num.roll(KK_C_Major_Profile, 10)
b = num.roll(KK_C_Major_Profile, 11)
Key_profile_matrix = num.vstack((KK_C_Major_Profile, c_sharp, d, d_sharp, e, f, f_sharp, g, g_sharp, a, a_sharp, b))

KK_C_Minor_Profile = num.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])
c_sharp = num.roll(KK_C_Minor_Profile, 1)
d = num.roll(KK_C_Minor_Profile, 2)
d_sharp = num.roll(KK_C_Minor_Profile, 3)
e = num.roll(KK_C_Minor_Profile, 4)
f = num.roll(KK_C_Minor_Profile, 5)
f_sharp = num.roll(KK_C_Minor_Profile, 6)
g = num.roll(KK_C_Minor_Profile, 7)
g_sharp = num.roll(KK_C_Minor_Profile, 8)
a = num.roll(KK_C_Minor_Profile, 9)
a_sharp = num.roll(KK_C_Minor_Profile, 10)
b = num.roll(KK_C_Minor_Profile, 11)

# this is our emission matrix which will be used on our observations
Key_profile_matrix = num.vstack(
    (Key_profile_matrix, KK_C_Minor_Profile, c_sharp, d, d_sharp, e, f, f_sharp, g, g_sharp, a, a_sharp, b))

# these will be used for validating our results
lookupVector_same = num.array([0, 0.83, 0.33, 0.5, 0.67, 0.17, 1, 0.17, 0.67, 0.5, 0.33, 0.83])
lookupVector_different = num.array([0.58, 0.58, 0.25, 0.92, 0.08, 0.75, 0.42, 0.42, 0.75, 0.08, 0.92, 0.25])


def nextRow(previousRow):
    next_row = num.array([])
    for i in range(0, len(previousRow)):
        if i == 0:
            next_row = num.append(next_row, float(previousRow[11]))
        elif i == 12:
            next_row = num.append(next_row, float(previousRow[23]))
        else:
            next_row = num.append(next_row, float(previousRow[i - 1]))
    return next_row


# these are major rows of transition probability matrix these will be used to construct the transition probability distribution matrix
C = num.array([0.9, 0.000009, 0.0009, 0.0009, 0.00009, 0.09, 0.000000009, 0.09, 0.00009, 0.0009, 0.0009, 0.000009, 0.09,
               0.00000009, 0.009, 0.0000009, 0.009, 0.009, 0.0000009, 0.009, 0.00000009, 0.09, 0.00009, 0.00009])
Cs = num.array(
    [0.000009, 0.9, 0.000009, 0.0009, 0.0009, 0.00009, 0.09, 0.000000009, 0.09, 0.00009, 0.0009, 0.0009, 0.00009, 0.09,
     0.00000009, 0.009, 0.0000009, 0.009, 0.009, 0.0000009, 0.009, 0.00000009, 0.09, 0.00009])
D = num.array(
    [0.0009, 0.000009, 0.9, 0.000009, 0.0009, 0.0009, 0.00009, 0.09, 0.000000009, 0.09, 0.00009, 0.0009, 0.00009,
     0.00009, 0.09, 0.00000009, 0.09, 0.0000009, 0.009, 0.009, 0.0000009, 0.009, 0.00000009, 0.09])
Ds = num.array(
    [0.0009, 0.0009, 0.000009, 0.9, 0.000009, 0.0009, 0.0009, 0.00009, 0.09, 0.000000009, 0.09, 0.00009, 0.09, 0.00009,
     0.00009, 0.09, 0.00000009, 0.09, 0.0000009, 0.009, 0.009, 0.0000009, 0.009, 0.00000009])
E = num.array(
    [0.00009, 0.0009, 0.0009, 0.000009, 0.9, 0.000009, 0.0009, 0.0009, 0.00009, 0.09, 0.000000009, 0.09, 0.00000009,
     0.09, 0.00009, 0.00009, 0.09, 0.00000009, 0.09, 0.0000009, 0.009, 0.009, 0.0000009, 0.009])
F = num.array(
    [0.09, 0.00009, 0.0009, 0.0009, 0.000009, 0.9, 0.000009, 0.0009, 0.0009, 0.00009, 0.09, 0.000000009, 0.009,
     0.00000009, 0.09, 0.00009, 0.00009, 0.09, 0.00000009, 0.09, 0.0000009, 0.009, 0.009, 0.0000009])
Fs = num.array(
    [0.000000009, 0.09, 0.00009, 0.0009, 0.0009, 0.000009, 0.9, 0.000009, 0.0009, 0.0009, 0.00009, 0.09, 0.0000009,
     0.009, 0.00000009, 0.09, 0.00009, 0.00009, 0.09, 0.00000009, 0.09, 0.0000009, 0.009, 0.009])
G = nextRow(Fs)
Gs = nextRow(G)
A = nextRow(Gs)
As = nextRow(A)
B = nextRow(As)
# these are minor rows of transition probability matrix, these will be used to construct the transition probability distribution matrix
c = num.array(
    [0.09, 0.00009, 0.00009, 0.09, 0.00000009, 0.009, 0.0000009, 0.009, 0.009, 0.0000009, 0.009, 0.00000009, 0.9,
     0.000009, 0.0009, 0.0009, 0.00009, 0.09, 0.000000009, 0.09, 0.00009, 0.0009, 0.0009, 0.000009])
cs = nextRow(c)
d = nextRow(cs)
ds = nextRow(d)
e = nextRow(ds)
f = nextRow(e)
fs = nextRow(f)
g = nextRow(fs)
gs = nextRow(g)
a = nextRow(gs)
ash = nextRow(a)  # a sharp minor
b = nextRow(ash)

#this is our transition probability distributions of size (24,24)
transition_probability_matrix = num.vstack(
    (C, Cs, D, Ds, E, F, Fs, G, Gs, A, As, B, c, cs, d, ds, e, f, fs, g, gs, a, ash, b))
#print(transition_probability_matrix)
#print(num.shape(transition_probability_matrix))
initial_state_probs=num.array([])
states=num.array([])
for i in range(24):
    states=num.append(states,i)
observation_symbols=num.array([])
for i in range(12):
    observation_symbols=num.append(observation_symbols,i)
for i in range(24):
    initial_state_probs=num.append(initial_state_probs,1/24);


class viterbiAlgorithm():
    _transitionMatrix="" #transition_probability_matrix,taken from Arda's calculations
    _emissionMatrix="" #Key_profile_matrix, taken from the key probability matrix of pre determined data
    _observationMatrix="" #observation_symbols,12 pitch classes reduced to int
    _initial_state_probs="" #initial state probs,1/24 for each variable
    _states="" #24 states for each of the 24 musical keys reduced to int
    
    def initialStateProbs(self):
        for i in range(24):
            self._initial_state_probs=num.append(self._initial_state_probs,1/24)
    def states(self):
        for i in range(24):
            self._states=num.append(self._states,i)
    def observationMatrix(self):
        for i in range(12):
            self._observationMatrix=num.append(self._observationMatrix,i)
    def setObservationMatrix(self,observationMatrix):
        self._observationMatrix=observationMatrix
    def __init__(self,transitionMatrix,emissionMatrix,observationMatrix,states,initialStateProbs):
        self._transitionMatrix=transitionMatrix
        self._emissionMatrix=emissionMatrix
        self._observationMatrix=observationMatrix
        self._states=states
        self._initial_state_probs=initialStateProbs
    #this is the implementation that I have made by keeping our algorithm in mind
    #this worked for my inputs,but I don't know about the array inputs for our project
    #fix the issues with arrays and we will figure out the next step from there
    def runAlgorithm(self):
        result=[{}]
        for st in self._states:
            result[0][st]={"prob":self._initial_state_probs[st]*self._transitionMatrix[st][self._observationMatrix[0]],"prev":None}
        for t in range(1,len(self._observationMatrix)):
            result.append({})
            for state in self._states:
                max_tr_prob=result[t-1][self._states[0]]["prob"]*self._transitionMatrix[self._states[0]][state]
                prev_state_selected=self._states[0]
                for prev_st in self._states[1:]:
                    tr_prob=result[t-1][prev_st]["prob"]*self._transitionMatrix[prev_st][state]
                    if tr_prob>max_tr_prob:
                        max_tr_prob=tr_prob
                        prev_state_selected=prev_st
                max_prob=max_tr_prob*self._emissionMatrix[state][self._observationMatrix[t]]
                result[t][state]={"prob":max_prob,"prev":prev_state_selected}
        opt=[]
        max_prob=0.0
        best_st=None
        for state,data in result[-1].items():
            if data["prob"] > max_prob:
                max_prob=data["prob"]
                best_st=state
        opt.append(best_st)
        previous=best_st
    
    
#this is abstract and does not work right now
class viterbi:
    def viterbi (self,observations):
        # A - initialise stuff
        nSamples = len(observations[0])
        nStates = self.transition.shape[0] # number of states
        c = num.zeros(nSamples) #scale factors (necessary to prevent underflow)
        viterbi = num.zeros((nStates,nSamples)) # initialise viterbi table
        psi = num.zeros((nStates,nSamples)) # initialise the best path table
        best_path = num.zeros(nSamples); # this will be your output

        # B- appoint initial values for viterbi and best path (bp) tables - Eq (32a-32b)
        viterbi[:,0] = self.priors.T * self.emission[:,observations(0)]
        c[0] = 1.0/num.sum(viterbi[:,0])
        viterbi[:,0] = c[0] * viterbi[:,0] # apply the scaling factor
        psi[0] = 0;

    # C- Do the iterations for viterbi and psi for time>0 until T
        for t in range(1,nSamples): # loop through time
            for s in range (0,nStates): # loop through the states @(t-1)
                trans_p = viterbi[:,t-1] * self.transition[:,s]
                psi[s,t], viterbi[s,t] = max(enumerate(trans_p), key=operator.itemgetter(1))
                viterbi[s,t] = viterbi[s,t]*self.emission[s,observations(t)]

            c[t] = 1.0/num.sum(viterbi[:,t]) # scaling factor
            viterbi[:,t] = c[t] * viterbi[:,t]

        # D - Back-tracking
        best_path[nSamples-1] =  viterbi[:,nSamples-1].argmax() # last state
        for t in range(nSamples-1,0,-1): # states of (last-1)th to 0th time step
            best_path[t-1] = psi[best_path[t],t]
        print(best_path)
        
        
        
         


#viterbi=viterbiAlgorithm(trans_p,emit_p,obs,states,start_p)
#viterbi.runAlgorithm()



