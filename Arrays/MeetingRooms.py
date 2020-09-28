# Meeting Rooms

'''
Given two sets of available time slots for two people,
find the first possible meeting time that is at least
'duration' minutes long.

Example:
    slotsA = [[10, 50], [60, 120], [140, 210]]
    slotsB = [[0, 15], [60, 70]]
    duration = 8
'''


def findMeeting(slotsA, slotsB, dur):
    # slotsA: available time slots for person A, array of pairs
    # slotsB: available time slots for person B, array of pairs
    # dur: length of meeting needed, integer

    overlaps = []
    for slotA in slotsA:
        for slotB in slotsB:
            startA, endA = slotA
            startB, endB = slotB
            if startB >= startA and startB <= endA:
                slot_dur = (endB if endB < endA else endA) - startB
                if slot_dur >= dur:
                    overlaps.append((startB, startB + dur))
            elif endB >= startA and endB <= endA:
                slot_dur = endB - startA
                if slot_dur >= dur:
                    overlaps.append((startA, startA + dur))
    print(overlaps)
    return overlaps[0]

slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
duration = 8
findMeeting(slotsA, slotsB, duration)
