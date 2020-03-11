r=0
c=0
fi=0
f=0
t=0
tw=0
o=0
while(1):
    s=input("Enter Rating: ")
    c=c+1
    if(s=="1"):
      r=r+1
      o=o+1
      print("Thank you for your feedback")
      print("if you want to break, press yes")
    elif(s=="2"):
      r=r+2
      tw=tw+1
      print("Thank you for your feedback") 
      print("if you want to break, press yes")
    elif(s=="3"):
      r=r+3
      t=t+1
      print("Thank you for your feedback")
      print("if you want to break, press yes")
    elif(s=="4"):
      r=r+4
      f=f+1
      print("Thank you for your feedback")
      print("if you want to break, press yes")
    elif(s=="5"):
      r=r+5
      fi=fi+1
      print("Thank you for your feedback")
      print("if you want to break, press yes")
    elif(s=="yes"):
      break
    else:
      print("invalid input")
      c=c-1

print("No of people rated is: ",c-1,"valid ratings")
print("No of people who rated: ")
print("5=",fi,"||4=",f,"||3=",t,"||2=",tw,"||1=",o)        
print("The average rating is: ",r/(c-1))

