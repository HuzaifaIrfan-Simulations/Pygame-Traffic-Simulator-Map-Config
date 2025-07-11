class TrafficSignal:
    def __init__(self, roads, config={}):
        # Initialize roads
        self.roads = roads
        self.cycle_length=30

        self.cycle=[]

        self.auto=True
        # Set default configuration
        self.set_default_config()

        self.set_individual_signal_cycle()

        
        self.update_properties(config)

        # Calculate properties
        self.init_properties()

    def update_cycle_length(self,cycle_length):
        self.cycle_length=cycle_length
        
    def set_cycle_index(self,cycle_index):
        self.set_to_manual()
        self.current_cycle_index=cycle_index

        

    def update_properties(self,config):

        # print(config)
        # Update configurations
        for attr, val in config.items():
            setattr(self, attr, val)

    def set_to_manual(self):
        self.auto = False

    def set_to_auto(self):
        self.auto = True

    def set_individual_signal_cycle(self):


        individual_signals=len(self.roads)

        signal_state = tuple(False for i in range(individual_signals))
        self.cycle.append(signal_state)

        signal_state = tuple(True for i in range(individual_signals))
        self.cycle.append(signal_state)

        for n in range(individual_signals):

            signal_state = tuple(True if i == n else False for i in range(individual_signals))
            # print(signal_state)

            self.cycle.append(signal_state)


            

    def set_default_config(self):

        # self.cycle = [(True, False,False,False), (False, True,False,False),(False, False,True,False),(False, False,False,True)]

        self.slow_distance = 50
        self.slow_factor = 0.4
        self.stop_distance = 15

        self.current_cycle_index = 0

        self.last_t = 0

    def init_properties(self):
        for i in range(len(self.roads)):
            for road in self.roads[i]:
                road.set_traffic_signal(self, i)

    @property
    def current_cycle(self):
        return self.cycle[self.current_cycle_index]
    
    def update(self, sim):
        # self.cycle_length = 30
        if self.auto:
            k = (sim.t // self.cycle_length) % len(self.roads)
            self.current_cycle_index = int(k)+2
