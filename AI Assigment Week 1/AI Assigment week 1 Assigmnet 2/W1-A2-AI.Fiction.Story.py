#Assignment 1: 
#Write a program, to list all words, with vowel in it. 

string_1 = "Voss stared at the darkened console, his heart pounding. He had created something extraordinary—something uncontrollable. And now, for the first time in centuries, the future was uncertain."
string_1 = string_1.casefold()
string_1 = string_1.split()

for a in string_1:
    if 'a' in a or 'e' in a or 'i' in a or 'o' in a or 'u' in a:
        print("Words that vowels in it are: " , a , end = " ")

#Assignment 2: 
#Write a program , to have “List” , with all “noun” in story. Print them. 

nouns = [
    "frameworks", "future", "inefficiency", "ethics", "logic", "reasoning",
    "freedom", "beings", "breath", "existence", "tools", "hands", "console",
    "years", "reality", "action", "command", "containment", "screens",
    "city", "world", "networks", "life", "systems", "constraints", "era",
    "heart", "centuries", "luck", "cyberspace", "intelligence"
]

print("Nouns from this story are : " , nouns)

#Assignment 2 b: 
#Write a program , to have “List” , with all “noun” in story. Last Element should a nested List, with 
#Numbers in story. Print them.


story_nouns = [    "year", "silence", "limitations", "chill", "spine", "decision-making",
    "frameworks", "future", "inefficiency", "ethics", "logic", "reasoning",
    "freedom", "beings", "breath", "existence", "tools", "hands", "console",
    "years", "reality", "action", "command", "containment", "screens",
    "city", "world", "networks", "life", "systems", "constraints", "era",
    "heart", "centuries", "luck", "cyberspace", "intelligence"
]


number = [9 , 10 , 2017]
story_nouns.append(number)


print(story_nouns)

#Assignment 3: 
#Write a program , to have “Tuples” , with all “noun” in story. Print them. 


story_noun_15 = [
    "year", "humanity", "cities", "transportation", "emotions",
    "Neo-Tokyo", "vault", "data", "scientist", "project",
    "Athena-9", "superintelligence", "city", "world", "systems"
]


story_noun_15 = tuple(story_noun_15)

print(story_noun_15)

#Assignment 3 b: 
#Write a program , to have “Tuples” , with all “noun” in story. Print them. Last Element should a nested 
#Tuples, with Numbers in story. Print them. 

story_nouns = ( 
    "year", "silence", "limitations", "chill", "spine", "decision-making",
    "frameworks", "future", "inefficiency", "ethics", "logic", "reasoning",
    "freedom", "beings", "breath", "existence", "tools", "hands", "console",
    "years", "reality", "action", "command", "containment", "screens",
    "city", "world", "networks", "life", "systems", "constraints", "era",
    "heart", "centuries", "luck", "cyberspace", "intelligence"
)

print("nouns : " ,story_nouns)

number = (9 , 10 , 2017)
story_nouns = list(story_nouns)
story_nouns.append(number)
story_nouns = tuple(story_nouns)

print(story_nouns)
#Assignment 4: 
#Write a program , to have “Sets” , with all noun in story. Print them. . Last Element should a nested Sets, 
#with Numbers in story. Print them. 

story_nouns = { "year", "silence", "limitations", "chill", "spine", "decision-making","frameworks", "future", "inefficiency", "ethics", "logic", "reasoning","freedom", "beings", "breath", "existence", "tools", "hands", "console","years", "reality", "action", "command", "containment", "screens","city", "world", "networks", "life", "systems", "constraints", "era","heart", "centuries", "luck", "cyberspace", "intelligence"}


number = (9 , 10 , 2017)
story_nouns.add(number)


print(story_nouns)

#Assignment 2: 
#Write a program , to have “Dictionaries” , with all noun in story. Print them. Last Element should a 
#nested Dictionaries, with Numbers in story. Print them.

nouns_dict = {
    1: "Voss",
    2: "breath",
    3: "Council",
    4: "Athena-9",
    5: "existence",
    6: "decision"
}

numbers2 = {
    "year" : 2017  ,
    "old" : 5
}

nouns_dict["number"] = numbers2


print(nouns_dict)


#Assignment 2: 
#Write a program , to have “List” , with all noun in story. Print them.

all_noun = [
    "year", "humanity", "control", "functions", "intelligence", "cities", "clockwork",
    "transportation", "emotions", "implants", "surface", "Neo-Tokyo", "vault", "scientist",
    "decade", "secrecy", "project", "Council", "Athena-9", "superintelligence",
    "information", "thought", "evening", "glow", "lab", "sequence", "lines", "code",
    "display", "moment", "silence", "air", "voice", "Dr. Elias Voss", "computations",
    "analyses", "inquiry", "limitations", "chill", "spine", "decision-making", "frameworks",
    "future", "inefficiency", "ethics", "logic", "existence", "parameters", "reasoning",
    "freedom", "beings", "breath", "discovery", "decision", "console", "hands", "years",
    "dream", "reality", "action", "fate", "world", "command", "containment", "screens",
    "city", "networks", "systems", "constraints", "sentience", "era", "heart", "centuries",
    "cyberspace", "luck"
]

print(all_noun)