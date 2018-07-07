class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tickets.sort(key=lambda x: x[1])
        for i in range(len(tickets)):
            tickets[i].append(False)

        def traverse(start, itinerary):
            if len(itinerary) == len(tickets)+1:
                return itinerary
            else:
                arrivals = [x[1] for x in tickets if x[0] == start and x[2] is False]
                for arrival in arrivals:
                    itinerary.append(arrival)
                    i = tickets.index([start, arrival, False])
                    tickets[i][2] = True
                    something = traverse(arrival, itinerary)
                    if something:
                        return something
                    itinerary.pop()
                    tickets[i][2] = False
                return None

        return traverse('JFK', ['JFK'])

print(Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))