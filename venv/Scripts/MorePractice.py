import tkinter as tk
from tkinter import ttk
from tkinter import *
from collections import defaultdict
import time
from threading import Thread
import threading

if __name__ == '__main__':
    window = tk.Tk()
    tabcontrol = ttk.Notebook(window)
    tab1 = ttk.Frame(tabcontrol)
    tabcontrol.pack(expand = 1, fill = "both")
    LinkedListFrame = ttk.Frame(tabcontrol)
#    tabcontrol.add(tab1, text='Binary Trees')
    tabcontrol.add(LinkedListFrame, text='LinkedLists')
    window.title("Data Structures Visualizations")
    window['background'] = 'yellow'
    window.geometry('1350x720')
#    c = tk.Canvas(tab1, width=600, height=400, bg = 'white')
#    c.pack()


StartXConst = 300
StartYConst = 20
StartX = 300
StartY = 20
Radius = 15

VarChange = 50
VarChangeLeft = 70
VarChangeY = -10
VarChangeX = 110

def create_square(x, y, r): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return c2.create_rectangle(x0, y0, x1, y1, fill = 'white')
def create_square2(x, y, r): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return c2.create_rectangle(x0, y0, x1, y1, fill = 'yellow')


class LL_Node(object):

    def __init__ (self, data= None, next = None):
        self.data = data
        self.next = next

class LinkedList():
    VarChange = 40
    def __init__(self,head = None):
        self.head = head

    def getHead(self):
        if head == None:
            return None
    def insert_at_head(self, data):
        new_node = LL_Node(data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        if (self.head == None):
            print("List is empty")
        else:
            while (temp):
                print(temp.data, " -> ", end='')
                temp = temp.next
            print("")
    def DesignLL(self,x,y):
        #create_square(x, y, 25)
        create_square(x, y, 25)
        #print(str(LLNodeSquareObj) + "added to canvas")
    def GetNumNode(self):
        temp = self.head
        count = 0
        while(temp):
            count = count - 1
            temp = temp.next
        return count
    def printList2(self, LL_Traversal_Sent, text):
        temp = self.head
        count = 0
        OutputText = Text(LinkedListFrame, width=50, height=5)
        OutputText.insert(END, "Output:")
        OutputText.pack()
        LL_TraversalCode(LL_Traversal_Sent, text, 0)
        Unhighlight(LL_Traversal_Sent, text, 0)
        LL_TraversalCode(LL_Traversal_Sent, text, 1)
        Unhighlight(LL_Traversal_Sent, text, 1)
        if (temp == None):
            LL_TraversalCode(LL_Traversal_Sent, text, 2)
            Unhighlight(LL_Traversal_Sent, text, 2)
            OutputText.insert(END, "List is empty")
            OutputText.update()
            time.sleep(1.0)
            window.update()
            OutputText.destroy()
            text.destroy()
        else:

            VariablesText = Text(LinkedListFrame, width=50, height = 5)
            VariablesText.insert(END, "Variables:")
            VariablesText.pack()

            Square_TBD = c2.create_rectangle(LinkLabel_Coord[count] - 25, 35 - 25, LinkLabel_Coord[count] + 25, 60,
                                            fill='Yellow')


            VariablesText.insert(END, "\nHead = " + str(temp.data))
            VariablesText.insert(END, "\nTemp = " + str(temp.data))


            LL_TraversalCode(LL_Traversal_Sent, text, 3)
            Unhighlight(LL_Traversal_Sent, text, 3)

            Highlight_Obj = []
            prev_data = temp.data
            while (temp):

                LL_TraversalCode(LL_Traversal_Sent, text, 4)
                Unhighlight(LL_Traversal_Sent, text, 4)
                print(temp.data, " -> ", end='')
                dat= temp.data + "->" + " "

                prevText= "Temp = "
                VariableTextCalculation(VariablesText, prev_data,temp.data,3,prevText)
                OutputText.insert(END,dat)
                OutputText.update()
                LL_TraversalCode(LL_Traversal_Sent, text, 5)
                Unhighlight(LL_Traversal_Sent, text, 5)
                prev_data = temp.data
                temp = temp.next
                c2.delete(Square_TBD)
                count = count + 1
                if (temp):
                    Square_TBD = c2.create_rectangle(LinkLabel_Coord[count] - 25, 35 - 25, LinkLabel_Coord[count] + 25, 60,
                                                 fill='Yellow')
                LL_TraversalCode(LL_Traversal_Sent,text, 6)
                Unhighlight(LL_Traversal_Sent, text, 6)

            #window.after(1000)
            print("")
            OutputText.destroy()
            VariablesText.destroy()
            text.destroy()
    def Remove_LLNode(self,LL_Removal, text,key):
        count = 0
        Square_TBD1 = c2.create_rectangle(LinkLabel_Coord[count] - 25, 35 - 25, LinkLabel_Coord[count] + 25, 60,
                                         fill='Yellow')
        Square_TBD2 = c2.create_rectangle(-1000, 35 - 25, -1000, 60,
                                         fill='Red')
        LL_TraversalCode(LL_Removal, text, 0)
        Unhighlight(LL_Removal, text, 0)
        temp = self.head
        prev = None
        LL_TraversalCode(LL_Removal, text, 1)
        Unhighlight(LL_Removal, text, 1)
        LL_TraversalCode(LL_Removal, text, 2)
        Unhighlight(LL_Removal, text, 2)
        # If head node itself holds the key to be deleted
        if (temp is not None):
            LL_TraversalCode(LL_Removal, text, 3)
            VariablesText = Text(LinkedListFrame, width=50, height=5)
            VariablesText.insert(END, "Variables:")

            VariablesText.insert(END, "\nHead = " + temp.data)

            VariablesText.insert(END, "\nTemp = " + temp.data)
            VariablesText.insert(END, "\nPrev = ")
            VariablesText.pack()
            PrevStr = "Prev = "
            TempStr = "Temp = "
            Unhighlight(LL_Removal, text, 3)
            if (temp.data == key):
                self.head = temp.next
                LL_TraversalCode(LL_Removal, text, 4)
                Unhighlight(LL_Removal, text, 4)
                temp = None
                LL_TraversalCode(LL_Removal, text, 5)
                Unhighlight(LL_Removal, text, 5)
                LL_TraversalCode(LL_Removal, text, 6)
                Unhighlight(LL_Removal, text, 6)
                return

        LL_TraversalCode(LL_Removal, text, 7)
        Unhighlight(LL_Removal, text, 7)
        while (temp is not None):

            LL_TraversalCode(LL_Removal, text, 8)
            Unhighlight(LL_Removal, text, 8)
            if temp.data == key:
                break
            if prev == None:
                The_Prev = "NULL"
            else:
                The_Prev = prev.data
            prev = temp

            VariableTextCalculation(VariablesText, The_Prev, prev.data,4,PrevStr)
            count = count + 1
            c2.delete(Square_TBD2)
            if count!=0:
                Square_TBD2 = c2.create_rectangle(LinkLabel_Coord[count-1] - 25, 35 - 25, LinkLabel_Coord[count-1] + 25, 60,
                                                 fill='Red')

            LL_TraversalCode(LL_Removal, text, 9)
            Unhighlight(LL_Removal, text, 9)

            c2.delete(Square_TBD1)
            temp = temp.next
            VariableTextCalculation(VariablesText, prev.data, temp.data,3, TempStr)
            Square_TBD1 = c2.create_rectangle(LinkLabel_Coord[count] - 25, 35 - 25, LinkLabel_Coord[count] + 25, 60,
                                             fill='Yellow')

            LL_TraversalCode(LL_Removal, text, 10)
            Unhighlight(LL_Removal, text, 10)


        if (temp == None):
            LL_TraversalCode(LL_Removal, text, 11)
            Unhighlight(LL_Removal, text, 11)
            return
            c2.delete(Square_TBD1)
            c2.delete(Square_TBD2)
            text.destroy()
            VariablesText.destroy()

        # Unlink the node from linked list
        LL_TraversalCode(LL_Removal, text, 12)
        Unhighlight(LL_Removal, text, 12)
        print("Found and deleted")
        prev.next = temp.next
        c2.delete(Square_TBD1)
        c2.delete(Square_TBD2)
        text.destroy()
        VariablesText.destroy()
        #c2.delete(LLNodeSquareObj[count])
        #LLNodeSquareObj.pop(count)
        print(LabelListObj)
        LabelListObj[count].destroy()
        LabelListObj.pop(count)
        LL_Data.pop(count)
        temp = None
        #print(str(LLNodeSquareObj) + "after deletion")
        print(str(LL_Data) + "LL_Data after the deletion")
        print(str(LabelListObj) + "LabelList Obj after the deletion")
        UpdateLinkedList()
        self.printList()
        #initialize_LL()
    def reverse(self, LL_Reverse_Code,text):

        LL_TraversalCode(LL_Reverse_Code, text,0)
        Unhighlight(LL_Reverse_Code, text, 0)
        prev = None
        LL_TraversalCode(LL_Reverse_Code, text, 2)
        Unhighlight(LL_Reverse_Code, text, 2)
        current = self.head
        LL_TraversalCode(LL_Reverse_Code, text, 1)
        Unhighlight(LL_Reverse_Code, text, 1)
        count = 0
        Square_TBD1 = c2.create_rectangle(LinkLabel_Coord[count] - 25, 35 - 25, LinkLabel_Coord[count] + 25, 60,
                                          fill='Yellow')
        Square_TBD2 = c2.create_rectangle(-1000, 35 - 25, -1000, 60,
                                          fill='Red')
        Square_TBD3 = c2.create_rectangle(-1000, 35 - 25, -1000, 60,
                                          fill='Red')

        while (current is not None):
            #Blue = Next
            #Red = prev
            #Yellow = curr
            LL_TraversalCode(LL_Reverse_Code, text,3 )
            Unhighlight(LL_Reverse_Code, text, 3)
            c2.delete(Square_TBD3)
            next = current.next
            Square_TBD3 = c2.create_rectangle(LinkLabel_Coord[count+1]-25, 35 - 25, LinkLabel_Coord[count+1]+25, 60,
                                              fill='Blue')
            LL_TraversalCode(LL_Reverse_Code, text, 4)
            Unhighlight(LL_Reverse_Code, text, 4)

            current.next = prev

            LL_TraversalCode(LL_Reverse_Code, text, 5)
            Unhighlight(LL_Reverse_Code, text, 5)
            c2.delete(Square_TBD2)
            prev = current
          #  if count !=0:
          #      Square_TBD2 = c2.create_rectangle(LinkLabel_Coord[count - 1] - 25, 35 - 25, LinkLabel_Coord[count - 1] + 25,60,
          #                                        fill='Red')
          #  else:
            Square_TBD2 = c2.create_rectangle(LinkLabel_Coord[count] - 25, 35 - 25,LinkLabel_Coord[count] + 25, 60,
                                                  fill='Red')
            LL_TraversalCode(LL_Reverse_Code, text, 6)
            Unhighlight(LL_Reverse_Code, text, 6)
            c2.delete(Square_TBD1)
            current = next
            Square_TBD1 = c2.create_rectangle(LinkLabel_Coord[count+1] - 25, 35 - 25, LinkLabel_Coord[count+1] + 25, 60,
                                              fill='Yellow')
            LL_TraversalCode(LL_Reverse_Code, text, 7)
            Unhighlight(LL_Reverse_Code, text, 7)
            count = count +1
        self.head = prev
        LL_TraversalCode(LL_Reverse_Code, text, 8)
        Unhighlight(LL_Reverse_Code, text, 8)
        c2.delete(Square_TBD1)
        c2.delete(Square_TBD2)
        c2.delete(Square_TBD3)
        self.printList()
        ReverseGraphic()
    def ClearList(self):
        temp = self.head

        while temp:
            prev = temp.next

            del temp.data

            temp = prev
        self.head = None
        print("The list after deleting the list is: ")
        self.printList()
#Global Variables
Obj_Initalized = False
LLChange = 100
LLlabelChange = 100
LL_Data = []
LabelListObj = []
LLNodeSquareObj = []
LinkLabel_Coord = [110, 210,310,410,510,610,710,810]

def Clear_Graphic():
    c2.delete("all")

    for i in range(len(LabelListObj)):
        LabelListObj[i].destroy()
    LabelListObj.clear()
    llist.ClearList()
    LL_Data.clear()
def ReverseGraphic():
    # NumNode=llist.GetNumNode()
    c2.delete("all")
    global Obj_Initalized
    global LLChange
    global LLlabelChange
    global LL_Data
    LLXConst = 10
    LLYConst = 10
    # LinkLabel_Coord = [110, 210,310,410,510,610,710,810]
    # iterator = 0
    for i in range(len(LabelListObj)):
         LabelListObj[i].destroy()
    LabelListObj.clear()
    print("LL_Data is: " + str(LL_Data))
    for i in range(len(LL_Data) - 1, -1, -1):
        print("After Reverse the LL Data for "  + str(i) + " is " + str(LL_Data[i]))
    for i in range(len(LL_Data)):
        llist.DesignLL(LinkLabel_Coord[len(LL_Data)-1-i], 35)
        c2.create_line(LinkLabel_Coord[i], 35, LinkLabel_Coord[i] + 100, 35, arrow=tk.LAST)
        llInfo = tk.Label(c2, text=str(LL_Data[i]), bg="white")
        llInfo.place(x=LinkLabel_Coord[len(LL_Data)-1-i] - 12, y=35)
        LabelListObj.insert(0, llInfo)
def VariableTextCalculation(VariablesText,prev_data,temp_data,line,variable):
    Leng = round((len(prev_data) / 10), 3)
    print("Leng is " + str(Leng))
    Decim_calc = Leng + .7
    print("Decim_calc is: " + str(Decim_calc))
    if Decim_calc >= 1.0:
        Decim_calc = str(Decim_calc / 10) + str(int(Decim_calc))
    print("Decim_calc is now: " + str(Decim_calc))
    EndRange = round(float(str(line) + str(Decim_calc)[1:]), 3)
    print("End Range is: " + str(EndRange))
    VariablesText.replace(float(line), str(EndRange), variable + temp_data)
def UpdateLinkedList():

    c2.delete("all")

    global Obj_Initalized
    global LLChange
    global LLlabelChange
    global LL_Data
    LLXConst = 10
    LLYConst = 10

    iterator = 0
    for i in range(len(LabelListObj)):
        LabelListObj[i].destroy()
    LabelListObj.clear()

    print("LL_Data is: " + str(LL_Data))
    for i in range(len(LL_Data)):
        llist.DesignLL(LinkLabel_Coord[i], 35)
        c2.create_line(LinkLabel_Coord[i], 35, LinkLabel_Coord[i] + 100, 35, arrow=tk.LAST)
        llInfo = tk.Label(c2, text=str(LL_Data[i]), bg="white")
        llInfo.place(x=LinkLabel_Coord[i] - 12, y=35)
        LabelListObj.insert(0, llInfo)

    LLChange = LLChange + 100
def SleepUpdate():
    time.sleep(0.5)
    LinkedListFrame.update()
def Highlight_LLNode(index):
    create_square2(LinkLabel_Coord[index],35,25)
def initialize_LL():
    global Obj_Initalized
    global LLChange
    global LLlabelChange
    global LL_Data
    LLXConst = 10
    LLYConst = 10

    iterator = 0
    for i in range(len(LabelListObj)):
        LabelListObj[i].destroy()
    LabelListObj.clear()
    llist.insert_at_head(LinkedListInput.get())
    llist.printList()
    LL_Data.insert(0, LinkedListInput.get())

    print ("LL_Data is: " + str(LL_Data))
    for i in range(len(LL_Data)):
        llist.DesignLL(LinkLabel_Coord[i], 35)
        c2.create_line(LinkLabel_Coord[i], 35, LinkLabel_Coord[i] + 100, 35, arrow=tk.LAST)
        llInfo = tk.Label(c2, text=str(LL_Data[i]), bg="white")
        llInfo.place(x=LinkLabel_Coord[i]-12, y=35)
        LabelListObj.insert(0,llInfo)

    LLChange = LLChange + 100
def Initialize_ReverseWT():
    text = Text(LinkedListFrame, width = 50, height = 20)
    LL_Reverse_Code ="void reverse() {\nNode * current = head;\nNode * prev = NULL, *next = NULL;\nwhile (current != NULL) {\nnext = current->next;\ncurrent->next = prev;\nprev = current;\ncurrent = next;}\nhead = prev;}"
    text.insert(INSERT,LL_Reverse_Code)
    text.configure(state = 'disabled')
    text.pack()
    map_ret = DetermineSentenceRange(LL_Reverse_Code)

    llist.reverse(LL_Reverse_Code,text)
def Initialize_DeletionWT(key):
    text = Text(LinkedListFrame, width = 50, height = 20)
    LL_Deletion_Code = "void deleteNode(Node head, int key){\n Node * temp = head;\nNode * prev = NULL;\nif (temp != NULL & & temp->data == key){\nhead = temp->next;\n delete temp; \n return;} \n else{\n    while (temp != NULL & & temp->data != key){\n prev = temp;\n temp = temp->next;} \n if (temp==NULL) return; } \n prev->next = temp->next;}}\n"
    text.insert(INSERT,LL_Deletion_Code)
    text.configure(state='disabled')
    text.pack()
    map_ret = DetermineSentenceRange(LL_Deletion_Code)

    llist.Remove_LLNode(LL_Deletion_Code, text,str(key))
def Destroy(win):
    win.destroy()

def popupwin():
   #Create a Toplevel window
   top= Toplevel(window)
   top.geometry("750x250")

   DeleteThisNode = ttk.Label(top, text = "Please enter the value of the node you would like deleted")
   DeleteThisNode.pack()
   entry= Entry(top, width= 25)
   entry.pack()
   button= Button(top, text="Ok", command=lambda: [Valid_Entry(entry,top)])
   button.pack(pady=5, side= TOP)

def Valid_Entry(entry,win):
    if entry == None:
        top1 = Toplevel(window)
        top1.geometry("750x250")
        ErrorMessage = ttk.Label(top1, text="You must type in something to the input")
        ErrorMessage.pack()
    try:
        val = int(entry.get())
        win.destroy()
        Initialize_DeletionWT(val)

    except ValueError:
        top1 = Toplevel(window)
        top1.geometry("750x250")
        ErrorMessage = ttk.Label(top1, text="Input must be an integer")
        ErrorMessage.pack()

def TraversalWalkThrough():
    text = Text(LinkedListFrame, width = 50, height = 10)
    # insert given string in text area
    LL_Traversal_Sent = " struct node *temp;\nif(head == NULL){\nprintf(List is empty.); return;}\ntemp = head;\nwhile(temp != NULL){\ncout << temp->data << " " \ntemp = temp->next;}\n"
    text.insert(INSERT, LL_Traversal_Sent)
    text.configure(state='disabled')
    text.pack()
    map_ret = DetermineSentenceRange(LL_Traversal_Sent)
    #LL_TraversalCode(LL_Traversal_Sent, text,0)
    llist.printList2(LL_Traversal_Sent,text)
def LL_TraversalCode(s, text,k):
    map_ret = DetermineSentenceRange(s)

    Begin_Range = str(k + 1) + "." + "0"
    End_Range = str(k + 1) + "." + str(map_ret[k])
    text.tag_add("start", Begin_Range, End_Range)
    text.tag_config("start", background="gray",
                    foreground="black")
    window.update()
    time.sleep(0.5)
    text.tag_delete("start")

c2 = tk.Canvas(LinkedListFrame, width=1000, height=100, bg = 'white')
c2.pack()
#Labels & Buttons for Linked List
LinkedListLabel = ttk.Label(LinkedListFrame, text = "Type number into ")
LinkedListLabel.pack()
LinkedListInput = ttk.Entry(LinkedListFrame, width = 15)
LinkedListInput.pack()
llist = LinkedList()
InsertLLNode = ttk.Button(LinkedListFrame, text = "Insert Node in Linked List", command =  initialize_LL)
InsertLLNode.pack()
TraversalBut = ttk.Button(LinkedListFrame, text = "Linked List Traversal Walk Through", command = TraversalWalkThrough)
TraversalBut.pack()
DeletionBut = ttk.Button(LinkedListFrame, text = "Linked List Deletion Walk Through", command = popupwin)
DeletionBut.pack()
ReverseLLBut = ttk.Button(LinkedListFrame, text = "Reverse Linked List Walk Through", command = Initialize_ReverseWT)
ReverseLLBut.pack()
ResetLLBut = ttk.Button(LinkedListFrame, text = "Reset Linked List", command = Clear_Graphic)
ResetLLBut.pack()

llist.printList()

label1 = ttk.Label(tab1, text = "Type number into")
label1.pack()

NumberEntered = ttk.Entry(tab1, width = 15)
NumberEntered.pack()


ObjCreated = False

def DetermineSentenceRange(s):
    sentence_count = 0
    ind = 0
    map1 = defaultdict(int)

    for i in range(len(s)):
        if s[i] == "\n":
            ind = ind+1
        else:
            map1[ind] +=  1
    #for k, v in map1.items():
     #   print(str(k) + " - " + str(v))
    return map1
def InOrderCode(s, text):

    map_ret = DetermineSentenceRange(s)
    for k in map_ret:
     #   print(str(k) + " - " + str(v))
        window.update()
        time.sleep(0.5)
        Begin_Range = str(k + 1) + "." + "0"
        End_Range = str(k + 1) + "." + str(map_ret[k])
        text.tag_add("start", Begin_Range, End_Range)
        text.tag_config("start", background="gray",
                        foreground="black")


def Unhighlight(s,text,k):
        window.update()
        time.sleep(0.5)
        map_ret = DetermineSentenceRange(s)
        INS1 = str(k+1) + "." + "0"
        INS2 = str(k+1) + "." + str(map_ret[k])
        text.tag_add("prev", INS1, INS2)
        text.tag_config("prev", background="white",
                        foreground="black")

window.mainloop()