from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import random


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
        self.jargon = {
            1: 'Кол',
            2: 'Служили два товарища',
            3: 'три товарища',
            4: 'тачанка',
            5: 'Отличник',
            6: 'Точка внизу',
            7: 'Кочережка',
            8: 'Обручальные кольца',
            9: 'Точка внизу',
            10: 'Червонец',
            11: 'Барабанные палочки',
            12: 'Дюжина',
            13: 'Чёртова дюжина',
            14: 'Олимпиада в Сочи',
            15: 'Пятнадцатилетний капитан',
            16: 'Кругом шестнадцать',
            17: 'Где мои семнадцать лет',
            18: 'В первый раз',
            19: 'COVID-19 "Коронавирус"',
            20: 'Гусь на тарелке',
            21: 'Очко',
            22: 'Гуси-лебеди',
            23: 'Два притопа, три прихлопа',
            24: ' ',
            25: 'Опять двадцать пять',
            26: ' ',
            27: ' ',
            28: ' ',
            29: ' ',
            30: 'Ума нет',
            31: ' ',
            32: ' ',
            33: 'Кудри',
            34: ' ',
            35: ' ',
            36: 'Нормальная температура',
            37: ' ',
            38: '38 попугаев',
            39: ' ',
            40: ' ',
            41: ' ',
            42: ' ',
            43: 'Сталинград',
            44: 'Стульчики',
            45: 'Баба ягодка опять',
            46: ' ',
            47: 'Баба ягодка совсем',
            48: 'Пеле',
            49: ' ',
            50: 'Полста',
            51: 'Великолепная пятёрка и вратарь',
            52: ' ',
            53: 'Холодное лето 53-го',
            54: ' ',
            55: 'Перчатки (Вместо валенок перчатки, натянул себе на пятки)',
            56: 'Оттепель',
            57: ' ',
            58: ' ',
            59: ' ',
            60: ' ',
            61: 'Гагарин',
            62: ' ',
            63: 'Валентина Терешкова',
            64: 'Шахматная доска',
            65: ' ',
            66: 'Валенки',
            67: ' ',
            68: ' ',
            69: 'Туда-сюда',
            70: ' ',
            71: ' ',
            72: ' ',
            73: ' ',
            74: ' ',
            75: ' ',
            76: ' ',
            77: 'Топорики',
            78: ' ',
            79: 'Золото',
            80: 'Бабушка',
            81: 'Бабка с клюшкой',
            82: 'Бабушка надвое сказала',
            83: ' ',
            84: ' ',
            85: ' ',
            86: '',
            87: ' ',
            88: 'Матрёшки',
            89: 'Дедушкин сосед',
            90: 'Дедушка'
        }

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


class Gui(Kegs):
    def fix(self, instance):
        pass

    def gui_menu(self):
        self.card_load()
        self.menu = BoxLayout(orientation='vertical', padding=[2], spacing=4)
        for i in range(1, 3):
            self.menu.add_widget(Button(text=f'[color=#000000]Играть в лотто с {i} картой?[/color]' if i == 1
                                        else f'[color=#000000]Играть в лотто с {i} картами?[/color]',
                                        font_size=30, markup=True, background_color=[.55, .64, .60, 1],
                                        background_normal='', on_press=self.gui_card))
        return self.menu

    def card(self, user, num):
        result = GridLayout(cols=9, rows=3, spacing=2)
        if user == 'user':
            for i in num:
                result.add_widget(Button(text=f'[color=#000000]{i}[/color]', markup=True, font_size=14,
                                         background_color=[.55, .64, .60, 1] if str(i).isdigit() == False
                                         else [.94, .92, .84, 1], background_normal='',
                                         on_press=Loglotto.lotto if str(i).isdigit() == True else self.fix))
        else:
            for i in num:
                result.add_widget(Button(text=f'[color=#000000]{i}[/color]', markup=True, font_size=14,
                                         background_color=[.55, .64, .60, 1] if str(i).isdigit() == False
                                         else [.94, .92, .84, 1], background_normal=''))
        return result

    def gui_card(self, instance):
        self.runs = instance.text
        self.user_card1 = self.card('user', self.card_user1)
        self.user_card2 = self.card('user', self.card_user2)
        self.user_card3 = self.card('user', self.card_user3)
        self.comp_card1 = self.card('comp', self.card_user1)
        self.comp_card2 = self.card('comp', self.card_user2)
        self.comp_card3 = self.card('comp', self.card_user3)

        self.lebl1 = Label(text=f'[color=#8DA399]Бочонок с номером № [color=#F0EAD6]'
                                f'{self.kegs_tur}\n{self.jargon[self.kegs_tur]}[/color]\n начал игру![/color]',
                           font_size=20, markup=True, halign='center')
        self.lebl_comp = Label(text=f'[color=#8DA399]Карточка компьютера[/color]',
                               font_size=12, markup=True, halign='center')
        self.lebl_user = Label(text=f'[color=#8DA399]Ваша карточка[/color]',
                               font_size=12, markup=True, halign='center')

        self.bll = BoxLayout(orientation='vertical', padding=[2], spacing=2)
        self.bll.add_widget(self.lebl_comp)
        self.bll.add_widget(self.lebl1)
        self.bll.add_widget(self.lebl_user)

        self.button1 = Button(text='Следующий бочонок?', font_size=30, background_color=[.55, .64, .60, 1],
                              background_normal='', on_press=Loglotto.lotto)

        self.bl = BoxLayout(orientation='vertical', padding=[2], spacing=4)
        if self.runs == 1:
            self.bl.add_widget(self.comp_card1)
            self.bl.add_widget(self.bll)
            self.bl.add_widget(self.user_card1)
            self.bl.add_widget(self.button1)
        elif self.runs == 2:
            self.bl.add_widget(self.comp_card1)
            self.bl.add_widget(self.comp_card2)
            self.bl.add_widget(self.bll)
            self.bl.add_widget(self.user_card1)
            self.bl.add_widget(self.user_card2)
            self.bl.add_widget(self.button1)
        else:
            self.bl.add_widget(self.comp_card1)
            self.bl.add_widget(self.comp_card2)
            self.bl.add_widget(self.comp_card3)
            self.bl.add_widget(self.bll)
            self.bl.add_widget(self.user_card1)
            self.bl.add_widget(self.user_card2)
            self.bl.add_widget(self.user_card3)
            self.bl.add_widget(self.button1)
        return self.bl

class Loglotto(Kegs, Gui):

    def lotto(self, instance):
        if self.kegs_tur in self.card_comp1:
            self.card_comp1.insert(self.card_comp1.index(self.kegs_tur), 'Yes!')
            self.card_comp1.remove(self.kegs_tur)
            self.comp_ball += 1
            self.gui_card()
            self.lebl_comp.text = f'[color=#8DA399]Карточка компьютера, Счет {self.comp_ball}/15[/color]'
            if self.comp_ball == 15:
                self.lebl1.text = f'[color=#8DA399]Вы проиграли\nКомп собрал все №[/color]'
                self.button1.text = 'Начать заново?'
                return

        if instance.text == 'Следующий бочонок?':
            if self.kegs_tur in self.card_user1:
                self.user_card1.clear_widgets()
                for i in self.card_user1:
                    self.user_card1.add_widget(Button(text=f'[color=#000000]{i}[/color]' if i != int(self.kegs_tur)
                                                      else f'[color=#FF0000]{i}[/color]', markup=True, font_size=14,
                                                      background_color=[.55, .64, .60, 1] if str(i).isdigit() == False
                                                      else [.94, .92, .84, 1], background_normal=''))
                self.lebl1.text = f'[color=#8DA399]Вы проиграли\n' \
                                  f'У вас был № [color=#F0EAD6]{self.kegs_tur}[/color][/color]'
                self.button1.text = 'Начать заново?'
                return
        else:
            if instance.text.find(str(self.kegs_tur)) != -1:
                self.card_user1.insert(self.card_user1.index(self.kegs_tur), 'Yes!')
                self.card_user1.remove(self.kegs_tur)
                instance.text = '[color=#000000]Yes![/color]'
                instance.background_color = [.94, .92, .84, 1]
                self.user_ball += 1
                self.lebl_user.text = f'[color=#8DA399]Ваша карточка, Счет {self.user_ball}/15[/color]'
                if self.user_ball == 15:
                    self.lebl1.text = f'[color=#8DA399]Победа\nВы собрал все №[/color]'
                    self.button1.text = 'Начать заново?'
                    self.runs = False
            else:
                self.lebl1.text = f'[color=#8DA399]Вы проиграли!\n' \
                                  f'У вас нет № [color=#F0EAD6]{self.kegs_tur}[/color][/color]'
                self.button1.text = 'Начать заново?'
                return
        self.kegs_tur = self.kegs.pop()
        self.lebl1.text = f'[color=#8DA399]Бочонок выпал с № [color=#F0EAD6]{self.kegs_tur}\n' \
                          f'{self.jargon[self.kegs_tur]}[/color][/color]'

class LottoApp(App, Gui):
    def build(self):
        return self.gui_menu()


if __name__ == "__main__":
    LottoApp().run()