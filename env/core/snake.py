import numpy as np

from settings.constants import DIRECTIONS, SNAKE_BLOCK


class Snake:
    def __init__(self, head_position, direction_index, length):
        """
        @param head_position: tuple
        @param direction_index: int
        @param length: int
        """
        # Information snake need to know to make the move
        self.snake_block = SNAKE_BLOCK
        self.current_direction_index = direction_index
        # Alive identifier
        self.alive = True
        # Place the snake
        self.blocks = [head_position]
        current_position = np.array(head_position)
        for i in range(1, length):
            # Direction inverse of moving
            current_position = current_position - DIRECTIONS[self.current_direction_index]
            self.blocks.append(tuple(current_position))

    def step(self, action):
        """
        @param action: int
        @param return: tuple, tuple
        """
        # Check if action can be performed (do nothing if in the same direction or opposite)
        if (DIRECTIONS[action][0] != DIRECTIONS[self.current_direction_index][0]) and \
                (DIRECTIONS[action][1] != DIRECTIONS[self.current_direction_index][1]) and \
                (DIRECTIONS[action][0] != -DIRECTIONS[self.current_direction_index][0]) and \
                (DIRECTIONS[action][1] != -DIRECTIONS[self.current_direction_index][1]):
            self.current_direction_index = action
        # Remove tail
        tail = self.blocks[:-1]
        self.blocks = self.blocks[0]
        # Check new head
        new_head = [self.blocks] + DIRECTIONS[self.current_direction_index]
        # Add new head
        self.blocks = [new_head[0]]
        for i in tail:
            self.blocks.append(i)
        new_head = new_head[0]
        return new_head, tail
