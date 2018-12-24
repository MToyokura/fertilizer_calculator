"""
kivyファイルとPyhonからなる形式。
kivyファイルでウィジェットの配置等を規定し、ボタンが押されたときとかの内部処理はpythonで行う。
"""
from kivy.app import App
from kivy.core.text import LabelBase, DEFAULT_FONT

LabelBase.register(DEFAULT_FONT, "ipaexg.ttf")

class FertilApp(App):
    pass

if __name__ == "__main__":
    FertilApp().run()
