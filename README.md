Data structure/model:
I used classes with appropriate methods/attributes to visualize the data I'm working with and to encapsulate
data. I created a Calendar to store a list of Dates and I wrote a method in the Calendar class to calculate
all the collisions of dates. Ideallly I would have

***THE WRITING BELOW IS ADDED AFTER TIME UP***
Ideally I would have had a method in my Date class called isColission(date1,date2) that takes two Dates as arguments to determine if there is a collision. And then in my Calendar class I would have written a method find_all_collisions and looped through all the dates, calling isColission for each date, which would allow for simpler and more easily debuggable functions. Finally, I chose to use classes because I knew that I would have to return the name of any event that had a collision (based on its time), so the easiest way to work with an object consisting of multiple properties such as time, date, and name was to use classes.

Input:
I chose to use a three-tuple to store my date because it could be easily compared for equality. I chose to use military time as input for time because it allowed me to do integer arithmetic without any parsing. These two decisions saved me a lot of time while writing my algorithm.

Algorithm:
I began by using heuristics to do a quick check to see if the dates were the same. If not, then there is guaranteed to be no collision.
I ran out of time before I was able to test my code due to some technical difficulties, but the idea of the algorithm is that if Event A begins after Event B begins and before Event B finishes, then there must be a colission. The same check is done when the events are flipped (Event B begins after Event A begins and before event A finishes). With these two checks, it accounts for the following situations:
1. A_start B_start A_end => Colission (it doesn't matter where B ends)
2. B_start A_start B_end => Colission (it doesn't matter where A ends)
In all other situations, there will be no colissions.

Test cases:
If I had time to create better test cases, I would have tested edge cases such as would an event that started at 4:30pm and ended at 5:00pm collide with an event that started at 5:00pm and ended at 6:00pm. While I did not test this, I accounted for this situation in my code by making sure I used the "less than" operator when searching for colissions so that I would only find a colission when the next event started strictly before the first event ended.
