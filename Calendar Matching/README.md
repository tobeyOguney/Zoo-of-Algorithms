## Calendar Matching

Imagine that you want to schedule a meeting of a certain duration with a coworker. You have access to your calendar and your coworker's
calendar (both of which contain your respective meetings for the day, in the form of [startTime, endTime]), as well as both of your daily
bounds (i.e., the earliest and latest times at which you're available for meetings every day, in the form of [earliestTime, latestTime]). Write a
function that takes in your calendar, your daily bounds, your coworker's calendar, your coworker's daily bounds, and the duration of the
meeting that you want to schedule, and that returns a list of all the time blocks (in the form of [startTime, endTime]) during which you could
schedule the meeting. Note that times will be given and should be returned in military time (example times: '8:30', '9:01', '23:56').

Sample input:
```
[['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
['9:00', '20:00']
[['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
['10:00', '18:30']
30
```

Sample output:
```
[['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
```
