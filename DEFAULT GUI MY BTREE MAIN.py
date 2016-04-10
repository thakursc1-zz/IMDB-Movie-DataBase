################ THIS IT THE GRAPHIC USER INTERFACE FILE ##################
import Btree              #<------------ That is the main btree file###
from Tkinter import *     #<------ That is header for GUI
import tkSimpleDialog     #<------ That is header for GUI
import tkMessageBox       #<------ That is header for GUI
import imdb               #<------ This is for imdb file


""" The GUI Interface is simple and starts by building a tree using Data BAse called Nodes.txt."""
def addmovie():           #<------- Fuction which adds movie to the data base
    class MyDialog(tkSimpleDialog.Dialog):
        def body(self, master):
            Label(master, text="Movie Name:").grid(row=0)
            Label(master, text="Imdb id:").grid(row=1)
            Label(master, text="Year:").grid(row=2)
            Label(master, text="Rating:").grid(row=3)

            self.e1 = Entry(master)
            self.e2 = Entry(master)
            self.e3 = Entry(master)
            self.e4 = Entry(master)

            self.e1.grid(row=0, column=1)
            self.e2.grid(row=1, column=1)
            self.e3.grid(row=2, column=1)
            self.e4.grid(row=3, column=1)
            return self.e1 # initial focus

        def apply(self):
            val = self.e1.get()
            id = self.e2.get()
            year = self.e3.get()
            rating = self.e4.get()
            Btree.My_Movie_BTree.put(id,val,year,rating)
            if Btree.My_Movie_BTree[val]:
                tkMessageBox.showinfo("Status","Movie added Succesfully")
            else:
                tkMessageBox.showinfo("Status","TRY AGAIN")
            return
    new = MyDialog(app)
    

    


def deletemovie():                         #<-------- Deletes Movie
    
    pass
def advsearch():                           #<----------- Searches for any movie on Imdb
       class MyDialog1(tkSimpleDialog.Dialog):
           def body(self, master):
               Label(master, text="Movie Name:").grid(row=0)
               self.e1 = Entry(master)
               self.e1.grid(row=0, column=1)
               return self.e1 # initial focus
           def apply(self):
               val = self.e1.get()
               ia = imdb.IMDb(accessSystem="http")
               try:
                   movies = ia.search_movie(val)
                   movieobj = movies[0]
                   ia.update(movieobj)
                   print movieobj['long imdb canonical title']
                   try:
                       print "Rating: ",movieobj['rating']
                   except(KeyError):
                       print "Unavailable"
                   try:
                       print "Runtime: ",movieobj['runtime']
                   except(KeyError):
                       print "Unavailable"
                   try:
                       director = movieobj['director']
                       print "List Of Directors"
                       for i in director:
                           print i['name']
                   except(KeyError):
                       print "Unavailable"
                   try:
                       cast= movieobj['cast']
                       print "************Cast*************"
                       for i in cast:
                           print i['name']
                       return 
                   except(KeyError):
                       print "Unavailable"
                   '''try:
                       image = movieobj['cover url']
                       print "URL",image
                       return 
                       fd = urllib.urlopen(image)
                       im = Image.open(StringIO(fd.read()))
                       im.show()
                   except(KeyError):
                       print "Unavailable" '''
               except:
                   print "No Internet Connection Or Movie Does not exist"
                   tkMessageBox.showinfo("Status","Displayed")
               return
       newadv = MyDialog1(app)
            
    
def premovie():     #<------ Displays movie in preorder
    Btree.My_Movie_BTree.pre_tree()
def postmovie():    #<------ Displays movie in preorder
    Btree.My_Movie_BTree.post_tree()
def inmovie():      #<------ Displays movie in preorder
    Btree.My_Movie_BTree.in_tree()

    
def getmovie():     #<------ Displays movie 
    k=movietobesearched.get()
    mov=Btree.My_Movie_BTree[k.lower()]
    if mov:
        tkMessageBox.showinfo("Query","Title: "+mov.title+"\n"+"Imdb id: "+str(mov.id)+"\n"+"Year: "+str(mov.year)+"\n"+"Rating: "+str(mov.rating))
    else:
        tkMessageBox.showinfo("Query","Sorry Not in database.\n TRY ADVANCED SEARCH")


#################### CODE FOR GUI #############################
app = Tk()
app.title("My Movie Btree")
app.geometry("600x400")

labelt = StringVar()
labelt.set("Click on the option below to perform various functions")
label1 = Label(app,textvariable=labelt,font=("Helvetica", 16)).pack()

Addmovie = Button(app,text="Add movie",width = 20,padx=10,pady=10,command=addmovie).pack()
Deletemovie = Button(app,text="Deletemovie",width = 20,padx=10,pady=10,command=deletemovie).pack()
PreOrder = Button(app,text="Preorder",width = 20,padx=10,pady=10,command=premovie).pack()
InOrder = Button(app,text="Inorder",width = 20,padx=10,pady=10,command=inmovie).pack()
PostOrder = Button(app,text="PostOrder",width = 20,padx=10,pady=10,command=postmovie).pack()

moviename=StringVar(None)
movietobesearched = Entry(app,textvariable=moviename,bd=5,width=25)
movietobesearched.pack(ipady=10)

search = Button(app,text="Search",width = 20,padx=10,pady=10,command=getmovie).pack()
advsearch=Button(app,text="Advance Search",width = 30,padx=10,pady=10,command=advsearch).pack()
app.mainloop()
################################## CODE ENDS ###################
