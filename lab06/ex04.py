# Function to remove punctuation and convert to lowercase
def normalizeLyrics(lyrics):
    lyrics = lyrics.lower()
    lyrics = lyrics.replace(",", "")
    lyrics = lyrics.replace(".", "")
    lyrics = lyrics.replace(":", "")
    lyrics = lyrics.replace("\n", " ")
    return lyrics.split()

# Function to count the frequency of words
def lyricsToFrequencies(words):
    freqDict = {}
    for word in words:
        if word in freqDict:
            freqDict[word] += 1
        else:
            freqDict[word] = 1
    return freqDict

def sortWords(freqDict):
    return sorted(freqDict.items(), key=lambda x: x[1], reverse=True)

print("Please enter the lyrics of the song. Press Enter twice to finish.")
input_lines = []
while True:
    line = input()
    if line == "":
        break
    input_lines.append(line)

lyrics = '\n'.join(input_lines)


# calling the functions to perform different operations
words = normalizeLyrics(lyrics)
freqDict = lyricsToFrequencies(words)
sortedWords = sortWords(freqDict)

# print the words with highest frequency
print("Words with highest frequency:")
for word, freq in sortedWords[:10]:
    print(word +": %s" % freq)

# print the words with lowest frequency
print("\nWords with lowest frequency:")
for word, freq in sortedWords[-10:]:
    print(word +": %s" % freq)