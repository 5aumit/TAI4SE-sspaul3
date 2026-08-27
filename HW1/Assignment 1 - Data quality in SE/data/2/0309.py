#This program is used to just clean up the Pronunciation Dictionary and
#remove all the consonants

def main():
    print("testing 123")
    file = open("PronunciationDictionary.txt")
    word_dict = {}
    consonant_set = {"B", "CH", "D", "F", "G", "K", "L", "M", "N",
                     "NG", "P", "R", "S", "SH", "T", "TH", "V", "W",
                     "Y", "Z", "ZH"}

    
    for line in file:
        curr_list = line.split()
        phonemes = curr_list[1:]
        vowels = ''
        for sound in phonemes:
            if(not(sound in consonant_set)):
                vowels += sound + " "
        word_dict[curr_list[0]] = vowels[:-1]
    #print(word_dict)

    f= open("ConsonantLess_PD.txt","w+")
    for word in word_dict:
        f.write(word + "  "+word_dict[word]+"\n")
        #print(word + "  "+word_dict[word]+"\n")
main()

#words with a hash tag are consonant examples 
'''
         AA	odd     AA D
        AE	at	AE T
        AH	hut	HH AH T
        AO	ought	AO T
        AW	cow	K AW
        AY	hide	HH AY D
#        B 	be	B IY
#        CH	cheese	CH IY Z
#        D 	dee	D IY
        DH	thee	DH IY
        EH	Ed	EH D
        ER	hurt	HH ER T
        EY	ate	EY T
#        F 	fee	F IY
#        G 	green	G R IY N
        HH	he	HH IY
        IH	it	IH T
        IY	eat	IY T
        JH	gee	JH IY
#        K 	key	K IY
#        L 	lee	L IY
#        M 	me	M IY
#        N 	knee	N IY
#        NG	ping	P IH NG
        OW	oat	OW T
        OY	toy	T OY
#        P 	pee	P IY
#        R 	read	R IY D
#        S 	sea	S IY
#        SH	she	SH IY
#        T 	tea	T IY
#        TH	theta	TH EY T AH
        UH	hood	HH UH D
        UW	two	T UW
#        V 	vee	V IY
#        W 	we	W IY
#        Y 	yield	Y IY L D
#        Z 	zee	Z IY
#        ZH
'''
