# Osmago's Phyrexian Search Engine
 Simple GUI to search among known phyrexian words and text

I did this little program to make it easier for myself (and now others) to search things among the known words/sources of Phyrexian.

In case you want to search for english words and get how to write them in phyrexian, there is the "Search English" function, but the best way to do it is checking out u/Frigorifico's [Phyrexian Dictionary](https://drive.google.com/drive/folders/1kXaIX-GNYtO6dFScdkkoMgnCyzVGrTh2). We still don't know enough words to translate many of the sentences asked in Reddit, but if you get creative you can say quite a lot.

Only tested in Windows 10, please let me know if you have problems running it.

## What files to use
To initiate, there are two options:

To run the program without python, just run 'phyrexian_search_engine.exe'. This still requires the .tsv files and fonts, but no extra installations.

To run it with python, run "phyrexian_search_engine.py"(made on **Python 3.7**, requires **pyglet** and **PySimpleGUI** packages). This method doesn't need the .exe file, so you can delete it to save some space.

The 'phrx_words.tsv' and 'phrx_raw.tsv' contain the transliterations for all searcheable words and source texts (as of March 2022).

## Usage
To search for words in Phyrexian, either click on the buttons to form your query or add to it by inputting text in transliterated Phyrexian. Attention, the program will handle things badly in case you try to use characters other than the ones in Phyrexian transliteration (I'm using the [Phyrexian Transliteration Chart v2.1 by u/Aldurethar](https://www.reddit.com/r/magicTCG/comments/nre288/an_update_for_the_new_phyrexian_transcription/), but without differentiating between X and Z. It's all Z here).

You can choose to include vowels and diacritics in your search or not. For example, the english words 'cap', 'cop' and 'cup' would be the same if you didn't include the vowels. This is especially important because Phyrexian is believed to be a consonantal root language, so the same word can be conjugated by changing its vowels. Not including diacritics will give you many false matches, but this feature is here to make up for poor clarity in some sources that makes some diacritics very dubious.

Once you have a result, you will see a popup window with two sections: a first showing any known word (at least the ones I'm quite certain of) that matches to your query, then a list of every instance from every official and accurate source of Phyrexian taht matches to your query. This means that known words will have duplicates in the second section.

You can also choose which font to use, including my own and three others from the community. Thank you u/Aldurethar for helping me find these.

An alternative way to use the Engine is trying to search for English terms with "Search English". Only exact matches will give results (so watch out for typos) and be aware that some words are not written in the Engine exactly like their translations. For example, "Upkeep" appears as "Step" and "Destroyer" as "Destroy". This was made to more accurately represent the roots of words, so if you want proper translations for every term check out the Phyrexian Dictionary.

## Disclaimers
What I mean by "official and accurate" Phyrexian sources is that they were released by WotC and are written in the Phyrexian language. For example, fan-made phyrexian text might be accurate but not official, and [the Phyrexian Wurmcoil Engine](https://www.reddit.com/r/PhyrexianLanguage/comments/ny0n2g/from_a_wotc_survey_dont_know_if_its_been_analyzed/) is official but not accurate (english words are phonetically written using phyrexian characters).

The English-to-Phyrexian relations are based on my own notes, so may differ from other sources like the wiki, the Pyrexian Dictionary, or reddit posts. There are some notable abscences from lines in the set trailers, which still don't have a solid word to word translation in my opinion. At least all texts with known or unknown translations are included in the raw search.

I personally transliterated all known Phyrexian texts because I had already found some mistakes in [u/Aldurethar's transliterations](https://www.reddit.com/r/magicTCG/comments/oj2ahk/a_full_transliteration_of_all_known_phyrexian/) and there were new sources released/found since then. I double checked with his transliteration and my only sources of doubt now are in the All Will be One and New Phyrexia trailers because of the bad video resolution.

Three wonderful fonts are included besides my own: [Progress Engine font by u/GuruJ_](https://www.reddit.com/r/magicTCG/comments/nqwqhn/first_release_of_progress_engine_font/)(see the [updated 1.1 version](https://www.reddit.com/r/PhyrexianLanguage/comments/sye8sf/updated_progressengine_font_v11_now_with_quote/) too), [Horizontal Gibberish by @PhieOrDie](https://twitter.com/PhieOrDie/status/1492591720952999946?cxt=HHwWlMC9oeOQ4LYpAAAA), and Phyrexian Engraved by u/Aldurethar (not released publicly and looks off because I haven't managed to integrate ligatures yet, but simple and amazing because it needs no adaptation from the transliteration chart). I made my own (which I called the Phyrexian Compleat font) because some characters were missing and I wanted something more legible from afar.

I plan on adding a way to change the window theme (colors), but for now please search the script for "sg.theme" and change 'DarkAmber' for [any of PySimpleGUI's themes](https://media.geeksforgeeks.org/wp-content/uploads/20200511200254/f19.jpg) (will not work with the executable).

Translating Phyrexian is a community effort and everyone that tries to discover more is stepping on the shoulders of giants. [The Phyrexian Language page in the MtG wiki](https://mtg.fandom.com/wiki/Phyrexian_(language)) page is a great place to start, but also please check out all the wonderful people at [r/PhyrexianLanguage](https://www.reddit.com/r/PhyrexianLanguage/), HiglyEntropicMind's youtube series [Deciphering Phyrexian](https://www.youtube.com/watch?v=NsINwVt7fgY&list=PLunDPaoIqC7swE6n_jWJjjQYIkLm29McE) and it's [Discord server](https://discord.gg/6nu8PTEAVc).
