import numpy as np
import random

class QLearningAgent:
    def __init__(self, actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0, exploration_decay=0.99):
        self.actions = actions  # ["buy", "sell"]
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay
        self.q_table = {}  # Q-values are stored in a dictionary with (state, action) as keys
    
    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def choose_action(self, state):
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < self.exploration_rate:
            return random.choice(self.actions)
        else:
            q_values = [self.get_q_value(state, action) for action in self.actions]
            max_q_value = max(q_values)
            return self.actions[q_values.index(max_q_value)]

    def learn(self, state, action, reward, next_state):
        current_q_value = self.get_q_value(state, action)
        next_max_q_value = max([self.get_q_value(next_state, a) for a in self.actions])

        # Update Q-value using the Q-learning formula
        new_q_value = (1 - self.learning_rate) * current_q_value + self.learning_rate * (
            reward + self.discount_factor * next_max_q_value
        )
        self.q_table[(state, action)] = new_q_value

        # Decay exploration rate
        self.exploration_rate *= self.exploration_decay
