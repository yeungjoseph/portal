class Date:
    #mmddyyyy is a 3-tuple of ints, begin_time (military time- hhmm), end_time (hhmm), and description are str
    def __init__(self, mmddyyyy, begin_time, end_time, description):
        self.mmddyyyy = mmddyyyy
        self.begin_time = begin_time
        self.end_time = end_time
        self.description = description
        
        
class Calendar:
    def __init__(self, list_of_events):
        self.events = list_of_events
        
    def calculate_collisions(self):
        num_events = len(self.events)
        collisions = set()
        for index in range(num_events):
            for index2 in range(index+1,num_events):
                event1 = self.events[index]
                event2 = self.events[index2]
                if event1.mmddyyyy == event2.mmddyyyy:
                    if event2.begin_time <= event1.begin_time < event2.end_time or\
                    event1.begin_time <= event2.begin_time < event1.end_time:
                        #collisions.append((event1.description,event2.description))
                        collisions.add(event1.description)
                        collisions.add(event2.description)
        return list(collisions)

def main():
    datelist = [Date((2,23,2017),1500,1600,'Interview at The Portal'),
                Date((2,25,2017),1200,1300,'Lunch with Cindy'),
                Date((2,24,2017),1700,1730,'Dinner with John'),
                Date((2,24,2017),1100,1730,'Conference'),
                Date((2,24,2017),1200,1300,'Stuff1'),
                Date((2,25,2017),1200,1300,'Stuff2'),
                Date((2,23,2017),1600,1700,'Stuff3'),
                Date((2,23,2017),1530,1600,'Stuff4'),
                Date((2,23,2017),1700,1800,'SDFDSF')]
    c = Calendar(datelist)
    print(c.calculate_collisions())
    
if __name__ == '__main__':
    main()
