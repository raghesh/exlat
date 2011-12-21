#!/usr/bin/env python

def getListofDictionary(List, EventName):
  EventCount = List.count(EventName)
  EventsList = []
  End = 0
  for EventIndex in range(0, EventCount):
    Dict = {}
    Start = List.index(EventName, End)
    End = List.index('SUMMARY', Start)
    KeyIndex = Start + 2
    for Entry in List[Start + 1:End:2]:
      Dict[Entry] = List[KeyIndex]
      KeyIndex += 2
    EventsList.append(Dict)

  return EventsList

F = open("basic.ics")
Content = F.read()
NewContent = Content.replace('\r\n', ':')
List = NewContent.split(':')
print getListofDictionary(List, 'Compiler Class')
