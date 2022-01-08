from keg import Kegs
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


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
                                         on_press=self.lotto if str(i).isdigit() == True else self.fix))
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

        for add in (self.lebl_comp, self.lebl1, self.lebl_user):
            self.bll.add_widget(add)


        self.button1 = Button(text='Следующий бочонок?', font_size=30, background_color=[.55, .64, .60, 1],
                              background_normal='', on_press=self.lotto)

        self.bl = BoxLayout(orientation='vertical', padding=[2], spacing=4)

        if self.runs == 1:
            run = (
                self.comp_card1, 
                self.bll, 
                self.user_card1, 
                self.button1
                )
        elif self.runs == 2:
            run = (
                self.comp_card1, 
                self.comp_card2, 
                self.bll, 
                self.user_card1, 
                self.user_card2, 
                self.button1
                )
        else:
            run = (
                self.comp_card1, 
                self.comp_card2, 
                self.comp_card3, 
                self.bll, 
                self.user_card1, 
                self.user_card2, 
                self.user_card3, 
                self.button1
                )

        for add in run:
            self.bl.add_widget(add)
        return self.bl
