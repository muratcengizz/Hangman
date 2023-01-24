class hangMan():
	def __init__(self):
		self.secret_word = "murat"
		self.user_quess = ""
		self.user_health = 10

	def gamerun(self):
		while True:
			for element in self.secret_word:
				if element in self.user_quess:
					print(element)
				else:
					print("-")

			self.user_input = input("Please enter a chrachter: ")
			self.user_quess += self.user_input

			if self.user_input in self.secret_word:
				print("True quess!")
			elif self.user_input not in self.secret_word:
				self.user_health -= 1
				print(f"Wrong quess!\nYou have {self.user_health} left!")

			if self.user_quess == self.secret_word:
				print("You won!")
				exit()
			elif self.user_health == 0:
				print("You die!")
				exit()


my_instance = hangMan()
my_instance.gamerun()