# Filename: process_melodies.py
# Author: Justine Lee
# Date: 10/20/14
import math 

class Melody:
	def __init__(self, csv_path):
		# Open the csv file
		csv_file = open(csv_path,'r')

		self.pitches = []
		prev_pitch = 0

		# Read file line by line and store pitches in array
		for line in csv_file:
			line_split = line.split(",")
			pitch = int(math.floor(round(float(line_split[1].strip()))))
			if pitch != 0 and pitch != prev_pitch:
				self.pitches.append(pitch-prev_pitch)
				prev_pitch = pitch

	def filter_array(self,min_diff):
		self.filtered_array = []
		i=1
		while i < len(self.pitches):
			pitch = self.pitches[i]
			if abs(pitch) >= min_diff:
				pitch = int(10 * round(float(pitch)/10))
				self.filtered_array.append(pitch)
			i += 1
		
		return self.filtered_array

	def count_occurrences(self):
		self.occurrence_dictionary = {}
		for difference in self.filtered_array:
			if difference not in self.occurrence_dictionary:
				self.occurrence_dictionary[difference] = 0

		for difference in self.filtered_array:
			self.occurrence_dictionary[difference] += 1

	def generate_transition_dictionary(self):
		self.transition_dictionary = {}
		i=0
		while i < len(self.filtered_array)-2:
			key = str(self.filtered_array[i])+":"+str(self.filtered_array[i+1])
			if key not in self.transition_dictionary:
				self.transition_dictionary[key]=0
			i += 1

		j=0
		while j < len(self.filtered_array)-2:
			key = str(self.filtered_array[j])+":"+str(self.filtered_array[j+1])
			self.transition_dictionary[key] += 1
			j+= 1

		for key in self.transition_dictionary:
			parse_key = key.split(":")
			start = parse_key[0]

			total_transitions = self.occurrence_dictionary[int(start)]

			self.transition_dictionary[key] = float(float(self.transition_dictionary[key])/float(total_transitions))

	def get_occurrence_dictionary(self):
		return self.occurrence_dictionary

	def get_transitions_dictionary(self):
		return self.transition_dictionary

	def get_filter_array(self):
		return self.filtered_array


new_melody = Melody("/Users/justinelee/Projects/Sound-Identification/Songs/I KNEW YOU WERE TROUBLE ~ TAYLOR SWIFT/Anny - I Knew You Were Trouble (Taylor Swift Cover)_vamp_mtg-melodia_melodia_melody.csv")
new_melody.filter_array(5)
new_melody.count_occurrences()
occurrences = new_melody.get_occurrence_dictionary()
new_melody.generate_transition_dictionary()
transitions = new_melody.get_transitions_dictionary()
for key in transitions:
	print key,
	print transitions[key]
print len(transitions)
# print occurrences

# new_melody_2 = Melody("/Users/justinelee/Projects/Sound-Identification/Songs/I KNEW YOU WERE TROUBLE ~ TAYLOR SWIFT/I Knew You Were Trouble - Taylor Swift (cover)_vamp_mtg-melodia_melodia_melody.csv")
# filtered_2 = new_melody_2.filter_array(5)
# print len(new_melody_2.pitches)
# print len(filtered_2)
# print filtered_2[50:100]
