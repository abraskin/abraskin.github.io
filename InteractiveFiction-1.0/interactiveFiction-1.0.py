#Chautauqua Overcomes Bias
#Interactve fiction 1.0
#Aaron Braskin & Anthony Pittman	

def introduction():
	print "Chautauqua Overcomes Bias"
	print "A story about good classroom norms."
	print ""
	
	print "CSP Prof. Karing assigns the Interactive Fiction assignment to his class. This assignment requires students to develop an interactive story in Python. In the Professor's class, students work in assiged groups of four. Our heroine, Chatauqua, has been assigned to a group with three boys: Dom, Nix, and Blink."
	print ""
	winningOverBlink()

def winningOverBlink():
	print "'Our story is going to be about a gigantic robot fighting a dragon,' Dom annonuces to everyone."
	print "Chatauqua is not too sure she like this idea. What is her idea for a story?"
	answer = raw_input()
	print""
	print "Blink just blinks."
	print "Nix says '" + answer + "' is a stupid idea."
	print "Dom continues 'So the dragon is red. Chatauqua, write this down."
	print""
	print"Does Chatauqua: a) accept the role of secretary but write her own ideas or b) politely refuse the job?"
	answer=raw_input()
	print""
	if answer == "a":
		print "A few minutes later, Dom finishes his idea and says 'Chataqua, give me your notes.' After a quick look, Dom exclaims 'This is that dumb idea YOU wanted. Blink, rewrite this with MY story!'"
	else:
		print "Dom scowls. 'Blink, you are the secretary because SHE wont do it!'"
	print""
	print"'Blink, start writing the flowchart now,' says Dom. Nix and Dom pull out their phones to play a quick game of Pokemon Go."
	print"Blink starts writing the setting in a circle at the top of the paper. Will Chatauqua tell him that it should be a rectangle? (Y/N)"
	answer = raw_input()
	while answer=="N" or answer=="n":
		print "Blink is now adding a rectangle to represent a decision block. Are you sure you don't want to correct him? (Y/N)"
		answer=raw_input()
		if answer=="N" or answer=="n":
			print "Blink is really screwing up the flowchart! Your grade is suffering!"
	print""
	print"'Blink, I think you use rectangles for starts and ends and diamonds for decisions,' says Chautauqua."
	print"Blink blinks."
	print"Blink continues screwing up the flowchart, until Prof. Karing happens to walk by. 'I think you want to use a diamond for decisions there, Blink,' says the Professor. The Professor keeps strolling by. Blink gives Chautauqua a sheepish look, 'I guess I should have listened to you,' he says."
	print""
	winningOverNix()
	
def winningOverNix():
	print"Dom looks up from his game. 'Nix, they're done. Start writing the code. I need to walk around the room  a few more times to hatch this Narusaur egg.'"
	print"'Aww man, ok,' says Nix. He puts away his phone, opens repl.it, and begins staring blankly at the editor."
	print""
	print"Fifteen minutes later, he presses the Run button to test his three lines of code. 'It's not working,' says Dom, who is now looking over Nix's shoulder - his Naurusaur freshly hatched. 'MAKE IT WORK. YOU'RE the programmer.'"
	print""
	print"Chautauqua sees the problem: Nix did not properly indent his 'if' statement. Should she help him out? (Y/N)"
	answer=raw_input()
	if answer=="N" or answer=="n":
		print "The next day, during the Gallery Walk, Dom proudly presses the 'Run' button...but nothing happens at all. The code is completely broken. Dom gives the other group members an icy look. Professor Karing, with a note of pain, says 'I'm sorry, but this groups hasn't earned a passing grade. You'll need to write a 6-page essay on what went wrong to make it up."
		exit()
	print""
	print"Chautauqua sits in the driver's seat and points out the error. She fixes Nix's mistake and continues to work with him on the programming."
	print"After working for 20 minutes, Chautauqua gets stuck on writing functions. Nix thinks he knows the solution. Should Chautauqua listen? (Y/N)"
	answer = raw_input()
	if answer=="N" or answer=="n":
		print "By the Gallery Walk the next morning, the program works...sort of. Professor Karing decided to give the group a 'C' because the program has no working functions - a part of the rubric."
		exit()
	print"Nix says, 'This works so much better when we work together! We've conquered if statements AND functions!' It seems like the project is coming to a happy ending, with Nix, Blink, and Chautauqua working together according to good group norms."
	print""
	goodGroupNorms()
	
def goodGroupNorms():
	print"Dom enters the class after having left to fetch a Pokemon item from the boy's bathroom. He walks over to the story. 'The Dragon didn't win. I thought I told you to make the Dragon win because they are cooler than robots.' Chautauqua, Blink, and Nix look at each other."
	print""
	print"Should Chatauqua a) change the ending as Dom wants or b) ask for the groups' opinion on the ending, risking Dom's wrath?"
	answer=raw_input()
	if answer=="a" or answer=="A":
		print "The next day, during the Gallery Walk, Dom proudly presses the 'Run' button...and the story plays...just as Dom wanted. Professor Karing says, 'Good job. My only complaint is that this story seems to represent the opinion of ony one group member.' The Professor gives Dom a knowing look. 'This is a 'B' project.'"
		exit()
	print "The next day, during the Gallery Walk, Dom proudly presses the 'Run' button...and the groups' story plays. Professor Karing says, 'Excellent job! I see you have learned Python and, more importantly, how to work together as a cohesive group!! You have earned an 'A' for this amazing project!'"
introduction()


	