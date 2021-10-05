'''
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 
 Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".


Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
'''

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        A= []
        B = []
        for i in paths:
            A.append(i[0])
            B.append(i[1])
        for i in B:
            if i not in A:
                return i

# class Solution:
#     def destCity(self, paths: List[List[str]]) -> str:
#         outgoing = {}
#         for path in paths:
#             city_a, city_b = path
#             outgoing[city_a] = outgoing.get(city_a, 0) +1
#             outgoing[city_b] = outgoing.get(city_b, 1)
#         for city in outgoing:
#             if outgoing[city] == 0:
#                 return city    


