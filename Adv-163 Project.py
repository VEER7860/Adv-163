from tkinter import *
root = Tk()
root.title("Heart_Diagnose_Report")
root.geometry("600x630")

question1_radioButton=StringVar(value="0")

Question1= Label(root, text ="Do you experience shortness of breath during routine activities? ")
Question1.pack()
question1_r1=Radiobutton(root, text ="yes",variable=question1_radioButton,value="yes" )
question1_r1().pack
question1_r2=Radiobutton(root, text ="no",variable=question1_radioButton,value="no" )
question1_r2().pack()

question2_radioButton=StringVar(value= "0")
Question2=Label(root, text ="Do you experience shortness of breath while at rest/lying down?")
Question2.pack()
Question2_r1=Radiobutton(root, text ="yes",variable=question2_radioButton,value="yes" )
Question2_r1.pack()
question2_r2=Radiobutton(root, text ="no",variable=question2_radioButton,value="no" )
question2_r2.pack()

question3_radioButton=StringVar(value= "0")
Question3=Label(root, text ="Do you feel short of breath while lying flat and feel the need to stack multiple pillows to sleep well?")
Question3.pack()
Question3_r1=Radiobutton(root, text ="yes",variable=question2_radioButton,value="yes" )
Question3_r1.pack()
question3_r2=Radiobutton(root, text ="no",variable=question2_radioButton,value="no" )
question3_r2.pack()

question4_radioButton=StringVar(value= "0")
Question4=Label(root, text ="Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus?")
Question4.pack()
Question4_r1=Radiobutton(root, text ="yes",variable=question2_radioButton,value="yes" )
Question4_r1.pack()
question4_r2=Radiobutton(root, text ="no",variable=question2_radioButton,value="no" )
question4_r2.pack()

question5_radioButton=StringVar(value= "0")
Question5=Label(root, text ="Do you have swelling in the feet/ ankles/legs (shoes feel tighter) or abdomen?")
Question5.pack()
Question5_r1=Radiobutton(root, text ="yes",variable=question2_radioButton,value="yes" )
Question5_r1.pack()
question5_r2=Radiobutton(root, text ="no",variable=question2_radioButton,value="no" )
question5_r2.pack()

def heart_score():
    score = 0
    if question1_radioButton.get()=="yes":
        score = score+10
        print(score)
    if question2_radioButton.get()=="yes":
        score = score+10
        print(score)
    if question3_radioButton.get()=="yes":
        score = score+10
        print(score)
    if question4_radioButton.get()=="yes":
        score = score+10
        print(score)
    if question5_radioButton.get()=="yes":
        score = score+10
        print(score)

if score <= 10:
        messagebox.showinfo("Report","You don't need to visit a doctor.")
    elif score > 10 and score <= 30:
         messagebox.showinfo("Report","You might perhaps have to visit a doctor.")
    else:
         messagebox.showinfo("Report","I strongly advise you to visit a doctor.")
btn = Button(root, text= "Click me", command= heart_score)        
btn.pack()
root.mainloop()
      