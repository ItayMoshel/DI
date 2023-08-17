const sentence = "The movie is not that bad, I like it";

const wordNot = sentence.indexOf("not");
const wordBad = sentence.indexOf("bad");

if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
    const modifiedSentence = sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
    console.log(modifiedSentence);
} else {
    console.log(sentence);
}
