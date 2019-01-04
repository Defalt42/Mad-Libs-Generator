adj1 = input("Enter an adjective: ")
adj2 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter a noun: ")
adj3 = input("Enter an adjective: ")
adj4 = input("Enter an adjective: ")
adj5 = input("Enter an adjective: ")
verb1 = input("Enter a verb: ")
adj6 = input("Enter an adjective: ")

story = "There is no power in the universe quite like the Force. The Force is what gives a Jedi his {} power.\n" \
        "It's an energy field created by all {} {}. It binds the {} together. The force can be used for {} or {}.\n" \
        "The dark side is {} and the {} side is good! The Force {} a Jedi strong.".format(adj1, adj2, noun1,
                                                                                          noun2, adj3, adj4,
                                                                                          adj5, verb1, adj6)
print(story)

