# Project6-Function/Main file
#
# Name: Hayden Tam
# Instructor: S. Einakian
# Section: 05
# Take in the inputs and split into lines


class Crime:
    def __init__(self, iD, category):
        self.iD = iD
        self.category = category
        self.day_of_week = None
        self.month = None
        self.hour = None

    def __eq__(self, other):
        # and self.day_of_week == other.category and self.month == other.month and self.hour == other.hour)
        return type(self) == type(other) and \
            self.iD == other.iD and self.category == other.category and self.day_of_week == other.day_of_week and \
            self.month == other.month and self.hour == other.hour

    def __repr__(self):
        return(("{},{}".format(
            self.iD, self.category)))  # self.day_of_week, self.month, self.hour)))

    def set_time(self, month, hour):

        numString = ""
        if (int(hour) > 12):
            numString = str(int(hour)-12)+"PM"
        elif(0 < int(hour) < 12):
            numString = str((int(hour)))+"AM"
        elif(int(hour) == 0):
            numString = str(12)+"AM"
        elif(int(hour) == 12):
            numString = str(12)+"PM"
        self.hour = numString
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
        stringRep = months[int(month)-1]
        self.month = stringRep

# Purpose: creates crime obj
# Signature: list->list


def create_crimes(crimeList):
    #test = open("Test.txt", "w")

    robberyListID = []
    robberyObjectList = []
    for count in range(0, len(crimeList), 1):

        iD = crimeList[count][0]

        iD.strip()

        category = crimeList[count][1]

        # 150025138
        category = category.split()

        if(category[0] == "ROBBERY" and iD not in robberyListID):

            robberyListID.append(iD)
            robberyObject = Crime(iD, "ROBBERY")
            robberyObjectList.append(robberyObject)

    return robberyObjectList


# Purpose: takes in the list of objects and sorts them
# Signature: list (Crime obj)->list(Crime obj)


def sort_crimes(crimes):
    for i in range(len(crimes)):
        minIndex = i
        for k in range(i + 1, len(crimes)):
            if (int(crimes[k].iD)) < int((crimes[minIndex].iD)):
                minIndex = k

        swap(crimes, minIndex, i)

    return crimes

# Purpose: swaps the variables around in the list accordingly
# Signature: list, int,int->None


def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp
# crimes is the sorted robbery list  list of objects

# Purpose: takes in the sorted crime list and the lines from times.tsv and updates each object accordingly
# Signature: list,list-> list


def update_crimes(crimes, lines):
    # print(crimes)
    updatedCrimes = []
    for line in lines:
        sections = line.split("\t")

        # print(sections)
        fc = find_crime(crimes, sections[0])
        month = str(sections[2])

        mnth = month.split("/")
        mnth = mnth[0]
        hr = sections[3]

        hr = hr.split(":")
        hr = hr[0]
        hr = hr.split(":")
        hr = hr[0]
        hr = hr.strip()

        #hr = changeTime((hr))
        if fc[0] == True:  # found ID is from the times file; list of all the ones that are robberies
            # fc.day_of_week = str(sections[1])

            crimes[fc[1]].day_of_week = str(sections[1])
            crimes[fc[1]].set_time(mnth, hr)

    for crime in crimes:
        updatedCrimes.append(crime)

    return updatedCrimes

# Purpose: finds the crime within the times. tsv file through binary research and returns the index if found to update the necessary object
# Signatuer: list(Obj list),int->tuple(bool,int)


def find_crime(robberList, crime_id):
    first = 0  # binary search
    last = len(robberList)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if int(robberList[midpoint].iD) == int(crime_id):
            found = True
            mid = midpoint
        else:
            if int(crime_id) < int(robberList[midpoint].iD):
                last = midpoint-1
            else:
                first = midpoint+1

    return found, midpoint

# Purpose: gets the mode for most crimes happening within a day, hour, and month
# Signature: list(Crime list)->tuple(string,string,string)


def stats(updatedCrimes):
    binofdays = ["Monday", "Tuesday", "Wednesday",
                 "Thursday", "Friday", "Saturday", "Sunday"]
    numberofRobberies = len(updatedCrimes)
    countDays = [0, 0, 0, 0, 0, 0, 0]

    for count in updatedCrimes:
        if(count.day_of_week == "Monday"):
            countDays[0] += 1
        elif(count.day_of_week == "Tuesday"):
            countDays[1] += 1
        elif(count.day_of_week == "Wednesday"):
            countDays[2] += 1
        elif(count.day_of_week == "Thursday"):
            countDays[3] += 1
        elif(count.day_of_week == "Friday"):
            countDays[4] += 1
        elif(count.day_of_week == "Saturday"):
            countDays[5] += 1
        elif(count.day_of_week == "Sunday"):
            countDays[6] += 1

    maxofDays = max(countDays)
    idxmaxDay = countDays.index(maxofDays)
    dayMax = binofdays[idxmaxDay]
    binofmonths = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    countmonthList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for countmonths in updatedCrimes:
        if(countmonths.month == "January"):
            countmonthList[0] += 1
        elif(countmonths.month == "February"):
            countmonthList[1] += 1
        elif(countmonths.month == "March"):
            countmonthList[2] += 1
        elif(countmonths.month == "April"):
            countmonthList[3] += 1
        elif(countmonths.month == "May"):
            countmonthList[4] += 1
        elif(countmonths.month == "June"):
            countmonthList[5] += 1
        elif(countmonths.month == "July"):
            countmonthList[6] += 1
        elif(countmonths.month == "August"):
            countmonthList[7] += 1
        elif(countmonths.month == "September"):
            countmonthList[8] += 1
        elif(countmonths.month == "October"):
            countmonthList[9] += 1
        elif(countmonths.month == "November"):
            countmonthList[10] += 1
        elif(countmonths.month == "December"):
            countmonthList[12] += 1
    maxMonthNum = max(countmonthList)
    idxmaxMonth = countmonthList.index(maxMonthNum)
    maxMonth = binofmonths[idxmaxMonth]

    binofTimes = ["12AM", "1AM", "2AM", "3AM", "4AM", "5AM", "6AM", "7AM", "8AM", "9AM", "10AM",
                  "11AM", "12PM", "1PM", "2PM", "3PM", "4PM", "5PM", "6PM", "7PM", "8PM", "9PM", "10PM", "11PM"]
    countTime = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for countingTime in updatedCrimes:
        if countingTime.hour == "12AM":
            countTime[0] += 1
        elif countingTime.hour == "1AM":
            countTime[1] += 1
        elif countingTime.hour == "2AM":
            countTime[2] += 1
        elif countingTime.hour == "3AM":
            countTime[3] += 1
        elif countingTime.hour == "4AM":
            countTime[4] += 1
        elif countingTime.hour == "5AM":
            countTime[5] += 1
        elif countingTime.hour == "6AM":
            countTime[6] += 1
        elif countingTime.hour == "7AM":
            countTime[7] += 1
        elif countingTime.hour == "8AM":
            countTime[8] += 1
        elif countingTime.hour == "9AM":
            countTime[9] += 1
        elif countingTime.hour == "10AM":
            countTime[10] += 1
        elif countingTime.hour == "11AM":
            countTime[11] += 1
        elif countingTime.hour == "12PM":
            countTime[12] += 1
        elif countingTime.hour == "1PM":
            countTime[13] += 1
        elif countingTime.hour == "2PM":
            countTime[14] += 1
        elif countingTime.hour == "3PM":
            countTime[15] += 1
        elif countingTime.hour == "4PM":
            countTime[16] += 1
        elif countingTime.hour == "5PM":
            countTime[17] += 1
        elif countingTime.hour == "6PM":
            countTime[18] += 1
        elif countingTime.hour == "7PM":
            countTime[19] += 1
        elif countingTime.hour == "8PM":
            countTime[20] += 1
        elif countingTime.hour == "9PM":
            countTime[21] += 1
        elif countingTime.hour == "10PM":
            countTime[22] += 1
        elif countingTime.hour == "11PM":
            countTime[23] += 1

    maxCountTime = max(countTime)
    idxmaxTime = countTime.index(maxCountTime)
    maxHour = binofTimes[idxmaxTime]
    return dayMax, maxMonth, maxHour


#testFile = open("Testing.txt", "w")

#Purpose: main
# Signature: none->none
def main():
    writeFile = open("robberies.tsv", "w")
    writeFile.write("ID"+"\t"+"Category"+"\t" +
                    "DayOfWeek"+"\t"+"Month"+"\t"+"Hour")
    writeFile.write("\n")
    listofCrimes = open("crimes.tsv", "r")
    actualListofCrimes = []
    for count in listofCrimes:
        count = count.strip().split("\t")

        actualListofCrimes.append(count)

    listofCrimes.close()

    # .split if index 1==robbery and index 0 not in list and then append it
    robberyObj = create_crimes(actualListofCrimes)

    sortedRobberyListID = sort_crimes(robberyObj)  # list of obj sorted

    # 3638, should be 3636   because of  #150028825        #150025138

    fin = open("times.tsv")

    lines = fin.readlines()[1:]

    updatedCrimes = update_crimes(sortedRobberyListID, lines)
    stat = stats(updatedCrimes)
    for count3 in updatedCrimes:
        writeFile.write(str(count3.iD)+"\t"+str(count3.category)+"\t" +
                        str(count3.day_of_week)+"\t" + str(count3.month)+"\t" + str(count3.hour))
        writeFile.write("\n")
    print("\n")
    print("NUMBER OF PROCESSED ROBBERIES:" + str(len(updatedCrimes)))
    print("\n")
    print("DAY WITH MOST ROBBERIES:"+str(stat[0]))
    print("\n")
    print("MONTH WITH MOST ROBBERIES:"+str(stat[1]))
    print("\n")
    print("HOUR WITH MOST ROBBERIES:"+str(stat[2]))
    writeFile.close()


if __name__ == '__main__':
    main()
