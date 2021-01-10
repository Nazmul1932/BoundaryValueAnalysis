import boundaryValueChecking
import robustChecking
import worstChecking




if __name__ == '__main__':
    maxValueList = []
    minValueList = []
    parameters = int(input('Enter parameters\n'))

    for i in range(0, parameters):
        minValues, maxValues = input().split()
        maxValueList.append(int(maxValues))
        minValueList.append(int(minValues))

    # print(maxValueList)
    # print(minValueList)

    boundaryValueChecking.computeBVC(minValueList, maxValueList, parameters)
    robustChecking.computeRobustTesting(minValueList, maxValueList, parameters)
    worstChecking.computeWorstTesting(minValueList, maxValueList, parameters)

    print('Test cases generated!\nTest files: bvc.csv, robust.csv, worst.csv')
