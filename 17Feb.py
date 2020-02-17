import threading

lock = threading.Lock()


class MovieTicket():
    def __init__(self, name, seatnum):
        self.name = name
        self.seatnum = seatnum
        self.isbooked = False

    def showMovieTicket(self):
        print("{} | {} | {}".format(self.name, self.seatnum, self.isbooked))

m1 = MovieTicket("Sultan", 1)
m2 = MovieTicket("Sultan", 2)
m3 = MovieTicket("Sultan", 3)
m4 = MovieTicket("Sultan", 4)
m5 = MovieTicket("Sultan", 5)

rowA = [m1, m2, m3, m4, m5]


class Bookmovieticket(threading.Thread):

    def selectMovieTicket(self, ticket, email):
        self.ticket = ticket
        self.email = email

    def run(self):
        lock.acquire()
        if self.ticket.isbooked == False:
            print(" Booking for {}".format(self.email))
            print(" Booked for {}".format(self.email))
            for i in range(0, 10):
                print("Processing Payment for {}".format(self.email))
                self.ticket.isbooked = True
                self.ticket.showMovieTicket()

        else:
            print("Sorry Ticket Not Available")

            lock.release()


def main():
    print("~~~~~~~~~~~~~")
    print("App Started")
    user1 = Bookmovieticket()
    user2 = Bookmovieticket()

    user1.selectMovieTicket(rowA[2], "yavar@gmail.com")
    user2.selectMovieTicket(rowA[2], "yasir@gmail.com")

    user1.start()
    user2.start()

    print("<><><App Finished><><>")


if __name__ == '__main__':
    main()