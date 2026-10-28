
# Exercise 1
Queue = [-1] * 10
HeadPointer = -1
TailPointer = -1
NumberItems = 0


def Enqueue(Data):
    global Queue, HeadPointer, TailPointer, NumberItems

    if NumberItems == 10:
        return False

    if NumberItems == 0:
        HeadPointer = 0
        TailPointer = 0
    else:
        TailPointer = TailPointer + 1

        if TailPointer == 10:
            TailPointer = 0

    Queue[TailPointer] = Data
    NumberItems = NumberItems + 1

    return True


def Dequeue():
    global Queue, HeadPointer, TailPointer, NumberItems

    if NumberItems == 0:
        return -999

    Data = Queue[HeadPointer]

    HeadPointer = HeadPointer + 1

    if HeadPointer == 10:
        HeadPointer = 0

    NumberItems = NumberItems - 1

    if NumberItems == 0:
        HeadPointer = -1
        TailPointer = -1

    return Data


# Exercise 2
def LoadQueue(Filename):
    global Queue, HeadPointer, TailPointer, NumberItems

    Count = 0

    with open(Filename, "r") as File:
        for Line in File:
            Line = Line.strip()

            if Line == "":
                continue

            Data = int(Line)

            if Enqueue(Data) == False:
                print("Queue full")
                break

            Count = Count + 1

    return Count


# Exercise 3
def RemoveNegatives():
    global Queue, HeadPointer, TailPointer, NumberItems

    OriginalCount = NumberItems
    RemovedCount = 0

    for i in range(OriginalCount):
        Data = Dequeue()

        if Data < 0:
            RemovedCount = RemovedCount + 1
        else:
            Enqueue(Data)

    return RemovedCount
