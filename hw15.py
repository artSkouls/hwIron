class Element:

    melting = 0
    evaporation = 0

    farMel = (melting * 1.8) + 32
    farEva = (evaporation * 1.8) + 32

    kelMel = melting + 273.15
    kelEva = farEva + 273.15

    def agg_state(self, t):
        if t < self.melting:
            print("замерзание")
        elif t > self.melting and t < self.evaporation:
            print("плавление")
        elif t > self.evaporation:
            print("испарение")

    def agg_state_far(self, t):
        if t < self.farMel:
            print("замерзание")
        elif t > self.farMel and t < self.farEva:
            print("плавление")
        elif t > self.farEva:
            print("испарение")

    def agg_state_kel(self, t):
        if t < self.kelMel:
            print("замерзание")
        elif t > self.kelMel and t < self.kelEva:
            print("плавление")
        elif t > self.kelEva:
            print("испарение")


class Iron(Element):

    melting = 1538
    evaporation = 2862

    farMel = (melting * 1.8) + 32
    farEva = (evaporation * 1.8) + 32

    kelMel = melting + 273.15
    kelEva = farEva + 273.15


a = Iron()
a.agg_state_kel(100)