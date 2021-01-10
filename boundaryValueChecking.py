import numpy as np
import pandas as pd


def computeBVC(minValueList, maxValueList, parameters):
    bvcTable = [[]]
    bvcCSVTable = pd.DataFrame()

    minValue = []
    for i in range(0, len(minValueList)):
        minValue.append(minValueList[i])
    bvcTable.insert(0, minValue)


    minValuePlus = []
    for i in range(0, len(minValueList)):
        minValuePlus.append(minValueList[i] + 1)
    bvcTable.insert(1, minValuePlus)


    maxValue = []
    for i in range(0, len(maxValueList)):
        maxValue.append(maxValueList[i])
    bvcTable.insert(2, maxValue)


    maxValueMinus = []
    for i in range(0, len(maxValueList)):
        maxValueMinus.append(maxValueList[i] - 1)
    bvcTable.insert(3, maxValueMinus)


    nominal = []
    for i in range(0, len(maxValueList)):
        nominal.append(np.math.ceil((maxValueList[i] + (minValueList[i] - 1)) / 2))
    bvcTable.insert(4, nominal)


    allNominalValue = []
    testID = list(range(1, 4 * parameters + 2))

    for i in range(0, parameters):
        tempBVCTable = []
        nominalValue = bvcTable[4][i]
        allNominalValue.append(nominalValue)

        for j in range(0, 4 * (parameters - 1)):
            tempBVCTable.append(nominalValue)

        for j in range(0, 4):
            position = j + (i * 4)
            tempBVCTable.insert(position, bvcTable[j][i])

        bvcCSVTable[i+1] = tempBVCTable

    bvcCSVTable.loc[len(bvcCSVTable)] = allNominalValue
    # print(bvcCSVTable)
    bvcCSVTable.insert(0, 'Test Case Id', testID)
    bvcCSVTable['Expected Output'] = ''
    bvcCSVTable.to_csv('bvc.csv', index=False)


