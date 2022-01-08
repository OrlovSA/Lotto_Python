from kivy.app import App
from log import Loglotto


class LottoApp(App, Loglotto):
    def build(self):
        return self.gui_menu()
        

if __name__ == "__main__":
    LottoApp().run()