import heapq
import random
import turtle
import numpy as np
import time


# verificare daca numarul de inversiuni este par/impar
def is_solvable(state):
    inversions = 0
    for i in range(8):
        for j in range(i + 1, 9):
            if state[i] and state[j] and state[i] > state[j]:
                inversions += 1
    print("Numarul  de inversiuni este", inversions)
    return inversions % 2 == 0


# determinarea distanței Manhattan între două poziții
def manhattan_distance(pos1, pos2):
    x1, y1 = pos1 // 3, pos1 % 3
    x2, y2 = pos2 // 3, pos2 % 3
    return abs(x1 - x2) + abs(y1 - y2)


# Funcție pentru a genera vecinii unei stări
def generate_neighbors(state):
    neighbors = []
    empty_index = state.index(0)
    possible_moves = [1, -1, 3, -3]  # Mutări posibile: dreapta, stânga, jos, sus
    for move in possible_moves:
        new_index = empty_index + move
        if 0 <= new_index < 9:
            neighbor = list(state)
            neighbor[empty_index], neighbor[new_index] = neighbor[new_index], neighbor[empty_index]
            neighbors.append(neighbor)
    return neighbors


# Funcție pentru a calcula costul estimat al drumului de la nodul curent la nodul scop
def heuristic_cost(state):
    total_cost = 0
    for i, value in enumerate(state):
        if value != 0:
            total_cost += manhattan_distance(i, value - 1)
    return total_cost


def solve_puzzle(start_state):
    if not is_solvable(start_state):
        print("Puzzle-ul nu poate fi rezolvat!")
        return

    goal_state = [1, 2, 3,
                  4, 5, 6,
                  7, 8, 0]  # Starea scop

    open_list = []
    closed_set = set()

    # Tuplu de forma (cost_g + cost_h, cost_g, state, path)
    start_node = (heuristic_cost(start_state), 0, start_state, [])
    heapq.heappush(open_list, start_node)

    # Initialize turtle
    window = turtle.Screen()
    window.bgcolor("blue")

    turtle.speed(0)
    turtle.penup()
    turtle.hideturtle()

    # Define square size and spacing
    square_size = 120
    spacing = 15

    while open_list:
        current_node = heapq.heappop(open_list)
        current_state = current_node[2]
        current_path = current_node[3]

        if current_state == goal_state:
            print("Puzzle-ul se rezolva astfel:")
            print("Numărul de mutări:", len(current_path))
            for state in current_path:
                print("Noua stare:")
                print(np.reshape(state, (3, 3)))
                # Draw current state
                turtle.clear()
                turtle.setpos(-square_size - spacing, square_size + spacing)
                turtle.pendown()
                for i in range(9):
                    if state[i] != 0:
                        turtle.write(state[i], font=("Arial", 35, "bold"))
                    else:
                        turtle.color("blue")
                        turtle.begin_fill()
                        for j in range(4):
                            turtle.forward(square_size)
                            turtle.right(90)
                        turtle.end_fill()
                        turtle.color("black")
                    if (i + 1) % 3 == 0:
                        turtle.penup()
                        turtle.setx(-square_size - spacing)
                        turtle.sety(turtle.ycor() - square_size - spacing)
                        turtle.pendown()
                    else:
                        turtle.penup()
                        turtle.setx(turtle.xcor() + square_size + spacing)
                        turtle.pendown()

                turtle.getcanvas().update()
                time.sleep(4)  # pauză de 4 secunde între afișarea fiecărei stări noi
            return

        closed_set.add(tuple(current_state))

        neighbors = generate_neighbors(current_state)
        for neighbor_state in neighbors:
            if tuple(neighbor_state) in closed_set:
                continue

            neighbor_path = current_path + [neighbor_state]
            cost_g = len(neighbor_path)
            cost_h = heuristic_cost(neighbor_state)
            total_cost = cost_g + cost_h
            neighbor_node = (total_cost, cost_g, neighbor_state, neighbor_path)
            heapq.heappush(open_list, neighbor_node)

    print("Nu s-a găsit soluție!")


# generare pozitie initiala aleatoare
start_state = random.sample(range(9), 9)
print("Starea initiala: ")
for i in range(0, 9, 3):
    print(start_state[i:i + 3])
solve_puzzle(start_state)
