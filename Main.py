import csv
import matplotlib.pyplot as plt
import numpy as num


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


def TruthIntoArray(fileLocation):
    truth = num.array([])
    with open(fileLocation, encoding="Latin-1") as z:
        csv_list = list(csv.reader(z))
    for row in csv_list:
        if row != csv_list[0]:
            truth = num.append(truth, int(row[1]))
    return truth


# these are our observesions and ground truth arrays
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

# creating the key profile matrix
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

# this is our emission matrix
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


# these are major rows of transition probability matrix
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

# these are minor rows of transition probability matrix
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
print(transition_probability_matrix)
print(num.shape(transition_probability_matrix))
