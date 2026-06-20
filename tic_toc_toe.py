class Game_statues:

    def __init__(self):
        self.board_setup()

    def board_setup(self):
        self.x_spaces = [0,1,1,
                         1,1,0,
                         0,0,0]  
        self.o_spaces = [1,0,0,
                         0,0,1,
                         1,0,0] 
        
                        
        
        self.statue = [self.x_spaces,self.o_spaces]
        self.winner = None

        print("here")
        self.test1(self.statue)
        print("here")

    def terminal(self,statue):#returns end state and who won
        #checks player who just moved
        turn = not self.Turn(self.statue)
        player = statue[turn]
        winner = self.Evaluation(turn)

        #victory statues 
        for row in range(3):
            #rows 
            if player[0 + row*3] + player[1 + row*3]+ player[2 + row*3] == 3:
                return [1,winner]
            #columns
            if player[0+row]+player[3+row]+player[6+row] == 3:
                return [1,winner]

        #diagonals 
        if player[4]:
            if player[0] and player[8]:
                return [1,winner]
                
            else:
                if player[2] and player[6]:
                    return [1,winner]
        #draw statues
        if sum(statue[0] + statue[1]) == len(statue[0]): 
            return [1,0]
        
        #if not terminal statue 
        return [0,0]

    def Actions(self,statue):#tested
        legal_moves = []
        for spaces in range(len(statue[0])):
            if statue[0][spaces] == 0 and statue[1][spaces] == 0:
                legal_moves.append(spaces)

        return legal_moves

    def Result(self,statue,action): #tested
        #returns game statue after speciffed action is applied
        bust = statue[self.Turn(statue)][:]
        bust[action] = 1

        if not self.Turn(statue):
            sculpture = [bust,statue[1]]
        else:
            sculpture = [statue[0],bust]
        # works fine but only returns one player's statue
        return sculpture

    def Turn(self,statue):#tested
        return (sum(statue[0]) + sum(statue[1]))%2

    def Evaluation(self,turn): #tested
        if turn == 0:
            return 1
        else:
            return -1

    def MaxValue(self,statue):#i think they work
        terminal,winner=self.terminal(statue)
        if terminal:
            return [winner,None]
        value = -1000000

        for action in self.Actions(statue):
            prevalue = value 
            value = max(value,self.MinValue(self.Result(statue,action))[0])
            if value != prevalue:
                BestAction = action
        return [value,BestAction]
    
    def MinValue(self,statue):#i think they work
        terminal,winner=self.terminal(statue)
        if terminal:
            return [winner,None]
        value = 1000000

        for action in self.Actions(statue):
            prevalue = value 
            value = min(value,self.MaxValue(self.Result(statue,action))[0])
            if value != prevalue:
                BestAction = action
        return [value,BestAction]

    # def FindBestMoveX(self,statue):
    #     if not self.Turn(statue):
    #         Bestvalue = -1000000
    #         bestMove = None 
    #         for action in self.Actions(statue):

    #             value= self.MinValue(self.Result(statue,action))
    #             print(value)
    #             print("""
                    
                    
    #                     """)

    #             if Bestvalue < value:
    #                 Bestvalue = value
    #                 bestMove = action

    #     return bestMove

    def test1(self,statue):
            print(self.MinValue(statue))
            self.visual(statue)
    # def FindBestMoveO(self,statue):
    #     if self.Turn(statue):
    #         value = 1000000
    #         bestMove = None 
    #         for action in self.Actions(statue):
    #             value= min(value,self.MaxValue(self.Result(statue,action)))
    #             bestMove = action

    #     return bestMove
        


    def visual(self,statue):
        for mark in range(len(statue[0])):
            if mark%3 ==0:
                print("")
                if statue[0][mark] == 1:

                    print("x", end ="/")
                elif statue[1][mark] == 1:
                    print("o", end ="/")
                else:
                    print("#", end ="/")
            else:
                if statue[0][mark] == 1:

                    print("x", end ="/")
                elif statue[1][mark] == 1:
                    print("o", end ="/")
                else:
                    print("#", end ="/")
        print("")
        

    def test2(self,statue):
        pass
        # print(self.MinValue(self.statue))
        # print(self.MaxValue(self.statue))
        # self.visual(self.statue)
        # self.visual(self.Result(self.statue,0))
        # self.visual(self.Result(self.statue,7))
        # self.visual(self.statue)
        # if self.terminal(self.statue):
        #     print(self.Evaluation(self.statue))
            # self.visual(self.statue)
        # self.visual(self.statue)
        # self.Actions(self.statue)
        # self.Turn(self.statue)



class node:
    def __init__(self,state,prev_action,pathcost):
        self.state = state
        self.prev_action = prev_action
        self.pathcost =pathcost 

class frontier:
    #tested
    def __init__(self):
        self.front = []

    def pop(self):
        if not self.isEmpty():
            temp = self.front[-1] 
            self.front =self.front[0:-1]
            return temp

    def push(self,node):
        self.front.append(node)
    
    def isEmpty(self):
        if len(self.front) == 0:
            return True
        else:
            return False
    
class explpored_nodes():
    #tested
    def __init__(self):
        self.explored = []

    def push(self,node):
        self.explored.append(node)
    
    def search(self,node):
        if node in self.explored:
            return True
        else:
            return False 

class playground:
    def __init__(self):
        self.idle =Game_statues()
        self.frontier = frontier()
        self.explored_nodes = explpored_nodes()
        self.node = node(self.idle.statue,None,1)
        self.frontier.push(self.node)
        self.update()


        

    def update(self):
        if self.frontier.isEmpty():
            print("no solution")
        else:
            temp = self.frontier.pop()
            if self.idle.terminal(temp.state):
                pass

        node = self.frontier.pop()
        print(node)


idle =Game_statues()
# idle.test()


# idle.visual()