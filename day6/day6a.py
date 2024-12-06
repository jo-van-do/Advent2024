map = []
x = -1

with open('day6\data6.txt', 'r') as f:
    for line in f.read().split('\n'):
        map.append(list(line))
        x += 1
        if '^' in line:
            y = line.index('^')
            begin = (x,y)
f.close()


class Agent:
    def __init__(self, position, map, direction):
        self.position = position
        self.map = map
        self.direction = direction
        self.finished = False
    
    def next_step(self):
        """
        Moves agent one step in the current direction
        """
    
        # get position of the agent
        (posX , posY) = self.position
    
        # UP
        if self.direction == 'up':
            posX = posX - 1
        # LEFT
        elif self.direction == 'left':
            posY = posY - 1
        # RIGHT
        elif self.direction == 'right':
            posY = posY + 1
        # DOWN
        elif self.direction == 'down':
            posX = posX + 1
        
        next_pos = (posX, posY)
    
        return next_pos
    
        
    def is_blocked(self, next_pos):
        """
        Checks if current agent position is possible.
            If possible: move into same directoin.
            If not possible: finish or change direction.
        """
        blocked = False
        
        (posX , posY) = next_pos
        
        if (posX < 0) or (posX == len(map)) or (posY < 0) or (posY == len(map[0])):
            self.finished = True
            
        elif map[posX][posY] == '#':
            blocked = True
            
        return blocked
    
    def change_direction(self):
        """
        Rotates agent to the right
        """
        if self.direction == 'up':
            new_direction = 'right'
        elif self.direction == 'right':
            new_direction = 'down'
        elif self.direction == 'down':
            new_direction = 'left'
        elif self.direction == 'left':
            new_direction = 'up'
            
        self.direction = new_direction
    
    def mark_map(self):
        """
        Mark the path agent takes

        """
        (posX, posY) = self.position
        self.map[posX][posY] = 'X'
    
    def visualise_map(self):
        """
        Save map with agent route
        """
        with open(".\day6\\route.txt", "w") as output:
            for line in self.map:
                for value in line:
                    output.write(value)
                output.write('\n')
                
        return self.map
    
    
    def count_positions(self):
        """
        Count all distinct positions that the agent has visited

        """
        count = 0
        for row in self.map:
            count += row.count('X')
    
        return count

    def play(self):
        """
        Let's agent walk in environment until he walks out.
        """
        
        while self.finished == False:
            self.mark_map()
            next_pos = self.next_step()
            
            while self.is_blocked(next_pos):
                self.change_direction()
                next_pos = self.next_step()
            
            self.position = next_pos
        
        print(self.count_positions())
            
 

ag = Agent(position=begin, map=map, direction='up')
ag.play()
ag.visualise_map()
