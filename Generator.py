import random

candid_List = []

candidates = input("Please enter the candidates:") ###enter candidates with no space

for candidate in candidates:
    candid_List.append(candidate)

### Case 1: All candidates are been voted.
all_votes_List = []
n = input("Please enter the number of random candidates sequences that you want to generate:")

for i in range(int(n)):
    random.shuffle(candid_List)
    all_votes_List.append(candid_List)
    
print(all_votes_List)

### Case 2: Only some of the candidates are been voted:
some_votes_List = []
k = input("Please enter the number of random candidates sequences that you want to generate:")

for i in range(int(k)):
    random_List = random.sample(candid_List, random.randint(1,len(candid_List)-1))
    some_votes_List.append(random_List)

print(some_votes_List)

###Add two lists together and random shuffle to generate voting sequences
final_votes_List = all_votes_List + some_votes_List
random.shuffle(final_votes_List)
print(final_votes_List)

###Write random voting sequences into a txt file
votes = open("votes.txt","w")

for row in final_votes_List:
    votes.write(str(row)+"\n")
