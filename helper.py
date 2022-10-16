#Script to help assist peiople to pick best guess in wordle. currently, mostly untested
import fnmatch
import random


def main():
    allposs = [] #all possible wordle-acceptable words, in list-format, initialize
    #first open word file, from other giothub repo
    allanswers = open("words","r")
    #next, string-fy list and put them into a list
    for line in allanswers:
        allposs.append(line)
    # Now habve list of all possible answers, prompt user if need starting word
    print("Welonme to Spencer's wordle-helper. Do need a random first word? Y/N: ")
    response = input()
    if response.lower()=="y":
        #generate a random number, and pick that number word, from sdolutions list
        numoptions = len(allposs)
        wordtotry = allposs[random.randint(0,numoptions-1)]
        print("ok, why don't you try using: "+wordtotry)
    else:
        print("Ok, suit yourself")
        #continue
        searchstr=""
    while not searchstr=="done":
        print("Ok,  now enter filter string using known letters, and *s + ?s, input done to quit")
        searchstr = input()
        searchstr+='\n' #all words in list end with newline, add to seach criteria, alternatively, add a star instead
        pos = fnmatch.filter(allposs,searchstr)
         
        numpos = len(pos)
        print("That seach criteria, yeilded: "+str(numpos)+" results total in wordlist")
        if numpos>0: 
            print("given that pattern, I found: "+str(numpos)+"words that fit thast criteria, picking one, now")
            totry = pos[random.randint(0,numpos-1)]
            print("ok, why don't youi try: "+totry)
        else:
            print("sorry, nnothing matched that pattern, try a different one, please")
    
    
if __name__=="__main__":
    main()
