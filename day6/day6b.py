import copy

map = []
x = -1

with open('day6\\data6.txt', 'r') as f:
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
        self.begin_pos, self.begin_dir = position, direction
        self.map = map
        self.direction = direction
        self.finished = False
        self.obs_locs = []

    def next_step(self):
        """
        Moves agent one step in the current direction
        """
    
        # get position of the agent
        (posX , posY) = self.position
    
        if self.direction == 'up':
            posX = posX - 1
            
        elif self.direction == 'left':
            posY = posY - 1

        elif self.direction == 'right':
            posY = posY + 1
 
        elif self.direction == 'down':
            posX = posX + 1
        
        next_pos = (posX, posY)
    
        return next_pos
    
        
    def is_blocked(self, next_pos, map):
        """
        Checks if current agent position is possible.
            If possible: move into same directoin.
            If not possible: finish or change direction.
        """
        self.blocked = False
        
        (posX , posY) = next_pos
        
        if (posX < 0) or (posX == len(map)) or (posY < 0) or (posY == len(map[0])):
            if self.loop_check == True:
                self.loop_check = False
                return
            else:
                self.finished = True
                return
            
        elif map[posX][posY] == '#':
            self.blocked = True
            
        return self.blocked
    
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
        
        if (self.direction == 'up') or (self.direction == 'down'):
            
            if self.map[posX][posY] in ['.','^']:
                self.map[posX][posY] = '|'
                
            elif (self.map[posX][posY]) == '_' :
                self.map[posX][posY] = '+'
         
        elif (self.direction == 'right') or (self.direction == 'left'):
            
            if self.map[posX][posY] in ['.','^']:
                self.map[posX][posY] = '_'
                
            elif (self.map[posX][posY] == '|'):
                self.map[posX][posY] = '+'
        
    
    
    def visualise_map(self):
        """
        Save map with agent route
        """
        with open("test.txt", "w") as output:
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
    
    def check_loop(self,obstacle):
        """
        Check if placing an object in front of agent will result in a loop
        """
        found_loop = False
        visited = {}

        (obsX , obsY) = obstacle
        
        if (obsX < 0) or (obsX == len(map)) or (obsY < 0) or (obsY == len(map[0])) or (obstacle == self.begin_pos):
            self.loop_check = False
            return
        else:
            self.loop_check = True
            temp_map = copy.deepcopy(self.map)
            
            if temp_map[obsX][obsY] == '#':
                self.loop_check = False
                return
            else:
                temp_map[obsX][obsY] = '#'
        
        while (found_loop == False) and (self.loop_check == True):
            next = self.next_step()
            
            while self.is_blocked(next, temp_map):

                self.change_direction()
                next = self.next_step()
                
            self.position = next

            if self.position not in visited:
                visited[self.position] = [self.direction]
            elif self.direction not in visited[self.position]:
                visited[self.position].append(self.direction)
            elif self.direction in visited[self.position]:
                if obstacle not in self.obs_locs:
                    self.obs_locs.append(obstacle)
                found_loop = True

        self.loop_check = False

        return found_loop
    
    def get_coords(self):
        """
        Save coordinates where obstacles might be placed BEFORE guard begins his whole route
        """
        
        self.loop_check = False
        
        coords = []
        
        while self.finished == False:
            next_pos = self.next_step()
            
            while self.is_blocked(next_pos,self.map):
                self.change_direction()
                next_pos = self.next_step()
            
            self.position = next_pos
            if self.position not in coords:
                coords.append(self.position)
        
        return coords
  
    
    def hinder_agent(self):
        """
        Let's agent walk in environment until he walks out.
        Return amount of loops could be made by placing objects on agent's path
        """
        
        coords = self.get_coords()

        for obstacle in coords:

            self.position = self.begin_pos
            self.direction = self.begin_dir
  
            self.check_loop(obstacle)
                
        print('amount of obstacles:', len(self.obs_locs))
                 
 

ag = Agent(position=begin, map=map, direction='up')
ag.hinder_agent()

