import csv # imports the needed csv functions

######################################
## COMP90059 - Assignment 2         ##
## This file and functions are      ##
## designed to support the needs    ##
## of assignemt 2.                  ##
##                                  ##
## read_data                        ##
## reads the data from the CSV file ##
##                                  ##
## You need not worry about the     ##
## content of this function. use it ##
## as needed to complete your code. ##
######################################
def read_data(filename):
    data = {}
    new_data = {}
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ID = row["ID"]
            del row["ID"]
            for key in row:
                if not row[key]:
                    row[key] = None
            data[ID]=row
            new_data[ID] = dict(list(row.items()))
    return new_data

def clean(data):
    years = ["2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012"]
    times = 0
    #Corrects derogatory remarks
    for id in data:
        if data[id]["Subcategory"] == "MUC-SUCK":
            data[id]["Subcategory"] = "Trespass"
            times += 1

    for id in data:
        for column in years:
            # Checks for "zero" and "null"
            if data[id][column] == "ZERO" or data[id][column] == "NULL":
                data[id][column] = "0"
                times += 1
            if int(data[id][column]) < 0:
                times += 1
            data[id][column] = abs(int(data[id][column]))

    return times

def worstYear(data):
    years = ["2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012"]
    #worst year
    sum = [0]*11
    for id in data:
        i = 0
        for column in years:
            sum[i]+=data[id][column]
            i+=1

def worstCrime(data):
    years = ["2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012"]
    newinfo = {}
    for id in data:
        sum = 0
        for year in years:
            sum += data[id][year]
        # new
        if data[id]["Statistical Division or Subdivision"] not in newinfo: #check whether is in the dictionary
            newinfo[data[id]["Statistical Division or Subdivision"]] = sum #adding item
        #update
        else:
            newinfo[data[id]["Statistical Division or Subdivision"]] = newinfo[data[id]["Statistical Division or Subdivision"]] + sum


    return newinfo


def mostActiveCrime(data):
    years = ["2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012"]
    newinfo = {}
    for id in data:
        sum = 0
        for year in years:
            sum += data[id][year]
        # check if the offence category is in the new dictionary
        if data[id]["Offence category"] not in newinfo: #check whether is in the dictionary
            newinfo[data[id]["Offence category"]] = sum #adding item
        else:
            newinfo[data[id]["Offence category"]] = newinfo[data[id]["Offence category"]] + sum

    return newinfo

def report(datafile):
    data = read_data(datafile)
    times = clean(data)
    worstYear(data)
    district = worstCrime(data)
    maximum = district[data["1"]["Statistical Division or Subdivision"]]
    for id in district:
        if maximum < district[id]:
            maximum = district[id]
    # get the key which hold the same value of maximum
    for id, crime in district.items():
        if crime == maximum:
            worstArea = maximum

    # find the smallest value (best area)
    minimum = district[data["1"]["Statistical Division or Subdivision"]]
    for id in district:
        if minimum > district[id]:
            minimum = district[id]
    # get the key which hold the same value of minimum
    for id, crime in district.items():
        if crime == minimum:
            bestArea = id

    crimeType = mostActiveCrime(data)
    maximum = 0
    for id in crimeType:
        if maximum < crimeType[id]:
            maximum = crimeType[id]
    # get the key which hold the same value of maximum
    for id, crime in crimeType.items():
        if crime == maximum:
            popular = id

    dataFact = [len(data), len(district), len(crimeType), worstArea, bestArea, popular]

    print()
    print("On behalf of the MUC (Made Up Company), "
          "I have analysed " + str(dataFact[0]) +" units of the crime statistics data, "
          "over a 10-year period. I have repaired " + str(times) +" corrupt data values. ")
    print("This data-set covered " + str(dataFact[1]) + " and found " + str(dataFact[2]) +" types of crimes.")
    print("I conclude that the worst area for crime is " + str(dataFact[3]) +
          "while the safest area is " + str(dataFact[4]) +" and that the most active category of crime is " + str(dataFact[5]) +" . ")
    print(" Sincerely, YUN-TING WANG:1063385.")
    return dataFact









#########################################
## Main method, to call functions etc, ##
#########################################
def main():
    ## change this filename variable to point to the location of the csv file
    ## you are wishing to work with.  Use the small set (supplied on LMS) to
    ## test your functions.  Then move on to the large sets, when you are happy
    ## NOTE: Large files take longer to process.
    filename ='COMP90059_CrimeData_Small_Clean.csv'

    ## read_data returns a dictionary of dictionaries.  
    data = read_data(filename)
    clean(data)
    years = worstYear(data)
    yearsIndex = ["2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012"]
    large = 0
    sum = [0] * 11
    for crimecount in range(len(sum)):
        if sum[large] < sum[crimecount]:
            large = crimecount
    print("Worst year: " + yearsIndex[large])

    district = worstCrime(data)
    # find the largest value (worst area)
    maximum = district[data["1"]["Statistical Division or Subdivision"]]
    for id in district:
        if maximum < district[id]:
            maximum = district[id]
    # get the key which hold the same value of maximum
    for id, crime in district.items():
        if crime == maximum:
            print('Worst district' + id)

    # find the smallest value (best area)
    minimum = district[data["1"]["Statistical Division or Subdivision"]]
    for id in district:
        if minimum > district[id]:
            minimum = district[id]
    # get the key which hold the same value of minimum
    for id, crime in district.items():
        if crime == minimum:
            print("Best area "+id)

    crimeType = mostActiveCrime(data)
    # find the largest value
    maximum = 0
    for id in crimeType:
        if maximum < crimeType[id]:
            maximum = crimeType[id]
    # get the key which hold the same value of maximum
    for id, crime in crimeType.items():
        if crime == maximum:
            print("Most active crime overall: "+id)


    overallReport = report(filename)

    ## Perform your functions calls here

############################
## Begins the application ##
############################
main()