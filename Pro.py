#-*- coding:utf-8 -*-
import arcade
import os
import tkinter as tk
import random
import pyglet
import typing


# Включение и отключение вывода отладочных сообщений
DEBUG = True


class TApp(arcade.Window):
    
    """ Основной класс приложения """
    def __init__(self, fs=False):
        """ Конструктор """
                
        self.otvet=-1

        self.RAND=[]
        for j in range(0,2):
            #print(j)
            self.RAND.append(j)
        random.shuffle(self.RAND)
        #print(self.RAND)

        self.RAND1=[]
        for j in range(0,4):
            #print(j)
            self.RAND1.append(j)
        random.shuffle(self.RAND1)
        #print(self.RAND1)

        self.RAND2=[]
        for j in range(0,6):
            #print(j)
            self.RAND2.append(j)
        random.shuffle(self.RAND2)
        #print(self.RAND2)

        self.RAND_1=[]
        for j in range(0,2):
            k=random.randint(0,5)
            for g in range(0,2):    
                self.RAND_1.append(k)
        random.shuffle(self.RAND_1)
        #print(self.RAND_1)

        self.RAND_2=[]
        for j in range(0,3):
            k=random.randint(0,5)
            for g in range(0,2):    
                self.RAND_2.append(k)
        random.shuffle(self.RAND_2)
        #print(self.RAND_2)

        self.RAND_3=[]
        for j in range(0,3):
            k=random.randint(0,5)
            for g in range(0,2):    
                self.RAND_3.append(k)
        random.shuffle(self.RAND_3)
        #print(self.RAND_3)

        # Заголовок окна
        self.title = "Game"
        self.subtitle = "Диагностика эмоционального развития"

        # Получаем реальные размеры экрана
        root = tk.Tk()
        self.SCREEN_WIDTH = root.winfo_screenwidth()
        #print(root.winfo_screenwidth())
        self.SCREEN_HEIGHT = root.winfo_screenheight()
        #print(root.winfo_screenheight())
        del root

        # Параметры масштабирования
        self.SPRITE_SCALING = 0.1
        self.VIEWPORT_MARGIN = 40

        # Открываем окно
        super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.title, fullscreen=True)

        # Устанавливаем рабочий каталог, где по умолчанию будут находится файлы
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Получаем размеры окна и устанавливаем окно просмотра равным этому окну приложения
        width, height = self.get_size()
        #print(width, height)
        self.set_viewport(0, width, 0, height)


    def setup(self):
        """ Установка основных параметров. """
        self.setPaths()
        self.setUserVars()
        self.setFonts()
        self.setColors()
        self.setMenu()
        self.mouseX = 0
        self.mouseY = 0
        self.isMouseDown = False
        self.loadAvatars()
        #self.setAbout()

    def setPaths(self):
        """ Задаем пути к ресурсам """
        self.imgPath = "images/"
        self.logoPath = self.imgPath + "logo/"
        self.avatarPath = self.imgPath+"avatars/"
        self.cardPath = self.imgPath+"cards/"
        self.GUIPath = self.imgPath + "GUI/"
        self.detectivePath = self.imgPath+"cards/detective/"
        self.detectivePath1=self.detectivePath+"1/"
        self.detectivePath2=self.detectivePath+"2/"
        self.detectivePath3=self.detectivePath+"card/"
        self.detectivePath4=self.detectivePath+"3/"
        self.detectivePath5=self.detectivePath+"4/"
        self.detectivePath6=self.detectivePath+"5/"
        self.detectivePath7=self.detectivePath+"6/"
        self.detectivePath8=self.detectivePath+"7/"
        self.menu1 = self.imgPath+"cards/menu/girl/"
        self.menu2 = self.imgPath+"cards/menu/boy/"
        self.soundPath = "sounds/"
        self.fontPath = "fonts/"
        self.savePath = "save"
        self.aboutLogo1 = arcade.Sprite(self.GUIPath + "1.jpg", 0.4)
        self.aboutLogo3 = arcade.Sprite(self.detectivePath4 + "2.jpg",0.3)
        self.aboutLogo4 = arcade.Sprite(self.imgPath + "megaphone.png", 0.09)
        self.Fon = arcade.Sprite(self.imgPath + "fon.png", 0.32)
        self.Strelka = arcade.Sprite(self.imgPath + "Strelka.png", 0.32)
        self.Strelka1 = arcade.Sprite(self.imgPath + "Strelka2.png", 0.32)

    def setUserVars(self):
        """ Переменные описывающие состояние пользователя """
        # Номер аватара, который выбрал пользователь
        self.userAvatar = 0
        #Выбранная карточка
        self.otvet = -1
        # Количество правильных ответов
        self.userGoodAnswers = 0
        #print(self.userGoodAnswers, self.userAvatar)
        # Количество не правильных ответов
        self.userBadAnswers = 0
        #Номер выбранного набора карточек
        self.userChoiceCards = 0
        self.MenuItemSelected = 0
        self.vernotvet = 0

    def setFonts(self):
        # шрифты отсюда https://fonts.google.com/?selection.family=Russo+One&subset=cyrillic&sort=popularity
        self.font_title="fonts/IrinaCTT.ttf"
        self.font = "fonts/IrinaCTT.ttf"

    def setColors(self):
        """ Задаем основные цвета """
        # Цвет фона
        self.bgcolor = arcade.color.DEEP_CHAMPAGNE
        # Цвет текста заголовка
        self.titlecolor = arcade.color.FUZZY_WUZZY
        # Цвет текста подзаголовка
        self.subtitlecolor = arcade.color.IRRESISTIBLE
        # Цвет текста пункта меню
        self.menucolor = arcade.color.IRRESISTIBLE
        # Цвет текста выбранного пункта меню
        self.menucolorselected = arcade.color.FRENCH_LILAC
        # Задаем фоновый цвет
        arcade.set_background_color(self.bgcolor)
        #arcade.Texture(1,"fon.png")
        #arcade.Texture.draw()


    def setMenu(self):
        #print('2')
        # Переменная состояния приложения
        # Если = 0, то выводится начальный экран
        self.state = 0
        self.state1=99
        # Словарь для хранения пунктов меню
        self.Menu = {}
        # Первый из отображаемых элементов меню
        self.MenuFirst = 1
        # Последний из отображаемых пунктов меню
        self.MenuLast = 5
        # Собственно сами пункты меню
        self.Menu[0] = "Стартовое меню"
        self.Menu[1] = "Выбор набора карточек"
        self.Menu[2] = "Выбор аватара"
        self.Menu[3] = "Начать"
        self.Menu[4] = "О программе"
        self.Menu[5] = "Выход"
        self.Menu[6] = "Игра Детектив"
        self.Menu[7] = "Игра Подбери маску"
        self.Menu[8] = "Игра Пятнашки"
        self.Menu[9] = "Дальше"
        self.Menu[10] = "Игра Детектив"
        self.Menu[11] = "Игра Детектив"
       
        self.Menu[99] = "Пауза"


    def loadAvatars(self):
        """ Загрузка ававтаров """
        files = os.listdir(self.avatarPath)

        self.imgAvatars = arcade.SpriteList()

        for i in files:
            self.imgAvatar = arcade.Sprite(self.avatarPath+i, 1)
            self.imgAvatar.width = 100
            self.imgAvatar.height = 100
            self.imgAvatar.center_x = 0
            self.imgAvatar.center_y = 0
            self.imgAvatars.append(self.imgAvatar)

    def on_draw(self):
        """ Рендерем экран """
        arcade.start_render()
        if self.state == 0:
            # Рисуем выбор аватара
            self.drawState0()
        elif self.state == 1:
            # Рисуем выбор набора карточек
            self.drawState1()
        elif self.state == 2:
            # Рисуем выбор игры
            self.drawState2()
        elif self.state == 3:
            # Рисуем игру Детектив 1
            self.drawState3()
        elif self.state == 4:
            # Рисуем игру Подбери маску 1
            self.drawState4()
        elif self.state == 5:
            # Рисуем игру Пятнашки
            self.drawState5()
        elif self.state == 6:
            # Рисуем игру Детектив 2
            self.drawState6()
        elif self.state == 7:
            # Рисуем игру Детектив 3
            self.drawState7()
        elif self.state == 8:
            # Рисуем игру Подбери маску 2
            self.drawState8()
        elif self.state == 9:
            # Рисуем игру Подбери маску 3
            self.drawState9()
        elif self.state == 10:
            # Рисуем игру Подбери маску 3
            self.drawState10()
        elif self.state == 11:
            # Рисуем игру Подбери маску 3
            self.drawState11()
        elif self.state == 50:
            # Рисуем О программе
            self.drawAbout()
        elif self.state == 51:
            # Рисуем Статистику
            self.drawStatistic()
        elif self.state == 97:
            #Подсчет верных/неверных ответов
            self.CountingAnswers()

        elif self.state == 98:
            quit()
        '''elif self.state == 9:
            # Рисуем сл игру
            self.drawState9()
        elif self.state == 10:
            # Рисуем сл игру
            self.drawState10()
        elif self.state == 11:
            # Рисуем сл игру
            self.drawState7()
        elif self.state == 12:
            # Рисуем сл игру
            self.drawState0()
        elif self.state == 5:
            # Выход
            try:
                quit()
            except:
                pass'''

    def load_sound_library():
        """
        Special code for Windows so we grab the proper avbin from our directory.
        Otherwise hope the correct package is installed.
        """
     
        # lazy loading
        if not load_sound_library._sound_library_loaded:
            load_sound_library._sound_library_loaded = True
        else:
            return
     
        import os
        appveyor = not os.environ.get('APPVEYOR') is None
     
        import platform
        system = platform.system()
        if system == 'Windows':
     
            import sys
            is64bit = sys.maxsize > 2**32
     
            import site
            packages = site.getsitepackages()
     
            if appveyor:
                if is64bit:
                    path = "Win64/avbin"
                else:
                    path = "Win32/avbin"
     
            else:
                if is64bit:
                    path = packages[0] + "/lib/site-packages/arcade/Win64/avbin"
                else:
                    path = packages[0] + "/lib/site-packages/arcade/Win32/avbin"
        elif system == 'Darwin':
            from distutils.sysconfig import get_python_lib
            path = get_python_lib() + '/lib/site-packages/arcade/lib/libavbin.10.dylib'
            pyglet.options['audio'] = ('openal', 'pulse', 'silent')
     
        else:
            path = "avbin"
            pyglet.options['audio'] = ('openal', 'pulse', 'silent')
     
        pyglet.lib.load_library(path)
        pyglet.have_avbin = True
     
    # Initialize static function variable
    load_sound_library._sound_library_loaded = False

    def load_sound(filename: str) -> typing.Any:
        """
        Load a sound and get it ready to play.
        """
     
        load_sound_library()
        source = pyglet.media.load(filename, streaming=False)
        return source
 
 
    def play_sound(sound: typing.Any):
        """
        Play a previously loaded sound.
        """
     
        load_sound_library()
        sound.play()

    def stop_sound(sound: typing.Any):
        """
        Stop a sound that is currently playing.

        :param sound:
        """
        sound.pause()


    def drawState0(self):
        # Выбор аватара
        self.text=""
        text = "Выбор аватара"
        color = self.titlecolor
        text_size = 44
        x = self.SCREEN_WIDTH // 3
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 9 + 10
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)
        #arcade.draw_rectangle_outline(660,680,450,65,color=arcade.color.RED)
               
        
        self.Fon.center_x = 0.5 * self.SCREEN_WIDTH - 10
        self.Fon.center_y = 0.5 * self.SCREEN_HEIGHT + 50
        self.Fon.draw()       
        
        #self.imgAvatars.draw()
        # Вывод конкретного спрайта
        w=self.imgAvatars.sprite_list[1].width
        h=self.imgAvatars.sprite_list[1].height
        counter = 4
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) //2
        y = self.SCREEN_HEIGHT // 2
        for i in range(0,len(self.imgAvatars.sprite_list)-1):
            self.imgAvatars.sprite_list[i].center_x = x
            x += w + s
            self.imgAvatars.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 4
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 2
                y += h + s

            self.imgAvatars.sprite_list[i].draw()
            # Определяем попадание курсора на аватар
            bottom =self.mouseY > self.imgAvatars.sprite_list[i].center_y - self.imgAvatars.sprite_list[i].height // 2
            top = self.mouseY < self.imgAvatars.sprite_list[i].center_y + self.imgAvatars.sprite_list[i].height // 2

            left = self.mouseX > self.imgAvatars.sprite_list[i].center_x - self.imgAvatars.sprite_list[i].width // 2
            right = self.mouseX < self.imgAvatars.sprite_list[i].center_x + self.imgAvatars.sprite_list[i].width // 2

            if (bottom and top) and (left and right):
                arcade.draw_rectangle_outline(self.imgAvatars.sprite_list[i].center_x,self.imgAvatars.sprite_list[i].center_y,self.imgAvatars.sprite_list[i].width,self.imgAvatars.sprite_list[i].height,color=arcade.color.DEEP_PEACH)
                if self.isMouseDown:
                    self.userAvatar = i

        # self.imgAvatars.sprite_list[self.userAvatar].center_x = 500
        # self.imgAvatars.sprite_list[self.userAvatar].center_y = 500
        # self.imgAvatars.sprite_list[self.userAvatar].draw()
        

        # Рисуем крестик
        self.aboutLogo1.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo1.width
        self.aboutLogo1.center_y = self.SCREEN_HEIGHT -(0.5*self.aboutLogo1.height)
        self.aboutLogo1.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo1.center_y - self.aboutLogo1.height // 2
        top = self.mouseY < self.aboutLogo1.center_y + self.aboutLogo1.height // 2

        left = self.mouseX > self.aboutLogo1.center_x - self.aboutLogo1.width // 2
        right = self.mouseX < self.aboutLogo1.center_x + self.aboutLogo1.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo1.center_x,self.aboutLogo1.center_y,self.aboutLogo1.width,self.aboutLogo1.height,color=arcade.color.DEEP_PEACH)
            if self.isMouseDown:
                self.MenuItemSelected = 98
                


        # Стрелка
        self.Strelka.center_x = self.SCREEN_WIDTH // 1.3 + 35
        self.Strelka.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka.draw()

        # Дальше
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15
        self.MenuItemSelected_2 = -1

        for i in range(0,self.MenuLasti):
            text = self.Menu[self.MenuFirst2+i]
            text_size = 35
            x = self.SCREEN_WIDTH // 1.3
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 1
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)

        #------------------------------


    def drawState1(self):
        # Выбор набора карточек
        text = "Выбор набора карточек"
        color = self.titlecolor
        text_size = 44
        x = self.SCREEN_WIDTH // 3.5
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 6
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        self.imgAvatars.sprite_list[self.userAvatar].center_x = self.imgAvatars.sprite_list[self.userAvatar].width
        self.imgAvatars.sprite_list[self.userAvatar].center_y = self.SCREEN_HEIGHT - self.imgAvatars.sprite_list[self.userAvatar].height
        self.imgAvatars.sprite_list[self.userAvatar].draw()

        """ Загрузка картинок """
        files1 = os.listdir(self.detectivePath3)

        self.imgCards1 = arcade.SpriteList()
        

        for i in files1:
            self.imgCard1 = arcade.Sprite(self.detectivePath3+i, 1)
            self.imgCard1.width = 300
            self.imgCard1.height = 350
            self.imgCard1.center_x = 0
            self.imgCard1.center_y = 0
            self.imgCards1.append(self.imgCard1)

        # Вывод конкретного спрайта
        w=self.imgCards1.sprite_list[1].width
        h=self.imgCards1.sprite_list[1].height
        counter = 2
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) // 5
        y = self.SCREEN_HEIGHT // 2
        for i in range(0,len(self.imgCards1.sprite_list)):
            self.imgCards1.sprite_list[i].center_x = x
            x += w + s
            self.imgCards1.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 5
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 2.9
                y += h + s

            self.imgCards1.sprite_list[i].draw()
            # Определяем попадание курсора на набор карточек
            bottom =self.mouseY > self.imgCards1.sprite_list[i].center_y - self.imgCards1.sprite_list[i].height // 2
            top = self.mouseY < self.imgCards1.sprite_list[i].center_y + self.imgCards1.sprite_list[i].height // 2

            left = self.mouseX > self.imgCards1.sprite_list[i].center_x - self.imgCards1.sprite_list[i].width // 2
            right = self.mouseX < self.imgCards1.sprite_list[i].center_x + self.imgCards1.sprite_list[i].width // 2

            if (bottom and top) and (left and right):
                arcade.draw_rectangle_outline(self.imgCards1.sprite_list[i].center_x,self.imgCards1.sprite_list[i].center_y,self.imgCards1.sprite_list[i].width,self.imgCards1.sprite_list[i].height,color=arcade.color.DEEP_PEACH)
                if self.isMouseDown:
                    self.userChoiceCards=i
                    self.MenuItemSelected = 2
        #print('выбрали набор карточек ',self.userChoiceCards)

        # Стрелка
        self.Strelka1.center_x =self.Strelka1.width // 3
        self.Strelka1.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka1.draw()
        
        # Назад
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15
        self.MenuItemSelected_2 = -1

        for i in range(0,self.MenuLasti):
            text = "Назад"
            text_size = 35
            x = self.Strelka1.width//9
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 0
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)
        
        # Стрелка
        self.Strelka.center_x = self.SCREEN_WIDTH // 1.3 + 35
        self.Strelka.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka.draw()

        # Дальше
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15
        self.MenuItemSelected_2 = -1

        for i in range(0,self.MenuLasti):
            text = self.Menu[self.MenuFirst2+i]
            text_size = 35
            x = self.SCREEN_WIDTH // 1.3
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 2
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)


        # Рисуем крестик
        self.aboutLogo1.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo1.width
        self.aboutLogo1.center_y = self.SCREEN_HEIGHT -(0.5*self.aboutLogo1.height)
        self.aboutLogo1.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo1.center_y - self.aboutLogo1.height // 2
        top = self.mouseY < self.aboutLogo1.center_y + self.aboutLogo1.height // 2

        left = self.mouseX > self.aboutLogo1.center_x - self.aboutLogo1.width // 2
        right = self.mouseX < self.aboutLogo1.center_x + self.aboutLogo1.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo1.center_x,self.aboutLogo1.center_y,self.aboutLogo1.width,self.aboutLogo1.height,color=arcade.color.DEEP_PEACH)
            if self.isMouseDown:
                self.MenuItemSelected = 98


    def drawState2(self):
        # Начать
        text = "Выбор игры"
        color = self.titlecolor
        text_size = 44
        x = self.SCREEN_WIDTH // 2.5
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 8
        arcade.draw_text(text, x, y, color, text_size, anchor_y = "center",font_name = self.font_title)
        self.setMenu1()
        self.drawMenu1()

        self.imgAvatars.sprite_list[self.userAvatar].center_x = self.imgAvatars.sprite_list[self.userAvatar].width
        self.imgAvatars.sprite_list[self.userAvatar].center_y = self.SCREEN_HEIGHT - self.imgAvatars.sprite_list[self.userAvatar].height
        self.imgAvatars.sprite_list[self.userAvatar].draw()

        # Рисуем крестик
        self.aboutLogo1.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo1.width
        self.aboutLogo1.center_y = self.SCREEN_HEIGHT -(0.5*self.aboutLogo1.height)
        self.aboutLogo1.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo1.center_y - self.aboutLogo1.height // 2
        top = self.mouseY < self.aboutLogo1.center_y + self.aboutLogo1.height // 2

        left = self.mouseX > self.aboutLogo1.center_x - self.aboutLogo1.width // 2
        right = self.mouseX < self.aboutLogo1.center_x + self.aboutLogo1.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo1.center_x,self.aboutLogo1.center_y,self.aboutLogo1.width,self.aboutLogo1.height,color=arcade.color.DEEP_PEACH)
            if self.isMouseDown:
                self.MenuItemSelected = 98
        # О программе
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=8
        self.MenuItemSelected_2 = -1

        for i in range(0,self.MenuLasti):
            text = 'О программе'
            text_size = 25
            x =  5
            y = self.SCREEN_HEIGHT - 4* height
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 50
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)

        # Статистика
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=8
        self.MenuItemSelected_2 = -1

        for i in range(0,self.MenuLasti):
            text = 'Статистика'
            text_size = 25
            x =  5
            y = 4* height
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 51
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)

        self.schet_card = 1
        self.coin=[0,0,0,0]
        self.coin_2=[0,0,0,0,0,0]
        self.coin_3=[0,0,0,0,0,0]

        
    def drawAbout(self):
        """ Рисуем о программе """
        x = self.SCREEN_WIDTH // 2.5
        lineHeight = 50
        # ------------------------
        text = "О программе"
        color = self.titlecolor
        text_size = 44
        y = self.SCREEN_HEIGHT  - 2*lineHeight
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        text =  "Программа предназначена для"
        color = self.subtitlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 2.6
        y = self.SCREEN_HEIGHT  - 3.3*lineHeight
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font)

        text =  "диагностики психологических особенностей детей"
        color = self.subtitlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 3.4
        y = self.SCREEN_HEIGHT  - 4*lineHeight
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font)

        # ------------------------
        text = "Заказчик:"
        color = self.titlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 2.2
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 3
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font)

        text = 'Гобу МО "Центр психолого-педагогической,'
        color = self.subtitlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 3
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 3 - 40
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font)

        text = 'медицинской и социальной помощи"'
        color = self.subtitlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 2.9
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 3 - 80
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font)

        #------------------------
        text = "Разработчики: "
        color = self.titlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 2.3
        y = self.SCREEN_HEIGHT - self.SCREEN_HEIGHT // 2
        arcade.draw_text(text, x, y, color, text_size, anchor_y="center", font_name=self.font)

        text = "Дарья Сумина (студентка 4 курса, группа МКН)"
        color = self.subtitlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 3.1
        y = self.SCREEN_HEIGHT - self.SCREEN_HEIGHT // 2 - 40
        arcade.draw_text(text, x, y, color, text_size,  anchor_y="center", font_name=self.font)

        text = "Олег Иванович Ляш (руководитель)"
        color = self.subtitlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 2.8
        y = self.SCREEN_HEIGHT - self.SCREEN_HEIGHT // 2 - 80
        arcade.draw_text(text, x, y, color, text_size, anchor_y="center", font_name=self.font)

        text = "Designed by Freepik"
        color = self.titlecolor
        text_size = 30
        x = self.SCREEN_WIDTH // 2.5
        y = self.SCREEN_HEIGHT - self.SCREEN_HEIGHT // 2 - 150
        arcade.draw_text(text, x, y, color, text_size, anchor_y="center", font_name=self.font)

        # Стрелка
        self.Strelka1.center_x =self.Strelka1.width // 3
        self.Strelka1.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka1.draw()

        # Назад
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15
        self.MenuItemSelected_2 = -1

        for i in range(0,self.MenuLasti):
            text = "Назад"
            text_size = 35
            x = self.Strelka1.width//9
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 2
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)
        
        # Рисуем крестик
        self.aboutLogo1.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo1.width
        self.aboutLogo1.center_y = self.SCREEN_HEIGHT -(0.5*self.aboutLogo1.height)
        self.aboutLogo1.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo1.center_y - self.aboutLogo1.height // 2
        top = self.mouseY < self.aboutLogo1.center_y + self.aboutLogo1.height // 2

        left = self.mouseX > self.aboutLogo1.center_x - self.aboutLogo1.width // 2
        right = self.mouseX < self.aboutLogo1.center_x + self.aboutLogo1.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo1.center_x,self.aboutLogo1.center_y,self.aboutLogo1.width,self.aboutLogo1.height,color=arcade.color.DEEP_PEACH)
            if self.isMouseDown:
                self.MenuItemSelected = 98

    def drawStatistic(self):
        # Рисуем статистику
        text = "Статистика"
        color = self.titlecolor
        text_size = 44
        x = self.SCREEN_WIDTH // 2.5
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 11
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)
        

        f=open('vern.txt', 'r')
        Alf=f.readlines()
        f.close()
        f=open('nevern.txt', 'r')
        Alf1=f.readlines()
        f.close()
        # Вывод конкретного спрайта для статистики
        w=self.imgAvatars.sprite_list[1].width
        h=self.imgAvatars.sprite_list[1].height
        counter = 2
        s = 450
        x = self.SCREEN_WIDTH // 2 - (counter * w) //0.5
        y = self.SCREEN_HEIGHT // 3
  
        for i in range(0,len(self.imgAvatars.sprite_list)-1):
            self.imgAvatars.sprite_list[i].center_x = x
            x += w + s
            self.imgAvatars.sprite_list[i].center_y = y
            counter -=1
            x1 = self.SCREEN_WIDTH // 2 - (counter * w) // 0.4
            x2 = self.SCREEN_WIDTH // 2 - (counter * w) //2.7
            if counter <=0:
                counter = 2
                x = self.SCREEN_WIDTH // 2 - (counter * w) //0.5
                x1 = self.SCREEN_WIDTH // 2 +  (counter * w) // 0.6
                x2 = self.SCREEN_WIDTH // 2 + (counter * w) //0.4
                # Выводим верные ответы во втором столбце
                text = "%s" % Alf[i]
                color = self.titlecolor
                text_size = 20
                arcade.draw_text(text, x1, y, color, text_size, anchor_y="center", font_name=self.font)
                # Выводим неверные ответы во втором столбце
                text1 = "%s" % Alf1[i]
                color = self.titlecolor
                text_size = 20
                arcade.draw_text(text1, x2+40, y, color, text_size, anchor_y="center", font_name=self.font)

                y += h
            else:
                # Выводим верные ответы в первом столбце
                text = "%s" % Alf[i]
                color = self.titlecolor
                text_size = 20
                arcade.draw_text(text, x1, y, color, text_size, anchor_y="center", font_name=self.font)
                # Вывоим неверные ответы в первом столбце
                text1 = "%s" % Alf1[i]
                color = self.titlecolor
                text_size = 20
                arcade.draw_text(text1, x2, y, color, text_size, anchor_y="center", font_name=self.font)

            
            self.imgAvatars.sprite_list[i].draw()

        
        s = 500

        text = "Верные"
        w=self.imgAvatars.sprite_list[1].width
        h=self.imgAvatars.sprite_list[1].height
        color = self.titlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) //0.7
        y = self.SCREEN_HEIGHT // 1.2
        arcade.draw_text(text, x, y, color, text_size, anchor_y="center", font_name=self.font)

        text = "Неверные"
        w=self.imgAvatars.sprite_list[1].width
        h=self.imgAvatars.sprite_list[1].height
        color = self.titlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) //2.7
        y = self.SCREEN_HEIGHT // 1.2
        arcade.draw_text(text, x, y, color, text_size, anchor_y="center", font_name=self.font)

        text = "Верные"
        w=self.imgAvatars.sprite_list[1].width
        h=self.imgAvatars.sprite_list[1].height
        color = self.titlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 2 + (counter * w) //0.7
        y = self.SCREEN_HEIGHT // 1.2
        arcade.draw_text(text, x, y, color, text_size, anchor_y="center", font_name=self.font)

        text = "Неверные"
        w=self.imgAvatars.sprite_list[1].width
        h=self.imgAvatars.sprite_list[1].height
        color = self.titlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 2 + (counter * w) //0.4
        y = self.SCREEN_HEIGHT // 1.2
        arcade.draw_text(text, x, y, color, text_size, anchor_y="center", font_name=self.font)

        
        # Стрелка
        self.Strelka1.center_x =self.Strelka1.width // 3
        self.Strelka1.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka1.draw()

        # Назад
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15
        self.MenuItemSelected_2 = -1

        for i in range(0,self.MenuLasti):
            text = "Назад"
            text_size = 35
            x = self.Strelka1.width//9
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 2
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)
        
        # Рисуем крестик
        self.aboutLogo1.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo1.width
        self.aboutLogo1.center_y = self.SCREEN_HEIGHT -(0.5*self.aboutLogo1.height)
        self.aboutLogo1.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo1.center_y - self.aboutLogo1.height // 2
        top = self.mouseY < self.aboutLogo1.center_y + self.aboutLogo1.height // 2

        left = self.mouseX > self.aboutLogo1.center_x - self.aboutLogo1.width // 2
        right = self.mouseX < self.aboutLogo1.center_x + self.aboutLogo1.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo1.center_x,self.aboutLogo1.center_y,self.aboutLogo1.width,self.aboutLogo1.height,color=arcade.color.DEEP_PEACH)
            if self.isMouseDown:
                self.MenuItemSelected = 98

    def setMenu1(self):
        # Переменная состояния приложения
        # Если = 0, то выводится начальный экран
        #self.state = 3
        # Словарь для хранения пунктов меню
        #self.Menu1 = {}
        # Первый из отображаемых элементов меню
        self.MenuFirst1 = 6
        # Последний из отображаемых пунктов меню
        self.MenuLastii = 3
        # Собственно сами пункты меню
        #self.Menu[6] = "Игра Детектив"
        #self.Menu[7] = "Игра Подбери маску"
        #self.Menu[8] = "Игра Пятнашки"

    def drawMenu1(self):
        """ Рисуем менюшку игры """
        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15
        self.MenuItemSelected_1 = -1

        """ Загрузка картинок """
        if self.userChoiceCards==0:
            files1 = os.listdir(self.menu1)
        elif self.userChoiceCards == 1:
            files1 = os.listdir(self.menu2)


        self.imgMenus = arcade.SpriteList()
        

        for i in files1:
            if self.userChoiceCards==0:
                self.imgMenu = arcade.Sprite(self.menu1+i, 1)
            elif self.userChoiceCards==1:
                self.imgMenu = arcade.Sprite(self.menu2+i, 1)
            self.imgMenu.width = 300
            self.imgMenu.height = 400
            self.imgMenu.center_x = 0
            self.imgMenu.center_y = 0
            self.imgMenus.append(self.imgMenu)

        # Вывод конкретного спрайта
        w=self.imgMenus.sprite_list[0].width
        h=self.imgMenus.sprite_list[0].height
        counter = 3
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) // 3.2
        y = self.SCREEN_HEIGHT // 2
        for i in range(0,len(self.imgMenus.sprite_list)):
            self.imgMenus.sprite_list[i].center_x = x
            x += w + s
            self.imgMenus.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 3
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 2.9
                y += h + s

            self.imgMenus.sprite_list[i].draw()
            # Определяем попадание курсора на набор карточек
            bottom =self.mouseY > self.imgMenus.sprite_list[i].center_y - self.imgMenus.sprite_list[i].height // 2
            top = self.mouseY < self.imgMenus.sprite_list[i].center_y + self.imgMenus.sprite_list[i].height // 2

            left = self.mouseX > self.imgMenus.sprite_list[i].center_x - self.imgMenus.sprite_list[i].width // 2
            right = self.mouseX < self.imgMenus.sprite_list[i].center_x + self.imgMenus.sprite_list[i].width // 2

            if (bottom and top) and (left and right):
                arcade.draw_rectangle_outline(self.imgMenus.sprite_list[i].center_x,self.imgMenus.sprite_list[i].center_y,self.imgMenus.sprite_list[i].width,self.imgMenus.sprite_list[i].height,color=arcade.color.DEEP_PEACH)
                if self.isMouseDown:
                    self.MenuItemSelected = self.MenuFirst1+i-3

        self.odin=0
        self.dva=0
        self.tri=0
        self.e=0
        '''for i in range(0,self.MenuLastii):
            text = self.Menu[self.MenuFirst1+i]
            text_size = 35
            x = self.SCREEN_WIDTH // 2.7
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 3 - 20 - i*40
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = self.MenuFirst1+i-3
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, anchor_y = "center",font_name = self.font_title)
'''
        # Стрелка
        self.Strelka1.center_x =self.Strelka1.width // 3
        self.Strelka1.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka1.draw()
        
        # Назад
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15
        self.MenuItemSelected_2 = -1

        for i in range(0,self.MenuLasti):
            text = "Назад"
            text_size = 35
            x = self.Strelka1.width//9
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 1
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)
        

        # Рисуем крестик
        self.aboutLogo1.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo1.width
        self.aboutLogo1.center_y = self.SCREEN_HEIGHT -(0.5*self.aboutLogo1.height)
        self.aboutLogo1.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo1.center_y - self.aboutLogo1.height // 2
        top = self.mouseY < self.aboutLogo1.center_y + self.aboutLogo1.height // 2

        left = self.mouseX > self.aboutLogo1.center_x - self.aboutLogo1.width // 2
        right = self.mouseX < self.aboutLogo1.center_x + self.aboutLogo1.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo1.center_x,self.aboutLogo1.center_y,self.aboutLogo1.width,self.aboutLogo1.height,color=arcade.color.DEEP_PEACH)
            if self.isMouseDown:
                self.MenuItemSelected = 98

    def drawState3(self):
        self.vernotvet=0
        # Игра Детектив 1
        self.text="Детектив 1"
        text = "Игра Детектив"
        color = self.titlecolor
        text_size = 38
        x = self.SCREEN_WIDTH // 2.7
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 12
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        self.imgAvatars.sprite_list[self.userAvatar].center_x = self.imgAvatars.sprite_list[self.userAvatar].width
        self.imgAvatars.sprite_list[self.userAvatar].center_y = self.SCREEN_HEIGHT - self.imgAvatars.sprite_list[self.userAvatar].height
        self.imgAvatars.sprite_list[self.userAvatar].draw()

        #print(self.userChoiceCards)

        if self.userChoiceCards==0:
            text = "Найди девочку, которой подарили подарок"
            text2 = "Какое у неё настроение?"
            files1 = os.listdir(self.detectivePath1)
            if self.odin==0:
                self.StateSound()
        elif self.userChoiceCards == 1:
            text = "Найди мальчика, которому подарили подарок"
            text2 = "Какое у него настроение?"
            files1 = os.listdir(self.detectivePath2)
            if self.odin==0:
                self.StateSound()

        color = self.subtitlecolor
        text_size = 33
        x = self.SCREEN_WIDTH // 4.2
        x2 = self.SCREEN_WIDTH // 3.5
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 6
        y2 = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 4
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)
        arcade.draw_text(text2,x2, y2,color, text_size, anchor_y = "center",font_name = self.font_title)
        
        #------------------------------

        """ Загрузка картинок """
        #files1 = os.listdir(self.detectivePath2)

        self.imgDetectives1 = arcade.SpriteList()

        for i in files1:
            #k=k+1
            if self.userChoiceCards==0:
                self.imgDetective1 = arcade.Sprite(self.detectivePath1+i, 1)
            elif self.userChoiceCards == 1:
                self.imgDetective1 = arcade.Sprite(self.detectivePath2+i, 1)
            else:
                self.imgDetective1 = arcade.Sprite(self.detectivePath1+i, 1)
            self.imgDetective1.width = 150
            self.imgDetective1.height = 200
            self.imgDetective1.center_x = 0
            self.imgDetective1.center_y = 0
            self.imgDetectives1.append(self.imgDetective1)

        #-------------

        # Стрелка
        self.Strelka1.center_x =self.Strelka1.width // 3
        self.Strelka1.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka1.draw()
        
        # Назад
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15
        self.MenuItemSelected_2 = -1

        for i in range(0,self.MenuLasti):
            text = "Назад"
            text_size = 35
            x = self.Strelka1.width//9
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 2
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)
        


        # Стрелка
        self.Strelka.center_x = self.SCREEN_WIDTH // 1.3 + 35
        self.Strelka.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka.draw()

        
        # Дальше
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15

        for i in range(0,self.MenuLasti):
            text = self.Menu[self.MenuFirst2+i]
            text_size = 35
            x = self.SCREEN_WIDTH // 1.3
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.sl=6
                self.MenuItemSelected = 97
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)

        #------------------------------

        # Вывод конкретного спрайта
        w=self.imgDetectives1.sprite_list[1].width
        h=self.imgDetectives1.sprite_list[1].height
        counter = 2
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) //2.3
        y = self.SCREEN_HEIGHT // 2
        for i in self.RAND:
            #print(i)
            self.imgDetectives1.sprite_list[i].center_x = x
            x += w + s
            self.imgDetectives1.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 2
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 2.3
                y += h + s

            self.imgDetectives1.sprite_list[i].draw()
            # Определяем попадание курсора на аватар
            bottom =self.mouseY > self.imgDetectives1.sprite_list[i].center_y - self.imgDetectives1.sprite_list[i].height // 2
            top = self.mouseY < self.imgDetectives1.sprite_list[i].center_y + self.imgDetectives1.sprite_list[i].height // 2

            left = self.mouseX > self.imgDetectives1.sprite_list[i].center_x - self.imgDetectives1.sprite_list[i].width // 2
            right = self.mouseX < self.imgDetectives1.sprite_list[i].center_x + self.imgDetectives1.sprite_list[i].width // 2

            if (bottom and top) and (left and right):
                arcade.draw_rectangle_outline(self.imgDetectives1.sprite_list[i].center_x,self.imgDetectives1.sprite_list[i].center_y,self.imgDetectives1.sprite_list[i].width,self.imgDetectives1.sprite_list[i].height,color=arcade.color.DEEP_PEACH)
                if self.isMouseDown:
                    self.otvet=i
                    if (self.otvet==self.vernotvet) and (self.tri_one==0):
                        self.StateSound()
                    elif (self.otvet!=self.vernotvet) and (self.tri_two==0):
                        self.StateSound()

        # Рисуем крестик
        self.aboutLogo1.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo1.width
        self.aboutLogo1.center_y = self.SCREEN_HEIGHT -(0.5*self.aboutLogo1.height)
        self.aboutLogo1.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo1.center_y - self.aboutLogo1.height // 2
        top = self.mouseY < self.aboutLogo1.center_y + self.aboutLogo1.height // 2

        left = self.mouseX > self.aboutLogo1.center_x - self.aboutLogo1.width // 2
        right = self.mouseX < self.aboutLogo1.center_x + self.aboutLogo1.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo1.center_x,self.aboutLogo1.center_y,self.aboutLogo1.width,self.aboutLogo1.height,color=arcade.color.DEEP_PEACH)
            if self.isMouseDown:
                self.MenuItemSelected = 98

        # Рисуем мегафон
        self.aboutLogo4.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo4.width
        self.aboutLogo4.center_y = self.SCREEN_HEIGHT -(1.2*self.aboutLogo4.height)
        self.aboutLogo4.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo4.center_y - self.aboutLogo4.height // 2
        top = self.mouseY < self.aboutLogo4.center_y + self.aboutLogo4.height // 2

        left = self.mouseX > self.aboutLogo4.center_x - self.aboutLogo4.width // 2
        right = self.mouseX < self.aboutLogo4.center_x + self.aboutLogo4.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo4.center_x,self.aboutLogo4.center_y,self.aboutLogo4.width,self.aboutLogo4.height,color=arcade.color.FELDSPAR)
            if (self.isMouseDown) and (self.tri_one==0):
                self.odin=0
                self.StateSound()
                self.MenuItemSelected = 3

                
                
                

    def StateSound(self):
        if self.text=="Детектив 1":
            if (self.userChoiceCards==0) and (self.odin==0):
                arcade.play_sound(arcade.load_sound('music/Детектив 1 0.wav'))
                self.odin=1
                self.state == 3
                self.tri_one=1
            elif (self.userChoiceCards==1) and (self.odin==0):
                arcade.play_sound(arcade.load_sound('music/Детектив 1 1.wav'))
                self.odin=1
                self.state == 3
                self.tri_one=1
            elif (self.otvet==self.vernotvet) and (self.tri_one==0):
                arcade.play_sound(arcade.load_sound('music/Детектив 3 3.wav'))
                self.tri_one=1
                self.state == 3
            elif (self.otvet!=self.vernotvet) and (self.tri_two==0):
                arcade.play_sound(arcade.load_sound('music/Детектив 3 4.wav'))
                self.tri_two=1
                self.state == 3
        elif self.text=="Детектив 2":
            if (self.userChoiceCards==0) and (self.dva==0):
                arcade.play_sound(arcade.load_sound('music/Детектив 2 0.wav'))
                self.dva=1
                self.state == 6
                self.tri_one=1
            elif (self.userChoiceCards==1) and (self.dva==0):
                arcade.play_sound(arcade.load_sound('music/Детектив 2 1.wav'))
                self.dva=1
                self.state == 6
                self.tri_one=1
            elif (self.otvet==self.vernotvet) and (self.tri_one==0):
                arcade.play_sound(arcade.load_sound('music/Детектив 3 3.wav'))
                self.tri_one=1
                self.state == 6
            elif (self.otvet!=self.vernotvet) and (self.tri_two==0):
                arcade.play_sound(arcade.load_sound('music/Детектив 3 4.wav'))
                self.tri_two=1
                self.state == 6
        elif self.text=="Детектив 3":
            if (self.userChoiceCards==0) and (self.tri==0):
                arcade.play_sound(arcade.load_sound('music/Детектив 3 0.wav'))
                self.tri=1
                self.state == 7
                self.tri_one=1
            elif (self.userChoiceCards==1) and (self.tri==0):
                arcade.play_sound(arcade.load_sound('music/Детектив 3 1.wav'))
                self.tri=1
                self.state == 7
                self.tri_one=1
            elif (self.otvet==self.vernotvet) and (self.tri_one==0):
                arcade.play_sound(arcade.load_sound('music/Детектив 3 3.wav'))
                self.tri_one=1
                self.state == 7
            elif (self.otvet!=self.vernotvet) and (self.tri_two==0):
                arcade.play_sound(arcade.load_sound('music/Детектив 3 4.wav'))
                self.tri_two=1
                self.state == 7
        elif self.text=="Подбери маску 1":
            if (self.userChoiceCards==0) and (self.odin==0):
                arcade.play_sound(arcade.load_sound('music/Подбери маску 1 0.wav'))
                self.odin=1
                self.state == 4
                self.tri_one=1
            elif (self.userChoiceCards==1) and (self.odin==0):
                arcade.play_sound(arcade.load_sound('music/Подбери маску 1 1.wav'))
                self.odin=1
                self.state == 4
                self.tri_one=1
            elif (self.otvet==self.vernotvet) and (self.tri_one==0):
                arcade.play_sound(arcade.load_sound('music/Детектив 3 3.wav'))
                self.tri_one=1
                self.state == 4
            elif (self.otvet!=self.vernotvet) and (self.tri_two==0):
                arcade.play_sound(arcade.load_sound('music/Детектив 3 4.wav'))
                self.tri_two=1
                self.state == 4
        elif self.text=="Подбери маску 2":
            if (self.userChoiceCards==0) and (self.dva==0):
                arcade.play_sound(arcade.load_sound('music/Подбери маску 2 0.wav'))
                self.dva=1
                self.state == 8
                self.tri_one=1
            elif (self.userChoiceCards==1) and (self.dva==0):
                arcade.play_sound(arcade.load_sound('music/Подбери маску 2 1.wav'))
                self.dva=1
                self.state == 8
                self.tri_one=1
            elif (self.otvet==self.vernotvet) and (self.tri_one==0):
                arcade.play_sound(arcade.load_sound('music/Детектив 3 3.wav'))
                self.tri_one=1
                self.state == 8
            elif (self.otvet!=self.vernotvet) and (self.tri_two==0):
                arcade.play_sound(arcade.load_sound('music/Детектив 3 4.wav'))
                self.tri_two=1
                self.state == 8
        elif self.text=="Подбери маску 3":
            if (self.userChoiceCards==0) and (self.tri==0):
                arcade.play_sound(arcade.load_sound('music/Подбери маску 3 0.wav'))
                self.Sound=arcade.load_sound('music/Подбери маску 3 0.wav')
                self.tri=1
                self.state == 9
                self.tri_one=1
            elif (self.userChoiceCards==1) and (self.tri==0):
                arcade.play_sound(arcade.load_sound('music/Подбери маску 3 1.wav'))
                self.tri=1
                self.state == 9
                self.tri_one=1
            elif (self.otvet==self.vernotvet) and (self.tri_one==0):
                arcade.play_sound(arcade.load_sound('music/Детектив 3 3.wav'))
                self.tri_one=1
                self.state == 9
            elif (self.otvet!=self.vernotvet) and (self.tri_two==0):
                arcade.play_sound(arcade.load_sound('music/Детектив 3 4.wav'))
                self.tri_two=1
                self.state == 9
                
            


    def drawState6(self):
        self.vernotvet=1
        #print("ghjghj", self.userBadAnswers)
        otvet=-1
        # Игра Детектив 2
        self.text="Детектив 2"
        text = "Игра Детектив"
        color = self.titlecolor
        text_size = 38
        x = self.SCREEN_WIDTH // 2.7
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 12
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        self.imgAvatars.sprite_list[self.userAvatar].center_x = self.imgAvatars.sprite_list[self.userAvatar].width
        self.imgAvatars.sprite_list[self.userAvatar].center_y = self.SCREEN_HEIGHT - self.imgAvatars.sprite_list[self.userAvatar].height
        self.imgAvatars.sprite_list[self.userAvatar].draw()

        #print(self.userChoiceCards)

        if self.userChoiceCards==0:
            text = "Найди девочку, которая  потеряла конфету"
            text2 = "Какое у неё настроение?"
            files1 = os.listdir(self.detectivePath1)
            if self.dva==0:
                self.StateSound()
        elif self.userChoiceCards == 1:
            text = "Найди мальчика, который потерял конфету"
            text2 = "Какое у него настроение?"
            files1 = os.listdir(self.detectivePath2)
            if self.dva==0:
                self.StateSound()
        color = self.subtitlecolor
        text_size = 33
        x = self.SCREEN_WIDTH // 4.2
        x2 = self.SCREEN_WIDTH // 3.5
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 6
        y2 = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 4
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)
        arcade.draw_text(text2,x2, y2,color, text_size, anchor_y = "center",font_name = self.font_title)
        
        #------------------------------

        """ Загрузка картинок """
        #files1 = os.listdir(self.detectivePath2)

        self.imgDetectives2 = arcade.SpriteList()

        for i in files1:
            if self.userChoiceCards==0:
                self.imgDetective2 = arcade.Sprite(self.detectivePath1+i, 1)
            elif self.userChoiceCards == 1:
                self.imgDetective2 = arcade.Sprite(self.detectivePath2+i, 1)
            else:
                self.imgDetective2 = arcade.Sprite(self.detectivePath1+i, 1)
            self.imgDetective2.width = 150
            self.imgDetective2.height = 200
            self.imgDetective2.center_x = 0
            self.imgDetective2.center_y = 0
            self.imgDetectives2.append(self.imgDetective2)

        

        #------------------------------

        # Вывод конкретного спрайта
        w=self.imgDetectives2.sprite_list[1].width
        h=self.imgDetectives2.sprite_list[1].height
        counter = 2
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) //2.3
        y = self.SCREEN_HEIGHT // 4
        for i in self.RAND1:
            self.imgDetectives2.sprite_list[i].center_x = x
            x += w + s
            self.imgDetectives2.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 2
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 2.3
                y += h + s

            self.imgDetectives2.sprite_list[i].draw()
            # Определяем попадание курсора на аватар
            bottom =self.mouseY > self.imgDetectives2.sprite_list[i].center_y - self.imgDetectives2.sprite_list[i].height // 2
            top = self.mouseY < self.imgDetectives2.sprite_list[i].center_y + self.imgDetectives2.sprite_list[i].height // 2

            left = self.mouseX > self.imgDetectives2.sprite_list[i].center_x - self.imgDetectives2.sprite_list[i].width // 2
            right = self.mouseX < self.imgDetectives2.sprite_list[i].center_x + self.imgDetectives2.sprite_list[i].width // 2

            if (bottom and top) and (left and right):
                arcade.draw_rectangle_outline(self.imgDetectives2.sprite_list[i].center_x,self.imgDetectives2.sprite_list[i].center_y,self.imgDetectives2.sprite_list[i].width,self.imgDetectives2.sprite_list[i].height,color=arcade.color.FELDSPAR)
                if self.isMouseDown:
                    self.otvet=i
                    if (self.otvet==self.vernotvet) and (self.tri_one==0):
                        self.StateSound()
                    elif (self.otvet!=self.vernotvet) and (self.tri_two==0):
                        self.StateSound()
                    """if i==0:
                        print('dthyj')
                        self.userGoodAnswers+=1
                        print(self.userGoodAnswers)
                    else:
                        print('----')
                        self.userBadAnswers+=1
                        print(self.userBadAnswers)"""
                    #self.userAvatar = i
                    #print(otvet)


        #-------------

        # Стрелка
        self.Strelka1.center_x =self.Strelka1.width // 3
        self.Strelka1.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka1.draw()
        
        # Назад
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15

        for i in range(0,self.MenuLasti):
            text = "Назад"
            text_size = 35
            x = self.Strelka1.width//9
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                if self.isMouseDown:
                    self.MenuItemSelected = 3
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)
        

        self.MenuItemSelected = 6
        
        # Стрелка
        self.Strelka.center_x = self.SCREEN_WIDTH // 1.3 + 35
        self.Strelka.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka.draw()

        
        # Дальше
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15

        for i in range(0,self.MenuLasti):
            text = self.Menu[self.MenuFirst2+i]
            text_size = 35
            x = self.SCREEN_WIDTH // 1.3
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.sl=7
                self.MenuItemSelected = 97
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)

        # Рисуем крестик
        self.aboutLogo1.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo1.width
        self.aboutLogo1.center_y = self.SCREEN_HEIGHT -(0.5*self.aboutLogo1.height)
        self.aboutLogo1.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo1.center_y - self.aboutLogo1.height // 2
        top = self.mouseY < self.aboutLogo1.center_y + self.aboutLogo1.height // 2

        left = self.mouseX > self.aboutLogo1.center_x - self.aboutLogo1.width // 2
        right = self.mouseX < self.aboutLogo1.center_x + self.aboutLogo1.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo1.center_x,self.aboutLogo1.center_y,self.aboutLogo1.width,self.aboutLogo1.height,color=arcade.color.RED)
            if self.isMouseDown:
                self.MenuItemSelected = 98

        # Рисуем мегафон
        self.aboutLogo4.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo4.width
        self.aboutLogo4.center_y = self.SCREEN_HEIGHT -(1.2*self.aboutLogo4.height)
        self.aboutLogo4.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo4.center_y - self.aboutLogo4.height // 2
        top = self.mouseY < self.aboutLogo4.center_y + self.aboutLogo4.height // 2

        left = self.mouseX > self.aboutLogo4.center_x - self.aboutLogo4.width // 2
        right = self.mouseX < self.aboutLogo4.center_x + self.aboutLogo4.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo4.center_x,self.aboutLogo4.center_y,self.aboutLogo4.width,self.aboutLogo4.height,color=arcade.color.FELDSPAR)
            if (self.isMouseDown) and (self.tri_one==0):
                self.dva=0
                self.StateSound()

    def drawState7(self):
        self.vernotvet=5
        #print("ghjghj", self.userBadAnswers)
        otvet=-1
        # Игра Детектив 3
        text = "Игра Детектив"
        self.text = "Детектив 3"
        color = self.titlecolor
        text_size = 38
        x = self.SCREEN_WIDTH // 2.7
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 12
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        self.imgAvatars.sprite_list[self.userAvatar].center_x = self.imgAvatars.sprite_list[self.userAvatar].width
        self.imgAvatars.sprite_list[self.userAvatar].center_y = self.SCREEN_HEIGHT - self.imgAvatars.sprite_list[self.userAvatar].height
        self.imgAvatars.sprite_list[self.userAvatar].draw()

        #print(self.userChoiceCards)

        if self.userChoiceCards==0:
            text = "Мама нашла спрятанные Катей фантики от конфет"
            text2 = "за диваном. Найди где Катя."
            text3 = "Как себя чувствует Катя?"
            files1 = os.listdir(self.detectivePath1)
            if self.tri==0:
                self.StateSound()
        elif self.userChoiceCards == 1:
            text = "Мама нашла спрятанные Вовой фантики от конфет"
            text2 = "за диваном. Найди где Вова."
            text3 = "Как себя чувствует Вова?"
            files1 = os.listdir(self.detectivePath2)
            if self.tri==0:
                self.StateSound()
        color = self.subtitlecolor
        text_size = 33
        x = self.SCREEN_WIDTH // 7
        x2 = self.SCREEN_WIDTH // 3.8
        x3 = self.SCREEN_WIDTH // 3.5
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 7
        y2 = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 5.25
        y3 = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 4
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)
        arcade.draw_text(text2,x2, y2,color, text_size, anchor_y = "center",font_name = self.font_title)
        arcade.draw_text(text3,x3, y3,color, text_size, anchor_y = "center",font_name = self.font_title)

        #------------------------------

        """ Загрузка картинок """
        #files1 = os.listdir(self.detectivePath2)

        self.imgDetectives3 = arcade.SpriteList()

        for i in files1:
            if self.userChoiceCards==0:
                self.imgDetective3 = arcade.Sprite(self.detectivePath1+i, 1)
            elif self.userChoiceCards == 1:
                self.imgDetective3 = arcade.Sprite(self.detectivePath2+i, 1)
            else:
                self.imgDetective3 = arcade.Sprite(self.detectivePath1+i, 1)
            self.imgDetective3.width = 150
            self.imgDetective3.height = 200
            self.imgDetective3.center_x = 0
            self.imgDetective3.center_y = 0
            self.imgDetectives3.append(self.imgDetective3)

        #-------------

        # Стрелка
        self.Strelka1.center_x =self.Strelka1.width // 3
        self.Strelka1.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka1.draw()
        
        # Назад
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15

        for i in range(0,self.MenuLasti):
            text = "Назад"
            text_size = 35
            x = self.Strelka1.width//9
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 6
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)
        

        # Стрелка
        self.Strelka.center_x = self.SCREEN_WIDTH // 1.3 + 35
        self.Strelka.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka.draw()


        # Дальше
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15

        for i in range(0,self.MenuLasti):
            text = self.Menu[self.MenuFirst2+i]
            text_size = 35
            x = self.SCREEN_WIDTH // 1.3
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                if self.isMouseDown:
                    color = self.menucolorselected
                    self.sl=2
                    self.MenuItemSelected = 97
                    #sound.pause()
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)

        #------------------------------

        # Вывод конкретного спрайта
        w=self.imgDetectives3.sprite_list[1].width
        h=self.imgDetectives3.sprite_list[1].height
        counter = 3
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) //2.3
        y = self.SCREEN_HEIGHT // 4
        for i in self.RAND2:
            self.imgDetectives3.sprite_list[i].center_x = x
            x += w + s
            self.imgDetectives3.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 3
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 2.3
                y += h + s

            self.imgDetectives3.sprite_list[i].draw()
            # Определяем попадание курсора на аватар
            bottom =self.mouseY > self.imgDetectives3.sprite_list[i].center_y - self.imgDetectives3.sprite_list[i].height // 2
            top = self.mouseY < self.imgDetectives3.sprite_list[i].center_y + self.imgDetectives3.sprite_list[i].height // 2

            left = self.mouseX > self.imgDetectives3.sprite_list[i].center_x - self.imgDetectives3.sprite_list[i].width // 2
            right = self.mouseX < self.imgDetectives3.sprite_list[i].center_x + self.imgDetectives3.sprite_list[i].width // 2

            if (bottom and top) and (left and right):
                arcade.draw_rectangle_outline(self.imgDetectives3.sprite_list[i].center_x,self.imgDetectives3.sprite_list[i].center_y,self.imgDetectives3.sprite_list[i].width,self.imgDetectives3.sprite_list[i].height,color=arcade.color.FELDSPAR)
                if self.isMouseDown:
                    self.otvet=i
                    if (self.otvet==self.vernotvet) and (self.tri_one==0):
                        self.StateSound()
                    elif (self.otvet!=self.vernotvet) and (self.tri_two==0):
                        self.StateSound()
                        
                    """if i==0:
                        print('dthyj')
                        self.userGoodAnswers+=1
                        print(self.userGoodAnswers)
                    else:
                        print('----')
                        self.userBadAnswers+=1
                        print(self.userBadAnswers)"""
                    #self.userAvatar = i
                    #print(otvet)

        # Рисуем крестик
        self.aboutLogo1.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo1.width
        self.aboutLogo1.center_y = self.SCREEN_HEIGHT -(0.5*self.aboutLogo1.height)
        self.aboutLogo1.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo1.center_y - self.aboutLogo1.height // 2
        top = self.mouseY < self.aboutLogo1.center_y + self.aboutLogo1.height // 2

        left = self.mouseX > self.aboutLogo1.center_x - self.aboutLogo1.width // 2
        right = self.mouseX < self.aboutLogo1.center_x + self.aboutLogo1.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo1.center_x,self.aboutLogo1.center_y,self.aboutLogo1.width,self.aboutLogo1.height,color=arcade.color.FELDSPAR)
            if self.isMouseDown:
                self.MenuItemSelected = 98

        # Рисуем мегафон
        self.aboutLogo4.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo4.width
        self.aboutLogo4.center_y = self.SCREEN_HEIGHT -(1.2*self.aboutLogo4.height)
        self.aboutLogo4.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo4.center_y - self.aboutLogo4.height // 2
        top = self.mouseY < self.aboutLogo4.center_y + self.aboutLogo4.height // 2

        left = self.mouseX > self.aboutLogo4.center_x - self.aboutLogo4.width // 2
        right = self.mouseX < self.aboutLogo4.center_x + self.aboutLogo4.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo4.center_x,self.aboutLogo4.center_y,self.aboutLogo4.width,self.aboutLogo4.height,color=arcade.color.FELDSPAR)
            if (self.isMouseDown) and (self.tri_one==0):
                self.tri=0
                self.StateSound()


    def drawState4(self):
        self.vernotvet=0
        # Игра Подбери маску
        text = "Игра Подбери маску"
        self.text = "Подбери маску 1"
        color = self.titlecolor
        text_size = 38
        x = self.SCREEN_WIDTH // 2.7
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 12
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        self.imgAvatars.sprite_list[self.userAvatar].center_x = self.imgAvatars.sprite_list[self.userAvatar].width
        self.imgAvatars.sprite_list[self.userAvatar].center_y = self.SCREEN_HEIGHT - self.imgAvatars.sprite_list[self.userAvatar].height
        self.imgAvatars.sprite_list[self.userAvatar].draw()


        if self.userChoiceCards==0:
            if self.e==0:
                self.aboutLogo2 = arcade.Sprite(self.detectivePath4 + "1_1.png",0.19)
            else:
                self.aboutLogo2 = arcade.Sprite(self.detectivePath7 + str(int(self.otvet)+1)+".png",0.19)
            text = "Сегодня Вика подружилась с девочкой. Какое у неё"
            text2 = "настроение? Найди такую маску."
            #files1 = os.listdir(self.detectivePath4)
            if self.odin==0:
                self.StateSound()
        elif self.userChoiceCards == 1:
            if self.e==0:
                self.aboutLogo2 = arcade.Sprite(self.detectivePath4 + "1.png",0.19)
            else:
                self.aboutLogo2 = arcade.Sprite(self.detectivePath7 + str(self.otvet+1)+"_1.png",0.19)
            text = "Сегодня Витя подружился с мальчиком. Какое у него"
            text2 = "настроение? Найди такую маску."
            if self.odin==0:
                self.StateSound()
        color = self.subtitlecolor
        text_size = 33
        x = self.SCREEN_WIDTH // 7
        x2 = self.SCREEN_WIDTH // 4.5
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 5
        y2 = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 3.75
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)
        arcade.draw_text(text2,x2, y2,color, text_size, anchor_y = "center",font_name = self.font_title)
        
        self.aboutLogo2.center_x = self.SCREEN_WIDTH // 2
        self.aboutLogo2.center_y = y - self.aboutLogo2.height // 1.1
        self.aboutLogo2.draw()


        files = os.listdir(self.detectivePath5)

        self.imgMaskes = arcade.SpriteList()

        for i in files:
            self.imgMask = arcade.Sprite(self.detectivePath5+i, 1)
            self.imgMask.width = 100
            self.imgMask.height = 100
            self.imgMask.center_x = 0
            self.imgMask.center_y = 0
            self.imgMaskes.append(self.imgMask)

        #self.imgAvatars.draw()
        # Вывод конкретного спрайта
        w=self.imgMaskes.sprite_list[1].width
        h=self.imgMaskes.sprite_list[1].height
        counter = 2
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) //2
        y = self.SCREEN_HEIGHT // 6
        for i in range(0,2):
            self.imgMaskes.sprite_list[i].center_x = x
            x += w + s
            self.imgMaskes.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 1
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 2
                #y += h + s

            self.imgMaskes.sprite_list[i].draw()
            # Определяем попадание курсора на аватар
            bottom =self.mouseY > self.imgMaskes.sprite_list[i].center_y - self.imgMaskes.sprite_list[i].height // 2
            top = self.mouseY < self.imgMaskes.sprite_list[i].center_y + self.imgMaskes.sprite_list[i].height // 2

            left = self.mouseX > self.imgMaskes.sprite_list[i].center_x - self.imgMaskes.sprite_list[i].width // 2
            right = self.mouseX < self.imgMaskes.sprite_list[i].center_x + self.imgMaskes.sprite_list[i].width // 2

            if (bottom and top) and (left and right):
                arcade.draw_rectangle_outline(self.imgMaskes.sprite_list[i].center_x,self.imgMaskes.sprite_list[i].center_y,self.imgMaskes.sprite_list[i].width,self.imgMaskes.sprite_list[i].height,color=arcade.color.FELDSPAR)
                if self.isMouseDown:
                    self.otvet=i
                    if (self.otvet==self.vernotvet) and (self.tri_one==0):
                        self.StateSound()
                        self.e=1
                    elif (self.otvet!=self.vernotvet) and (self.tri_two==0):
                        self.StateSound()
                        self.e=1
                    #x=self.mouseX
                    #y=self.mouseY
                    #self.imgMaskes.sprite_list[i].draw()
                    #self.userAvatar = i
                    #print('всё ок')
        

        # Стрелка
        self.Strelka1.center_x =self.Strelka1.width // 3
        self.Strelka1.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka1.draw()
        
        # Назад
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15
        self.MenuItemSelected_2 = -1

        for i in range(0,self.MenuLasti):
            text = "Назад"
            text_size = 35
            x = self.Strelka1.width//9
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 2
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)
        

        # Стрелка
        self.Strelka.center_x = self.SCREEN_WIDTH // 1.3 + 35
        self.Strelka.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka.draw()

        
        # Дальше
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15

        for i in range(0,self.MenuLasti):
            text = self.Menu[self.MenuFirst2+i]
            text_size = 35
            x = self.SCREEN_WIDTH // 1.3
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                if self.isMouseDown:
                    color = self.menucolorselected
                    self.sl=8
                    self.MenuItemSelected = 97
                    self.e=0
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)

        # Рисуем крестик
        self.aboutLogo1.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo1.width
        self.aboutLogo1.center_y = self.SCREEN_HEIGHT -(0.5*self.aboutLogo1.height)
        self.aboutLogo1.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo1.center_y - self.aboutLogo1.height // 2
        top = self.mouseY < self.aboutLogo1.center_y + self.aboutLogo1.height // 2

        left = self.mouseX > self.aboutLogo1.center_x - self.aboutLogo1.width // 2
        right = self.mouseX < self.aboutLogo1.center_x + self.aboutLogo1.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo1.center_x,self.aboutLogo1.center_y,self.aboutLogo1.width,self.aboutLogo1.height,color=arcade.color.FELDSPAR)
            if self.isMouseDown:
                self.MenuItemSelected = 98

        # Рисуем мегафон
        self.aboutLogo4.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo4.width
        self.aboutLogo4.center_y = self.SCREEN_HEIGHT -(1.2*self.aboutLogo4.height)
        self.aboutLogo4.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo4.center_y - self.aboutLogo4.height // 2
        top = self.mouseY < self.aboutLogo4.center_y + self.aboutLogo4.height // 2

        left = self.mouseX > self.aboutLogo4.center_x - self.aboutLogo4.width // 2
        right = self.mouseX < self.aboutLogo4.center_x + self.aboutLogo4.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo4.center_x,self.aboutLogo4.center_y,self.aboutLogo4.width,self.aboutLogo4.height,color=arcade.color.FELDSPAR)
            if (self.isMouseDown) and (self.tri_one==0):
                self.odin=0
                self.StateSound()


    def drawState8(self):
        self.vernotvet=1
        # Игра Подбери маску 2
        text = "Игра Подбери маску"
        self.text = "Подбери маску 2"
        color = self.titlecolor
        text_size = 38
        x = self.SCREEN_WIDTH // 2.7
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 12
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        self.imgAvatars.sprite_list[self.userAvatar].center_x = self.imgAvatars.sprite_list[self.userAvatar].width
        self.imgAvatars.sprite_list[self.userAvatar].center_y = self.SCREEN_HEIGHT - self.imgAvatars.sprite_list[self.userAvatar].height
        self.imgAvatars.sprite_list[self.userAvatar].draw()

        
        if self.userChoiceCards==0:
            if self.e==0:
                self.aboutLogo2 = arcade.Sprite(self.detectivePath4 + "1_1.png",0.19)
            else:
                self.aboutLogo2 = arcade.Sprite(self.detectivePath7 + str(self.otvet+1)+".png",0.19)
            text = "Ребята из детского сада ходили в Цирк, вот только"
            text2 = "Света заболела и не смогла пойти. Какое настроение"
            text3 = "у Светы? Найди такую маску."
            x2 = self.SCREEN_WIDTH // 7.2
            if self.dva==0:
                self.StateSound()
        elif self.userChoiceCards == 1:
            if self.e==0:
                self.aboutLogo2 = arcade.Sprite(self.detectivePath4 + "1.png",0.19)
            else:
                self.aboutLogo2 = arcade.Sprite(self.detectivePath7 + str(self.otvet+1)+"_1.png",0.19)
            text = "Ребята из детского сада ходили в Цирк, вот только"
            text2 = "Коля заболел и не смог пойти. Какое настроение"
            text3 = "у Коли? Найди такую маску."
            x2 = self.SCREEN_WIDTH // 6.5
            if self.dva==0:
                self.StateSound()
        color = self.subtitlecolor
        text_size = 33
        x = self.SCREEN_WIDTH // 7
        x3 = self.SCREEN_WIDTH // 3.1
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 7
        y2 = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 5
        y3 = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 4
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)
        arcade.draw_text(text2,x2, y2,color, text_size, anchor_y = "center",font_name = self.font_title)
        arcade.draw_text(text3,x3, y3,color, text_size, anchor_y = "center",font_name = self.font_title)

        self.aboutLogo2.center_x = self.SCREEN_WIDTH // 2
        self.aboutLogo2.center_y = y - self.aboutLogo2.height // 1.1
        self.aboutLogo2.draw()


        files = os.listdir(self.detectivePath5)

        self.imgMaskes = arcade.SpriteList()

        for i in files:
            if (i=="3.png") and (self.userChoiceCards == 1):
                self.imgMask = arcade.Sprite(self.detectivePath+"3_1.png", 1)
            else:
                self.imgMask = arcade.Sprite(self.detectivePath5+i, 1)
            self.imgMask.width = 100
            self.imgMask.height = 100
            self.imgMask.center_x = 0
            self.imgMask.center_y = 0
            self.imgMaskes.append(self.imgMask)

        #self.imgAvatars.draw()
        # Вывод конкретного спрайта
        w=self.imgMaskes.sprite_list[1].width
        h=self.imgMaskes.sprite_list[1].height
        counter = 4
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) //2
        y = self.SCREEN_HEIGHT // 6
        for i in range(0,4):
            self.imgMaskes.sprite_list[i].center_x = x
            x += w + s
            self.imgMaskes.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 4
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 2
                #y += h + s

            self.imgMaskes.sprite_list[i].draw()
            # Определяем попадание курсора на аватар
            bottom =self.mouseY > self.imgMaskes.sprite_list[i].center_y - self.imgMaskes.sprite_list[i].height // 2
            top = self.mouseY < self.imgMaskes.sprite_list[i].center_y + self.imgMaskes.sprite_list[i].height // 2

            left = self.mouseX > self.imgMaskes.sprite_list[i].center_x - self.imgMaskes.sprite_list[i].width // 2
            right = self.mouseX < self.imgMaskes.sprite_list[i].center_x + self.imgMaskes.sprite_list[i].width // 2

            if (bottom and top) and (left and right):
                arcade.draw_rectangle_outline(self.imgMaskes.sprite_list[i].center_x,self.imgMaskes.sprite_list[i].center_y,self.imgMaskes.sprite_list[i].width,self.imgMaskes.sprite_list[i].height,color=arcade.color.FELDSPAR)
                if self.isMouseDown:
                    self.otvet=i
                    if (self.otvet==self.vernotvet) and (self.tri_one==0):
                        self.StateSound()
                        self.e=1
                        self.MenuItemSelected = 8
                    elif (self.otvet!=self.vernotvet) and (self.tri_two==0):
                        self.StateSound()
                        self.e=1
                        self.MenuItemSelected = 8
                    


        # Стрелка
        self.Strelka1.center_x =self.Strelka1.width // 3
        self.Strelka1.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka1.draw()
        
        # Назад
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15

        for i in range(0,self.MenuLasti):
            text = "Назад"
            text_size = 35
            x = self.Strelka1.width//9
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 4
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)
        
        
        # Стрелка
        self.Strelka.center_x = self.SCREEN_WIDTH // 1.3 + 35
        self.Strelka.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka.draw()

        
        # Дальше
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15

        for i in range(0,self.MenuLasti):
            text = self.Menu[self.MenuFirst2+i]
            text_size = 35
            x = self.SCREEN_WIDTH // 1.3
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//4 and mx<x+width//2:
                if self.isMouseDown:
                    color = self.menucolorselected
                    self.sl=9
                    self.MenuItemSelected = 97
                    self.e=0
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)

        # Рисуем крестик
        self.aboutLogo1.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo1.width
        self.aboutLogo1.center_y = self.SCREEN_HEIGHT -(0.5*self.aboutLogo1.height)
        self.aboutLogo1.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo1.center_y - self.aboutLogo1.height // 2
        top = self.mouseY < self.aboutLogo1.center_y + self.aboutLogo1.height // 2

        left = self.mouseX > self.aboutLogo1.center_x - self.aboutLogo1.width // 2
        right = self.mouseX < self.aboutLogo1.center_x + self.aboutLogo1.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo1.center_x,self.aboutLogo1.center_y,self.aboutLogo1.width,self.aboutLogo1.height,color=arcade.color.FELDSPAR)
            if self.isMouseDown:
                self.MenuItemSelected = 98

        '''# Рисуем мегафон
        self.aboutLogo4.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo4.width
        self.aboutLogo4.center_y = self.SCREEN_HEIGHT -(1.2*self.aboutLogo4.height)
        self.aboutLogo4.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo4.center_y - self.aboutLogo4.height // 2
        top = self.mouseY < self.aboutLogo4.center_y + self.aboutLogo4.height // 2

        left = self.mouseX > self.aboutLogo4.center_x - self.aboutLogo4.width // 2
        right = self.mouseX < self.aboutLogo4.center_x + self.aboutLogo4.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo4.center_x,self.aboutLogo4.center_y,self.aboutLogo4.width,self.aboutLogo4.height,color=arcade.color.FELDSPAR)
            if (self.isMouseDown) and (self.tri_one==0):
                self.dva=0
                self.StateSound()'''


    def drawState9(self):
        self.vernotvet=0
        # Игра Подбери маску 3
        text = "Игра Подбери маску"
        self.text = "Подбери маску 3"
        color = self.titlecolor
        text_size = 38
        x = self.SCREEN_WIDTH // 2.7
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 12
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        self.imgAvatars.sprite_list[self.userAvatar].center_x = self.imgAvatars.sprite_list[self.userAvatar].width
        self.imgAvatars.sprite_list[self.userAvatar].center_y = self.SCREEN_HEIGHT - self.imgAvatars.sprite_list[self.userAvatar].height
        self.imgAvatars.sprite_list[self.userAvatar].draw()

        
        if self.userChoiceCards==0:
            if self.e==0:
                self.aboutLogo2 = arcade.Sprite(self.detectivePath4 + "1_1.png",0.19)
            else:
                #print(self.otvet)
                self.aboutLogo2 = arcade.Sprite(self.detectivePath7 + str(self.otvet+1)+".png",0.19)
            text = "Наташа очень любит солнечную погоду. Сегодня на "
            text2 = "улице светит солнце. Какое у неё настроение?"
            text3 = "Найди такую маску."
            if self.tri==0:
                self.StateSound()
        elif self.userChoiceCards == 1:
            if self.e==0:
                self.aboutLogo2 = arcade.Sprite(self.detectivePath4 + "1.png",0.19)
            else:
                self.aboutLogo2 = arcade.Sprite(self.detectivePath7 + str(self.otvet+1)+"_1.png",0.19)
            text = "Миша очень любит солнечную погоду. Сегодня на "
            text2 = "улице светит солнце. Какое у него настроение?"
            text3 = "Найди такую маску."
            if self.tri==0:
                self.StateSound()
        color = self.subtitlecolor
        text_size = 33
        x = self.SCREEN_WIDTH // 7
        x2 = self.SCREEN_WIDTH // 6.9
        x3 = self.SCREEN_WIDTH // 3.1
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 7
        y2 = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 5.25
        y3 = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 4
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)
        arcade.draw_text(text2,x2, y2,color, text_size, anchor_y = "center",font_name = self.font_title)
        arcade.draw_text(text3,x3, y3,color, text_size, anchor_y = "center",font_name = self.font_title)

        self.aboutLogo2.center_x = self.SCREEN_WIDTH // 2
        self.aboutLogo2.center_y = y - self.aboutLogo2.height // 1.1
        self.aboutLogo2.draw()


        files = os.listdir(self.detectivePath5)

        self.imgMaskes = arcade.SpriteList()

        for i in files:
            if (i=="3.png") and (self.userChoiceCards == 1):
                self.imgMask = arcade.Sprite(self.detectivePath+"3_1.png", 1)
            else:
                self.imgMask = arcade.Sprite(self.detectivePath5+i, 1)
            self.imgMask.width = 100
            self.imgMask.height = 100
            self.imgMask.center_x = 0
            self.imgMask.center_y = 0
            self.imgMaskes.append(self.imgMask)

        #self.imgAvatars.draw()
        # Вывод конкретного спрайта
        w=self.imgMaskes.sprite_list[1].width
        h=self.imgMaskes.sprite_list[1].height
        counter = 6
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) //2
        y = self.SCREEN_HEIGHT // 6
        for i in range(0,6):
            self.imgMaskes.sprite_list[i].center_x = x
            x += w + s
            self.imgMaskes.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 6
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 2
                #y += h + s

            self.imgMaskes.sprite_list[i].draw()
            # Определяем попадание курсора на аватар
            bottom =self.mouseY > self.imgMaskes.sprite_list[i].center_y - self.imgMaskes.sprite_list[i].height // 2
            top = self.mouseY < self.imgMaskes.sprite_list[i].center_y + self.imgMaskes.sprite_list[i].height // 2

            left = self.mouseX > self.imgMaskes.sprite_list[i].center_x - self.imgMaskes.sprite_list[i].width // 2
            right = self.mouseX < self.imgMaskes.sprite_list[i].center_x + self.imgMaskes.sprite_list[i].width // 2

            if (bottom and top) and (left and right):
                arcade.draw_rectangle_outline(self.imgMaskes.sprite_list[i].center_x,self.imgMaskes.sprite_list[i].center_y,self.imgMaskes.sprite_list[i].width,self.imgMaskes.sprite_list[i].height,color=arcade.color.FELDSPAR)
                if self.isMouseDown:
                    self.otvet=i
                    if (self.otvet==self.vernotvet) and (self.tri_one==0):
                        self.StateSound()
                        self.e=1
                        self.MenuItemSelected = 9
                    elif (self.otvet!=self.vernotvet) and (self.tri_two==0):
                        self.StateSound()
                        self.e=1
                        self.MenuItemSelected = 9

        
        # Стрелка
        self.Strelka1.center_x =self.Strelka1.width // 3
        self.Strelka1.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka1.draw()
        
        # Назад
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15
        self.MenuItemSelected_2 = -1

        for i in range(0,self.MenuLasti):
            text = "Назад"
            text_size = 35
            x = self.Strelka1.width//9
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 8
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)
        


        # Рисуем крестик
        self.aboutLogo1.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo1.width
        self.aboutLogo1.center_y = self.SCREEN_HEIGHT -(0.5*self.aboutLogo1.height)
        self.aboutLogo1.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo1.center_y - self.aboutLogo1.height // 2
        top = self.mouseY < self.aboutLogo1.center_y + self.aboutLogo1.height // 2

        left = self.mouseX > self.aboutLogo1.center_x - self.aboutLogo1.width // 2
        right = self.mouseX < self.aboutLogo1.center_x + self.aboutLogo1.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo1.center_x,self.aboutLogo1.center_y,self.aboutLogo1.width,self.aboutLogo1.height,color=arcade.color.FELDSPAR)
            if self.isMouseDown:
                self.MenuItemSelected = 98

        # Рисуем мегафон
        self.aboutLogo4.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo4.width
        self.aboutLogo4.center_y = self.SCREEN_HEIGHT -(1.2*self.aboutLogo4.height)
        self.aboutLogo4.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo4.center_y - self.aboutLogo4.height // 2
        top = self.mouseY < self.aboutLogo4.center_y + self.aboutLogo4.height // 2

        left = self.mouseX > self.aboutLogo4.center_x - self.aboutLogo4.width // 2
        right = self.mouseX < self.aboutLogo4.center_x + self.aboutLogo4.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo4.center_x,self.aboutLogo4.center_y,self.aboutLogo4.width,self.aboutLogo4.height,color=arcade.color.FELDSPAR)
            if (self.isMouseDown) and (self.tri_one==0):
                self.tri=0
                self.StateSound()


                # Стрелка
        self.Strelka.center_x = self.SCREEN_WIDTH // 1.2 + 35
        self.Strelka.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka.draw()

        
        # Дальше
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15

        for i in range(0,self.MenuLasti):
            text = self.Menu[self.MenuFirst2+i]
            text_size = 35
            x = self.SCREEN_WIDTH // 1.2
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//4 and mx<x+width//2:
                if self.isMouseDown:
                    color = self.menucolorselected
                    self.sl=2
                    self.MenuItemSelected = 97
                    self.e=0
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)



    def drawState5(self):
        self.MenuItemSelected = 5
        self.clic = 0
        lop=0
        # Игра Пятнашки 1
        self.text="Пятнашки"
        text = "Игра Пятнашки"
        color = self.titlecolor
        text_size = 38
        x = self.SCREEN_WIDTH // 2.7
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 12
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = "Comic Sans MS")

        self.imgAvatars.sprite_list[self.userAvatar].center_x = self.imgAvatars.sprite_list[self.userAvatar].width
        self.imgAvatars.sprite_list[self.userAvatar].center_y = self.SCREEN_HEIGHT - self.imgAvatars.sprite_list[self.userAvatar].height
        self.imgAvatars.sprite_list[self.userAvatar].draw()


        #Создаем сами картинки

        
        if self.userChoiceCards==0:
            files = os.listdir(self.detectivePath1)
        elif self.userChoiceCards==1:
            files = os.listdir(self.detectivePath2)

        self.imgPytns_1 = arcade.SpriteList()

        for j in range(0,4):
            for i in files:
                k=str(self.RAND_1[j]+1)+'.jpg'
                if str(i)==k:
                    
                    if self.userChoiceCards==0:
                        self.imgPytn = arcade.Sprite(self.detectivePath1+i, 1)
                    
                    elif self.userChoiceCards == 1:
                        self.imgPytn = arcade.Sprite(self.detectivePath2+i, 1)
                    #self.imgPytn = arcade.Sprite(self.detectivePath1+i, 1)
                    self.imgPytn.width = 150
                    self.imgPytn.height = 250
                    self.imgPytn.center_x = 0
                    self.imgPytn.center_y = 0
                    self.imgPytns_1.append(self.imgPytn)

        #self.imgAvatars.draw()
        # Вывод конкретного спрайта
        w=self.imgPytns_1.sprite_list[1].width
        h=self.imgPytns_1.sprite_list[1].height
        counter = 2
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) // 3
        y = self.SCREEN_HEIGHT // 3
        for i in range(0,len(self.imgPytns_1.sprite_list)):
            self.imgPytns_1.sprite_list[i].center_x = x
            x += w + s
            self.imgPytns_1.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 2
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 3
                y += h + s
        
            #self.imgPytns_1.sprite_list[i].draw()'''
        #Создаем "рубашки" карточек
        files = os.listdir(self.detectivePath6)

        self.imgPytns = arcade.SpriteList()

        for i in files:
            self.imgPytn = arcade.Sprite(self.detectivePath6+i, 1)
            self.imgPytn.width = 150
            self.imgPytn.height = 250
            self.imgPytn.center_x = 0
            self.imgPytn.center_y = 0
            self.imgPytns.append(self.imgPytn)

        #self.imgAvatars.draw()
        # Вывод конкретного спрайта
        w=self.imgPytns.sprite_list[1].width
        h=self.imgPytns.sprite_list[1].height
        counter = 2
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) // 3
        y = self.SCREEN_HEIGHT // 3
        for i in range(0,len(self.imgPytns.sprite_list)):
            self.imgPytns.sprite_list[i].center_x = x
            x += w + s
            self.imgPytns.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 2
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 3
                y += h + s
                
            if self.coin[i] == 0:
                self.imgPytns.sprite_list[i].draw()
            elif self.coin[i] == 1:
                self.imgPytns_1.sprite_list[i].draw()
            if self.coin[i] == -1:
                #arcade.pause(1)
                pass
                


            # Определяем попадание курсора на аватар
            bottom =self.mouseY > self.imgPytns.sprite_list[i].center_y - self.imgPytns.sprite_list[i].height // 2
            top = self.mouseY < self.imgPytns.sprite_list[i].center_y + self.imgPytns.sprite_list[i].height // 2

            left = self.mouseX > self.imgPytns.sprite_list[i].center_x - self.imgPytns.sprite_list[i].width // 2
            right = self.mouseX < self.imgPytns.sprite_list[i].center_x + self.imgPytns.sprite_list[i].width // 2

            if (bottom and top) and (left and right):
                arcade.draw_rectangle_outline(self.imgPytns.sprite_list[i].center_x,self.imgPytns.sprite_list[i].center_y,self.imgPytns.sprite_list[i].width,self.imgPytns.sprite_list[i].height,color=arcade.color.FELDSPAR)
                if self.isMouseDown:
                    if (self.schet_card>1) and (self.schet_card<3):
                        k=str(self.RAND_1[i]+1)+'.jpg'
                        #print('номер карточки ',k)
                        #print(i)
                        #print(k)
                        if self.coin[i]==0:
                            self.coin[i]=1
                        #print(self.coin)
                        #print("нажал",self.schet_card)
                        self.imgPytns_1.sprite_list[i].draw()
                        for c in range(0, len(self.coin)-1):
                            for s in range(1, len(self.coin)):
                                if (self.coin[c]==1) and (self.coin[s]==1) and (self.RAND_1[c]==self.RAND_1[s]) and (c!=s):
                                    self.imgPytns_1.sprite_list[i].draw()
                                    #print(c, self.coin[c], s, self.coin[s], self.RAND_1[c], self.RAND_1[s])
                                    arcade.pause(0.1)
                                    self.coin[c]=-1
                                    self.coin[s]=-1
                                    self.schet_card=1
                                    #print(self.coin)
                                elif (self.coin[c]==1) and (self.coin[s]==1) and (self.RAND_1[c]!=self.RAND_1[s]) and (c!=s):
                                    self.coin[c]=0
                                    self.coin[s]=0
                                    self.coin[i]=0
                                    self.schet_card=1
                                #print(self.coin)
                        self.schet_card=1
                    elif self.schet_card>2:
                        self.schet_card=1
                        for f in range(0, len(self.coin)):
                            if self.coin[f] != -1:
                                self.coin[f]=0
                    

                            
                    #print(self.imgPytns.sprite_list[i])
        # Стрелка
        self.Strelka1.center_x =self.Strelka1.width // 3
        self.Strelka1.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka1.draw()
        
        # Назад
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15
        self.MenuItemSelected_2 = -1

        for i in range(0,self.MenuLasti):
            text = "Назад"
            text_size = 35
            x = self.Strelka1.width//9
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 2
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)
        

        # Стрелка
        self.Strelka.center_x = self.SCREEN_WIDTH // 1.3 + 35
        self.Strelka.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka.draw()

        
            # Дальше
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15

        for i in range(0,self.MenuLasti):
            text = self.Menu[self.MenuFirst2+i]
            text_size = 35
            x = self.SCREEN_WIDTH // 1.3
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 10
                self.schet_card=1
                self.coin_2=[0,0,0,0,0,0]
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)

        # Рисуем крестик
        self.aboutLogo1.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo1.width
        self.aboutLogo1.center_y = self.SCREEN_HEIGHT -(0.5*self.aboutLogo1.height)
        self.aboutLogo1.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo1.center_y - self.aboutLogo1.height // 2
        top = self.mouseY < self.aboutLogo1.center_y + self.aboutLogo1.height // 2

        left = self.mouseX > self.aboutLogo1.center_x - self.aboutLogo1.width // 2
        right = self.mouseX < self.aboutLogo1.center_x + self.aboutLogo1.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo1.center_x,self.aboutLogo1.center_y,self.aboutLogo1.width,self.aboutLogo1.height,color=arcade.color.FELDSPAR)
            if self.isMouseDown:
                self.MenuItemSelected = 98

    def drawState10(self):
        self.MenuItemSelected = 10
        self.clic = 0
        lop=0
        # Игра Пятнашки 2
        self.text="Пятнашки 2"
        text = "Игра Пятнашки"
        color = self.titlecolor
        text_size = 38
        x = self.SCREEN_WIDTH // 2.7
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 12
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = "Comic Sans MS")

        self.imgAvatars.sprite_list[self.userAvatar].center_x = self.imgAvatars.sprite_list[self.userAvatar].width
        self.imgAvatars.sprite_list[self.userAvatar].center_y = self.SCREEN_HEIGHT - self.imgAvatars.sprite_list[self.userAvatar].height
        self.imgAvatars.sprite_list[self.userAvatar].draw()


        #Создаем сами картинки

        
        if self.userChoiceCards==0:
            files = os.listdir(self.detectivePath1)
        elif self.userChoiceCards==1:
            files = os.listdir(self.detectivePath2)

        self.imgPytns_2 = arcade.SpriteList()

        for j in range(0,6):
            for i in files:
                k=str(self.RAND_2[j]+1)+'.jpg'
                if str(i)==k:
                    
                    if self.userChoiceCards==0:
                        self.imgPytn = arcade.Sprite(self.detectivePath1+i, 1)
                    
                    elif self.userChoiceCards == 1:
                        self.imgPytn = arcade.Sprite(self.detectivePath2+i, 1)
                    #self.imgPytn = arcade.Sprite(self.detectivePath1+i, 1)
                    self.imgPytn.width = 150
                    self.imgPytn.height = 250
                    self.imgPytn.center_x = 0
                    self.imgPytn.center_y = 0
                    self.imgPytns_2.append(self.imgPytn)

        #self.imgAvatars.draw()
        # Вывод конкретного спрайта
        w=self.imgPytns_2.sprite_list[1].width
        h=self.imgPytns_2.sprite_list[1].height
        counter = 3
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) // 3
        y = self.SCREEN_HEIGHT // 3
        for i in range(0,len(self.imgPytns_2.sprite_list)):
            self.imgPytns_2.sprite_list[i].center_x = x
            x += w + s
            self.imgPytns_2.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 3
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 3
                y += h + s
        
            #self.imgPytns_1.sprite_list[i].draw()'''
        #Создаем "рубашки" карточек
        files = os.listdir(self.detectivePath8)

        self.imgPytns = arcade.SpriteList()

        for i in files:
            self.imgPytn = arcade.Sprite(self.detectivePath8+i, 1)
            self.imgPytn.width = 150
            self.imgPytn.height = 250
            self.imgPytn.center_x = 0
            self.imgPytn.center_y = 0
            self.imgPytns.append(self.imgPytn)

        #self.imgAvatars.draw()
        # Вывод конкретного спрайта
        w=self.imgPytns.sprite_list[1].width
        h=self.imgPytns.sprite_list[1].height
        counter = 3
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) // 3
        y = self.SCREEN_HEIGHT // 3
        for i in range(0,len(self.imgPytns.sprite_list)):
            self.imgPytns.sprite_list[i].center_x = x
            x += w + s
            self.imgPytns.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 3
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 3
                y += h + s
                
            if self.coin_2[i] == 0:
                self.imgPytns.sprite_list[i].draw()
            elif self.coin_2[i] == 1:
                self.imgPytns_2.sprite_list[i].draw()
            if self.coin_2[i] == -1:
                #arcade.pause(1)
                pass
                


            # Определяем попадание курсора на аватар
            bottom =self.mouseY > self.imgPytns.sprite_list[i].center_y - self.imgPytns.sprite_list[i].height // 2
            top = self.mouseY < self.imgPytns.sprite_list[i].center_y + self.imgPytns.sprite_list[i].height // 2

            left = self.mouseX > self.imgPytns.sprite_list[i].center_x - self.imgPytns.sprite_list[i].width // 2
            right = self.mouseX < self.imgPytns.sprite_list[i].center_x + self.imgPytns.sprite_list[i].width // 2

            if (bottom and top) and (left and right):
                arcade.draw_rectangle_outline(self.imgPytns.sprite_list[i].center_x,self.imgPytns.sprite_list[i].center_y,self.imgPytns.sprite_list[i].width,self.imgPytns.sprite_list[i].height,color=arcade.color.FELDSPAR)
                if self.isMouseDown:
                    if (self.schet_card>1) and (self.schet_card<3):
                        k=str(self.RAND_2[i]+1)+'.jpg'
                        #print('номер карточки ',k)
                        #print(i)
                        #print(k)
                        if self.coin_2[i]==0:
                            self.coin_2[i]=1
                        #print(self.coin_2)
                        #print("нажал",self.schet_card)
                        self.imgPytns_2.sprite_list[i].draw()
                        for c in range(0, len(self.coin_2)-1):
                            for s in range(1, len(self.coin_2)):
                                if (self.coin_2[c]==1) and (self.coin_2[s]==1) and (self.RAND_2[c]==self.RAND_2[s]) and (c!=s):
                                    self.imgPytns_2.sprite_list[i].draw()
                                    #print(c, self.coin_2[c], s, self.coin_2[s], self.RAND_2[c], self.RAND_2[s])
                                    arcade.pause(0.1)
                                    self.coin_2[c]=-1
                                    self.coin_2[s]=-1
                                    self.schet_card=1
                                    #print(self.coin)
                                elif (self.coin_2[c]==1) and (self.coin_2[s]==1) and (self.RAND_2[c]!=self.RAND_2[s]) and (c!=s):
                                    self.coin_2[c]=0
                                    self.coin_2[s]=0
                                    self.coin_2[i]=0
                                    self.schet_card=1
                                #print(self.coin_2)
                        self.schet_card=1
                    elif self.schet_card>2:
                        self.schet_card=1
                        for f in range(0, len(self.coin_2)):
                            if self.coin_2[f] != -1:
                                self.coin_2[f]=0
                    

                            
                    #print(self.imgPytns.sprite_list[i])
        # Стрелка
        self.Strelka1.center_x =self.Strelka1.width // 3
        self.Strelka1.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka1.draw()
        
        # Назад
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15
        self.MenuItemSelected_2 = -1

        for i in range(0,self.MenuLasti):
            text = "Назад"
            text_size = 35
            x = self.Strelka1.width//9
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 5
                self.coin=[0,0,0,0]
                self.schet_card=1
                
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)
        

        # Стрелка
        self.Strelka.center_x = self.SCREEN_WIDTH // 1.3 + 35
        self.Strelka.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka.draw()

        
            # Дальше
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15

        for i in range(0,self.MenuLasti):
            text = self.Menu[self.MenuFirst2+i]
            text_size = 35
            x = self.SCREEN_WIDTH // 1.3
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 11
                self.coin_3=[0,0,0,0,0,0]
                self.schet_card=1
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)

        # Рисуем крестик
        self.aboutLogo1.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo1.width
        self.aboutLogo1.center_y = self.SCREEN_HEIGHT -(0.5*self.aboutLogo1.height)
        self.aboutLogo1.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo1.center_y - self.aboutLogo1.height // 2
        top = self.mouseY < self.aboutLogo1.center_y + self.aboutLogo1.height // 2

        left = self.mouseX > self.aboutLogo1.center_x - self.aboutLogo1.width // 2
        right = self.mouseX < self.aboutLogo1.center_x + self.aboutLogo1.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo1.center_x,self.aboutLogo1.center_y,self.aboutLogo1.width,self.aboutLogo1.height,color=arcade.color.FELDSPAR)
            if self.isMouseDown:
                self.MenuItemSelected = 98


    def drawState11(self):
        self.MenuItemSelected = 11
        self.clic = 0
        lop=0
        # Игра Пятнашки 3
        self.text="Пятнашки 3"
        text = "Игра Пятнашки"
        color = self.titlecolor
        text_size = 38
        x = self.SCREEN_WIDTH // 2.7
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 12
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = "Comic Sans MS")

        self.imgAvatars.sprite_list[self.userAvatar].center_x = self.imgAvatars.sprite_list[self.userAvatar].width
        self.imgAvatars.sprite_list[self.userAvatar].center_y = self.SCREEN_HEIGHT - self.imgAvatars.sprite_list[self.userAvatar].height
        self.imgAvatars.sprite_list[self.userAvatar].draw()


        #Создаем сами картинки

        
        if self.userChoiceCards==0:
            files = os.listdir(self.detectivePath1)
        elif self.userChoiceCards==1:
            files = os.listdir(self.detectivePath2)

        self.imgPytns_3 = arcade.SpriteList()

        for j in range(0,6):
            for i in files:
                k=str(self.RAND_3[j]+1)+'.jpg'
                if str(i)==k:
                    
                    if self.userChoiceCards==0:
                        self.imgPytn = arcade.Sprite(self.detectivePath1+i, 1)
                    
                    elif self.userChoiceCards == 1:
                        self.imgPytn = arcade.Sprite(self.detectivePath2+i, 1)
                    #self.imgPytn = arcade.Sprite(self.detectivePath1+i, 1)
                    self.imgPytn.width = 150
                    self.imgPytn.height = 250
                    self.imgPytn.center_x = 0
                    self.imgPytn.center_y = 0
                    self.imgPytns_3.append(self.imgPytn)

        #self.imgAvatars.draw()
        # Вывод конкретного спрайта
        w=self.imgPytns_3.sprite_list[1].width
        h=self.imgPytns_3.sprite_list[1].height
        counter = 3
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) // 3
        y = self.SCREEN_HEIGHT // 3
        for i in range(0,len(self.imgPytns_3.sprite_list)):
            self.imgPytns_3.sprite_list[i].center_x = x
            x += w + s
            self.imgPytns_3.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 3
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 3
                y += h + s
        
            #self.imgPytns_1.sprite_list[i].draw()
        #Создаем "рубашки" карточек
        files = os.listdir(self.detectivePath8)

        self.imgPytns = arcade.SpriteList()

        for i in files:
            self.imgPytn = arcade.Sprite(self.detectivePath8+i, 1)
            self.imgPytn.width = 150
            self.imgPytn.height = 250
            self.imgPytn.center_x = 0
            self.imgPytn.center_y = 0
            self.imgPytns.append(self.imgPytn)

        #self.imgAvatars.draw()
        # Вывод конкретного спрайта
        w=self.imgPytns.sprite_list[1].width
        h=self.imgPytns.sprite_list[1].height
        counter = 3
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) // 3
        y = self.SCREEN_HEIGHT // 3
        for i in range(0,len(self.imgPytns.sprite_list)):
            self.imgPytns.sprite_list[i].center_x = x
            x += w + s
            self.imgPytns.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 3
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 3
                y += h + s
                
            if self.coin_3[i] == 0:
                self.imgPytns.sprite_list[i].draw()
            elif self.coin_3[i] == 1:
                self.imgPytns_3.sprite_list[i].draw()
            if self.coin_3[i] == -1:
                #arcade.pause(1)
                pass
                


            # Определяем попадание курсора на аватар
            bottom =self.mouseY > self.imgPytns.sprite_list[i].center_y - self.imgPytns.sprite_list[i].height // 2
            top = self.mouseY < self.imgPytns.sprite_list[i].center_y + self.imgPytns.sprite_list[i].height // 2

            left = self.mouseX > self.imgPytns.sprite_list[i].center_x - self.imgPytns.sprite_list[i].width // 2
            right = self.mouseX < self.imgPytns.sprite_list[i].center_x + self.imgPytns.sprite_list[i].width // 2

            if (bottom and top) and (left and right):
                arcade.draw_rectangle_outline(self.imgPytns.sprite_list[i].center_x,self.imgPytns.sprite_list[i].center_y,self.imgPytns.sprite_list[i].width,self.imgPytns.sprite_list[i].height,color=arcade.color.FELDSPAR)
                if self.isMouseDown:
                    if (self.schet_card>1) and (self.schet_card<3):
                        k=str(self.RAND_3[i]+1)+'.jpg'
                        #print('номер карточки ',k)
                        #print(i)
                        #print(k)
                        if self.coin_3[i]==0:
                            self.coin_3[i]=1
                        #print(self.coin_3)
                        #print("нажал",self.schet_card)
                        self.imgPytns_3.sprite_list[i].draw()
                        for c in range(0, len(self.coin_3)-1):
                            for s in range(1, len(self.coin_3)):
                                if (self.coin_3[c]==1) and (self.coin_3[s]==1) and (self.RAND_3[c]==self.RAND_3[s]) and (c!=s):
                                    self.imgPytns_3.sprite_list[i].draw()
                                    #print(c, self.coin_3[c], s, self.coin_3[s], self.RAND_3[c], self.RAND_3[s])
                                    arcade.pause(0.1)
                                    self.coin_3[c]=-1
                                    self.coin_3[s]=-1
                                    self.schet_card=1
                                    #print(self.coin)
                                elif (self.coin_3[c]==1) and (self.coin_3[s]==1) and (self.RAND_3[c]!=self.RAND_3[s]) and (c!=s):
                                    self.coin_3[c]=0
                                    self.coin_3[s]=0
                                    self.coin_3[i]=0
                                    self.schet_card=1
                                #print(self.coin_3)
                        self.schet_card=1
                    elif self.schet_card>2:
                        self.schet_card=1
                        for f in range(0, len(self.coin_3)):
                            if self.coin_3[f] != -1:
                                self.coin_3[f]=0
                    

                            
                    #print(self.imgPytns.sprite_list[i])
        # Стрелка
        self.Strelka1.center_x =self.Strelka1.width // 3
        self.Strelka1.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka1.draw()
        
        # Назад
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15
        self.MenuItemSelected_2 = -1

        for i in range(0,self.MenuLasti):
            text = "Назад"
            text_size = 35
            x = self.Strelka1.width//9
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 10
                self.coin_2=[0,0,0,0,0,0]
                self.schet_card=1
                
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)
        

        # Стрелка
        self.Strelka.center_x = self.SCREEN_WIDTH // 1.3 + 35
        self.Strelka.center_y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2 
        self.Strelka.draw()

        
            # Дальше
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15

        for i in range(0,self.MenuLasti):
            text = self.Menu[self.MenuFirst2+i]
            text_size = 35
            x = self.SCREEN_WIDTH // 1.3
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = 2
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)

        # Рисуем крестик
        self.aboutLogo1.center_x = self.SCREEN_WIDTH - 0.5*self.aboutLogo1.width
        self.aboutLogo1.center_y = self.SCREEN_HEIGHT -(0.5*self.aboutLogo1.height)
        self.aboutLogo1.draw()
        # Определяем попадание курсора на крестик
        bottom =self.mouseY > self.aboutLogo1.center_y - self.aboutLogo1.height // 2
        top = self.mouseY < self.aboutLogo1.center_y + self.aboutLogo1.height // 2

        left = self.mouseX > self.aboutLogo1.center_x - self.aboutLogo1.width // 2
        right = self.mouseX < self.aboutLogo1.center_x + self.aboutLogo1.width // 2

        if (bottom and top) and (left and right):
            arcade.draw_rectangle_outline(self.aboutLogo1.center_x,self.aboutLogo1.center_y,self.aboutLogo1.width,self.aboutLogo1.height,color=arcade.color.FELDSPAR)
            if self.isMouseDown:
                self.MenuItemSelected = 98



    def CountingAnswers(self):
        """Обработка верных/неверных отетов"""
        if self.otvet==self.vernotvet:
            self.userGoodAnswers += 1
            #print("верные ответы:", self.userGoodAnswers)
            #print("неверные ответы:", self.userBadAnswers)
            f = open('vern.txt', 'r')
            Alf=f.readlines()
            for i in range(0,8):
                if self.userAvatar == i:
                    Alf[i]=str(int(Alf[i])+1)+'\n'
            f.close()
            #print(Alf)
            f = open('vern.txt', 'w')
            f.writelines("%s" % j for j in Alf)
            f.close()
            self.state=self.sl
            self.otvet=-1
            '''self.aboutLogo1.center_x = self.SCREEN_WIDTH 
            self.aboutLogo1.center_y = self.SCREEN_HEIGHT 
            self.aboutLogo1.draw()'''
        else:
            self.userBadAnswers += 1
            #print("верные ответы:", self.userGoodAnswers)
            #print("неверные ответы:", self.userBadAnswers)
            f = open('nevern.txt', 'r')
            Alf=f.readlines()
            for i in range(0,8):
                if self.userAvatar == i:
                    Alf[i]=str(int(Alf[i])+1)+'\n'
            f.close()
            f = open('nevern.txt', 'w')
            f.writelines("%s" % j for j in Alf)
            f.close()
            self.state=self.sl
            self.otvet=-1



    def on_key_press(self, key, modifiers):
        """ Обработка нажатий на кнопки """
        if key == arcade.key.F:
            # Переключение между полноэкранным режимом и обычным
            self.set_fullscreen(not self.fullscreen)
            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)

        if key == arcade.key.S:
            # Еще один способ переключеие между полноэкранным режимом и обычным. Разница будет заметна, если разрешение экрана будет меньше чем текущее
            self.set_fullscreen(not self.fullscreen)
            self.set_viewport(0, self.SCREEN_WIDTH, 0, self.SCREEN_HEIGHT)

        # Обрабатываем клавишу ESCAPE
        if key == arcade.key.ESCAPE:
            if self.state == 0:
                self.close()
                quit()
            elif self.state > 0 and self.state < 4:
                self.state=self.state-1
            elif (self.state > 1 and self.state < 6) or (self.state==50) or (self.state == 51):
                self.state=2
            elif self.state == 6:
                self.state=3
            elif self.state == 8:
                self.state=4
            elif self.state == 10:
                self.state=5
            elif self.state > 6 and self.state < 12:
                self.state=self.state-1
            #elif self.state == 9:
            #    self.state=6

    def on_mouse_motion(self, x, y, dx, dy):
        """ Перемещение мышки """
        # Запоминаем текущие координаты мыши и ее смещение
        self.mouseX = x
        self.mouseY = y
        self.mouseDX = dx
        self.mouseDY = dy



    def on_mouse_press(self, x, y, button, modifiers):
        """ Когда кнопка мыши нажата """
        #print(f"You clicked button number: {button}")
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.bgGUIColor  = arcade.color.GREEN
            self.isMouseDown = True
            #self.count()

    def on_mouse_release(self, x, y, button, modifiers):
        """ Когда кнопка мыши отпущена """
        if button == arcade.MOUSE_BUTTON_LEFT:
            if (self.text=="Пятнашки") or (self.text=="Пятнашки 2") or (self.text=="Пятнашки 3"):
                self.schet_card=self.schet_card+1
                #print('всего нажато ', self.schet_card)
            self.tri_two=0
            self.tri_one=0
            #if self.otvet == 
            if self.MenuItemSelected == 98:
                self.state = self.MenuItemSelected
                quit()
            if self.MenuItemSelected == 50:
                self.state = self.MenuItemSelected

            if self.MenuItemSelected == 51:
                self.state = self.MenuItemSelected

            if self.MenuItemSelected>-1 and self.MenuItemSelected <=21:
                #print("Перключаемся в состояние %s"%(self.MenuItemSelected))
                self.state = self.MenuItemSelected

            if self.MenuItemSelected == 97:
                self.state = self.MenuItemSelected

            self.isMouseDown = False

            '''if self.schet_card == 1:
                 self.clic = 1'''
            #self.count()

        
def main():
    """ Main method """
    app = TApp(False)
    app.setup()
    arcade.run()

if __name__ == "__main__":
    main()
