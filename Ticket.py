class Ticket:
    counter=2000
    ticketList=[]
    def __init__(self,staff_id,staff_name, email, description):
        self.id=Ticket.counter
        Ticket.counter =Ticket.counter +1
        self.staff_id=staff_id
        self.name=staff_name
        self.email=email
        self.desc=description
        self.status="open"
        self.responce="Not Yet Provided"
        if "password change" in self.desc:
            self.changePassword()
    def respond(self):
        self.responce=input("please insert a responce")
        self.status="Closed"
        self.print()
    def print(self):
        print("Ticket ID:",self.id)
        print("Ticket ID:",self.name)
        print("Ticket ID:",self.email)
        print("Ticket ID:",self.status)
        print("Ticket ID:",self.desc)
        print("Ticket Responce",self.responce)

    def changePassword(self):
        newpassword=self.staff_id[0:2]+self.name[0:3]
        self.responce ="Password changed"
        self.status="Closed"
        self.print()
    def printTicketStats():
        pass

class Main():
   def main():
       
        while True:
            
            print("1. Create a ticket ")
            print("2. print a ticket ")
            print("3. respond to  ticket ")
            print("4. View Course ")
            print("5. Enrol a student ")
            print("6. Display all courses of a student")
            print("7. Exit")
            option=int(input("Please select an option: "))

            match option:
                case 1:
                    s_id=input("Please enter your staff ID")
                    s_name=input("Please enter your Name ")
                    email=input("Please enter email ")
                    desc=input("Please enter descition of your problem")
                    ticket=Ticket(s_id,s_name, email, desc)
                    Ticket.ticketList.append(ticket)
                case 2:
                    t_id=int(input("Enter ticket id"))
                    ticket=  next((x for x in Ticket.ticketList if x.id == t_id), None)
                    if ticket==None:
                        print("Ticket not found")
                    else:
                        ticket.print()
                case 3:
                    t_id=int(input("Enter ticket id"))
                    ticket=  next((x for x in Ticket.ticketList if x.id == t_id), None)
                    if ticket==None:
                        print("Ticket not found")
                    else:
                        ticket.respond()
                case 4:
                    pass
                case 5:
                     pass
                case 6:
                    pass
                case 7:
                    break
                case _:
                    print("Incorrect Option Selected ")
                    


Main.main()



