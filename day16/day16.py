import sys
import time
from typing import List

def main(input):
    print("Start")
    #start = time.time()
    global sep
    global valves
    sep = [" ", ";", ",", "="]

    lines = []
    with open(input) as file:
        lines = file.readlines()

    valve_model = {
            "flow_rate": 0,
            "connected_to_valves": []}
    valves = {}

    for line in lines:
        valve_model = {}
        valve_name = line.split(sep[1])[0].split(sep[0])[1]
        flow_rate = int(line.split(sep[1])[0].split(sep[3])[1])
        connected_to_valves = line.split(sep[1])[1].split(sep[0])[5:]
        connected_to_valves = [valve.replace(",","") for valve in connected_to_valves]
        connected_to_valves = [valve.strip() for valve in connected_to_valves]
        valve_model["flow_rate"] = flow_rate
        valve_model["connected_to_valves"] = connected_to_valves
        valves[valve_name] = valve_model

    print(find_cost_of_move("AA","JJ"))
    
    #find start point
    #set start time as time_left: int in minutes
    #sort valves after flow_rate
    #find path to next valve
    #turn on valve
    #find next valve
    #do until time is 0

    #find shortest path to a valve from a specific valve. return cost
    #return cost

def find_cost_of_move(start, goal):
    cost = 0
    current_valve = start
    possible_paths = valves[current_valve]["connected_to_valves"]
    for path in possible_paths:
        #something recursive here
        pass
    print(possible_paths)
    if goal in possible_paths:
        return cost



def find_next_valve(not_used_valves: List, used_valves: List):
    next_valve = ""
    flow_rate = 0
    for valve in not_used_valves:
        if valves[valve]["flow_rate"] > flow_rate and valve not in used_valves:
            flow_rate = valves[valve]["flow_rate"]
            next_valve = valve
    return next_valve

if __name__ == "__main__":
    main(sys.argv[1])