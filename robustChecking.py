import numpy as np
import pandas as pd


def computeRobustTesting(minValueList, maxValueList, parameters):
    robustTable = [[]]
    robustCSVTable = pd.DataFrame()

    minValue = []
    for i in range(0, len(minValueList)):
        minValue.append(minValueList[i])
    robustTable.insert(0, minValue)

    minValuePlus = []
    for i in range(0, len(minValueList)):
        minValuePlus.append(minValueList[i] + 1)
    robustTable.insert(1, minValuePlus)

    minValueMinus = []
    for i in range(0, len(minValueList)):
        minValueMinus.append(minValueList[i] - 1)
    robustTable.insert(2, minValueMinus)


    maxValue = []
    for i in range(0, len(maxValueList)):
        maxValue.append(maxValueList[i])
    robustTable.insert(3, maxValue)


    maxValueMinus = []
    for i in range(0, len(maxValueList)):
        maxValueMinus.append(maxValueList[i] - 1)
    robustTable.insert(4, maxValueMinus)


    maxValuePlus = []
    for i in range(0, len(maxValueList)):
        maxValuePlus.append(maxValueList[i] + 1)
    robustTable.insert(5, maxValuePlus)

    nominalValue = []
    for i in range(0, len(maxValueList)):
        nominalValue.append(np.math.ceil((maxValueList[i] + (minValueList[i] - 1)) / 2))
    robustTable.insert(6, nominalValue)


    allNominalValue = []
    testID = list(range(1, 6 * parameters + 2))

    for i in range(0, parameters):
        tempRobustTable = []
        nominalValue = robustTable[6][i]
        allNominalValue.append(nominalValue)

        for j in range(0, 6 * (parameters - 1)):
            tempRobustTable.append(nominalValue)

        for j in range(0, 6):
            position = j + (i * 6)
            tempRobustTable.insert(position, robustTable[j][i])
        robustCSVTable[i+1] = tempRobustTable

    robustCSVTable.loc[len(robustCSVTable)] = allNominalValue
    # print(robustCSVTable)
    robustCSVTable.insert(0, 'Test Case Id', testID)
    robustCSVTable['Expected Output'] = ''
    robustCSVTable.to_csv('robust.csv', index=False)
