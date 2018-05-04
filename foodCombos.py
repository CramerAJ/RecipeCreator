#
 # Title: PROTOTYPE
 # Name: Andrew Cramer
 # Date: 4/30/18
 # Description: The code below, takes in a list of user recipes, 
 ##             and outputs a list of recipes, it thinks the user may want
 ##				based on weighted values found in a certain ingredient 
## this program can be run in any command line
## python foodCombos.py for Linux

## Importing tools to be used

import numpy as np
from numpy.random import choice
import itertools as itertools
from itertools import *
from Tkinter import *

#This is creating a GUI using tkinter

root = Tk()
root.title("Recipe Creator")
root.geometry("1000x600")
root.config(bg='lightblue')
header = Label(root,text="Recipe Creator",bg='lightblue',font=("arial",25,"bold")).pack()
label = Label(root,bg='lightblue', text="Insert as many Recipes as you wish (Example: Bread Egg Fish, etc....): ").place(x=10,y=50)

userRecipe = StringVar()
appEntry = Entry(root, textvariable = userRecipe,width=50,).place(x=10,y=80)


## creating a function called FoundCombos
## passing in user inserted recipes, a static matrix, and a empty list
def foundCombos( parse_userRecipes, totalTimeFound, matrix,baseListIngredients):
	print ("Creating Recommended Recipe")
	label = Label(root,bg='lightblue',text="Creating Recommended Recipes!!!!").place(x=10,y=110)
	##this is our rows for the matrix, determined by the number of recipes parsed

	parse_UR = parse_userRecipes 
	label = Label(root,bg='lightblue',text="Given User Recipes:").place(x=10,y=130)
	#label = Label(root,parse_UR) 

	print ('')

	totTF = totalTimeFound
	#Declaring variable form atrix row and columns

	matrixRows = len(parse_userRecipes)
	matrixColumns = len(baseListIngredients)
	#New list for ingredients that weren't in the original list, too reinsert later
	#Of course with this approach the structure and format of matching ingredients becomes incredbly
	#slow with a double list storage, or matrix
	
	newIngredients = list()
	##This loop scans through the staticly created matrix and fills in spots
	##Where an ingredient is found in a recipe
	for i in range(len(parse_UR)):

		#grabs the parsed index
		recipeIndex = parse_UR[i]
		listOfIngredients = recipeIndex
		tmp = listOfIngredients.split(" ")
		label = Label(root,bg='lightblue',text='Looking at Recipes for Known Ingredients').place(x=10,y=150)
		print ('Looking at recipe Number:')
		print (i + 1)
		for j in range(len(tmp)):

			#if the ingredients match it places a 1 in that index and row
			for k in range(len(baseListIngredients)):
				if (tmp[j].startswith(baseListIngredients[k])):
					matrix[i][k] = 1
					totTF[k] += 1
				#Here I wanted to add the ingredient if it wasn't found in the original list,
				#I was getting weird erros here so commented it out
				#else
					#this way adds too many new ingredients so ignore it
					#newIngredients.append(tmp[j])
					

	##Adding new ingredients that didnt match to our original list so it can become more accurate
	#baseListIngredients.append(newIngredients)

	print ('Final Matrix')
	print (matrix)
	print (totTF)
	print ("# of times an Ingredient was found")
	print (baseListIngredients)
	print ("Now creating a list of Desired Recipes Based on Weights: ")

	sumofIngred = sum(totTF)
	weightsOfIngredients = list()

	for i in range(len(totTF)):
		ingredientNum = totTF[i]

		weightIngre = (float(ingredientNum) / float(sumofIngred)) 
		weightsOfIngredients.append(weightIngre)

	print (weightsOfIngredients)





## This code isn't used in the final prdocut, but important to have when understanding how to find
## pairs in the matrix
	## For this I first scan one matrix row at a time
	foundPairs = list()
	for i in range(matrixRows):
		#making a tmp to hold the row index
		print ('Looking at Matrix Row #:')
		print (i)
		tmp = matrix[i]
		print (tmp)
		#creating an empty list to store all matched ingredients
		ingreIndexList = []
		for j in range(len(tmp)):
			print ('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
			#If the sum of the row is greater than 1, we know there exists atleast one pair to grab
			value = sum(tmp)
			if (value > 1):			
				if (matrix[i][j] == 1):
					#when confirmed the ingredient value is 1(or matched) 
					#we output the index value for the base list of ingredients, and store that ingredient
					index = baseListIngredients[j]
					ingreIndexList.append(index)
					print (index)
					print (ingreIndexList)
					print ('Save Found Ingredient in matrix Row')
		
		print ('Done checking row')
		print ('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
		print ('Looking for pairs in list')
		print (ingreIndexList)
		#Using itertools we grab all pairs of ingredients
		
		comb = itertools.combinations(ingreIndexList,2)
		temp_list = list(comb)
		print ('Found Pairs:')
		print (temp_list)
		print ('Appending Pair to List of All Known Pairs:')
		

		#We then check for how many times a pair occurs in the user provided recipes
		
		for pair in temp_list:
			#Making sure no duplicate pairs, or rather duplicate index pairs are passed in
			#Made this change, when 2 pairs of (A,B) were present, but was showing 4 total
			if pair not in foundPairs:
				foundPairs.append(pair)
	
	print ('Printing the found Pairs in the user Recipe')
	print (foundPairs)
	#Here we grab the most commonly found pair and perform a 
	#cross reference on the total times one of the ingredients has been found
	#For instance A came up twice, but B only once, so the pair AB is 1 over 2 = 50% of the time
	
	totalPairCount = list()
	
	for pair in foundPairs:
		pair_count = 0 
		index_1 = baseListIngredients.index(pair[0])
		index_2 = baseListIngredients.index(pair[1])
	
		for row in matrix:
			if (row[index_1] == 1 and row[index_2]==1):
				pair_count+=1
				print (pair_count) 
		totalPairCount.append(pair_count)
	print (totalPairCount)
	#Outputs the recommended recipe
	
	finalRecipe = list()
	for x in range(1):
		recipe = totalPairCount.index(max(totalPairCount))
		pairRecipe = foundPairs[recipe]
		finalRecipe.append(pairRecipe)



	## Outputting all the new recipes based on user input

	threeIngredient = choice(baseListIngredients, 3, p=weightsOfIngredients)
	fourIngredient = choice(baseListIngredients, 4, p=weightsOfIngredients)
	fiveIngredient = choice(baseListIngredients, 5, p=weightsOfIngredients)
	sixIngredient = choice(baseListIngredients, 6, p=weightsOfIngredients)
	
	label = Label(root,bg='lightblue',text='New Recipes Created').place(x=10,y=170)
	print ('New Recipes Created')
	
	label = Label(root,bg='lightblue',text='We Made a Recipe of Size 3').place(x=10,y=210)
	label = Label(root,bg='lightblue',text=threeIngredient).place(x=250,y=210)
	
	print ('Recipe Size 3')
	print (threeIngredient)
	label = Label(root,bg='lightblue',text='We Made a Recipe of Size 4').place(x=10,y=230)
	
	print ('Recipe Size 4')
	label = Label(root,bg='lightblue',text=fourIngredient).place(x=250,y=230)
	print (fourIngredient)

	label = Label(root,bg='lightblue',text='We Made a Recipe of Size 5').place(x=10,y=250)
	label = Label(root,bg='lightblue',text=fiveIngredient).place(x=250,y=250)
	
	print ('Recipe Size 5')
	print (fiveIngredient)

	label = Label(root,bg='lightblue',text='Recipes in Our DataBase').place(x=10,y=310)
	label = Label(root,bg='lightblue',text=baseListIngredients).place(x=10,y=330)

	label = Label(root,bg='lightblue',text='Found this pair to work the best with eachother, Recommend to include in each recipe:').place(x=10,y=350)
	label = Label(root,bg='lightblue',text=finalRecipe).place(x=10,y=370)
	


#This is similar to the if__name_== main loop, except its called when the user presses the button
def run_it():
	baseListIngredients = ["Avacado","Apple","Bread","Chicken","Cheese","Date","Egg","Fish","Garlic","Ham","Ice","Jelly","Kale","Lemon","Lettuce","Mango","Nuts","Oregano","Pepper","Quail","Rice","Salt","Thyme","Urchin","Veal","Wasabi","Yeast","Zucchini"]
	#filling a list with 0s, this will be a counter to reevaluate when seeing how often an ingredient occurs
	ingredientTotalCounter = []
	for i in range(len(baseListIngredients)):
		ingredientTotalCounter.append(0)
	
	##User info stored as a tmp to pass along once parsed
	tmp = userRecipe.get()
	print ('tmp')
	print (tmp)
	parse_userRecipe = tmp.split(",")
	shape = (len(parse_userRecipe),len(baseListIngredients))
	matrix = np.zeros(shape)
	print matrix
	foundCombos(parse_userRecipe,ingredientTotalCounter,matrix,baseListIngredients)
	pass

button = Button(root,text="Create New Recipes!",bg='lightblue',width=30,height=1,command=run_it).place(x=500,y=80)
root.mainloop()
	
#if __name__ == "__main__":
	#baseListIngredients = ["Avacado","Bread","Chicken","Date","Egg","Fish","Grape","Ham","Ice","Jelly","Kale","Lemon","Mango","Nuts","Oregano","Pepper","Quail","Rice","Salt","Thyme","Urchin","Veal","Wasabi","Yeast","Zucchini"]
	#ingredientTotalCounter = []
	#filling a list with 0s, this will be a counter to reevaluate when seeing how often an ingredient occurs
	#print ("Insert as many Recipes as you wish (Example: Bread Egg Fish, etc....)")
	#for i in range(len(baseListIngredients)):
	#	ingredientTotalCounter.append(0)
	#userRecipe = raw_input()
	#parse_userRecipe = userRecipe.split(",")
	#shape = (len(parse_userRecipe),len(baseListIngredients))
	#matrix = np.zeros(shape)
	#label = Label(root,matrix)
	#label.pack()
	#print matrix
	#foundCombos(parse_userRecipe,ingredientTotalCounter,matrix)
