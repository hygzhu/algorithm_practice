"""
LeetCode wants to give one of its best employees the option to travel among N cities to collect algorithm problems. But all work and no play makes Jack a dull boy, you could take vacations in some particular cities and weeks. Your job is to schedule the traveling to maximize the number of vacation days you could take, but there are certain rules and restrictions you need to follow.

Rules and restrictions:
You can only travel among N cities, represented by indexes from 0 to N-1. Initially, you are in the city indexed 0 on Monday.
The cities are connected by flights. The flights are represented as a N*N matrix (not necessary symmetrical), called flights representing the airline status from the city i to the city j. If there is no flight from the city i to the city j, flights[i][j] = 0; Otherwise, flights[i][j] = 1. Also, flights[i][i] = 0 for all i.
You totally have K weeks (each week has 7 days) to travel. You can only take flights at most once per day and can only take flights on each week's Monday morning. Since flight time is so short, we don't consider the impact of flight time.
For each city, you can only have restricted vacation days in different weeks, given an N*K matrix called days representing this relationship. For the value of days[i][j], it represents the maximum days you could take vacation in the city i in the week j.
You're given the flights matrix and days matrix, and you need to output the maximum vacation days you could take during K weeks.

Example 1:
Input:flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]
Output: 12
Explanation: 
Ans = 6 + 3 + 3 = 12. 

One of the best strategies is:
1st week : fly from city 0 to city 1 on Monday, and play 6 days and work 1 day. 
(Although you start at city 0, we could also fly to and start at other cities since it is Monday.) 
2nd week : fly from city 1 to city 2 on Monday, and play 3 days and work 4 days.
3rd week : stay at city 2, and play 3 days and work 4 days.
Example 2:
Input:flights = [[0,0,0],[0,0,0],[0,0,0]], days = [[1,1,1],[7,7,7],[7,7,7]]
Output: 3
Explanation: 
Ans = 1 + 1 + 1 = 3. 

Since there is no flights enable you to move to another city, you have to stay at city 0 for the whole 3 weeks. 
For each week, you only have one day to play and six days to work. 
So the maximum number of vacation days is 3.
Example 3:
Input:flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[7,0,0],[0,7,0],[0,0,7]]
Output: 21
Explanation:
Ans = 7 + 7 + 7 = 21

One of the best strategies is:
1st week : stay at city 0, and play 7 days. 
2nd week : fly from city 0 to city 1 on Monday, and play 7 days.
3rd week : fly from city 1 to city 2 on Monday, and play 7 days.
Note:
N and K are positive integers, which are in the range of [1, 100].
In the matrix flights, all the values are integers in the range of [0, 1].
In the matrix days, all the values are integers in the range [0, 7].
You could stay at a city beyond the number of vacation days, but you should work on the extra days, which won't be counted as vacation days.
If you fly from the city A to the city B and take the vacation on that day, the deduction towards vacation days will count towards the vacation days of city B in that week.
We don't consider the impact of flight hours towards the calculation of vacation days.
"""
import math

#Passes most tests, times out on later ones
#Inefficient because we are storing more dimensions of data than neccesary
def maxVacationDaysInefficient(flights, days):
    """
    :type flights: List[List[int]]
    :type days: List[List[int]]
    :rtype: int
    """
    numCities = len(flights)
    numWeeks = len(days[0])

    #Let M[k][i] denote the max vacation time at week k, where we have last stopped at city i
    M = []

    #Base case, initially we are at week 0 located in city 0 with no vacation time
    M.append([0] + [-math.inf]*(numCities-1))
    for _ in range(1, numWeeks+1):
        M.append([-math.inf]*(numCities))

    #k weeks, each possible plane trip needs to be considered
    for k in range(1, numWeeks+1):
        for i in range(0,numCities):
            for j in range(0, numCities):
                if flights[i][j] == 1:
                    M[k][j] = max(days[j][k-1] + M[k-1][i], M[k][j])
                elif i == j:
                    #Always consider just staying in the current city
                    M[k][j] = max(days[j][k-1] + M[k-1][j], M[k][j])
    
    return max(M[numWeeks] + [0])

#Still fails the same efficiency tests for some reason
#Time complexity: O(k*n*n) same as above
#Space complexity: O(k) better than before
def maxVacationDays(flights, days):
    """
    :type flights: List[List[int]]
    :type days: List[List[int]]
    :rtype: int
    """
    numCities = len(flights)
    numWeeks = len(days[0])

    #Let M[[i] be max vacation time where we have last stopped at city i

    #Base case, initially we are at week 0 located in city 0 with no vacation time
    M = [0] + [-math.inf]*(numCities-1)

    #k weeks, each possible plane trip needs to be considered
    for k in range(1, numWeeks+1):
        MPrev = M.copy()
        for i in range(0,numCities):
            for j in range(0, numCities):
                if flights[i][j] == 1:
                    M[j] = max(days[j][k-1] + MPrev[i], M[j])
                elif i == j:
                    #Always consider just staying in the current city
                    M[j] = max(days[j][k-1] + MPrev[j], M[j])
    
    return max(M + [0])
                    
#print(maxVacationDays([[0,1,1],[1,0,1],[1,1,0]], [[1,3,1], [6,0,3], [3,3,3]]))                  
#print(maxVacationDays([[0,0,0],[0,0,0],[0,0,0]], [[1,1,1],[7,7,7],[7,7,7]]))
