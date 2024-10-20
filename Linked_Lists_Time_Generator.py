class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return f'{self.data}\t{self.next}'


class Clock:
    def __init__(self,hour,minute,second):
        self.flag=False
        self.meridium=['AM','PM']
        self.hour=hour
        self.minute=minute
        self.second=second

    def __tick_hour(self):
        if self.hour.data==11:
            self.flag=not self.flag
        self.hour=self.hour.next
    def __tick_minute(self):
        if self.minute.data==59:
            self.__tick_hour()
        self.minute=self.minute.next
    def tick(self):
        if self.second.data==59:
            self.__tick_minute()
        self.second=self.second.next

    def __call__(self):
        return (self.hour.data,self.minute.data,self.second.data)
                
    def __str__(self):
        return f'{self.hour.data:02}:{self.minute.data:02}:{self.second.data:02} {self.meridium[self.flag]}'


def append(Start,value):
    if Start==None:
        Start=Node(value)
        Start.next=Start
    else:
        newnode=Node(value)
        end=Start
        while end.next!=Start:
            end=end.next
        end.next=newnode
        newnode.next=Start
    return Start

def create_CLL(th=1,tm=0,ts=0):
    global hourStart
    tm+=ts//60
    ts%=60
    th+=tm//60
    tm%=60
    th=((th-1)%12)+1

    from copy import deepcopy
    secondStart=None
    minuteStart=None
    hourStart=None
    for i in range(60):
        minuteStart=append(minuteStart,i)
    secondStart=deepcopy(minuteStart)
    for i in range(12):
        hourStart=append(hourStart,i+1)

    while (hourStart.data!=th or minuteStart.data!=tm or secondStart.data!=ts):
        if hourStart.data!=th:
            hourStart=hourStart.next
        elif minuteStart.data!=tm:
            minuteStart=minuteStart.next
        else:
            secondStart=secondStart.next
    obj=Clock(hourStart,minuteStart,secondStart)
    return obj
