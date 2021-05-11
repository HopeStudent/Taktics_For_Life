
# Импортируем элементы Kivy, которые будем использовать
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Импортируем элементы Kivy, которые будем использовать
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker
from kivymd.uix.picker import MDThemePicker

screen_helper = '''

# Правила для класса ItemMDLabel 
<ItemMDLabel@MDLabel>:
    font_size:'25sp'
    halign: "center"
    color:'blue'
# Создание поля
Screen:
    # Создание всех виджетов (объектов)
    BoxLayout:
        orientation:'vertical'

        MDToolbar:
            title: 'Taktics for Life'
            md_bg_color: .24, .67, .24, 1
            specific_text_color: 1, 1, 1, 1
            right_action_items: [["dots-vertical", lambda x: app.navigation_draw()]]
            elevation:5
            
        
            
        MDBottomNavigation:
            panel_color: .24, .67, .24, 1
            
            # Создание экранов и объектов в них
            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Clock'
                icon: 'clock'
                
                MDFloatingActionButton:
                    icon: "clock"
                    md_bg_color: app.theme_cls.primary_color
                    user_font_size: "20sp"
                    pos_hint:{'center_x':0.5, 'center_y': 0.5}
                    on_release: app.show_time_picker() # Действие при нажатии на кнопку

                    
                        
           
            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'Calendar'
                icon: 'calendar'
                
                MDFloatingActionButton:
                    icon: 'calendar'
                    md_bg_color: app.theme_cls.primary_color
                    user_font_size: "25sp"
                    pos_hint:{'center_x':0.5, 'center_y': 0.5}
                    on_release: app.show_datepicker() # Действие при нажатии на кнопку

            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'Challenges'
                icon: 'sword-cross'
                
                GridLayout:
                    rows: 5
                    
                    BoxLayout:
                        orientation: 'vertical'
                        pos_hint:{'center_x':0.5, 'center_y': 0.5}
                        ItemMDLabel:
                            text: "Заниматься тем, что любите"
                            
            
                        ItemMDLabel:
                            text: "Нырнуть с аквалангом"
            
                        ItemMDLabel:
                            text: "Достичь своего идеального веса"
                            
                        ItemMDLabel:
                            text: "Встретить рассвет"
                            
                        ItemMDLabel:
                            text: "Полетать на воздушном шаре"
                
              
'''

class TacticsApp(MDApp):
    # переменная для создания нового окна
    dialog = None

    # Основной метод для построения программы
    def build(self):

        # Изменение цветовой схемы оттенка приложения:
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = 'A700'

        # Основная переменная с screen_helper.kv файлом
        screen = Builder.load_string(screen_helper)
        return screen


    def navigation_draw(self):
        '''
         функция navigation_draw() создаёт новое окно
        '''
        if not self.dialog:
            self.dialog = MDDialog(
                title="A few words",
                text="Thank you for downloading this app",
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self):
        '''
        функция close_dialog() закрывает новое окно при нажатии кнопок 'OK' или 'CANCEL'
        '''
        self.dialog.dismiss()


    def show_datepicker(self):
        '''
        функция show_datepicker() открывает календарь в новом окне
        '''
        picker = MDDatePicker(callback=self.got_date)
        picker.open()

    def got_date(self, the_date):
        '''
        функция show_time_picker() нужна для стабильной работы функции show_datepicker
        '''
        print(the_date)

    def show_time_picker(self):
        '''
        функция show_time_picker() открывает часы в новом окне
        '''

        time_dialog = MDTimePicker()
        time_dialog.open()

    def get_time(self, time):
        '''
        функция get_time() нужна для стабильной работы функции show_time_picker
        '''
        print(time)

# Запуск проекта
TacticsApp().run()