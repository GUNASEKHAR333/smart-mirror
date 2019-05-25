from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivymd.theming import ThemeManager
from kivymd.navigationdrawer import NavigationDrawer
#from navigationdrawer import NavigationDrawer
#from kivy.uix.image import Image

from kivy.uix.screenmanager import ScreenManager, Screen ,NoTransition
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock
import time
main_widget_kv = '''
#:import Toolbar kivymd.toolbar.Toolbar

BoxLayout:
    orientation: 'vertical'
    Toolbar:
        id: toolbar
        title: 'Welcome'
        background_color: app.theme_cls.primary_dark
        left_action_items: [['menu', lambda x: app.nav_drawer.toggle()]]
    Label:
        text: 'Instructions here'
        size_hint_y:(0.3)
        color:(1,0,0,1)

<Navigator>:
    NavigationDrawerIconButton:
        icon: 'face'
        text: 'task 1'
    NavigationDrawerIconButton:
        icon: 'face'
        text: 'task 2'
    NavigationDrawerIconButton:
        icon: 'face'
        text: 'task 3'
    NavigationDrawerIconButton:
        icon: 'face'
        text: 'task 4'
    NavigationDrawerIconButton:
        icon: 'face'
        text: 'task 5'
    NavigationDrawerIconButton:
        icon: 'face'
        text: 'task 6'
    '''

class Navigator(NavigationDrawer):
    image_source = StringProperty('images/me.jpg')
    title = StringProperty('Tasks')

sm = ScreenManager(transition=NoTransition())
splashScr = Screen(name='SplashScreen')
splashScr.add_widget(Image(source='000.PNG'))
sm.add_widget(splashScr)


def function(instance):
    sm.current="naviga"

    
class NavigateApp(App):
    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()
        
    def build(self):
        #main_widget = Builder.load_string(main_widget_kv)
        #mainscr=Screen(Navi(name='main'))
        #mainscr.add_widget(main_widget)
        #main_widget = Builder.load_string(main_widget_kv)
        #sm.add_widget(main_widget)
        #sm.current='SplashScreen'
        #sm.current='SplashScreen'
        main_widget = Builder.load_string(main_widget_kv)
        nav=Screen(name="naviga")
        nav.add_widget(main_widget)
        sm.add_widget(nav)
        Clock.schedule_once(function,5)
        #sm.remove_widget(splashScr)
        #sm.current='naviga'
        self.nav_drawer = Navigator()
        return sm

NavigateApp().run()














"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen ,NoTransition
from kivy.uix.image import Image
from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '560')
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string(
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Goto settings'
            on_press: root.manager.current = 'settings'

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
)
from kivy.animation import Animation
from kivy.clock import Clock

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager(transition=NoTransition())
#sm.add_widget(MenuScreen(name='menu'))
#sm.add_widget(SettingsScreen(name='settings'))
#sm = ScreenManager(transition=NoTransition())

splashScr = Screen(name='SplashScreen')
splashScr.add_widget(Image(source='000.png'))
sm.add_widget(splashScr)

sm.add_widget(SettingsScreen(name='settings'))

#sm2 = ScreenManager(transition=NoTransition())

#sm2.add_widget(SettingsScreen(name='settings'))
def switchToMainScr(instance):
    sm.current = 'settings'
#splashScr = Screen(name='SplashScreen')
#splashScr.add_widget(Image(source='000.png'))
#sm.add_widget(splashScr)
#def settingscreen(Screen):
#    sm.current='settings'

class TestApp(App):

    def build(self):
        #wing = Image(source='000.png',pos=(400,560))
        #animation = Animation(x=0, y=0);
        #animation.start(wing)
        Clock.schedule_once(switchToMainScr,5)
        return sm

if __name__ == '__main__':
    TestApp().run()


#/////////////////////////







from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '560')


from kivy.app import App
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock

class timer():
    def work1(self):
        print('Hello World')

class arge(App):

    def build(self):

        wing = Image(source='000.png',pos=(400,560))
        animation = Animation(x=0, y=0);
        animation.start(wing)

        Clock.schedule_once(timer.work1, 5)

        return wing

if __name__ == '__main__':
    arge().run()
/////////////////////


















from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '700')

class text_display(App):

    def build(self):

        return FloatLayout()

if __name__ == '__main__':

    text_display().run()
"""























"""
from kivy.uix.screenmanager import ScreenManager, Screen ,NoTransition
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock
import time


from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivymd.theming import ThemeManager,ThemableBehavior
# from kivymd.navigationdrawer import NavigationDrawer
from navigationdrawer import NavigationDrawer
from kivy.uix.button import Button
from kivy.uix.label import Label


main_widget_kv='''

#:import Toolbar kivymd.toolbar.Toolbar
    
BoxLayout:
    orientation: 'vertical'
    Toolbar:
        id: toolbar
        title: 'smart mirror'
        background_color: app.theme_cls.primary_dark
        left_action_items: [['menu', lambda x: app.nav_drawer.toggle()]]
    Label:
        text: 'Instructions here'
        size_hint_y:(0.3)
        color:(1,0,0,1)
<Navigator>:
    NavigationDrawerIconButton:
        text: 'task 1'
    NavigationDrawerIconButton:
        text: 'task 2'
    NavigationDrawerIconButton:
        text: 'task 3'
    NavigationDrawerIconButton:
        text: 'task 4'
    NavigationDrawerIconButton:
        text: 'task 5'
    NavigationDrawerIconButton:
        text: 'task 6'
''' 


class Navi(Screen):
    pass

class Navigator(NavigationDrawer):
    image_source = StringProperty('images/kivymd_logo.png')
    title = StringProperty('Navigation')

sm = ScreenManager(transition=NoTransition())
splashScr = Screen(name='SplashScreen')
splashScr.add_widget(Image(source='000.png'))
sm.add_widget(splashScr)



main_widget = Builder.load_string(main_widget_kv)
#mainscr=Screen(Navi(name='main'))
#mainscr.add_widget(main_widget)
#main_widget = Builder.load_string(main_widget_kv)
sm.add_widget(main_widget)
#sm.current='SplashScreen'
#time.wait(5)

def switchtonavi(instance):
    sm.remove_widget(splashScr)
    #sm.current="main"

class NavigateApp(App):
    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()
    def build(self):

        self.nav_drawer = Navigator()
        Clock.schedule_once(switchtonavi,5)
        #sm.current='navi'
        return sm
if(__name__=='__main__'):
    NavigateApp().run()
"""
