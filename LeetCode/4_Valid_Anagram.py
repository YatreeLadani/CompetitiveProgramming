def validanagram(s,t):
    if (1 <= len(s) and 1 <= len(t)) or (len(s) <= 5 * (10**4) and len(t) <= 5 * (10**4)):
        if sorted(s)==sorted(t):
            print("True")
        else:
            print("Flase")
    

validanagram("rat", "art")