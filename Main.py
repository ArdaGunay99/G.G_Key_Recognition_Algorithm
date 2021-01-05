import csv
import matplotlib.pyplot as plt
import numpy as num
from typing import List, Optional, Tuple
import xlsxwriter
import re


   
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


# This function is used to create the transition probability distribution matrix
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


# this function is used to change the transitio probability arrays of C major and C minor
def changeTransitionArray(arr, _all):
    temp = arr
    for i in range(len(temp)):
        if temp[i] == 0.9:
            temp[i] = _all[0]
        elif temp[i] == 0.09:
            temp[i] = _all[1]
        elif temp[i] == 0.009:
            temp[i] = _all[2]
        elif temp[i] == 0.0009:
            temp[i] = _all[3]
        elif temp[i] == 0.00009:
            temp[i] = _all[4]
        elif temp[i] == 0.000009:
            temp[i] = _all[5]
        elif temp[i] == 0.0000009:
            temp[i] = _all[6]
        elif temp[i] == 0.00000009:
            temp[i] = _all[7]
        elif temp[i] == 0.000000009:
            temp[i] = _all[8]
    return temp


# this function creates our transition probability distributions matrix of size (24,24) and with the given ratio
def createTransitionMatrix(ratio):
    _next = ratio
    _all = num.array([ratio])
    for i in range(8):
        _next = _next / ratio
        _all = num.append(_all, _next)
    _sum = sum(_all)
    for i in range(len(_all)):
        _all[i] = _all[i] / _sum
    cMaj = num.array(
        [0.9, 0.000009, 0.0009, 0.0009, 0.00009, 0.09, 0.000000009, 0.09, 0.00009, 0.0009, 0.0009, 0.000009, 0.09,
         0.00000009, 0.009, 0.0000009, 0.009, 0.009, 0.0000009, 0.009, 0.00000009, 0.09, 0.00009, 0.00009])
    cMin = num.array(
        [0.09, 0.00009, 0.00009, 0.09, 0.00000009, 0.009, 0.0000009, 0.009, 0.009, 0.0000009, 0.009, 0.00000009, 0.9,
         0.000009, 0.0009, 0.0009, 0.00009, 0.09, 0.000000009, 0.09, 0.00009, 0.0009, 0.0009, 0.000009])
    # these are major rows of transition probability matrix these will be used
    # to construct the transition probability distribution matrix
    cMaj = changeTransitionArray(cMaj, _all)
    Cs = nextRow(cMaj)
    D = nextRow(Cs)
    Ds = nextRow(D)
    E = nextRow(Ds)
    F = nextRow(E)
    Fs = nextRow(F)
    G = nextRow(Fs)
    Gs = nextRow(G)
    A = nextRow(Gs)
    As = nextRow(A)
    B = nextRow(As)

    # these are minor rows of transition probability matrix
    cMin = changeTransitionArray(cMin, _all)
    cs = nextRow(cMin)
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

    transition_probability_matrix = num.vstack(
        (cMaj, Cs, D, Ds, E, F, Fs, G, Gs, A, As, B, cMin, cs, d, ds, e, f, fs, g, gs, a, ash, b))

    return transition_probability_matrix


# this is our Key profile matrix which will be used on our observations to create our emission probability matrix
# This function will create the key profile matrix from its C major and c minor rows
def createKeyProfileMatrix(cMajor, cMinor):
    c_sharp = num.roll(cMajor, 1)
    d = num.roll(cMajor, 2)
    d_sharp = num.roll(cMajor, 3)
    e = num.roll(cMajor, 4)
    f = num.roll(cMajor, 5)
    f_sharp = num.roll(cMajor, 6)
    g = num.roll(cMajor, 7)
    g_sharp = num.roll(cMajor, 8)
    a = num.roll(cMajor, 9)
    a_sharp = num.roll(cMajor, 10)
    b = num.roll(cMajor, 11)
    Key_profile_matrix = num.vstack((cMajor, c_sharp, d, d_sharp, e, f, f_sharp, g, g_sharp, a, a_sharp, b))

    c_sharp = num.roll(cMinor, 1)
    d = num.roll(cMinor, 2)
    d_sharp = num.roll(cMinor, 3)
    e = num.roll(cMinor, 4)
    f = num.roll(cMinor, 5)
    f_sharp = num.roll(cMinor, 6)
    g = num.roll(cMinor, 7)
    g_sharp = num.roll(cMinor, 8)
    a = num.roll(cMinor, 9)
    a_sharp = num.roll(cMinor, 10)
    b = num.roll(cMinor, 11)
    Key_profile_matrix = num.vstack(
        (Key_profile_matrix, cMinor, c_sharp, d, d_sharp, e, f, f_sharp, g, g_sharp, a, a_sharp, b))
    return Key_profile_matrix


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
KK_C_Major_Profile = num.array([0.15195022732711172, 0.0533620483369227, 0.08327351040918879,
                                0.05575496530270399, 0.10480976310122037, 0.09787030390045463,
                                0.06030150753768843, 0.1241923905240488, 0.05719071548217276,
                                0.08758076094759511, 0.05479779851639147, 0.06891600861450106])
KK_C_Minor_Profile = num.array([0.14221523253201526, 0.06021118849696697, 0.07908335205571781,
                                0.12087171422152324, 0.05841383958660975, 0.07930802066951245,
                                0.05706582790384183, 0.1067175915524601, 0.08941810829027184,
                                0.06043585711076162, 0.07503931700741405, 0.07121995057290496])

Aarden_Essen_C_Major_Profile = num.array([0.17766092893562843, 0.001456239417504233, 0.1492649402940239,
                                          0.0016018593592562562, 0.19804892078043168, 0.11358695456521818,
                                          0.002912478835008466, 0.2206199117520353, 0.001456239417504233,
                                          0.08154936738025305, 0.002329979068008373, 0.049512180195127924])
Aarden_Essen_C_Minor_Profile = num.array([0.18264800547944018, 0.007376190221285707, 0.14049900421497014,
                                          0.16859900505797015, 0.0070249402107482066, 0.14436200433086013,
                                          0.0070249402107482066, 0.18616100558483017, 0.04566210136986304,
                                          0.019318600579558018, 0.07376190221285707, 0.017562300526869017])

Bellman_Budge_C_Major_Profile = num.array([0.168, 0.0086, 0.1295, 0.0141, 0.1349, 0.1193,
                                           0.0125, 0.2028, 0.018000000000000002, 0.0804, 0.0062, 0.1057])
Bellman_Budge_C_Minor_Profile = num.array([0.1816, 0.0069, 0.12990000000000002,
                                           0.1334, 0.010700000000000001, 0.1115,
                                           0.0138, 0.2107, 0.07490000000000001,
                                           0.015300000000000001, 0.0092, 0.10210000000000001])

Sapp_C_Major_Profile = num.array([0.2222222222222222, 0.0, 0.1111111111111111, 0.0,
                                  0.1111111111111111, 0.1111111111111111, 0.0, 0.2222222222222222,
                                  0.0, 0.1111111111111111, 0.0, 0.1111111111111111])
Sapp_C_Minor_Profile = num.array([0.2222222222222222, 0.0, 0.1111111111111111, 0.1111111111111111,
                                  0.0, 0.1111111111111111, 0.0, 0.2222222222222222,
                                  0.1111111111111111, 0.0, 0.05555555555555555, 0.05555555555555555])

Temperley_C_Major_Profile = num.array([0.17616580310880825, 0.014130946773433817, 0.11493170042392838,
                                       0.019312293923692884, 0.15779557230334432, 0.10833725859632594,
                                       0.02260951483749411, 0.16839378238341965, 0.02449364107395195,
                                       0.08619877531794629, 0.013424399434762127, 0.09420631182289213])
Temperley_C_Minor_Profile = num.array([0.1702127659574468, 0.020081281377002155, 0.1133158020559407,
                                       0.14774085584508725, 0.011714080803251255, 0.10996892182644036,
                                       0.02510160172125269, 0.1785799665311977, 0.09658140090843893,
                                       0.016017212526894576, 0.03179536218025341, 0.07889074826679417])

Albrecht_Shanahan_C_Major_Profile = num.array([0.238, 0.006, 0.111, 0.006, 0.137, 0.094,
                                               0.016, 0.214, 0.009, 0.080, 0.008, 0.081])
Albrecht_Shanahan_C_Minor_Profile = num.array([0.220, 0.006, 0.104, 0.123, 0.019, 0.103,
                                               0.012, 0.214, 0.062, 0.022, 0.061, 0.052])

Albrecht_Shanahan2_C_Major_Profile = num.array([0.21169, 0.00892766, 0.120448, 0.0100265, 0.131444, 0.0911768,
                                                0.0215947, 0.204703, 0.012894, 0.0900445, 0.012617, 0.0844338])
Albrecht_Shanahan2_C_Minor_Profile = num.array([0.201933, 0.009335, 0.107284, 0.124169, 0.0199224, 0.108324,
                                                0.014314, 0.202699, 0.0653907, 0.0252515, 0.071959, 0.049419])

Temperley_Sapp_C_Major_Profile = num.array([0.17616580310880825, 0.014130946773433817, 0.11493170042392838,
                                            0.019312293923692884, 0.15779557230334432, 0.10833725859632594,
                                            0.02260951483749411, 0.17329251059821005, 0.01959491285916156,
                                            0.08619877531794629, 0.013424399434762127, 0.09420631182289213])
Temperley_Sapp_C_Minor_Profile = num.array([0.2222222222222222, 0.0, 0.1111111111111111, 0.12222222222222222,
                                            0.0, 0.1111111111111111, 0.008888888888888889, 0.2222222222222222,
                                            0.1111111111111111, 0.0, 0.05555555555555555, 0.03555555555555555])

Napoles6_C_Major_Profile = num.array([0.13675520459440055, 0.0533620483369227, 0.08327351040918879,
                                      0.05575496530270399, 0.12000478583393154, 0.09787030390045463,
                                      0.06030150753768843, 0.1241923905240488, 0.05719071548217276,
                                      0.08758076094759511, 0.05479779851639147, 0.06891600861450106])
Napoles6_C_Minor_Profile = num.array([0.14221523253201526, 0.06021118849696697, 0.07908335205571781,
                                      0.12087171422152324, 0.05841383958660975, 0.07930802066951245,
                                      0.05706582790384183, 0.1067175915524601, 0.08941810829027184,
                                      0.06043585711076162, 0.07503931700741405, 0.07121995057290496])

Napoles128_C_Major_Profile = num.array([0.136755204594401, 0.065608997367791, 0.074946159368270,
                                        0.050179468772434, 0.100358937544867, 0.103445800430725,
                                        0.054271356783920, 0.139387413256760, 0.060904522613065,
                                        0.087580760947595, 0.049318018664752, 0.077243359655420])
Napoles128_C_Minor_Profile = num.array([0.148236351381712, 0.048771062682543, 0.079083352055718,
                                        0.120871714221523, 0.047315210065154, 0.079308020669512,
                                        0.068950797573579, 0.096045832397214, 0.101959110312289,
                                        0.059649516962480, 0.085711076162660, 0.064097955515614])
# simple natural minor
SNM_Major_Profile = num.array([0.2222222222222222, 0.0, 0.1111111111111111, 0.0,
                               0.1111111111111111, 0.1111111111111111, 0.0, 0.2222222222222222,
                               0.0, 0.1111111111111111, 0.0, 0.1111111111111111])
SNM_Minor_Profile = num.array([0.2222222222222222, 0.0, 0.1111111111111111, 0.1111111111111111,
                               0.0, 0.1111111111111111, 0.0, 0.2222222222222222,
                               0.1111111111111111, 0.0, 0.1111111111111111, 0.0])
# simple harmonic minor
SHM_Major_Profile = num.array([0.2222222222222222, 0.0, 0.1111111111111111, 0.0,
                               0.1111111111111111, 0.1111111111111111, 0.0, 0.2222222222222222,
                               0.0, 0.1111111111111111, 0.0, 0.1111111111111111])
SHM_Minor_Profile = num.array([0.2222222222222222, 0.0, 0.1111111111111111, 0.1111111111111111,
                               0.0, 0.1111111111111111, 0.0, 0.2222222222222222,
                               0.1111111111111111, 0.0, 0.0, 0.1111111111111111])

# simple melodic minor
SMM_Major_Profile = num.array([0.2222222222222222, 0.0, 0.1111111111111111, 0.0,
                               0.1111111111111111, 0.1111111111111111, 0.0, 0.2222222222222222,
                               0.0, 0.1111111111111111, 0.0, 0.1111111111111111])
SMM_Minor_Profile = num.array([0.2222222222222222, 0.0, 0.1111111111111111, 0.1111111111111111,
                               0.0, 0.1111111111111111, 0.0, 0.2222222222222222,
                               0.05555555555555555, 0.05555555555555555, 0.05555555555555555, 0.05555555555555555])

# creating the key profile matrices
KK = createKeyProfileMatrix(KK_C_Major_Profile, KK_C_Minor_Profile)
AE = createKeyProfileMatrix(Aarden_Essen_C_Major_Profile, Aarden_Essen_C_Minor_Profile)
BB = createKeyProfileMatrix(Bellman_Budge_C_Major_Profile, Bellman_Budge_C_Minor_Profile)
S = createKeyProfileMatrix(Sapp_C_Major_Profile, Sapp_C_Minor_Profile)
T = createKeyProfileMatrix(Temperley_C_Major_Profile, Temperley_C_Minor_Profile)
AS = createKeyProfileMatrix(Albrecht_Shanahan_C_Major_Profile, Albrecht_Shanahan_C_Minor_Profile)
AS2 = createKeyProfileMatrix(Albrecht_Shanahan2_C_Major_Profile, Albrecht_Shanahan2_C_Minor_Profile)
TS = createKeyProfileMatrix(Temperley_Sapp_C_Major_Profile, Temperley_Sapp_C_Minor_Profile)
N6 = createKeyProfileMatrix(Napoles6_C_Major_Profile, Napoles6_C_Minor_Profile)
N128 = createKeyProfileMatrix(Napoles128_C_Major_Profile, Napoles128_C_Minor_Profile)
SNM = createKeyProfileMatrix(SNM_Major_Profile,SNM_Minor_Profile)
SHM = createKeyProfileMatrix(SHM_Major_Profile,SHM_Minor_Profile)
SMM = createKeyProfileMatrix(SMM_Major_Profile,SMM_Minor_Profile)


# these will be used for validating our results
lookupVector_same = num.array([0, 0.83, 0.33, 0.5, 0.67, 0.17, 1, 0.17, 0.67, 0.5, 0.33, 0.83])
lookupVector_different = num.array([0.58, 0.58, 0.25, 0.92, 0.08, 0.75, 0.42, 0.42, 0.75, 0.08, 0.92, 0.25])


# This function iteratively takes dot product of each row in our observation matrix and our key profile matrix
# to create our emission probability matrix. This emission matrix will represent each key's probabilities of emitting
# each measure in the song
def emissionsDotObservations(em, obs):
    desiredMatrix = num.array([])
    iteration = 0
    for row in obs:
        if iteration == 0:
            desiredMatrix = num.append(desiredMatrix, num.dot(em, row))
        else:
            desiredMatrix = num.vstack((desiredMatrix, num.dot(em, row)))
        iteration = iteration + 1
    return desiredMatrix.transpose()


# This function extracts the row indices from our observation matrix and converts them into an array
# which will represent the list of observed states in our algorithm.
def convertObservationMatrixIntoArray(obs):
    desiredMatrix = []
    counter = 0
    for i in range(len(obs)):
        desiredMatrix = desiredMatrix + [i]
        counter = counter + 1
    return desiredMatrix


# This function calculates the distance between the key values we calculate and the actual values
# to show how accurate is the algorithm.
def calculateDistance(computed, truth):
    distanceValues = num.array([])
    for i in range(len(computed)):
        diff = int(abs(computed[i] - truth[i]))
        if (computed[i] >= 13 and truth[i] >= 13) or (computed[i] <= 12 and truth[i] <= 12):
            distanceValues = num.append(distanceValues, lookupVector_same[diff])
        elif (computed[i] >= 13 and truth[i] <= 12) or (computed[i] <= 12 and truth[i] >= 13):
            distanceValues = num.append(distanceValues, lookupVector_different[diff % 12])
    totalDistance = sum(distanceValues)
    return distanceValues, totalDistance


def calculateScore(computed, actual):
    score = 0
    for i in range(len(computed)):
        if int(abs(computed[i] - actual[i])) == 0:
            score = score + 1
        elif int(abs(computed[i] - actual[i])) == 12:  # parallel major/minor
            score = score + 0.2
        elif int(abs(computed[i] - actual[i])) == 21:  # relative major/minor
            score = score + 0.3
        elif int(abs(computed[i] - actual[i])) == 7:  # perfect fifth
            score = score + 0.5
    return score / len(computed)


def step(mu_prev: num.ndarray,
         emission_probs: num.ndarray,
         transition_probs: num.ndarray,
         observed_state: int) -> Tuple[num.ndarray, num.ndarray]:

    pre_max = mu_prev * transition_probs.T
    max_prev_states = num.argmax(pre_max, axis=1)
    max_vals = pre_max[num.arange(len(max_prev_states)), max_prev_states]
    mu_new = max_vals * emission_probs[:, observed_state]
    return mu_new, max_prev_states


def viterbi(emission_probs: num.ndarray,
            transition_probs: num.ndarray,
            start_probs: num.ndarray,
            observed_states: List[int]) -> Tuple[List[int], float]:
   

    # Runs the forward pass, storing the most likely previous state.
    mu = start_probs * emission_probs[:, observed_states[0]]
    all_prev_states = []
    for observed_state in observed_states[1:]:
        mu, prevs = step(mu, emission_probs, transition_probs, observed_state)
        all_prev_states.append(prevs)

    # Traces backwards to get the maximum likelihood sequence.
    state = num.argmax(mu)
    sequence_prob = mu[state]
    state_sequence = [state]
    for prev_states in all_prev_states[::-1]:
        state = prev_states[state]
        state_sequence.append(state)

    return state_sequence[::-1], sequence_prob


# this function runs the viterbi algorithm implemented above and prints the computed values, actual values,
# distance values and total distance
def runViterbi(key_matrix, transition_ratio, observation, truth):
    states = num.array([])
    for i in range(24):
        states = num.append(states, i)

    initProbs = num.array([])
    for i in range(24):
        initProbs = num.append(initProbs, 1 / 24)

    emissions = emissionsDotObservations(key_matrix, observation)
    observations = convertObservationMatrixIntoArray(observation)
    max_seq, seq_prob = viterbi(
        emissions,
        createTransitionMatrix(transition_ratio),
        initProbs,
        observations,
    )

    for i in range(len(max_seq)):
        max_seq[i] = max_seq[i] + 1
    # accurates with KK: crazy, japan, chiquitita, dancing queen, godzilla, deep, New world Symphony(almost),
    # oneDay(relative major), polovtsian(relative major), poto(meh), ppfc, stayin alive
    # print("algorithm values: ")
    # print(max_seq)
    # print(len(max_seq))
    # print("actual values: ")
    # print(truth)
    # # print(seq_prob)
    distanceValues, totalDistance = calculateDistance(max_seq, truth)
    score = calculateScore(max_seq, truth)
    # print("distanceValues: ")
    # print(distanceValues)
    # print("totalDistance: ")
    # print(totalDistance)
    # print("score: ")
    # print(score)

    # plotting the results
    # plt.figure()
    # plt.title("Key Values for given observations")
    # plt.scatter(observations, max_seq, label="calculated values", c="r", marker="x")
    # plt.scatter(observations, truth, label="actual values", c="b", marker="+")
    # plt.xlabel("observation")
    # plt.ylabel("Key value")
    # plt.legend()
    # plt.show()
    return score, totalDistance


# this function calculates the best transition matrix ratio for given key profile and observation
def calculateBestRatio(key_profile, observation, truth):
    maxScores = num.array([])
    minDistances = num.array([])
    max_score = 0
    max_ratio = 0
    min_distance = 1000
    min_distance_ratio = 0
    for i in num.arange(1.5, 100.5, 0.5):
        score, distance = runViterbi(key_profile, i, observation, truth)
        if score > max_score:
            max_score = score
            max_ratio = i
            #print("score for ratio " + str(i) + " is " + str(score))
            maxScores = num.append(maxScores, i)
        elif score == max_score:
            #print("score for ratio " + str(i) + " is " + str(score))
            maxScores = num.append(maxScores, i)
        if distance < min_distance:
            min_distance = distance
            min_distance_ratio = i
            #print("distance for ratio " + str(i) + " is " + str(distance))
            minDistances = num.append(minDistances, i)
        elif distance == min_distance:
            #print("distance for ratio " + str(i) + " is " + str(distance))
            minDistances = num.append(minDistances, i)
    #print("Maximum score is " + str(max_score) + " resulted from ratio " + str(max_ratio))
    #print("\n")
    #print("Minimum distance is " + str(min_distance) + " resulted from ratio " + str(min_distance_ratio))
    return max_score, max_ratio, min_distance, min_distance_ratio


calculateBestRatio(SMM, potoDuration, potoTruth)


# runViterbi(TS, 4, barbieDuration, barbieTruth)


class viterbiAlgorithm():
    _transitionMatrix = ""  # transition_probability_matrix,taken from Arda's calculations
    _emissionMatrix = ""  # Key_profile_matrix, taken from the key probability matrix of pre determined data
    _observationMatrix = ""  # observation_symbols,12 pitch classes reduced to int
    _initial_state_probs = ""  # initial state probs,1/24 for each variable
    _states = ""  # 24 states for each of the 24 musical keys reduced to int

    def initialStateProbs(self):
        for i in range(24):
            self._initial_state_probs = num.append(self._initial_state_probs, 1 / 24)

    def states(self):
        for i in range(24):
            self._states = num.append(self._states, i)

    def observationMatrix(self):
        for i in range(12):
            self._observationMatrix = num.append(self._observationMatrix, i)

    def setObservationMatrix(self, observationMatrix):
        self._observationMatrix = observationMatrix

    def __init__(self, transitionMatrix, emissionMatrix, observationMatrix):
        self._transitionMatrix = transitionMatrix
        self._emissionMatrix = emissionsDotObservations(emissionMatrix, observationMatrix)
        self._observationMatrix = convertObservationMatrixIntoArray(observationMatrix)
        self.states()
        self.initialStateProbs()

    # this is the implementation that I have made by keeping our algorithm in mind
    # this worked for my inputs,but I don't know about the array inputs for our project
    # fix the issues with arrays and we will figure out the next step from there
    def runAlgorithm(self):
        result = [{}]
        for st in self._states:
            result[0][st] = {
                "prob": self._initial_state_probs[st] * self._emissionMatrix[st][self._observationMatrix[0]],
                "prev": None}
        for t in range(1, len(self._observationMatrix)):
            result.append({})
            for state in self._states:
                max_tr_prob = result[t - 1][self._states[0]]["prob"] * self._transitionMatrix[self._states[0]][state]
                prev_state_selected = self._states[0]
                for prev_st in self._states[1:]:
                    tr_prob = result[t - 1][prev_st]["prob"] * self._transitionMatrix[prev_st][state]
                    if tr_prob > max_tr_prob:
                        max_tr_prob = tr_prob
                        prev_state_selected = prev_st
                max_prob = max_tr_prob * self._emissionMatrix[state][self._observationMatrix[t]]
                result[t][state] = {"prob": max_prob, "prev": prev_state_selected}
        opt = []
        max_prob = 0.0
        best_st = None
        for state, data in result[-1].items():
            if data["prob"] > max_prob:
                max_prob = data["prob"]
                best_st = state
        opt.append(best_st)
        previous = best_st
        print("The steps of states are " + " ".join(opt) + " with highest probability of %s" % max_prob)


class dictionaryKeeper():
    __presenceDict={}
    __occurenceDict={}
    __durationDict={}
    __truthDict={}
    __keyProfileDict={}
    
    def addPresence(self,presenceName,presenceArray):
        self.__presenceDict[presenceName.lower()]=presenceArray
    def getPresenceArray(self,presenceName):
        return self.__presenceDict[presenceName.lower()]
    def addOccurence(self,occurenceName,occurenceArray):
        self.__occurenceDict[occurenceName.lower()]=occurenceArray
    def getOccurenceArray(self,occurenceName):
        return self.__occurenceDict[occurenceName.lower()]
    def addDuration(self,durationName,durationArray):
        self.__durationDict[durationName.lower()]=durationArray
    def getDurationArray(self,durationName):
        return self.__durationDict[durationName]
    def addTruth(self,truthName,truthArray):
        self.__truthDict[truthName.lower()]=truthArray
    def getTruthArray(self,truthName):
        return self.__truthDict[truthName.lower()]
    def addKeyProfile(self,keyProfileName,keyProfileArray):
        self.__keyProfileDict[keyProfileName]=keyProfileArray
    def getKeyProfileArray(self,keyProfileName):
        return self.__keyProfileDict[keyProfileName]
    def storeKeyValues(self):
        self.__presenceKeys={*self.__presenceDict}
        self.__occurenceKeys={*self.__occurenceDict}
        self.__durationKeys={*self.__durationDict}
        self.__truthKeys={*self.__truthDict}
        self.__keyProfileKeys={*self.__keyProfileDict}
    def returnKeyValues(self,keyType):
        keyValues={}
        if keyType.lower() == "presence":
            keyValues=self.__presenceKeys
        elif keyType.lower() == "occurence":
            keyValues=self.__occurenceKeys
        elif keyType.lower() == "duration":
            keyValues=self.__durationKeys
        elif keyType.lower() == "truth":
            keyValues=self.__truthKeys
        elif keyType.lower() == "profile":
            keyValues=self.__keyProfileKeys
        else:
            print("Wrong given type")
        return keyValues



class excelWriter():
    #the actual excel file
    __excelFile=""
    #the worksheet we write
    __workSheet=""
    #column Headers should be ordered when given,it should be list
    __columnHeaders=""
    #row counter
    __row=0
    
    def __init__(self,fileName,columnHeaders):
        print("Creating the object")
        self.__excelFile=xlsxwriter.Workbook(fileName+".xlsx")
        self.__workSheet=self.__excelFile.add_worksheet()
        self.__columnHeaders=columnHeaders
        
    def getExcelFile(self):
        if(self.__excelFile != ""):
            return self.__excelFile
        else:
            print("File not created")
    def setColumnHeaders(self,colHeaderNames):
        #col headers should be ordered
        self.__columnHeaders=colHeaderNames
    def writeColumnHeaders(self):
        #check if the file is created
        if(self.__workSheet == ""):
            print("Document not created")
        else:
            for index in range(len(self.__columnHeaders)):
                print("Writing the value {}".format(self.__columnHeaders[index]))
                self.__workSheet.write(0,index,self.__columnHeaders[index])
        self.__row+=1
    def writeToFile(self,data):
        #check if the file is created
        if(self.__workSheet==""):
            print("Document not created")
        else:
            #check the data and column header is same
            if(len(self.__columnHeaders)==len(data)):
                if(self.__row==0):
                        self.writeColumnHeaders()
                for index in range(len(data)):                    
                    print("Writing the value {}".format(data[index]))
                    self.__workSheet.write(self.__row,index,data[index])
                    
        self.__row+=1
    def closeFile(self):
        print("Closing the file")
        self.__excelFile.close()
                    
            
    
     
                
    
        
    
#first word for each dictionary string concat is song name
#second word is the key profile matrix used it is all UPPERCASE !
#third word is type used (presence,occurence,duration)
#for example potodurationSMM
class viterbiCalculator:
    maxScoreDict={}
    maxRatioDict={}
    minDistanceDict={}
    minDistanceRatioDict={}
    __matrixHolder=dictionaryKeeper()
    __presenceKeys={}
    __occurenceKeys={}
    __durationKeys={}
    __truthKeys={}
    __profileKeys={}
    maxSongScore={}
    maxSongScoreRatio={}
    minSongDistance={}
    minSongDistanceRatio={}
    def setDictionary(self,matrixHolder):
        self.__matrixHolder=matrixHolder
    def getDictionary(self):
        return self.__matrixHolder
    def printAllInfo(self):
        i=0
        for maxScoreDict in self.maxScoreDict:
            print("Max score for the key {} is {}".format(maxScoreDict,self.maxScoreDict[maxScoreDict]))
            print("Max ratio for the key {} is {}".format(maxScoreDict,self.maxRatioDict[maxScoreDict]))
            print("Min distance for the key {} is {}".format(maxScoreDict,self.minDistanceDict[maxScoreDict]))
            print("Min distance ratio for the key {} is {}".format(maxScoreDict,self.minDistanceRatioDict[maxScoreDict]))
            
            
    def printBestInfo(self):
        for bestResults in self.maxSongScore:
            print("Max score for the key {} is {}".format(bestResults,self.maxSongScore[bestResults]))
            print("Max ratio for the key {} is {}".format(bestResults,self.maxSongScoreRatio[bestResults]))
        for bestResults in self.minSongDistance:
            print("Min distance for the key {} is {}".format(bestResults,self.minSongDistance[bestResults]))
            print("Min distance ratio for the key {} is {}".format(bestResults,self.minSongDistanceRatio[bestResults]))
                    
    def validateBestResultMaxScore(self):
        maxScoreValue=0
        songNameHolder=""
        keyProfileNameHolder=""
        sheetTypeHolder=""
        maxScoreValueHolder=""
        maxScoreRatioHolder=""
        docHeaders=["Song Name","Best Key Profile","Type(Presence,Occurence,Duration)","Max Score","Max Score Ratio"]
        maxScoreWriter=excelWriter("maxScoreSheet",docHeaders)
        for songName in self.__presenceKeys:
            songNameHolder=songName
            maxScoreValue=0
            maxScoreHolder=""
            for maxScore in self.maxScoreDict:
                if(songName in maxScore):
                    if(self.maxScoreDict[maxScore]>maxScoreValue):
                        maxScoreValue=self.maxScoreDict[maxScore]
                        maxScoreHolder=maxScore
            if(maxScoreHolder!=""):
              upperString=re.findall('[A-Z]',maxScoreHolder)  
              keyProfileNameHolder=''.join([str(elem) for elem in upperString])
              sheetTypeHolder=maxScoreHolder.split(keyProfileNameHolder,1)[1]
              self.maxSongScore[maxScoreHolder]=self.maxScoreDict[maxScoreHolder]
              maxScoreValueHolder=self.maxScoreDict[maxScoreHolder]
              self.maxSongScoreRatio[maxScoreHolder]=self.maxRatioDict[maxScoreHolder]
              maxScoreRatioHolder=self.maxRatioDict[maxScoreHolder]
              valuesToWriteToExcel=[songNameHolder,keyProfileNameHolder,sheetTypeHolder,maxScoreValueHolder,maxScoreRatioHolder]
              maxScoreWriter.writeToFile(valuesToWriteToExcel)
        maxScoreWriter.closeFile()
                        
    def validateBestResultMinDistance(self):
        minDistanceValue=9999
        for songName in self.__presenceKeys:
            minDistanceValue=9999
            minDistanceHolder=""
            for minDistance in self.minDistanceDict:
                if(songName in minDistance):
                    if(self.minDistanceDict[minDistance]<minDistanceValue):
                        minDistanceValue=self.minDistanceDict[minDistance]
                        minDistanceHolder=minDistance
            if(minDistanceHolder!=""):
                self.minSongDistance[minDistanceHolder]=self.minDistanceDict[minDistanceHolder]
                self.minSongDistanceRatio[minDistanceHolder]=self.minDistanceRatioDict[minDistanceHolder]
                            
                
            
        
    def calculateValues(self):
        self.__matrixHolder.storeKeyValues()
        self.__presenceKeys=self.__matrixHolder.returnKeyValues("presence")
        self.__occurenceKeys=self.__matrixHolder.returnKeyValues("occurence")
        self.__durationKeys=self.__matrixHolder.returnKeyValues("duration")
        self.__truthKeys=self.__matrixHolder.returnKeyValues("truth")
        self.__profileKeys=self.__matrixHolder.returnKeyValues("profile")
        for truth in self.__truthKeys:
            truthArray=self.__matrixHolder.getTruthArray(truth)
            for profile in self.__profileKeys:
                profileArray=self.__matrixHolder.getKeyProfileArray(profile)
                presenceArray=self.__matrixHolder.getPresenceArray(truth)
                occurenceArray=self.__matrixHolder.getOccurenceArray(truth)
                durationArray=self.__matrixHolder.getDurationArray(truth)
                print("Inside the loop")
                self.maxScoreDict[truth+profile+"presence"],self.maxRatioDict[truth+profile+"presence"],self.minDistanceDict[truth+profile+"presence"],self.minDistanceRatioDict[truth+profile+"presence"]=calculateBestRatio(profileArray, presenceArray, truthArray)                 
                self.maxScoreDict[truth+profile+"occurence"],self.maxRatioDict[truth+profile+"occurence"],self.minDistanceDict[truth+profile+"occurence"],self.minDistanceRatioDict[truth+profile+"occurence"]=calculateBestRatio(profileArray, occurenceArray, truthArray)
                self.maxScoreDict[truth+profile+"duration"],self.maxRatioDict[truth+profile+"duration"],self.minDistanceDict[truth+profile+"duration"],self.minDistanceRatioDict[truth+profile+"duration"]=calculateBestRatio(profileArray, durationArray, truthArray)
                
    
                
                         
#key profiles for trial KK,AE
#musical pieces for trial 
#first song barbie
#arrays are as follows barbiePresence,barbieOccurence,barbieDuration,barbieTruth
#second song japan
#arrays are as follows japanPresence,japanOccurence,japanDuration,japanTruth
#dictionary keeper object
matrixHolder=dictionaryKeeper()

#putting the key profiles inside the object
matrixHolder.addKeyProfile("KK",KK)
matrixHolder.addKeyProfile("AE",AE)
#putting the first songs data into the object
matrixHolder.addPresence("barbie",barbiePresence)
matrixHolder.addOccurence("barbie",barbieOccurrence)
matrixHolder.addDuration("barbie",barbiePresence)
matrixHolder.addTruth("barbie",barbieTruth)
#putting the second songs data into the object
matrixHolder.addPresence("japan",japanPresence)
matrixHolder.addOccurence("japan",japanOccurrence)
matrixHolder.addDuration("japan",japanPresence)
matrixHolder.addTruth("japan",japanTruth)

#updating the key values inside object

#def writeData(self,excelData):
#        if(len(excelData)!=len(self.__columnHeaders)):
#            print("Illegal length the two should be with the same size")
#        else:
#            for    
#viterbi object
viterbiObject=viterbiCalculator()
viterbiObject.setDictionary(matrixHolder)
viterbiObject.calculateValues()
viterbiObject.printAllInfo()
viterbiObject.validateBestResultMaxScore()
viterbiObject.validateBestResultMinDistance()
viterbiObject.printBestInfo()
#maxScore,maxRatio,minDistance,minDistRatio=calculateBestRatio(AE, japanOccurrence, japanTruth)
#print("Max score {}".format(maxScore))
#print("Max ratio {}".format(maxRatio))
#print("Min distance {}".format(minDistance))
#print("Min distance ratio {}".format(minDistRatio))
#
#maxScore,maxRatio,minDistance,minDistRatio=calculateBestRatio(AE, japanDuration, japanTruth)
#print("Max score {}".format(maxScore))
#print("Max ratio {}".format(maxRatio))
#print("Min distance {}".format(minDistance))
#print("Min distance ratio {}".format(minDistRatio))


#Max score for the key japanaeoccurence is 0
#Max ratio for the key japanaeoccurence is 0
#Min distance for the key japanaeoccurence is 9.680000000000007
#Min distance ratio for the key japanaeoccurence is 1.5           
    
    
    

   
        
    


    
        
        

