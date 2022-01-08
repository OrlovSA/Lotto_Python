from gui import Gui
from kivy.uix.button import Button


class Loglotto(Gui):

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