from kivy.app import App
##from kivmob import KivMob, TestIds
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty, ReferenceListProperty, ObjectProperty, dpi2px)
from kivy.vector import Vector
from kivy.clock import Clock
from plyer import accelerometer
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.popup import Popup
import random
from kivy.uix.scrollview import ScrollView
Builder.load_string("""
#:kivy 1.0.9
#:import accelerometer plyer.accelerometer
#:import Factory kivy.factory.Factory
<CustomButton@Button>:
    color:0,0,0,.7
    background_color:(0,0,0,0)
    background_normal: ''
    back_color: (1,0,1,1)
    border_radius:[50,2,50,2]
    canvas.before:
        Color:
            rgba: self.back_color
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:self.border_radius
<LevelOne@Popup>:       
    size_hint:.8,.5
    title_color:1,1,0,1
    title_size:'30sp'
    separator_color:.9,0,.3,1
    title_align:'center'
    title:'Level 1'
    auto_dismiss:False
    BoxLayout:
        orientation:'vertical'
        padding:10
        Label:
            text:"If ball goes beyond the Upper Wall then you will lose"
            size_hint:1,.3
            pos_hint:{"x":0, "y":0.4}
            multiline:True
            font_size:'20sp'
            text_size:self.width,None
            size:self.texture_size
            bold:True
        Button:
            text:'Start Level'
            size_hint:.5,.1
            background_color:1,.5,.3,1
            pos_hint:{"x":.25,"y":.1}
            on_release:
                root.dismiss()
                accelerometer.enable()
                app.AccelEnable=0

<LevelTwo@Popup>:       
    size_hint:.8,.5
    title_color:1,1,0,1
    title_size:'30sp'
    separator_color:.9,0,.3,1
    title_align:'center'
    title:'Level 2'
    auto_dismiss:False
    BoxLayout:
        orientation:'vertical'
        padding:10
        Label:
            text:"Right wall has become deadly, if ball touches it then you will lose"
            size_hint:1,.3
            pos_hint:{"x":0, "y":0.4}
            multiline:True
            font_size:'20sp'
            text_size:self.width,None
            size:self.texture_size
            bold:True
        Button:
            text:'Start Level'
            size_hint:.5,.1
            background_color:1,.5,.3,1
            pos_hint:{"x":.25,"y":.1}
            on_release:
                root.dismiss()
                accelerometer.enable()
                app.AccelEnable=0

<LevelThree@Popup>:       
    size_hint:.8,.5
    title_color:1,1,0,1
    title_size:'30sp'
    separator_color:.9,0,.3,1
    title_align:'center'
    title:'Level 3'
    auto_dismiss:False
    BoxLayout:
        orientation:'vertical'
        padding:10
        Label:
            text:"Bottom wall has also become deadly, if ball touches it then you will lose"
            size_hint:1,.3
            pos_hint:{"x":0, "y":0.4}
            multiline:True
            font_size:'20sp'
            text_size:self.width,None
            size:self.texture_size
            bold:True
        Button:
            text:'Start Level'
            size_hint:.5,.1
            background_color:1,.5,.3,1
            pos_hint:{"x":.25,"y":.1}
            on_release:
                root.dismiss()
                accelerometer.enable()
                app.AccelEnable=0

<LevelFour@Popup>:       
    size_hint:.8,.5
    title_color:1,1,0,1
    title_size:'30sp'
    separator_color:.9,0,.3,1
    title_align:'center'
    title:'Level 4'
    auto_dismiss:False
    BoxLayout:
        orientation:'vertical'
        padding:10
        Label:
            text:"Left wall has also become deadly, if ball touches it then you will lose"
            size_hint:1,.3
            pos_hint:{"x":0, "y":0.4}
            multiline:True
            font_size:'20sp'
            text_size:self.width,None
            size:self.texture_size
            bold:True
        Button:
            text:'Start Level'
            size_hint:.5,.1
            background_color:1,.5,.3,1
            pos_hint:{"x":.25,"y":.1}
            on_release:
                root.dismiss()
                accelerometer.enable()
                app.AccelEnable=0

<ThankWindow@Popup>:
    size_hint:.8,.5
    title_color:0,1,0,1
    title_size:'30sp'
    separator_color:.9,0,.3,1
    title_align:'center'
    title:'WallBall'
    auto_dismiss:False
    BoxLayout:
        orientation:'vertical'
        padding:10
        spacing:10
        Button:
            text:'White'
            size_hint:.5,.1
            background_color:1,.5,.3,1
            pos_hint:{"x":.25,"y":.1}
            on_release:
                app.BRed=1
                app.BGreen=1
                app.BBlue=1
                root.dismiss()
        Button:
            text:'Blue'
            size_hint:.5,.1
            background_color:1,.5,.3,1
            pos_hint:{"x":.25,"y":.1}
            on_release:
                app.BRed=0
                app.BGreen=1
                app.BBlue=1
                root.dismiss()
        Button:
            text:'Pink'
            size_hint:.5,.1
            background_color:1,.5,.3,1
            pos_hint:{"x":.25,"y":.1}
            on_release:
                app.BRed=1
                app.BGreen=0
                app.BBlue=1
                root.dismiss()
        Button:
            text:'Yellow'
            size_hint:.5,.1
            background_color:1,.5,.3,1
            pos_hint:{"x":.25,"y":.1}
            on_release:
                app.BRed=1
                app.BGreen=1
                app.BBlue=0
                root.dismiss()


                
<PongBall>:
    size:'0.9cm','0.9cm'
    canvas:
        Color:
            rgba:app.BRed,app.BGreen,app.BBlue,1
        Ellipse:
            pos:self.pos
            size:self.size

<TargetBall>:
    size:'0.9cm','0.9cm'
    canvas:
        Color:
            rgba:1,0,0,1
        Ellipse:
            pos:self.pos
            size:self.size





<MainMenu>:
    BoxLayout:
        padding:50,190,50,70
        spacing:100
        orientation:'vertical'
        canvas.before:
            Color:
                rgba:1,1,1,1
            Rectangle:
                pos:self.pos
                size:self.size
        Label:
            text:'WallBall'
            pos_hint:{"x":.5,"center_x":0,"y":1}
            size_hint:1,.2
            bold:True
            font_size:'80sp'
            color:0,0,0,1
        BoxLayout:
            orientation:'vertical'
            padding:20,50,20,200
            spacing:80
            CustomButton:
                text:'Instructions'
                bold:True
                font_size:'20sp'
                back_color:0.157,0.455,0.753,1
                on_release:
                    app.root.current='Instruct'
                    app.root.transition.direction='left'
            CustomButton:
                text:"Striker Colour"
                bold:True
                font_size:'20sp'
                back_color:0.157,0.455,0.753,1
                on_release:
                    Factory.ThankWindow().open()

            CustomButton:
                text:'Play Now'
                bold:True
                font_size:'20sp'
                back_color:0.157,0.455,0.753,1
                on_release:
                    app.root.current='Main'
                    app.root.transition.direction='left'
                    app.Flag=0
                    app.SF=0
                    app.GO=0

            
<ScrollViewL@ScrollView>:
    do_scroll_x:False
    do_scroll_y:True
    scroll_distance:1000
    Label:
        text:"1.Tilt your device to move the ball\\n\\n2.Overlap the Striker ball on Red ball\\n\\n3.Overlapping the ball will give you a point\\n\\n4.This game has Four Levels\\n\\n5.First level doesn't have any upper walls\\n\\n6.In further levels all walls will become deadly one-by-one\\n\\n7.Deadly Walls(Red Colour) means that if the ball touches it then you will lose\\n\\n8.First Level is of 20 pts\\n\\n9.Second Level is of 15 pts\\n\\n10.Third Level is of 10 pts\\n\\n11.Fourth Level is of UNLIMITED pts(This level will check your focus at extreme level)\\n\\nNote:-This application works on Earth's Gravity and tests your focus"
        font_size:'20dp'
        text_size:self.width,None
        height:self.texture_size[1]
        color:0,0,0,1
        size_hint_y:None

<Instructions>:
    insta:ins_label
    BoxLayout:
        padding:20,80,20,100
        spacing:10
        orientation:'vertical'
        canvas.before:
            Color:
                rgba:1,1,1,1
            Rectangle:
                pos:self.pos
                size:self.size
        Label:
            text:'Instructions'
            pos_hint:{"x":.5,"center_x":0,"y":1}
            size_hint:1,.3
            bold:True
            font_size:'50sp'
            color:0,0,0,1
        ScrollViewL:
            id:ins_label    
        CustomButton:
            text:'Menu'
            bold:True
            pos_hint:{"x":.5,"center_x":0}
            size_hint:.5,.3
            font_size:'20sp'
            back_color:0.157,0.455,0.753,1
            on_release:
                app.root.current='Menu'
                app.root.transition.direction='right'
                

<PongGame>:
    ball:pong_ball
    target:target_ball
    
    canvas.before:
        Color:
            rgba:app.BottomWallRed,app.BottomWallGreen,0,1
        Rectangle:
            size:root.width,5
            pos:0,0
        Color:
            rgba:app.LeftWallRed,app.LeftWallGreen,0,1
        Rectangle:
            size:5,root.height
            pos:0,0
        Color:
            rgba:app.RightWallRed,app.RightWallGreen,0,1
        Rectangle:
            size:5,root.height
            pos:root.width-5,0

    TargetBall:
        id:target_ball
        center:self.parent.center
    PongBall:
        id:pong_ball
        center:self.parent.center


        
        
<GameOver>:
    BoxLayout:
        padding:80,100,80,190
        spacing:80
        orientation:'vertical'
        canvas.before:
            Color:
                rgba:1,1,1,1
            Rectangle:
                pos:self.pos
                size:self.size

        Label:
            text:'GAME OVER'
            pos_hint:{"x":.5,"center_x":0,"y":1}
            bold:True
            font_size:'50sp'
            color:1,0,0,1
        Label:
            text:"Score: "+str(app.SF)
            pos_hint:{"x":.5,"center_x":0,"y":1}
            bold:True
            font_size:'50sp'
            color:0,0,0,1
        CustomButton:
            text:"Play Again"
            bold:True
            font_size:'20sp'
            back_color:0.157,0.455,0.753,1
            on_release:
                app.root.current='Main'
                app.root.transition.direction='right'
                app.Flag=0
                app.SF=0
                app.GO=0
                
        CustomButton:
            text:"Home"
            bold:True
            font_size:'20sp'
            back_color:0.157,0.455,0.753,1
            on_release:
                app.root.current='Menu'
                app.root.transition.direction='right'
                app.Flag=1
                app.SF=0
                app.GO=0
    
    
""")

class LevelOne(Popup):
    pass
class LevelTwo(Popup):
    pass
class LevelThree(Popup):
    pass
class LevelFour(Popup):
    pass
class ThankWindow(Popup):
    pass
class MainMenu(BoxLayout):
    pass

class ScrollViewL(ScrollView):
    pass
class Instructions(BoxLayout):
    insta=ObjectProperty(None)

class TargetBall(Widget):
    tx=NumericProperty(0)
    ty=NumericProperty(0)
    txy=ReferenceListProperty(tx,ty)
    def GenerateTarget(self,sxi,syi,sxf,syf):
        sxcm=int(dpi2px(1,'cm'))
        sycm=int(dpi2px(1,'cm'))
        sxfv=sxf-sxcm
        syfv=syf-sycm
        sxinit=sxi+8
        syinit=syi+8
        self.tx=random.randint(sxinit,sxfv)
        self.ty=random.randint(syinit,syfv)
        self.pos=Vector(*self.txy)
        




        
class PongBall(Widget):
    vx=NumericProperty(0)
    vy=NumericProperty(0)
    v=ReferenceListProperty(vx,vy)
    ax=NumericProperty(0)
    ay=NumericProperty(0)
    a=ReferenceListProperty(ax,ay)

    accelerometer.enable()
    def move(self):
        if App.get_running_app().AccelEnable==0:
            val=accelerometer.acceleration
            if not val[0]==None:
                self.ax=-1*val[0]
                self.ay=-1*val[1]
            self.v=Vector(*self.v)+Vector(*self.a)
            self.pos=Vector(*self.v)+self.pos

class GameOver(BoxLayout):
    pass
        
class PongGame(Widget):
    ball=ObjectProperty(None)
    target=ObjectProperty(None)
    score=NumericProperty(0)
    fl=NumericProperty(0)
    fl_check=NumericProperty(0)
    lf1=True
    lf2=True
    lf3=True
    lf4=True
    def serve_ball(self):
        self.ball.center=self.center
        App.get_running_app().SF=0
        

    def serve_ball_1(self):
        self.ball.center=self.center
        App.get_running_app().SF=0
        #test
        self.ball.ax=0
        self.ball.ay=0

    def LevelPopup(self,level):
        if level==1:
            p=LevelOne()
            p.open()
        elif level==2:
            p=LevelTwo()
            p.open()
        elif level==3:
            p=LevelThree()
            p.open()
        elif level==4:
            p=LevelFour()
            p.open()
        accelerometer.disable()
        App.get_running_app().AccelEnable=1
        self.ball.center=self.center

    def Game_Over(self):
        if self.fl_check==0:
            App.get_running_app().SF=self.score-1
            self.fl_check=1
        else:
            App.get_running_app().SF=self.score
        App.get_running_app().ads.new_banner('ca-app-pub-3940256099942544/6300978111', top_pos=True)
        App.get_running_app().ads.request_banner()
        App.get_running_app().ads.show_banner()
        MainGame.screen_manager.current='gameover'
        self.ball.center=self.center
        self.score=0
        App.get_running_app().GO=1
        App.get_running_app().Flag=1
        App.get_running_app().Level=0
        self.fl=1
        self.lf1=True
        self.lf2=True
        self.lf3=True
        self.lf4=True
        App.get_running_app().RightWallGreen=1
        App.get_running_app().RightWallRed=0
        App.get_running_app().BottomWallGreen=1
        App.get_running_app().BottomWallRed=0
        App.get_running_app().LeftWallGreen=1
        App.get_running_app().LeftWallRed=0


    def update(self,dt):
        if App.get_running_app().Flag==0:
            if App.get_running_app().GO==0 and self.fl==1:
                self.target.GenerateTarget(self.x,self.y,self.width,self.height)
                self.serve_ball_1()
                self.fl=0
            self.ball.move()
            
            if self.lf1:
                App.get_running_app().ads.hide_banner()
                self.LevelPopup(1)
                self.lf1=False
                   
            #initialisation for variables 
            diffx=self.ball.x-self.target.x
            diffy=self.ball.y-self.target.y
            rs=int(dpi2px(1,'cm'))
            right_screen=self.width-rs
            
            #Checking the distance between target and main ball and making it +ve
            if diffx<0:
                diffx*=-1
            if diffy<0:
                diffy*=-1
            #Checking for the collisions in ball    
            if diffx<50 and diffy<50:
                self.score=self.score+1
                self.target.GenerateTarget(self.x,self.y,self.width,self.height)

            #Level checking and increasing
            if self.fl_check==1:
                if self.score>19 and self.lf4:
                    App.get_running_app().Level=4
                    self.LevelPopup(4)
                    self.lf4=False
                    App.get_running_app().LeftWallGreen=0
                    App.get_running_app().LeftWallRed=1
                elif self.score>9 and self.lf3:
                    App.get_running_app().Level=3
                    self.LevelPopup(3)
                    self.lf3=False
                    App.get_running_app().BottomWallGreen=0
                    App.get_running_app().BottomWallRed=1
                elif self.score>4 and self.lf2:
                    App.get_running_app().Level=2
                    self.LevelPopup(2)
                    self.lf2=False
                    App.get_running_app().RightWallGreen=0
                    App.get_running_app().RightWallRed=1
            else:
                if self.score>20 and self.lf4:
                    App.get_running_app().Level=4
                    self.LevelPopup(4)
                    self.lf4=False
                    App.get_running_app().LeftWallGreen=0
                    App.get_running_app().LeftWallRed=1
                elif self.score>10 and self.lf3:
                    App.get_running_app().Level=3
                    self.LevelPopup(3)
                    self.lf3=False
                    App.get_running_app().BottomWallGreen=0
                    App.get_running_app().BottomWallRed=1
                elif self.score>5 and self.lf2:
                    App.get_running_app().Level=2
                    self.LevelPopup(2)
                    self.lf2=False
                    App.get_running_app().RightWallGreen=0
                    App.get_running_app().RightWallRed=1

                
            #Checking for the collisions between wall and ball
            if (self.ball.y<self.y) and (self.ball.x<self.x):
                if App.get_running_app().Level>=3 or App.get_running_app().Level>=4:
                    self.Game_Over()
                else:
                    self.ball.y=self.y
                    self.ball.x=self.x
                    self.ball.vx*=-0.8
                    self.ball.vy*=-0.8
            elif (self.ball.y<self.y) and (self.ball.x>right_screen):
                if App.get_running_app().Level>=2 or App.get_running_app().Level>=3:
                    self.Game_Over()
                else:
                    self.ball.y=self.y
                    self.ball.x=right_screen
                    self.ball.vx*=-0.8
                    self.ball.vy*=-0.8
            elif (self.ball.y < self.y):
                if App.get_running_app().Level>=3:
                    self.Game_Over()
                else:
                    self.ball.y=self.y
                    self.ball.vy*=-0.8
            elif (self.ball.x < self.x):
                if App.get_running_app().Level>=4:
                    self.Game_Over()
                else:
                    self.ball.x=self.x
                    self.ball.vx*=-0.8
            elif (self.ball.x>right_screen):
                if App.get_running_app().Level>=2:
                    self.Game_Over()
                else:
                    self.ball.x=right_screen
                    self.ball.vx*=-0.8
                
            #Top is always game over
            if (self.ball.y>self.height):
                self.Game_Over()
      

class PongApp(App):
    SF=NumericProperty(0)
    Flag=NumericProperty(1)
    GO=NumericProperty(0)
    Level=NumericProperty(1)
    AccelEnable=NumericProperty(1)
    RightWallGreen=NumericProperty(1)
    RightWallRed=NumericProperty(0)
    BottomWallGreen=NumericProperty(1)
    BottomWallRed=NumericProperty(0)
    LeftWallGreen=NumericProperty(1)
    LeftWallRed=NumericProperty(0)
    BRed=NumericProperty(1)
    BGreen=NumericProperty(1)
    BBlue=NumericProperty(1)
    ads=KivMob('ca-app-pub-3940256099942544~3347511713')
    def build(self):
        ads.new_banner('ca-app-pub-3940256099942544/6300978111', top_pos=True)
        ads.request_banner()
        ads.show_banner()

        self.screen_manager=ScreenManager()
        
        main_menu=MainMenu()
        screen=Screen(name='Menu')
        screen.add_widget(main_menu)
        self.screen_manager.add_widget(screen)

        inst=Instructions()
        screen=Screen(name='Instruct')
        screen.add_widget(inst)
        self.screen_manager.add_widget(screen)

        
        game=PongGame()
        screen=Screen(name='Main')
        screen.add_widget(game)
        self.screen_manager.add_widget(screen)
        game.serve_ball()
        Clock.schedule_interval(game.update,1.0/60.0)

        game_over=GameOver()
        screen=Screen(name='gameover')
        screen.add_widget(game_over)
        self.screen_manager.add_widget(screen)
        return self.screen_manager


if __name__=='__main__':
    MainGame=PongApp()
    MainGame.run()

