# Monkey Banana Problem using Goal Stack Planning

# Initial State
state = {
    "monkey_at": "door",
    "box_at": "window",
    "monkey_on_floor": True,
    "monkey_on_box": False,
    "box_under_banana": False,
    "has_banana": False
}

# Goal Stack
goal_stack = ["has_banana"]

print("Initial State:")
print(state)
print("\nGoal:", goal_stack[0])
print("\nPlan:")

while goal_stack:

    goal = goal_stack.pop()

    # Goal: Monkey has bananas
    if goal == "has_banana":

        if state["has_banana"]:
            continue

        # Conditions required to get bananas
        goal_stack.append("grasp_banana")
        goal_stack.append("monkey_on_box")

    # Goal: Monkey is on the box
    elif goal == "monkey_on_box":

        if state["monkey_on_box"]:
            continue

        goal_stack.append("climb_box")
        goal_stack.append("box_under_banana")

    # Goal: Box is under the banana
    elif goal == "box_under_banana":

        if state["box_under_banana"]:
            continue

        goal_stack.append("push_box")
        goal_stack.append("monkey_at_window")

    # Goal: Monkey is at window
    elif goal == "monkey_at_window":

        if state["monkey_at"] == "window":
            continue

        goal_stack.append("move_to_window")

    # Actions
    elif goal == "move_to_window":

        state["monkey_at"] = "window"
        print("1. Monkey moves from door to window.")

    elif goal == "push_box":

        if state["monkey_at"] == "window":
            state["box_at"] = "under_banana"
            state["box_under_banana"] = True
            print("2. Monkey pushes the box under the bananas.")

    elif goal == "climb_box":

        if state["box_under_banana"]:
            state["monkey_on_floor"] = False
            state["monkey_on_box"] = True
            print("3. Monkey climbs onto the box.")

    elif goal == "grasp_banana":

        if state["monkey_on_box"]:
            state["has_banana"] = True
            print("4. Monkey grasps the bananas.")

print("\nFinal State:")
print(state)

if state["has_banana"]:
    print("\nGoal Achieved: Monkey has the bananas!")
else:
    print("\nGoal not achieved.")



OUTPUT

Initial State:
{'monkey_at': 'door', 'box_at': 'window', 'monkey_on_floor': True, 'monkey_on_box': False, 'box_under_banana': False, 'has_banana': False}

Goal: has_banana

Plan:
1. Monkey moves from door to window.
2. Monkey pushes the box under the bananas.
3. Monkey climbs onto the box.
4. Monkey grasps the bananas.

Final State:
{'monkey_at': 'window', 'box_at': 'under_banana', 'monkey_on_floor': False, 'monkey_on_box': True, 'box_under_banana': True, 'has_banana': True}

Goal Achieved: Monkey has the bananas!
