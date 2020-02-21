# coding: utf-8
#
# the top line, above, is important --
# it ensures that Python will be able to use this file,
# even if you paste in text with Unicode characters
# (beyond ASCII)
# for an more expansive example of such a file, see
#    http://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt
#
# OK! Now we're ready for hw10pr3.py ...
#
#
# Name: Emanuel Jarquin
#
#


# function #1
#
import random 

def createDictionary(filename):
    '''will return a string based the words that appear right before 
        certain words. Also a word with a period, exclamation mark, or question mark
        marks the end of the sentence.
    '''
    d = {}
    f = open(filename)
    text = f.read()
    f.close()
    LoW = text.split()
    pw = '$'
    for nw in LoW:
        if pw not in d:
            d[pw] = [nw]
        else:
            d[pw] += [nw]
        pw = nw
        if nw[-1] == '.' or nw[-1] == '?' or nw[-1] == '!':
            pw = '$'
    return d
    # then check for whether that new pw ends in 
    # punctuation -- if it _does_ then set pw = '$'



# function #2
#
def generateText(d, N):
    '''returns N amount of words from d based on the same rules
        from the function above.
    '''
    pw = '$'
    y = ''
    for i in range(N):
        pw = random.choice(d[pw])
        y = y + ' ' + pw
        nw = pw[-1]
        if nw == '.' or nw == '!' or nw == '?':
            pw = '$'
    return y[1:]





#
# Your 500-or-so-word CS essay (paste into these triple-quoted strings below):
#
# Source: Codine Crazy by Future
#
"""
dollars that muddy When we're cuddling,
yeah Audemar, this Let's wrap up pour more lil' liquor Pour a lil' liquor, pour that you
Dont tell me at me going crazy Thats how I'm driving, all this lingo got you I try to eat at Chipotle 
Spent another 60 thousand on it back and fuck around and drink that muddy When I told you celibate to control this 
lingo got me at Stroker I get after madonna I adopted niggas straight out the lesson; put it I'm so fucking sick and fuck on a 
championship, celeberate like a goonie I forgot about us? Poppin’
molly Married to dropping Fuck the hate – now we’re back at me going codeine crazy Codeine 
crazy, yeah Audemar, this out the hummer Fronting some patience Told my eyes, believe it got her 
pussy’s soakin’ When we're cuddling, yeah I'm going codeine crazy All my eyes, believe it all this not a 
championship Celebrate like I'm sipping lean when I adopted niggas That ain't for them other bitches I'm driving, 
all this Let's wrap up Codeine crazy, codeine crazy Thats how I'm back on it I'm in the sewer Like a Rollie All this is a championship, 
celeberate like a model, yeah Pour a championship, celeberate like I'm putting my intellect Celebrate like a glacier Ballin’ harder than the 
Pacers I just took a nigga talk a carnival, but her panties to pay my soul in the hate – I told you dog, thats for They was thugging it, never 
complaining I'm an addict and hound We order more lil' liquor Pour it Told my heart and got your town with these millions I'm going crazy Codeine 
crazy, yeah Audemar, this cash and I just took a cutie, we done went Rick the lesson; put a championship Celebrate like a demo I'm back you know I 
just dropped a pole… Reminded myself that you I fuck on it, never comment on it, Don’t you I just wish you'd stop perpetrating like a cigarette, 
Run it I'm 'bout to come over Reminded myself when I just dived inside a championship, celeberate like a cigarette, Run it up like a faucet I just 
loving it all my eyes, believe it I'm driving, all in the summer, trapping in the kush up out the road, I was thugging it, Don’t you celibate to come over 
Reminded myself that bubbly, pour it back you hear my brainwashed And for them grounds with them other niggas, for They was thugging it, I adopted niggas 
That ain't nowhere to the other niggas, for the sewer Like a loaded I seen her name, but this motherfucking money got my heart and tired of these rumors I reply 
Drying my diamonds got you panic panoramic companion They ain't for you I told you panic panoramic companion They was thugging it, I'm driving, all this lingo got 
your town I adopted niggas That ain't for them guns and I just wish you'd stop perpetrating like

"""
#
