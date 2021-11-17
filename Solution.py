import networkx
import matplotlib.pyplot
import reading_graphml as file

class RateA:
    def __init__(self,cabinets,verge_length,road_length,chambers,pots):
        self.cabinets=cabinets
        self.verge_length=verge_length
        self.road_length=road_length
        self.chambers=chambers
        self.pots=pots

    def cabinet(self):
        return self.cabinets * 1000    

    def verge(self):
        return self.verge_length * 50
    def road(self,):
        return self.road_length * 100
    def chamber(self):
        return self.chambers * 200
    def pot(self):
        return self.pots *100
    def total_cost(self):
        return self.cabinet()+self.verge()+self.road()+self.chamber()+self.pot()



class RateB(RateA):
    def __init__(self, cabinets, verge_length, road_length, chambers, pots):
        
        super().__init__(cabinets, verge_length, road_length, chambers, pots)        
    
    def cabinet(self):
        return self.cabinets * 1200
    def verge(self):
        return self.verge_length * 40
    def road(self):
        return self.road_length * 80
    def pot(self):
        self.total_length=self.verge_length+self.road_length
        return self.total_length * 20

""" Rate_C={"cabinet":1,
"verge_length":220,
"road_legth":290,
"chambers":4,
"pots":4
} """

if __name__=="__main__":
    print("Network cost  compared between rate A and B")

        
    network=RateA(file.cabinet_counter,file.verge_length,file.road_length,file.chamber_counter,file.pot_counter)
    print(f"Rate card A cost £ {network.total_cost()}")



    network=RateB(file.cabinet_counter,file.verge_length,file.road_length,file.chamber_counter,file.pot_counter)
    print(f"Rate card B cost £ {network.total_cost()}")

    print("Thank for your time")
