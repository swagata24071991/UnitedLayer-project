# -*- coding: utf-8 -*-
"""
Created on Fri May 22 13:18:40 2020

@author: Payel
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:47:44 2020

@author: Payel
"""

class Hotel():
	def __init__(self):
		self.data = {}
		self.addHotel1()

	def addHotel1(self):
		name = input("Enter Hotel name: ")
		if self.data.get(name, False):
			print("Hotel with same name already exist!..")
			self.addHotel2()
		else:
			self.data[name]={}
			self.addRoom1(name)

	def addRoom1(self, name):
		room_no = input("Enter Room Number: ")
		self.data[name][room_no]={"amenities": [], "amenitiesList": [], "cost": 0}
		i = 0
		while i < 5:
			self.addAllAmenities(name, room_no)
			i += 1
		self.addAmenities2(name, room_no)

	def addAllAmenities(self, name, roomNo):
		item = input("Enter the amenities name: ")
		price = input("Enter amenities prize in $ (should be a number): ")
		self.data[name][roomNo]["amenities"].append({item:price})
		self.data[name][roomNo]["amenitiesList"].append(item)
		self.data[name][roomNo]["cost"] += int(price)


	def addAmenities1(self, name, roomNo):
		item = input("Enter the amenities name: ")
		price = input("Enter amenities prize in $ (should be a number): ")
		self.data[name][roomNo]["amenities"].append({item:price})
		self.data[name][roomNo]["amenitiesList"].append(item)
		self.data[name][roomNo]["cost"] += int(price)
		self.addAmenities2(name, roomNo)


	def addHotel2(self):
		add_hotel = input("Do you want to add New Hotel (Yes/No): ")
		if add_hotel.lower() == "yes":
			self.addHotel1()
		elif add_hotel.lower() == "no":
			self.show()
		else:
			print("Invalid Input")
			self.addHotel2()

	def addRoom2(self, name):
		add_room = input("Do you want to add more Room(Yes/No): ")
		if add_room.lower() == "yes":
			self.addRoom1(name)
		elif add_room.lower() == "no":
			self.addHotel2()
		else:
			print("Invalid Input")
			self.addRoom2(name)


	def addAmenities2(self, name, roomNo):
		add_amenities = input("Do you want to add more amenities(Yes/No): ")
		if add_amenities.lower() == "yes":
			self.addAmenities1(name, roomNo)
		elif add_amenities.lower() == "no":
			self.addRoom2(name)
		else:
			print("Invalid Input")
			self.addAmenities2(name, roomNo)

	def show(self, budget=0):
		for hotel_name, room_info in self.data.items():
			context = "\nRoom No {0} have the amenities like {1}, and room rent is ${2}."
			if budget == 0:
				data = '\n\n\n{0} Hotel have following rooms\n'.format(hotel_name)
				for room, amenti_info in room_info.items():
					amenti = ', '.join(amenti_info['amenitiesList'])
					cost = amenti_info['cost']
					data += context.format(room, amenti, cost)
				print(data)
			else:
				data = '\n\n\n{0} Hotel have following rooms matching your budget\n'.format(hotel_name)
				availability = False
				for room, amenti_info in room_info.items():
					cost = amenti_info['cost']
					if cost <= budget:
						amenti = ', '.join(amenti_info['amenitiesList'])
						availability = True
						data += context.format(room, amenti, cost)
				if availability:
					print(data)
				else:
					print("\n\n\nNo room available for your budget in hotel {0}".format(hotel_name))
			print("\n***********************************************************\n")
		if budget == 0:
			self.getUserBudget()

	def getUserBudget(self):
		print("\n***********************************************************\n")
		budget = int(input("Please enter your budget: "))
		if budget > 1:
			self.show(budget)
		else:
			print("Invalid Budget range")
			self.getUserBudget()


Hotel()