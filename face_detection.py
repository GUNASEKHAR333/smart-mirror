from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivymd.theming import ThemeManager
from kivymd.navigationdrawer import NavigationDrawer
#from navigationdrawer import NavigationDrawer
#from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen ,NoTransition
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock
import easygui

#import cv2
#from imutils import face_utils
#import numpy as np
#import dlib
#import imutils

Builder.load_string("""
<MainScreen>:
    BoxLayout:
        orientation:'vertical'
        Image:
            size_hint_y: 0.9
            source: '000.png'
        Button:
            size_hint_y:0.1
            pos_hint_x:0.3
            color: (1, 0,0, 1)
            text: 'back'
            on_release:root.manager.current="naviga"
<uploadScreen>:
    FloatLayout:
        orientation:'vertical'
        Button:
            text:'upload'
            pos_hint:{'x': 0.4, 'center_y': .5}
            size_hint:0.2,0.2
            on_release:root.face()
""")

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
        on_release:root.navifunc()
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
class MainScreen(Screen):
    pass
#def back():
#    sm.current='naviga'
class uploadScreen(Screen):
    def back(self,instance):
        sm.current='naviga'
        return sm
    def face(self):
        image=easygui.fileopenbox()
        floater = FloatLayout()
        
        
        face_detect = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("F:/DC/internship/product/shape_predictor_68_face_landmarks.dat")

        image = cv2.imread("F:/DC/internship/product/images/download.jpg")
        #cv2.imshow("im",imag)
        image = cv2.resize(image,(500,500))
        grayimage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        
        rects = face_detect(grayimage,1)

        for (i,rect) in enumerate(rects):
            shape = predictor(grayimage,rect)
            shape = face_utils.shape_to_np(shape)
            (x,y,w,h) = face_utils.rect_to_bb(rect)
            cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)
            cv2.putText(image, "Face {}".format(i+1), (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)
            
            for (x,y) in shape:
                cv2.circle(image,(x,y),1,(0,255,0),1)
                
        logo = Image(source=image, pos_hint={'center_x': 0.5, 'center_y': .6})        
        enter = Button(text='back', size_hint=(0.2,0.1), pos_hint={'center_x': 0.5, 'center_y': .05})
        enter.bind(on_release=self.back)
        #image2=Image(image)
        floater.add_widget(logo)
        floater.add_widget(enter)
        s1=Screen(name='display')
        s1.add_widget(floater)
        sm.add_widget(s1)
        sm.current='display'
        return sm     
sm = ScreenManager(transition=NoTransition())
splashScr = Screen(name='SplashScreen')
splashScr.add_widget(Image(source='000.PNG'))
sm.add_widget(splashScr)
sm.add_widget(MainScreen(name="image"))
sm.add_widget(uploadScreen(name="upload"))




def function(instance):
    sm.current="naviga"

def function2(instance):
    sm.current="image"

class Navigator(NavigationDrawer):
    image_source = StringProperty('images/me.jpg')
    title = StringProperty('Tasks')
    def navifunc(self):
        sm.current="upload"
        return sm
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
        Clock.schedule_once(function,10)
        #sm.remove_widget(splashScr)
        #sm.current='naviga'
        self.nav_drawer = Navigator()
        return sm

NavigateApp().run()
