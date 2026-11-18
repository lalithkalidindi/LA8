#-------------------------------------------------------------------------------
# Name: FirstName LastName
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References:
#-------------------------------------------------------------------------------
# Comments to grader:
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------

from tkinter import *
# making a my_frame class
class MyFrame(Frame):
    # making a init function 
    def __init__(self, root):
        Frame.__init__(self, root)
        # making the items 
        self.items = [['egg', 'dairy', 1.99, '12/12/2023'],
                      ['milk', 'dairy', 2.99, '1/2/2024'],
                      ['salmon', 'seafood', 4.99, '12/10/2024']]  # 2d List, each small list contains item info

        # your code here
        # Initialize StringVar and set current subtotal to be 0.0
        # call welcome method to start the code

        # making data of self which is a string variable
        self.data = StringVar()

        # making a self data of set
        self.data.set("0.0")
        # making self of welcom,e
        self.welcome()

    def init_container(self):
        self.quantity_entries = []  # making it an empty list 
        self.states = []  # making a states an empty list 

    def clear_frame(self):  # making a function of clear frames 
        for widget in self.winfo_children():  # making a for loop of winfo_childrean
            widget.destroy()

    def welcome(self):# making a function of welcome 
        self.clear_frame()# making a clear_frame of self

        # your code here
        # start ordering button: command = self.start
        # layout button

        start_button = Button(self, text="Start Ordering",
                              command=self.start)# making the start button with the statment 
        start_button.pack()

    def start(self):# making a start function 
        self.clear_frame()# making a self of clear frame 
        self.init_container()#making a self of init_container

        for row, item in enumerate(self.items):# making a for loop of row
            self.states.append(IntVar())# making self of states 

            c = Checkbutton(self, text=item[0],
                            variable=self.states[row])
            c.grid(row=row, column=0)

            # your code here
            # create and layout a price_label where text set to price of an item
            # create and layout an qunatity_entry - user enter quantity
            # append to quantity_entries list - see init_container method
            # create and layout expiration_label, set text to exipration date of an item

            # printing the labels of the text
            price_label = Label(self, text="$" + str(item[2]))
            price_label.grid(row=row, column=1)  # row and column of proce label

            quantity_entry = Entry(self)# making a quantity_entry
            quantity_entry.grid(row=row, column=2)# making a grid 
            self.quantity_entries.append(quantity_entry)# making a append function at the end of the list 

            expiration_label = Label(self, text=item[3])# making a experation label
            expiration_label.grid(row=row, column=3)# with column = 3 

        # your code here
        # create and layout subtotal_label and set textvariable to StringVar created in __init__
        # create and layout add_to_cart_button and set command = add_to_cart method

        subtotal_label = Label(self, textvariable=self.data) # making a label called subtotal_label
        subtotal_label.grid(row=len(self.items), column=0)# making the grid of the label 

        add_to_cart_button = Button(self,
                                    text="Add To Cart",
                                    command=self.add_to_cart)# making a button with a text 
        add_to_cart_button.grid(row=len(self.items) + 1, column=0)# the grid part of it 

    def add_to_cart(self): # making a function of add to cart 

        current_subtotal = 0  # initialize current subtotal

        for i in range(len(self.items)):# making a for loop 

            # your code here

            # making item name
            item_name = self.items[i][0]

            # obtain item name from self.items using index notation

            if (self.states[i].get() == 1):  # check if item selected using get()

                product_quantity = int(self.quantity_entries[i].get())  # get the quantity user selected

                # your code here

                # obtain item price from self.items using index notation
                # calculate current subtotal multiplying item price with quantity

                # making the item_price of self items
                item_price = self.items[i][2]

                # making a current subtotal which comes based off the product quantity
                current_subtotal += item_price * product_quantity

        # your code here
        # set the self.data to current_subtotal

        self.data.set(str(current_subtotal))


# Create root window
root = Tk()
root.title("Grocery Cart")

# Object of MyFrame class
app = MyFrame(root)

# Layout and call mainloop()
app.pack()

root.mainloop()

# create root window
# object of MyFrame class
# layout and call mainloop()
# main driver code