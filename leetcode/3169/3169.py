class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        before_meeting = meetings[0]
        temp_meetings = []
        for i, meeting in enumerate(meetings):
            if (i != 0) and ((meeting[0] <= before_meeting[1] and meeting[0] >= before_meeting[0]) or (before_meeting[0] <= meeting[1] and before_meeting[0] >= meeting[0])):
                merged_meeting = []
                merged_meeting.extend(before_meeting)
                merged_meeting.extend(meeting)
                merged_meeting.sort()
                temp_meetings.pop()
                temp_meetings.append([merged_meeting[0], merged_meeting[-1]])
                before_meeting = [merged_meeting[0], merged_meeting[-1]]
            else:
                temp_meetings.append(meeting)
                before_meeting = meeting
        
        for temp_meeting in temp_meetings:
            days -= (temp_meeting[1] - temp_meeting[0] + 1)
            
        return days

        