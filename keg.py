import random
from jargon import jargon

class Kegs:
    def __init__(self):
        self.kegs = []
        self.card_user1 = []
        self.card_user2 = []
        self.card_user3 = []
        self.card_comp1 = []
        self.card_comp2 = []
        self.card_comp3 = []
        self.kegs_tur = 0
        self.user_ball = 0
        self.comp_ball = 0
        self.runs = 0
        self.jargon = jargon

    def card_load(self):
        self.kegs = [i for i in range(1, 91)]
        random.shuffle(self.kegs)
        self.kegs_tur = self.kegs.pop()
        self.user_ball = 0
        self.comp_ball = 0
        self.runs = 0
        self.card_user1 = self._card_generation()
        self.card_user2 = self._card_generation()
        self.card_user3 = self._card_generation()
        self.card_comp1 = self._card_generation()
        self.card_comp2 = self._card_generation()
        self.card_comp3 = self._card_generation()

    def _card_generation(self):
        result = []
        card_1 = [i for i in range(1, 10)]
        random.shuffle(card_1)
        card_2 = [i for i in range(10, 20)]
        random.shuffle(card_2)
        card_3 = [i for i in range(20, 30)]
        random.shuffle(card_3)
        card_4 = [i for i in range(30, 40)]
        random.shuffle(card_4)
        card_5 = [i for i in range(40, 50)]
        random.shuffle(card_5)
        card_6 = [i for i in range(50, 60)]
        random.shuffle(card_6)
        card_7 = [i for i in range(60, 70)]
        random.shuffle(card_7)
        card_8 = [i for i in range(70, 80)]
        random.shuffle(card_8)
        card_9 = [i for i in range(80, 91)]
        random.shuffle(card_9)
        for _ in range(3):
            card = []
            card.append(card_1.pop())
            card.append(card_2.pop())
            card.append(card_3.pop())
            card.append(card_4.pop())
            card.append(card_5.pop())
            card.append(card_6.pop())
            card.append(card_7.pop())
            card.append(card_8.pop())
            card.append(card_9.pop())
            result.extend(card)
        s_1 = result[:9]
        s_11 = []
        s_2 = result[9:18]
        s_22 = []
        s_3 = result[18:]
        s_33 = []
        result.clear()
        for a, b, c in zip(s_1, s_2, s_3):
            i = []
            i.append(int(a))
            i.append(int(b))
            i.append(int(c))
            i.sort()
            s_11.append(i[0])
            s_22.append(i[1])
            s_33.append(i[2])
        for _ in range(1):
            i = [i for i in range(0, 9)]
            random.shuffle(i)
            for _ in range(4):
                s_11[i.pop()] = ' '
            result.extend(s_11)
        for _ in range(1):
            i = [i for i in range(0, 9)]
            random.shuffle(i)
            for _ in range(4):
                s_22[i.pop()] = ' '
            result.extend(s_22)
        for _ in range(1):
            i = [i for i in range(0, 9)]
            random.shuffle(i)
            for _ in range(4):
                s_33[i.pop()] = ' '
            result.extend(s_33)
        return result
