# Simple AI Robot Simulation in Python
# Inspired by ethical hacking principles: secure, modular, and validated code
# Author: Conceptual design, not attributed to any specific individual

import random
import time

class AIRobot:
    def __init__(self, name="AI_Robot", position=(0, 0)):
        """Initialize the AI robot with a name and starting position."""
        self.name = self._sanitize_input(name)
        self.position = position  # (x, y) coordinates
        self.battery = 100  # Battery percentage
        self.is_active = True
        print(f"{self.name} initialized at position {self.position}")

    def _sanitize_input(self, input_str):
        """Validate and sanitize input to prevent injection-like issues."""
        if not isinstance(input_str, str) or not input_str.strip():
            return "Default_Robot"
        # Remove potentially harmful characters (ethical hacking principle)
        return ''.join(c for c in input_str if c.isalnum() or c in ['_', ' '])

    def move(self, direction):
        """Move the robot in the specified direction with AI decision-making."""
        if not self.is_active:
            print(f"{self.name} is out of battery or deactivated!")
            return

        directions = {
            "up": (0, 1),
            "down": (0, -1),
            "left": (-1, 0),
            "right": (1, 0)
        }

        if direction not in directions:
            print(f"Invalid direction: {direction}. Choose from {list(directions.keys())}")
            return

        # Simulate AI decision: Check for obstacles (randomly generated for demo)
        if random.random() < 0.2:  # 20% chance of obstacle
            print(f"Obstacle detected! {self.name} avoids it.")
            self._consume_battery(5)
            return

        # Update position
        dx, dy = directions[direction]
        new_position = (self.position[0] + dx, self.position[1] + dy)

        # Boundary check (ethical hacking: prevent out-of-bounds errors)
        if not (-10 <= new_position[0] <= 10 and -10 <= new_position[1] <= 10):
            print(f"Cannot move {direction}: Out of bounds!")
            return

        self.position = new_position
        self._consume_battery(10)
        print(f"{self.name} moved {direction} to {self.position}")

    def _consume_battery(self, amount):
        """Simulate battery consumption."""
        self.battery -= amount
        if self.battery <= 0:
            self.battery = 0
            self.is_active = False
            print(f"{self.name} battery depleted!")
        else:
            print(f"Battery level: {self.battery}%")

    def scan_environment(self):
        """Simulate AI scanning for nearby objects (random for demo)."""
        if not self.is_active:
            print(f"{self.name} is deactivated!")
            return

        objects = ["nothing", "wall", "item", "enemy"]
        detected = random.choice(objects)
        print(f"{self.name} scans environment: Detected {detected}")
        self._consume_battery(5)

def main():
    # Create an AI robot instance
    robot = AIRobot(name="Sabaz_AI_Robot")

    # Simulate robot actions
    actions = ["move up", "move right", "scan", "move left", "move down", "scan"]
    
    for action in actions:
        if not robot.is_active:
            break
        time.sleep(1)  # Simulate processing time
        if action.startswith("move "):
            robot.move(action.split()[1])
        elif action == "scan":
            robot.scan_environment()
        else:
            print(f"Unknown action: {action}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Ethical hacking principle: Graceful error handling
        print(f"Error occurred: {e}")