################################################################################
# Copyright 2012 ExLat Team                                                    #
#                                                                              #
# This file is part of ExLat.                                                  #
#                                                                              #
# ExLat is free software: you can redistribute it and/or modify it             #
# under the terms of the GNU General Public License as published by            #
# the Free Software Foundation, either version 3 of the License, or at         #
# your option) any later version.                                              #
#                                                                              #
# ExLat is distributed in the hope that it will be useful, but                 #
# WITHOUT ANY WARRANTY; without even the implied warranty of                   #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU General Public License for more details.                                 #
#                                                                              #
# You should have received a copy of the GNU General Public License            #
# along with ExLat.  If not, see <http://www.gnu.org/licenses/>.               #
################################################################################

#!/usr/bin/env python
import sys
import exchange as E

def getListofDictionary(List, EventName):
  """Get a list of dictionaries. Each dictionary
     corresponds to a record of a single event
     with EventName as SUMMARY. Empty list will be
     returned if EventName is not found.
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
      # FIXIT: If the event in the calender is not part of a series of events
      # the dates strings are different. That is if the event is planned as an
      # extra event
      if Entry == 'DTSTART;TZID=Asia/Calcutta':
        Dict['Start Date'] = List[KeyIndex]
      if Entry == 'DTEND;TZID=Asia/Calcutta':
        Dict['End Date'] = List[KeyIndex]
      if Entry == 'DESCRIPTION':
        Dict['Topic'] = List[KeyIndex]
      KeyIndex += 2
    EventsList.append(Dict)

  return EventsList

if len(sys.argv) != 3:
  print "Usage: ./gcalread.py <.ics file> <SUMMARY String>"
  sys.exit(1)

ICSFile = sys.argv[1]
SummaryString = sys.argv[2]
F = open(ICSFile)
Content = F.read()
NewContent = Content.replace('\r\n', ':')
List = NewContent.split(':')
ListOfDict = getListofDictionary(List, SummaryString)
TableList = ListOfDict
print TableList

Obj = E.ExportToLatex()
TableString = Obj.createLatexTable(TableList)
Obj.createOutputString(TableString)
Obj.createLatexFile()

#Clearing Memory
del Obj
