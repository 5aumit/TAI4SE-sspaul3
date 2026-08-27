StringBuilder text = new StringBuilder();

// deal with potential null variables
if(sentenceVariance == null){
sentenceVariance = 0;
}
if(includeEnochian == null){
includeEnochian = false;
}
if(enochianWeight == null){
enochianWeight = 1;
}

int sentenceLengthMin = SENTENCE_LENGTH_MIN - sentenceVariance;
int sentenceLengthMax = SENTENCE_LENGTH_MAX - sentenceVariance;
ArrayList<String> words = new ArrayList<String>();
words.addAll(WORDS);

// append Enochian words to list if includeEnochian is true,
// and add n times according to the weighting.
if(includeEnochian.booleanValue()){
while(enochianWeight >= 1){
words.addAll(ENOCHIAN);
enochianWeight--;
}
}

// randomize array order
Collections.shuffle(words);

for(int p=0;p<nParagraphs;p++){
StringBuilder paragraph = new StringBuilder();
int paragraphSentenceCount = randomInRange(PARAGRAPH_SENTENCE_COUNT_MIN,PARAGRAPH_SENTENCE_COUNT_MAX);

// add sentences to paragraph
for(int i=0;i<paragraphSentenceCount;i++){
StringBuilder sentence = new StringBuilder();
int sentenceLength = randomInRange(sentenceLengthMin,sentenceLengthMax);
int previousWordIndex = 0;

// add words to sentence
for(int l=0;l<sentenceLength;l++){
int index = randomInRange(0,words.size());
// if index is the same as the previous word index, get a new one
while (index == previousWordIndex){
index = randomInRange(0,words.size());
}
previousWordIndex = index;
// append the word
sentence.append(words.get(index));
// unless it is the last word in the sentence, add a space
if(l < sentenceLength-1){
sentence.append(" ");
}
}
sentence.append(". ");
// capitalize first letter of the sentence
sentence.setCharAt(0,Character.toUpperCase(sentence.charAt(0)));
paragraph.append(sentence);
}

// if it is the first paragraph, prepend Satan ipsum to paragraph
if(p == 0){
String leaderText = "Satan ipsum ";
paragraph.insert(0,leaderText);
paragraph.setCharAt(leaderText.length(),Character.toLowerCase(paragraph.charAt(leaderText.length())));
}

text.append(paragraph);
text.append("<br/><br/>");
}
return text.toString();