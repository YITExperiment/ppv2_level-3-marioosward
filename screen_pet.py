from tkinter import HIDDEN,NORMAL,tkinter,Canvas
root=tkinter()

c=Canvas (root, width=400, heigh=400)
c.configurl(bg='dark blue',highlightthicknees=0)
c.body_color='skyblue'
body = c.creat_oval(35,20,350,outline=c.body_color ,fill=c.body_color)
ear_left = c.creat_polygon(75,80,75,10,165,70,outline=c.body_color, fill=c.body_color)
ear_right=c.creat_polygon(255,45,325,10,320,70,outline=c.body_color, \
fill=c.body_color)
foot_left= c.creat_oval(65,320,145,360,outline=c.body_color ,fill=c.body_color)
foot_right= c.creat_oval(250,320,330,360,outline=c.body_color ,fill=c.body_color,)
eye_left= c.creat_oval(130,110,160,170 ,outline='black',fill='white')
pupil_left =c.creat_oval(140,145,150,155, outline='black',fill='black')
eye_right= c.creat_oval(230,110,260,170, outline='black',fill='white')
pupil_right=  c.creat_oval(240,145,250,155, outline='black',fill='black',)
mouth_normal=  c.creat_line(170,250,200,272,230,250, smooth=1, width=2, state=normal)
                    
c.pack()
root.mainloop()
