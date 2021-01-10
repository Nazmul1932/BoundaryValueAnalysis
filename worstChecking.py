import numpy as np
import pandas as pd


def computeWorstTesting(minValueList, maxValueList, parameters):
    worstTable = [[]]
    worstCSVTable = pd.DataFrame()

    minValue = []
    for i in range(0, len(minValueList)):
        minValue.append(minValueList[i])
    worstTable.insert(0, minValue)

    minValuePlus = []
    for i in range(0, len(minValueList)):
        minValuePlus.append(minValueList[i] + 1)
    worstTable.insert(1, minValuePlus)

    maxValue = []
    for i in range(0, len(maxValueList)):
        maxValue.append(maxValueList[i])
    worstTable.insert(2, maxValue)

    maxValueMinus = []
    for i in range(0, len(maxValueList)):
        maxValueMinus.append(maxValueList[i] - 1)
    worstTable.insert(3, maxValueMinus)

    nominal = []
    for i in range(0, len(maxValueList)):
        nominal.append(np.math.ceil((maxValueList[i] + (minValueList[i] - 1)) / 2))
    worstTable.insert(4, nominal)

    print(worstTable)

    testID = list(range(1, pow(5, parameters) + 1))

    for i in range(0, parameters):
        tmpWorstTable = []
        while len(tmpWorstTable) < pow(5, parameters):
            for j in range(0, 5):
                for k in range(0, pow(5, parameters - (i + 1))):
                    tmpWorstTable.append(worstTable[j][i])

        worstCSVTable[i+1] = tmpWorstTable

    worstCSVTable.insert(0, 'Test Case Id', testID)
    worstCSVTable['Expected Output'] = ''
    worstCSVTable.to_csv('worst.csv', index=False)