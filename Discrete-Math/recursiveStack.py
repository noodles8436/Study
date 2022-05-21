import matplotlib.pyplot as plt
import numpy as np
import time


class RecursiveManager:

    def __init__(self):
        self.stackCnt = list()
        self.stackCnt.append(0)
        self.memo = list()
        self.memo.append(0)
        self.memo.append(1)

    def addStackCnd(self):
        self.stackCnt.append(self.stackCnt[-1] + 1)
        return 0

    def removeStackCnd(self):
        self.stackCnt.append(self.stackCnt[-1] - 1)
        return 0

    def plotStackCnd(self, resultTitle, _xmax=0, _ymax=0):
        x = np.arange(len(self.stackCnt))
        xmax = max(len(self.stackCnt), _xmax)
        ymax = max(np.max(self.stackCnt), _ymax)
        print(xmax, ymax)
        plt.title('Recursive :: ' + str(resultTitle))
        plt.plot(x, self.stackCnt, label='stackCnt', color='forestgreen')
        plt.xlim([0, xmax])
        plt.ylim([0, ymax])
        plt.show()

    def clear(self):
        self.stackCnt = list()
        self.stackCnt.append(0)
        self.memo = list()
        self.memo.append(0)
        self.memo.append(1)

    def recursive_merge_sort(self, arr):
        self.addStackCnd()
        if len(arr) < 2:
            self.removeStackCnd()
            return arr

        print(arr)

        mid = len(arr) // 2
        low_arr = self.recursive_merge_sort(arr[:mid])
        high_arr = self.recursive_merge_sort(arr[mid:])

        print(low_arr, high_arr)

        merged_arr = []
        l = h = 0

        while l < len(low_arr) and h < len(high_arr):
            if low_arr[l] < high_arr[h]:
                merged_arr.append(low_arr[l])
                l += 1
            else:
                merged_arr.append(high_arr[h])
                h += 1

        merged_arr += low_arr[l:]
        merged_arr += high_arr[h:]

        print(merged_arr)

        self.removeStackCnd()
        return merged_arr

    def merge_sort_alg(self, data, left, right, drawData, timeTick):
        if left < right:
            middle = (left + right) // 2
            self.merge_sort_alg(data, left, middle, drawData, timeTick)
            self.merge_sort_alg(data, middle + 1, right, drawData, timeTick)
            self.merge(data, left, middle, right, drawData, timeTick)

    def merge_sort(self, data, drawData, timeTick):
        self.merge_sort_alg(data, 0, len(data) - 1, drawData, timeTick)

    def merge(self, data, left, middle, right, drawData, timeTick):
        drawData(data, self.getColorArray(len(data), left, middle, right))
        time.sleep(timeTick)

        leftPart = data[left:middle + 1]
        rightPart = data[middle + 1: right + 1]

        leftIdx = rightIdx = 0

        for dataIdx in range(left, right + 1):
            if leftIdx < len(leftPart) and rightIdx < len(rightPart):
                if leftPart[leftIdx] <= rightPart[rightIdx]:
                    data[dataIdx] = leftPart[leftIdx]
                    leftIdx += 1
                else:
                    data[dataIdx] = rightPart[rightIdx]
                    rightIdx += 1

            elif leftIdx < len(leftPart):
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1

        drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
        time.sleep(timeTick)

    def getColorArray(self, leght, left, middle, right):
        colorArray = []

        for i in range(leght):
            if i >= left and i <= right:
                if i >= left and i <= middle:
                    colorArray.append("yellow")
                else:
                    colorArray.append("pink")
            else:
                colorArray.append("white")

        return colorArray

    def recursive_Fibo(self, num):
        self.addStackCnd()
        if num == 0:
            return 0 + self.removeStackCnd()
        elif num == 1:
            return 1 + self.removeStackCnd()
        else:
            return self.recursive_Fibo(num - 1) + self.recursive_Fibo(num - 2) \
                   + self.removeStackCnd()

    def recursiveTail_Fibo(self, num, prevFibo=1, twoPrevFibo=0):
        self.addStackCnd()
        if num == 0:
            return twoPrevFibo + self.removeStackCnd()
        elif num == 1:
            return prevFibo + self.removeStackCnd()
        else:
            currentFibo = prevFibo + twoPrevFibo
            twoPrevFibo = prevFibo
            prevFibo = currentFibo
            return self.removeStackCnd() + self.recursiveTail_Fibo(num - 1, prevFibo, twoPrevFibo)

    def recursive_Mem_Fibo(self, num):
        self.addStackCnd()
        if num >= len(self.memo):
            self.memo.append(self.recursive_Mem_Fibo(num - 1) + self.recursive_Mem_Fibo(num - 2))
        return self.memo[num] + self.removeStackCnd()


recurManger = RecursiveManager()

testNum = 10
_xmax = 50
_ymax = 20

result = recurManger.recursive_Fibo(testNum)
resultTitle = "Fibo" + str(testNum) + " :: Result - " + str(result)
recurManger.plotStackCnd(resultTitle=resultTitle, _xmax=_xmax, _ymax=_ymax)
recurManger.clear()

result = recurManger.recursiveTail_Fibo(testNum)
resultTitle = "FiboTail" + str(testNum) + " :: Result - " + str(result)
recurManger.plotStackCnd(resultTitle=resultTitle, _xmax=_xmax, _ymax=_ymax)
recurManger.clear()

result = recurManger.recursive_Mem_Fibo(testNum)
resultTitle = "FiboMem" + str(testNum) + " :: Result - " + str(result)
recurManger.plotStackCnd(resultTitle=resultTitle, _xmax=_xmax, _ymax=_ymax)
recurManger.clear()

arr = [3, 2, 6, 4, 5, 8, 9, 7, 10, 1]
result = recurManger.recursive_merge_sort(arr)
resultTitle = "MergeSort" + str(testNum) + " :: Result - " + str(result)
recurManger.plotStackCnd(resultTitle=resultTitle, _xmax=_xmax, _ymax=_ymax)
recurManger.clear()
