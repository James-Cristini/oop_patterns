from __future__ import print_function

class Transport(object):
    def __init__(self, destination, means_of_transportation):
        print("Arranging transport to desination {} by means of {}")
        self.desination = destination
        self.means_of_transportation = means_of_transportation

    def book_travel(self):
        if self.means_of_transportation == 'owncar':
            print("Customer does not need transportation booking!")
        elif self.means_of_transportation == 'plane':
            print("Booking travel to {0} by plane!".format(self.desination))
        elif self.means_of_transportation == 'bus':
            print("Booking travel to {0} by bus!".format(self.desination))

class Hotelier(object):
    def __init_(self):
        print("Arranging hotel accomodations")

    def room_available(self):
        return True

    def book_room(self):
        print("Checking if there are any rooms available.")
        if self.room_available:
            print("There area vailable rooms, booking now.")
        else:
            print("No rooms available at this time.")

    def arrange_food(self):
        print("arranging food for the customers!")

class SightSeeing(object):
    def __init__(self):
        print("Arranging sightseeing options!")

    def book_tour(self):
        print("Setting up a fancy tour!")

class TravelOrganizer(object):
    def __init__(self):
        print("Travel organizer: Let me arrange travel for you!")

    def arrange_travel(self, destination, means_of_transportation):
        print('The desination is: {0}'.format(destination))

        self.means_of_transportation = Transport(destination=destination, means_of_transportation=means_of_transportation)
        self.means_of_transportation.book_travel()

        self.accomodations = Hotelier()
        self.accomodations.book_room()
        self.accomodations.arrange_food()

        self.sightseeing = SightSeeing()
        self.sightseeing.book_tour()


class You(object):
    """ """

    def __init__(self, name):
        print("{0}, get ready to travel!".format(name))
        self.name = name

    def speak_to_agent(self):
        self.agent = TravelOrganizer()
        print("Asking agent to arrange travel!")
        self.agent.arrange_travel("Greece", 'plane')

    def __del__(self):
        print("Thank you agent for arranging the wonderful trip!")

def main():
    me = You('James')
    me.speak_to_agent()

if __name__ == '__main__':
    main()