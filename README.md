# Osmago's Phyrexian Search Engine
 Simple GUI to search among known phyrexian words and text

I did this little program to make it easier for myself (and now others) to search things among the known words/sources of Phyrexian.

## Installations
To initiate, download the whole folder and run "phyrexian_search_engine.py"(made on **Python 3.7**, requires **pyglet** and **PySimpleGUI** packages, I will build a simple executable later).

## Usage
To search for words in Phyrexian, either click on the buttons to form your query or add to it by inputting text in transliterated Phyrexian. Attention, the program will handle things badly in case you try to use characters other than the ones in Phyrexian transliteration (I'm using the [Phyrexian Transliteration Chart v2.1 by u/Aldurethar](https://www.reddit.com/r/magicTCG/comments/nre288/an_update_for_the_new_phyrexian_transcription/), but without differentiating between X and Z. It's all Z here).

You can choose to include vowels and diacritics in your search or not. For example, in english the words 'cap', 'cop' and 'cup' would be the same if you didn't include the vowels. This is especially important because Phyrexian is believed to be a consonantal root language, so the same word can be conjugated by changing its vowels. Not including diacritics will give you many false matches, but this feature is here to make up for poor clarity in some sources that makes some diacritics very dubious.

Once you have a result, you will see a popup window with two sections: a first showing any known word (at least the ones I'm quite certain of) that matches to your query, then a list of every instance from every official and accurate source of Phyrexian taht matches to your query. This means that known words will have duplicates in the second section.

## Disclaimers
What I mean by "official and accurate" Phyrexian sources is that they were released by WotC and are written in the Phyrexian language. For example, fan-made phyrexian text might be accurate but not official, and [the Phyrexian Wurmcoil Engine](https://www.reddit.com/r/PhyrexianLanguage/comments/ny0n2g/from_a_wotc_survey_dont_know_if_its_been_analyzed/) is official but not accurate (english words are phonetically written using phyrexian characters).

I personally transliterated all known Phyrexian texts because I had already found some mistakes in [u/Aldurethar's transliterations](https://www.reddit.com/r/magicTCG/comments/oj2ahk/a_full_transliteration_of_all_known_phyrexian/) and there were new sources released/found since then. I double checked with his transliteration and my only sources of doubt now are in the All Will be One and New Phyrexia trailers because of the bad video resolution.

The wonderful [Progress Engine font by u/GuruJ_](https://www.reddit.com/r/magicTCG/comments/nqwqhn/first_release_of_progress_engine_font/) is included in the files, but I made my own (which I called the Phyrexian Compleat font) because some characters were missing and I wanted something that would be more legible from afar. Progress Engine is still prettier and you can use it by 'Ctrl+F'ing for "font_choice" in the python script and replacing 'Phyrexian Compleat' for 'Progress Engine' (will not work with the executable).

Translating Phyrexian is a community effort and everyone that tries to discover more is stepping on the shoulders of giants. Please check out all the wonderful people at [r/PhyrexianLanguage](https://www.reddit.com/r/PhyrexianLanguage/), HiglyEntropicMind's youtube series [Deciphering Phyrexian](https://www.youtube.com/watch?v=NsINwVt7fgY&list=PLunDPaoIqC7swE6n_jWJjjQYIkLm29McE) and it's [Discord server](https://discord.gg/6nu8PTEAVc).
