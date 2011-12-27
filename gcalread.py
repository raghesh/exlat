#!/usr/bin/env python
import sys

def getListofDictionary(List, EventName):
  """Get a list of dictionaries. Each dictionary
     corresponds to a record of a single event
     with EventName as SUMMARY.
  """
  EventCount = List.count(EventName)
  EventsList = []
  End = 0

  # Iterate through all the records with SUMMARY = EventName
  for I in range(0, EventCount):
    Dict = {}

    # Get the start and end indices of a single record
    EventIndex = List.index(EventName, End)
    Start = EventIndex - (List[EventIndex:0:-1].index('BEGIN'))
    End = List.index('END', EventIndex)
    KeyIndex = Start + 1

    for Entry in List[Start:End:2]:
      Dict[Entry] = List[KeyIndex]
      KeyIndex += 2
    EventsList.append(Dict)

  return EventsList

if len(sys.argv) != 3:
  print "Usage: ./gcalread.py <.ics file> <SUMMARY String>"
  sys.exit(0)

ICSFile = sys.argv[1]
SummaryString = sys.argv[2]
F = open(ICSFile)
Content = F.read()
NewContent = Content.replace('\r\n', ':')
List = NewContent.split(':')
print getListofDictionary(List, SummaryString)
