import numpy as np
import random

class QLearning:

    def __init__(self, shape=(81,4), learning_rate=0.85, discount=0.9, epsilon = 0.9):
        assert 0 < learning_rate < 1, "Learning rate must be between 0 and 1, exclusive"
        assert 0 < discount < 1, "Discount factor must be between 0 and 1, exclusive"

        self.learning_rate = learning_rate
        self.discount = discount
        self.epsilon = epsilon
        self.table = np.zeros(shape)

    def update(self, s_now, a_now, reward, s_next):
        self.table[s_now][a_now] += self.learning_rate * self.__get_temporal_diff(s_now, a_now, reward, s_next)

    def __get_temporal_diff(self, s_now, a_now, reward, s_next):
        return self.__get_td_target(reward, s_next) - self.table[s_now][a_now]

    def __get_td_target(self, reward, s_next):
        return reward + self.discount * np.max(self.table[s_next])

    def get_action(self, s_now):
        if random.random() > self.epsilon:
            return random.randint(0, 3)

        actions = self.table[s_now]
        max_reward = np.max(actions)

        max_actions = []

        for i in range(0, 4):
            if actions[i] == max_reward:
                max_actions.append(i)

        return random.choice(max_actions)