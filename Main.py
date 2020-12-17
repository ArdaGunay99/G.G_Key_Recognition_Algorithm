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
