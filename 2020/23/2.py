cups = "135468729"
cups = [int(cup) for cup in cups]

min_value = min(cups)
max_initial_value = max(cups)
max_value = 1000000
max_moves = 10000000

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = int(value)
        self.next = next
    def __repr__(self):
        return f"({self.value})"

# Building the circular linked list
nodes = [Node(int(cup)) for cup in cups]

for i in range(max_initial_value+1, max_value+1):
    nodes.append(Node(i))

for i in range(0,len(nodes)-1):
    nodes[i].next = nodes[i+1]
nodes[-1].next = nodes[0]   # Wrap the circular linked list

lookup_map = {}
for node in nodes:
    lookup_map[node.value] = node

moves = 1
current = nodes[0]
while moves <= max_moves:
    pickup_1 = current.next
    pickup_2 = pickup_1.next
    pickup_3 = pickup_2.next

    current.next = pickup_3.next
    pickup = [pickup_1.value, pickup_2.value, pickup_3.value]
    destination_value = current.value - 1

    while (destination_value in pickup or destination_value < min_value):
        if(destination_value in pickup):
            destination_value -= 1
        if(destination_value < min_value):
            destination_value = max_value

    destination = lookup_map[destination_value] # Find destination node in lookup hashmap
    pickup_3.next = destination.next            # Node next of destination node will be inserted after pickup_3
    destination.next = pickup_1                 # Insert pickup_1 node after destination

    current = current.next
    moves += 1

target_node = lookup_map[1]
print(target_node.next.value * target_node.next.next.value)