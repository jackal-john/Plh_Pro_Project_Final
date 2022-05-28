import tkinter as tk
import random
import time
import matplotlib.pyplot as plt
#Βιβλιοθήκη για να εμφανίσω το γράφημα μέσα στο παράθυρο
#του tkinder
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)



#=====================================
#Παίρνει ως είσοδο μια πλειάδα t
#και επιστρέφει την τιμή της συνάρτησης f(t0, t1, t2)
# To x**2 σημαίνει x εις την δευτέρα.
def  standard_function(t):
    return  t[0]**2 + t[1]**3 + t[2]**4 + t[0]*t[1]*t[2]
#--------------------------------------


#=====================================
#Παίρνει ως είσοδο μια πλειάδα t
#και επιστρέφει την τιμή της συνάρτησης f(t0, t1, t2)
def  function1(t):
    return  (t[0] - 5)**2  +  (t[1] - 10)**2  + (t[2]- 15)**2
#--------------------------------------
    

#=====================================
#Παίρνει ως είσοδο μια πλειάδα t
#και επιστρέφει την τιμή της συνάρτησης f(t0, t1, t2)
def  function2(t):
    return  t[0]**2 - t[1]**3 + t[2]**4 - t[0]*t[1]*t[2]
#--------------------------------------


#=======================================
#Δημιουργεί έναν τυχαίο πραγματικό αριθμό στο διάστημα [α,b]
#Χρησιμοποιώ την συνάρτηση random.random() από τη βιβλιοθήκη
#random για να δημιουργήσω μια τυχαία τιμή στο διάστημα [0,1].
#Ακολούθως για την μεταβλητή x μετατρέπω αυτή την τιμή στο διάστημα [a, b] με τον
#παρακάτω τύπο.
def  random_number(a, b):
    return (b-a)*random.random() + a
#---------------------------------------




#==============================
#Παίρνει ένα tupple (t0, t1, t2) και θα αλλάζει
#ένα στοιχειο του στην τύχη
#Επιστρέφει το νέο t (new_t)
# a = [0, 0, 0]
# b = [10, 20, 30]
def   mutation(t, a, b):
    #Φτιάχνω μια νέα λίστα με τα 3 πεδία του tuple
    #Γιατί δεν μπορώ να αλλάξω τα πεδία ενός tuple
    new_t = list(t)
    #Επιλέγω ένα k στην τύχη (μεταξύ του 1 και του 3)
    #αυτό δείχνει πόσες θέσεις θα αλλάξω από το αρχικό
    #tupple
    k = random.randint(1,3)
    #Φτιάχνω μια λίστα από k δείκτες του new_t που
    #θα αλλάξουν (mutation)  -->  αν κ=2  [0, 2]
    indices = random.sample(range(3), k)
    #αλλάζω όλα τα στοιχεία που είναι σε αυτές τις θέσεις
    #στη λίστα
    for i in indices:
        if type(new_t[i]) == int:
            new_t[i] = random.randint(a[i],b[i])
        else:
            new_t[i] = random_number(a[i],b[i])
    #Στο τέλος μετατρέπω τη λίστα σε tuple για να
    #επιστρέψω tuple
    return tuple(new_t)
#-------------------------------



#===================================
#Θα παίρνει τα tupples t και s και θα
#δημιουργεί ένα νέο tupple με στοιχεία από τα
#t, s  (t0, t1, t2)  (s0, s1, s2)
#Επιλέγω κάποια στοιχείο του t  και τα αλλάζω με
#τα αντίστοιχα στοιχεία της s.
def  crossbreed(t, s):
    #Φτιάχνω μια νέα λίστα με τα 3 πεδία του tuple
    #Γιατί δεν μπορώ να αλλάξω τα πεδία ενός tuple
    new_t = list(t)
    #Επιλέγω ένα k στην τύχη (μεταξύ του 1 και του 3)
    #Το κ περιγράφει το πλήθος των στοιχείων του t που
    #θα αλλάξω (1, 2, ή 3).
    k = random.randint(1,3)
    #Φτιάχνω μια λίστα από k δείκτες του new_t που
    #θα αλλάξουν (crossbreed) αν κ=2 -->  [0, 2]
    indices = random.sample(range(3), k)
    #αλλάζω όλα τα στοιχεία που είναι σε αυτές τις θέσεις
    #στη λίστα με στοιχεία από το s
    for i in indices:
        new_t[i] = s[i]
    #Στο τέλος μετατρέπω τη λίστα σε tuple για να
    #επιστρέψω tuple
    return tuple(new_t)
    
#-----------------------------------




#Ο παρακάτω γενετικός αλγόριθμος δουλεύει για όλες 
#τις συναρτήσεις.
#Η συνάρτηση παράγει μια λίστα λύσεων του προβλήματος
#Παράμετροι
#Ν: πλήθος λύσεων
#Κ: πλήθος επιλεγμένων λύσεων για το επόμενο βήμα
#steps: Ο αριθμός βημάτων (γεννεών) του γεννετικού αλγορίθμου.
#input_type : Ο τύπος των δεδομένων που χειρίζεται ο αλγόριθμος
#0:  for integers 
#1:  for reals
#p_m: πιθανότητα μετάλλαξης  (1-p_m) η πιθανότητα διασταύρωσης
#a = [a1, a2, a3]
#b = [b1, b2, b3]
#Το a και το b περιγράφουν τα άκρα των πεδίων των μεταβλητών.
#printflag: Αν εδώ βάλουμε την τιμή True τότε το πρόγραμμα θα τυπώνει σε κάθε επανάληψη την καλύτερη λύση.
#Επιστρέφει:
def genetic_algorithm(N, K, steps, input_type, p_m=0.3, a=[0, 0, 0], b=[10, 20, 30], objective_function=standard_function, printflag=False):
    #Αρχικοποιώ τις λύσεις
    #To παρακάτω loop δημιουργεί μια λίστα (population) από 
    #N tuples.
    population = []
    for n in range(N):
        if (input_type == 1):
            x = random_number(a[0], b[0])
            y = random_number(a[1], b[1])
            z = random_number(a[2], b[2])
        else:
            x = random.randint(a[0], b[0])
            y = random.randint(a[1], b[1])
            z = random.randint(a[2], b[2])
        atom = (x,y,z)
        population.append(atom)

    #Αποτίμηση Λύσεων
    #Φτιάχνω ένα λεξικό που θα έχει ως πεδία, μια λύση και την τιμή της
    #(στην f) Το λεξικό θα περιέχει πεδία της μορφής:
    #{tupple : number}
    #π.χ.
    #{(1.2,  3.4,   5.1) :  25.12,
    # (2.4,  4.12,  3.5) :  24.12}
    
    dictionary = {}
    for atom in population:
        value = objective_function(atom)
        dictionary[atom] = value
    #Ταξινομώ το λεξικό ως προς τα values.
    #Kαι κρατάω τα Κ με τις μεγαλύτερες τιμές.
    dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[:K])

    if printflag == True:
            #Τυπώνω την καλύτερη λύση.
            s = list(dictionary)[0]
            print('Initial ', ' ', s, ' ', standard_function(s) )
    
    #---------------------------------------------
    #Επανάληψη (βρόγχος) του Γεννετικού Αλγορίθμου
    value_over_time = [] #κενή λίστα
    for n in range(steps):
        #Φτιάχνω μια λίστα με τα keys του λεξικού
        #για να τα χρησιμοποιήσω μετά.
        mylist = list(dictionary)
        items = 1 #μετράω τα items που σαρώνω
        for  s  in  mylist:
            x = random.random()
            #Επέλεξε τι από τα δύο θα γίνει
            if x < p_m:
                #Εδώ κάνω mutation. Δηλαδή φτιάχνω με μετάλλαξη μια νέα λύση
                #με βάση τη λύση s.
                new_solution = mutation(s, a, b) 
                #Προσθέτω τη νέα υποψήφια λύση στο λεξικό dictionary.
                value = objective_function(new_solution)
                dictionary[new_solution] = value
            else:
                #Εδώ κάνω crossbread
                #Πρέπει να επιλέξω και μια ακόμη λύση.
                #ΔΙΟΡΘΩΝΩ
                index = random.randrange(K)
                s2 = mylist[index]
                new_solution1 = crossbreed(s, s2)
                new_solution2 = crossbreed(s2, s)
                #Προσθέτω τις νέες υποψήφιες λύσεις στο λεξικό dictionary.
                value1 = objective_function(new_solution1)
                dictionary[new_solution1] = value1
                value2 = objective_function(new_solution2)
                dictionary[new_solution2] = value2
            items = items + 1
        dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[:K])
        #η λίστα value_over_time περιέχει τις μέγιστες τιμές από 
        #τα values του λεξικού σε κάθε επανάληψη του γενετικού αλγορίθμου
        value_over_time.append(  max(dictionary.values())  )
        if printflag == True:
            #Τυπώνω την καλύτερη λύση.
            s = list(dictionary)[0]
            print(n, ' ', s, ' ', standard_function(s) )
    
    #Τέλος Επανάληψης Γεννετικού 
    #----------------------------------------------
    return dictionary, value_over_time
        






#Επιστρέφει True αν το string x είναι ακέραιος
def   is_integer(x):
    try:
        y = int(x)
        return True
    except:
        return False
#--------------------------------------

#Επιστρέφει True αν το string x είναι θετικός ακέραιος
def   is_positive_integer(x):
    try:
        y = int(x)
        if y>0:
            return True
        else:
            return False
    except:
        return False
#--------------------------------------



#Επιστρέφει True αν το string x είναι '0' ή '1'
def   is_binary_digit(x):
    try:
        y = int(x)
        if y==0 or y==1:
            return True
        else:
            return False
    except:
        return False
#--------------------------------------


#Επιστρέφει True αν το string x είναι μεταξύ του 0 και του 1
def   is_prob(x):
    try:
        y = float(x)
        if y>=0 and y<=1:
            return True
        else:
            return False
    except:
        return False
#--------------------------------------
    


#tkinter function
def  run_genetic():
    #Καθαρίζω τα προηγούμενα κείμενα αν υπάρχουν.
    result_outpout.delete(0.0,tk.END)
    solutions_outpout.delete(0.0,tk.END)
    
    #ελέγχω αν οι τιμές είναι σωστές
    N_entered = N_entry.get()
    if is_positive_integer(N_entered):
        N = int(N_entered)
    else:
        msg = 'Λάθος τιμή στο πλήθος αρχικών λύσεων'
        result_outpout.insert(tk.END,msg)
        return
    
    K_entered = K_entry.get()
    if  is_positive_integer(K_entered):
        K = int(K_entered)
    else:
        msg = 'Λάθος τιμή στο πλήθος λύσεων επόμενης γενιάς'
        result_outpout.insert(tk.END,msg)
        return
    
    steps_entered = steps_entry.get()
    if  is_positive_integer(steps_entered):
        steps = int(steps_entered)
    else:
        msg = 'Λάθος τιμή στο πλήθος βημάτων'
        result_outpout.insert(tk.END,msg)
        return
    
    type_entered = type_entry.get()
    if  is_binary_digit(type_entered):
        input_type = int(type_entered)
    else:
        msg = 'Λάθος τιμή στον τύπο λύσεων'
        result_outpout.insert(tk.END,msg)
        return
    
    pm_entered = pm_entry.get()
    if  is_prob(pm_entered):
        p_m = float(pm_entered)
    else:
        msg = 'Λάθος τιμή στην πιθανότητα μετάλλαξης'
        result_outpout.insert(tk.END,msg)
        return
    
    #Διαβάζω τη συνάρτηση που έχει επιλέξει ο χρήστης
    #στο dropdown menu
    selected_function = variable.get()
    if selected_function == 'Standard':
        my_function = standard_function
    elif selected_function == 'Function1':
        my_function = function1
    else: my_function = function2
    
    #Τρέχω τον γενετικό αλγόριθμο
    msg = 'Ο Γεννετικός Αλγόριθμος Ξεκίνησε'
    result_outpout.insert(tk.END,msg)
    start = time.time()
    solutions, values = genetic_algorithm(N, K, steps, input_type, p_m, objective_function=my_function, printflag=False)
    end = time.time()
    result_outpout.delete(0.0,tk.END)
    msg = 'Ο Γεννετικός Αλγόριθμος Ολοκληρώθηκε! Συνολικός χρόνος: ' + '{:.2f}'.format(end-start) + ' sec'
    result_outpout.insert(tk.END,msg)
    
    #Τύπωσε τις 20 πρώτες λύσεις
    n = 0
    msg = ''
    for s in solutions:
         msg += 'x = '+'{:.4f}'.format(s[0]) + '\t\t' + 'y = ' +'{:.4f}'.format(s[1]) + '\t\t' + 'z = ' + '{:.4f}'.format(s[2]) +   '\t\t value='  +  '{:.2f}'.format(solutions[s]) + '\n'
         n = n + 1 
         # if n>19:
         #     break
    solutions_outpout.insert(tk.END, msg)
    
    #clear canvas
    # for item in canvas.get_tk_widget().find_all():
    #    canvas.get_tk_widget().delete(item)
    #Καθαρίζω το γράφημα ώστε να μπει το καινούριο
    #ax.clear()
    #draw figure
    #Σχεδιάζω το καινούριο γράφημα
    ax.plot(values)
    #Εμφανίζεται στην οθόνη ο canvas
    canvas.draw()




#tkinter function
def close_window():
    window.destroy()
    return


def clear_plots():
    ax.clear()
    canvas.draw()
    result_outpout.delete(0.0,tk.END)
    solutions_outpout.delete(0.0,tk.END)
    return










#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Κυρίως πρόγραμμα

#initial values
#N: Πλήθος αρχικών λύσεων (x, y, z) που θα ξεκινήσουν τον αλγόριθμο
N = 500
#Κ: Πλήθος λύσεων που κρατάει κάθε γενιά (κρατώ τις Κ καλύτερες)
K = 100
#steps: Βήματα που θα κάνει ο γεννετικός αλγόριθμος
steps = 100
#input_type:  0 για ακέραιους,  1 για πραγματικούς
input_type = 1
#p_m: Πιθανότητα μετάλαξης
p_m = 0.4
#printflag
printflag = False

window = tk.Tk()
window.title("Genetic Algorithm Project")
#labels
N_label = tk.Label(window, text="Πλήθος Αρχικών Λύσεων: ", fg="black", font ="none 14 bold" ) .grid(row=0,  column=0, sticky=tk.W)
K_label = tk.Label(window, text="Πλήθος λύσεων επόμενης γενιάς: ", fg="black", font ="none 14 bold" ) .grid(row=1,  column=0, sticky=tk.W)
steps_label = tk.Label(window, text="Βήματα: ", fg="black", font ="none 14 bold" ) .grid(row=2,  column=0, sticky=tk.W)
type_label = tk.Label(window, text="Τύπος Λύσεων (0: ακέραιοι, 1: πραγματικοί): ", fg="black", font ="none 14 bold" ) .grid(row=3,  column=0, sticky=tk.W)
pm_label =  tk.Label(window, text="Πιθανότητα Μετάλλαξης: ", fg="black", font ="none 14 bold" ) .grid(row=4,  column=0, sticky=tk.W)
function_label = tk.Label(window, text="Συνάρτηση: ", fg="black", font ="none 14 bold" ) .grid(row=5,  column=0, sticky=tk.W)


#text entries
N_entry = tk.Entry(window, width=6, bg="white", font="none 14")
N_entry.grid(row=0, column=1, sticky=tk.W)
N_entry.insert(tk.END, N)  #Βάζω αρχική τιμή
K_entry = tk.Entry(window, width=6, bg="white", font="none 14")
K_entry.grid(row=1, column=1, sticky=tk.W)
K_entry.insert(tk.END, K)
steps_entry = tk.Entry(window, width=6, bg="white", font="none 14")
steps_entry.grid(row=2, column=1, sticky=tk.W)
steps_entry.insert(tk.END, steps)
type_entry = tk.Entry(window, width=3, bg="white", font="none 14")
type_entry.grid(row=3, column=1, sticky=tk.W)
type_entry.insert(tk.END, input_type)
pm_entry = tk.Entry(window, width=6, bg="white", font="none 14")
pm_entry.grid(row=4, column=1, sticky=tk.W)
pm_entry.insert(tk.END, p_m)

#Dropdown menus
options_list = ['Standard', 'Function1', 'Function2']
variable = tk.StringVar(window)
variable.set(options_list[0]) # default value
dd_menu = tk.OptionMenu(window, variable, *options_list).grid(row=5, column=1, sticky=tk.W)


#Buttons
run_button = tk.Button(window, text="RUN", width=10, font ="none 18 bold", command=run_genetic).grid(row = 15,  column = 0, sticky=tk.W)
exit_button = tk.Button(window, text="EXIT", width=10, font ="none 18 bold", command=close_window).grid(row = 15,  column = 2, sticky=tk.E)
clear_button = tk.Button(window, text="CLEAR", width=10, font ="none 18 bold", command=clear_plots).grid(row = 15,  column = 1, sticky=tk.E) 

#Outputs!
result_outpout = tk.Text(window, width=70, height=1, wrap=tk.WORD, background="white")
result_outpout.grid(row = 20, column=0, columnspan=2, sticky=tk.W)
#space_outpout = tk.Text(window, width=80, height=1, wrap=tk.WORD, background="white")
#space_outpout.grid(row = 21, column=0, columnspan=2, sticky=tk.W)
solutions_outpout = tk.Text(window, width=70, height=20, wrap=tk.WORD, background="white")
solutions_outpout.grid(row = 22, column=0, columnspan=2, sticky=tk.W)


fig = plt.Figure(figsize=(4.5, 3), dpi=100)
#Μικραίνω τη γραμματοσειρά του γραφήματος
plt.rcParams.update({'font.size': 8})
#Φτιάχνω ένα γράφημα
ax = fig.add_subplot(111)
ax.set_xlabel('Generations')
ax.set_ylabel('Fitness')


canvas = FigureCanvasTkAgg(fig,  master=window)
canvas.draw()
canvas.get_tk_widget().grid(row=22, column=2, sticky=tk.E, ipadx=40, ipady=20)

# navigation toolbar
toolbarFrame = tk.Frame(master=window)
toolbarFrame.grid(row=23,column=2)
toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)


#Εδώ τρέχει ο κώδικας για το παράθυρο
window.mainloop()



#console code
# start = time.time()
# solutions = genetic_algorithm(5000, 1000, 200, 1, 0.4, printflag=False)
# end = time.time()
# print('Time needed = ',  end - start)
# n = 0
# for s in solutions:
#     print ('{:.4f}'.format(s[0]) + '\t' '{:.4f}'.format(s[1]) + '\t' + '{:.4f}'.format(s[2]),   '\t\t value=','{:.2f}'.format(solutions[s]) ) 
#     n = n + 1 
#     if n>20:
#         break