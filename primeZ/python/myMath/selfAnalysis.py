# selfAnalysis.py
#
# Self-analysis, or code-analysis
#

file_path = "myMath1.py"

def readDNAFile():
    fileLines = []

    with open(file_path, 'r') as inFile:
        for line in inFile:
            fileLines.append(line.strip("\n"))
    inFile.close()
    return fileLines

def listDefs(code):
    lstDefs = []
    firstTripleQuotes = False
    pfFlag = False

    for line in code:
        # Need to skip over TripleQuotes blocks
        if '"""' in line or "'''" in line:
            firstTripleQuotes = not firstTripleQuotes
            continue

        if firstTripleQuotes:
            continue
        
        if "def" in line:
            print("line: ", line)
            # Skip commented out single lines
            if not line.strip()[0] == "#":
                print("no #? line: ", line)
                print(line.strip())
                print(len(line.strip()))
                      
                if line[-1] == "(":
                    print("process further...: ", line)
                    pfFlag = True
                    


                    
                functionName = line.split()[1]
                functionName = functionName.split("(")[0]

                functionParameters = line.split("(")[-1][:-2]
                print("1st fP: ", functionParameters)
                if ":" in functionParameters:
                    delimiter = ":"
                    functionParameters = functionParameters.split(delimiter)[0]

                print("2nd fP: ", functionParameters)
                functionParameters = functionParameters.split(',')
                functionParameters = [item.strip() for item in functionParameters]
                functionParameters = functionParameters
                print("fP: ", functionParameters)
                print("fN: ", functionName)
                if not pfFlag:
                    lstDefs.append((functionName, functionParameters))

        if pfFlag:
            functionParameters = []
            print("pfFlag true further processing...: ", line)
            tmpLine = line.strip()
            print(tmpLine)
            if not "def" in line:
                functionParameters.append(tmpLine[:-1])
                if len(tmpLine) == 2:
                    if tmpLine[0] == ")" and tmpLine[1] == ":":
                        pfFlag = False
                        print("stop further processing: ", line)


            lstDefs.append((functionName, functionParameters))

    return lstDefs

def selectDef(code):
    selectedDef = []

    return selectedDef


if __name__ == "__main__":

    rawCode = readDNAFile()

    print(len(rawCode))
    print(type(rawCode))
    for line in rawCode:
        print(line)

    print('-----')
    defList = listDefs(rawCode)

    print(len(defList))
    print(type(defList))
    print('-----')
    for d in defList:
        print(d)


    selectedDef = selectDef(rawCode)
