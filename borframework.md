# Borframework - BrailleOrch Software Development Framework

By Hu Haipeng

Opening Date: Jan 31, 2016  
First draft: Feb 26, 2016  
Last updated: May 22, 2018  
Project designer: [Hu Haipeng](mailto:hhpcomposer@gmail.com)  

Copyright (C) 2016-2018 By Hu Haipeng

**********

# Contents

Preliminary Materials

- [A. Purpose](#purpose)
- [B. About This Framework](#framework)
- [C. The BrailleOrch Format, Why And How To](#formats)
- [D. Braille Music Notation Codebooks Used In This Development](#codebooks)
- [E. Capabilities The Software Must Reach](#capability)
- [F. Development Requirements](#requirements)
- [G. Working Progress](#progress)

Part I: General Overview Of The Software

- [Chapter 1: Menus Overview](#menus)
- [1.1 File](#1-1)
- [1.2 Edit](#1-2)
- [1.3 View](#1-3)  
- [1.4 Navigation](#1-4)
- [1.5 Transcription](#1-5)
- [1.6 Braille Music](#1-6)
- [1.7 Playback](#1-7)
- [1.8 Options](#1-8)
- [1.9 Window](#1-9)
- [1.10 Help](#1-10)
- [Chapter 2: Deeper View Of Transcription Functions](#transcription)
- [2.1 Transcription Dialog](#2-1)
- [2.2 Transpose Dialog](#2-2)
- [2.3 Score Management Dialog](#2-3)
- [2.4 Part Management Dialog](#2-4)
- [2.5 Text Management Dialog](#2-5)
- [2.6 Lyrics Management Dialog](#2-6)
- [2.7 Chords Dialog](#2-7)
- [2.8 Metronome Dialog](#2-8)
- [2.9 Percussion Dialog](#2-9)
- [Chapter 3: Settings Dialog](#settings)
- [3.1 General Page](#3-1)
- [3.2 Transcription Page](#3-2)
- [3.3 Single-line Page](#3-3)
- [3.4 Bar-over-bar Page](#3-4)
- [3.5 Line-over-line Page](#3-5)
- [3.6 Section-by-section Page](#3-6)
- [3.7 BrailleOrch Format Page](#3-7)

Part II: General References Of Important Points

- [Chapter 4: Development Phases](#phases)
- [4.1 First Phase](#4-1)
- [4.2 Second Phase](#4-2)
- [4.3 Third Phase](#4-3)
- [4.4 Fourth Phase](#4-4)
- [4.5 Last Phase](#4-5)
- [Chapter 5: BMML Enhancements](#bmml)
- [5.1 Limited Learning Resources](5-1)
- [5.2 Implementation Steps](#5-2)
- [5.3 Flows](#5-3)
- [Chapter 6: Braille Music Transcription Specified Points](#braille)
- [6.1 Braille Window](#6-1)
- [6.2 Navigation In The Score](#6-2)
- [6.3 MusicXML Related](#6-3)
- [6.4 Transcription Related](#6-4)
- [Chapter 7: Braille Music Editing, Correction And Other Advanced Features](#advanced)
- [7.1 GUI Specifications](#7-1)
- [7.2 Entering And Marking Items, Transcription Related](#7-2)
- [7.3 Keyboard Style](#7-3)
- [7.3.1 The Keyboard Options Dialog](7-3-1)
- [7.3.2 Other Contextual Items](7-3-2)
- [7.4 Percussion Problems](#7-4)
- [7.5 Split And Merge](#7-5)
- [7.5.1 Split Dialog](#7-5-1)
- [7.5.2 Merge Dialog](#7-5-2)
- [7.5.3 Merge Non-splitted Files](#7-5-3)
- [7.6 Debugging Mode](#7-6)
- [7.7 Define New Features](#7-7)
- [7.8 The Play-along Function](#7-8)
- [Contact Information](#contact)

**********

# Preliminary Materials

<h2 id="purpose">A. Purpose</h2>

This is a detailed framework of BrailleOrch, braille music transcription software for advanced formatting and publishing purpose. The final software will convert [Musicxml](http://www.musicxml.org) files, or via a separate plugin, Sibelius files, into our extended Braille Music Markup Language (BMML) format (originally created, developed and copyrighted by [Veia Progetti s.r.l.](http://www.veia.it), Italy, as free software. See copyright information in the BMML package for details), which can be flexibly edited and modified, to fulfill most of the requirements of braille music publishment.

Currently, most of the braille music transcription services still prefer to use traditional manual method to transcribe print music into braille, which is both expensive and time consuming. Although there are some free and commercial softwares available for braille music transcription, they are not accepted by transcribers due to their various limitations. What's more, although composers and mainstream music publishers use notation softwares, they are not willing to provide their source files out of office in case of copyright infringement. So it's very difficult to find high-quality original notation sources for authentic transcription. Our goal is to develop a software which makes braille music transcription as easy and smart as possible, and solves copyright problems, building a bridge between composers/publishers and braille music transcribers, and paving the last one kilometer of the way for blind musicians to easily access music scores like sighted people.

**********

<h2 id="framework">B. About This Framework</h2>

This comprehensive document will describe all menus and functions of BrailleOrch software. People who wants to develop/enhance the software must read it carefully. The whole framework is divided into seven chapters. The first three chapters give a general overview of the software's menus and functions, and the remaining four chapters give detailed working progress information, development designs of improving BMML and Musicxml-to-braille transcription, and advanced braille music editing and management functions. More in-depth issues will be discussed in a future mailinglist or forum during the development process. Only very critical issues needed to be done are shown here. For detailed rules of braille and braille music, please always consult the [codebooks](#codebooks) mentioned below.

A note on the reading convention of braille dot number indications: Dots within a single cell are number combinations, and dots in separate cells are separated by commas. For example, a right-hand prefix is dots 46,345, a large value sign is dots 45,126,2.

**********

<h2 id="formats">C. The BrailleOrch Format, Why And How To</h2>

This software is based on a format which will either use and extend the  existing BMML, or create a new descriptive format. Most of the current braille music transcription softwares only output pure braille code in either ASCII or Unicode form. The disadvantage of this way is, there are no flexible formatting and editing possibilities available. Transcribers must do all adjustments manually, and they prefer to use totally manual method to transcribe the whole music. Moreover, different countries have different formatting rules from the same source, so one kind of output can't fulfill all requirements. Therefore, a descriptive format is needed. It it will ease the publishing process, leaving less effort to the transcribers, saving their time and energy, and eventually reduce the cost of transcription. Currently, I resume we'll develop the software based on BMML. If we decide to create a new format, I'll open a new document about that.

BrailleOrch (.bor) format is a compressed file. It contains original musicxml (if transcribed from musicxml) and bmml sources, and additional debugging information such as error records. When the final editing and correction has been finished, the musicxml source and most debugging information can be removed to save file size. People can still edit and reformat braille output, though. See Make final document in [File Menu](#1-1).

For BMML format, I think we should design two stages.  
The one is the current format, and we can just extend it to include more signs and functions. This kind of BMML file contains both musical and braille information.  
The second one is a BMML file which is just a mapped format from Musicxml, and is ready for braille transcription. Music publishers can first generate such an intermediate file for transcribers or end users, and the braille users can check and format music with their own preferences. This format can be developed later, since it needs very smart on-the-fly formatting. and previewing functions of the software. This format is inspired by Sunshine professional, a Chinese braille translation software made by China Braille Publishing House. The wording, hyphening and formatting are constantly changed while the user is editing the file, like MS Word, and this interface is very friendly and smart.  

**********

<h2 id="codebooks">D. Braille Music Notation Codebooks Used In This Development</h2>

Braille music code used by BrailleOrch is based on New International Manual Of Braille Music Notation (NIM) published in 1996 in Switzerland. You can download a MS Word version [here](http://www.rnib.org.uk/sites/default/files/New%20International%20Manual.doc) from RNIB, and a zipped braille version which contains both Grades 1 and 2 English braille editions [here](https://www.sbs.ch/fileadmin//documents/musik/sy_engl.zip) from the original publisher SBS. This manual is just a brief introduction to all available signs. For detailed rules, some additional features and symbols, it's highly recommended to consult the newer Music Braille Code 2015 published in The US. You can download the 2015 American code as both PDF and Braille formats [here](http://www.brailleauthority.org/music/music.html). Since this book is mainly used by American countries, the format may be slightly different, especially the braille version, which is written using Unified English Braille. So the New International Manual should always be the first reference when there are any conflicts. In future development, we can implement both codebooks to output both formats via the users' choice.

Literary braille transcription can be considered later, because we rely on the automatic transcription package [Liblouis](http://www.liblouis.org). There's only one exception, Chinese braille used in the main continent other than Hongkong and Taiwan. It needs additional complex wording and toning rules, so there must be a  separate development in the future. (The Zh-chn table is currently under check, and we hope it will appear in the next release of Liblouis. Then this exception can be removed, and we only need to do some implementations for Chinese texts within music context.)

**********

<h2 id="capability">E. Capabilities The Software Must Reach</h2>

- Convert Musicxml files directly into well-formatted braille music scorres, leaving few post-editing effort to the users;
- Transcribe all kinds of music from instrumental and vocal solo to complicated symphonic and dramatic works;
- Brief and clear description of music objects via screen readers while navigating;
- Flexible playback functions, including a smart [play-along](#7-8) mode, to enhance the learning speed for blind musicians;
- Powerful and flexible editing and formatting ability for both blind users and sighted transcribers;
- Support bar-over-bar, line-over-line, section-by-section and customized BrailleOrch formats, to fit most countries' braille music publishing standards;
- Support transposition, part extraction etc, producing various editions from one document;
- Support multiple language braille output with the help of [Liblouis](http://www.liblouis.org) translation tables;
- Smart copy protection mechanism for music publishers to work with braille music transcribers;
- Two-sided xml integration for developers to enhance transcription quality;
- Powerful debugging mode for dealing with Musicxml with problems or non-standard elements;
- Support user-defined new symbols and features, to let the software keep up with the latest music and Musicxml techniques

**********

<h2 id="requirements">F. Development Requirements</h2>

An experienced C++ or Python skill plus XML knowledge is required for developing this software. C++ can process large XML files fast, but Python or other advanced languages can make programing easier. We have to decide what programing language or language combination should be used. A basic Git knowledge is required for committing changes. Knowledge of music, musicxml, braille and/or braille music is recommended, which will largely enhance the efficiency and quality of development. Sibelius Reference is required for learning some notation, selection and advanced functions which can be borrowed. Sibelius Manuscript Language is required if anyone who wants to make a BrailleOrch export plugin for Sibelius (see the fifth phase in [the next section](#progress)). Some items in Sibelius can't be correctly exported into musicxml via its internal export function and/or Dolet For Sibelius plugin.

The software must be accessible via keyboard and screen readers in all of its parts. Every menu and toolbar item, every music object name and all messages must be put in plain text files to make it possible to add more language support in the future. The initial languages are English and simplified Chinese (if developed by Chinese programmers).

Besides general components for software development, we also need the following:

- A screen reader such as [NVDA](http://www.nvaccess.org) for accessibility test  
- [Liblouis](http://www.liblouis.org) for multilingual braille translation  
- Plenty of Musicxml, BMML and plain braille music resources, which I can provide during the development

The software will run under any Microsoft Windows systems, from Windows 2000/XP to Windows 10, both 32 and 64 bits. A screen reader such as [NVDA](http://www.nvaccess.org) is required for announcing unicode braille objects. Music publishers and sighted braille transcribers are not asked for this option.

**********

<h2 id="progress">G. Working Progress</h2>

Since this is an extensive project for a highly sophisticated software, we have to divide the development session into several phases. Below is an overview of every phase. For detailed points on every phase, please read [Chapter 4](#phases).

The first phase is to build up a general GUI, containing basic menus and functions. Use original BMML source and extend it. Map most Musicxml elements except visual layout to BMML, create coresponding braille symbol elements, and define rules for transcription. Basic functions in Page setup, Score/Part/Text/Lyrics/Chords/Metronome/Percussion management and Transcription dialogs should be done. Bar-over-bar and line-over-line formats are firstly considered, also my special BrailleOrch format is OK. The result braille music score can represent at least 95% information of print version. The  score can be manually edited, but not reformatted and retagged automatically, since this requires deeper research of BMML and further development of the software. The user-edited strings are gray-colored, and simply marked as "other" in BMML, and can be tagged in future versions of the software.

The second phase is to enhance transcription quality. Items in Musicxml 3.1 or later should be added, and the formatting function must be more flexible. Add [Define New Features](#7-7) function. Add section-by-section format. Enhance translation table to add support to Chinese Mandarin braille (Cantonese and Taiwanese Chinese braille have already been done in Liblouis).

The third phase is to enhance the reformatting function. The software can recognize most user-entered strings as music signs, texts etc, and can correctly break lines when reformatted.

The fourth phase is to develop the Play-along function described in the last chapter. This will ease braille music reading, and enhance the learning progress and quality for blind musicians.

The fifth phase is to develop a Sibelius plug-in, directly exporting .bor files from Sibelius. Musicxml exported from Sibelius has some information missing, because there are special user items. We can use Manuscript Language to make the braille version more close to the original. Unspecified items can also be exported and tagged for manual editing. BMML exported from this plugin may not correctly formatted, so this tool has to be delayed to the time BrailleOrch is powerful and flexible enough.

The last phase is to develop the braille music composing function. Since the software can already recognize common braille music signs entered, the main focus is on advanced signs, creating parts and groups, writing chord symbols, handling visual appearance, Midi functions etc.

**********

# Part I: General Overview Of The Software

The three sections below will give a very brief view of the software. Some items may contain detailed description, while others will be directed to corresponding topics in Part II.

<h2 id="menus">Chapter 1: Menus Overview</h2>

This chapter describes all menus and submenus. It gives us a brief view of the major functions of BrailleOrch.

<h3 id="1-1">1.1 File</h3>

New  
To create a new BMML document. This will not be considered currently, unless we decide to develop braille music composing side. Braille Music Editor 2 from [Veia Progetti](http://www.veia.it) can do a intermediate level work of it, and blind musicians can now use ABC, Lilypond and Sibelius to produce print music scores. So our main goal is to develop a transcription software.

Open  
Open a BMML file (.bmml), both original Veia version and our extended new version. Our new version contains more information and functions, so for portability purpose, it will be a compressed xml file with the extension .bor. Another kind of unprocessed .bor file can also be opened, see Import below.  

Open recent  
A list of recent created/opened files. Number of files can be set or cleared in [Settings dialog](#settings).

Save  
Save the current BMML file in either BMML or Bor format. The BMML format is not an old version of BMML, but an uncompressed Bor file. This can be used for researching the format to help developers get familiar with BMML. Note: the uncompressed BMML file will not contain any original Musicxml sources from which the file is transcribed.

Save As  
Save the file using a different name or to a different location, in either BMML or Bor format.

Versioning (submenu)  
Save Version  
open Version  
Versioning function is for further comparison of the score. The version files will be saved using .bor format, with a time/date stamp after the extension. E.G., foo.bor~01312016.  
Saving an earlier version will bring up a dialog, asking whether you want to save a new version or overwrite the current non-version file.

Split  
Merge  
The above two menus will open dialogs for transcribers to control voluming of the book or work with colleagues on the same book. This idea is taken from both music notation and literary braille translation softwares. Please see [section 7.4](#7-4) for details.

Set copy protection  
This is a special function for protecting music pubisher's copyright. After they convert their scores into musicxml and import into BrailleOrch, they can immediately set this option. The braille score can still be edited, reformatted and embossed, but can't be exported into musicxml for back-translation. The file is also encrypted, so it also can't be saved as bmml format. Any debugging process upon the xml source and bmml score can, however, be done using the internal [debugging](#7-6) interface.  
Be careful to use this function, since it's not reversable. We should provide two times of verification dialog for this. Another possibility is, we can toggle this item visible and invisible in the [Settings dialog](#settings), to prevent accidental operation by common users.

Make final document  
Be careful to use it like Set copy protection. This will remove musicxml source and most debugging information from the file. So don't use it before the final correction of braille music is done, especially when there are still many errors. As I said before, the metadata will be protected using Set copy protection function, so the protected musicxml source can't be extracted. So don't worry about the source. After making the final document, people can still edit and reformat braille music score, but can't debug and make enhancement of the software.

Close  
Close All  
Close the current working document(s).

Import  
Import Musicxml files, from version 1.0 to the latest version, both compressed (.mxl) and uncompressed (.xml and .musicxml). The transcription process will begin, see [Transcription dialog](#2-1) for details.  
Import ASCII/unicode braille file, making ASCII2Unicode or vice versa conversion according to chosen braille table. This will not automatically generate a BMML format, but just storing and converting original data. This way, the .bor file is just a compressed version of original source. When we decide to develop braille music composing side, this situation will be changed.  
Importing MIDI file will also be considered in the future.

Export  
Export MIDI and Musicxml formats will be considered later.  
Export to unicode or ASCII braille. This is the current function. When exporting to ASCII, an option dialog will appear for choosing a braille table. Different country uses different braille mapping table.

Page setup  
Settings for braille pages.  
In this dialog:  
Lines per page: line amount spin editbox, default 25  
Cells per page: Cell amount spin editbox, default 32  
Adding form feeds: checkbox for inserting form feeds. Default checked  
Print page numbers: output printing page numbers. Default checked  
Print page number position: combo box, topleft, topright, bottomleft and bottomright. Default topleft  
Braille page numbers: output braille page numbers. Default checked  
Braille page number position: combo box, topleft, topright, bottomleft and bottomright. Default topright  
When these two positions get conflicted, a warning message will appear, asking the user to adjust the position correctly.  
Show page turn: checkbox, visible when Print page numbers is checked. Page turn includes dots 5,25 with (or without) new page number.  
Page turn format: combo box. Choices are: within music, above music, within music without page number.

Emboss  
Emboss braille music scores using installed braille embosser drivers.

Exit  
Quit the software.

**********

<h3 id="1-2">1.2 Edit</h3>

Undo  
Undo the previous operations.

Redo    
Redo undone operations.

Undo history  
A 128-step history list, to choose an undo item to roll back or forward.

Select all  
Select all items.

Special selection (submenu)  
Set begin of selection block (F5)  
Set end of selection block (F6)  
Set from begin to current location (F7)  
Select from current location to end (F8)  
Select line (F9) (current print line of current part, from beginning to end measures)  
Select part (F9) (current part, for whole piece/movement)  
select staff (F10) (current braille staff)  
Select system (F12) (current braille system. System means a whole group of staves, showing all instruments and voices playing simultaneously.)  
Remove selection (F4) (remove the current selection. The selection will not be removed if this is pressed, or a new selection block is made.)

Cut/Copy/Paste/Delete  
Cut/copy/paste/delete selection.

Cut/Copy/Paste/Delete part/voice/measure/measure of the system  
The same cut/copy/paste/delete function for curent location or selection, but deal with different items.

Search/replace  
Common search/replace functions.  
However, there's an checkbox to switch on "searching for texts", which switches of unicode braille input (fsd for dots 123, jkl for 456), and directly search within the xml sources for standard texts, including dynamics and any text-based values. The result will bring the cursor to correct braille location.

**********

<h3 id="1-3">1.3 View</h3>

The common view menu for sighted users. It includes simple view options such as zooming, visibility of toolbar, and braille reading modes etc.  
Braille reading mode will give us options to choose white-screen-black-dots or black-screen-white/blue/green-dots.

**********

<h3 id="1-4">1.4 Navigation</h3>

Besides common arrow navigations of individual braille cells or lines, there are some special functions.

Next note (tab)  
Previous note (shift+tab)  
Next beat (alt+right)  
Previous beat (alt+left)  
Next measure (ctrl+right)  
Previous measure (ctrl+left)  
Next voice (win+right)  
Previous voice (win+left)  
Next part in the same measure (ctrl+down)  
Previous part in the same measure (ctrl+up)  
Next print line (alt+down)  
Previous print line (alt+up)  
Next braille system (win+down)  
Previous braille system (win+up)  
Next print system (ctrl+win+down)  
Previous print system (ctrl+win+up)  
Next braille page (pgdn)  
Previous braille page (pgup)  
Next print page (ctrl+pgdn)  
Previous print page (ctrl+pgup)  
Begin of current braille page (home)  
End of current braille page (end)  
Begin of current system (alt+home)  
End of current system (alt+end)  
Begin of file (ctrl+home)  
End of file (ctrl+end)

Go to measure/part  
Enter measure and part numbers. If measure number is left empty, then stay in the current measure; ff part number is left empty, then bring to the first part of the measure.

Go to selection (submenu)  
Go to begin of selection (ctrl+F5)  
Go to end of selection (Ctrl+F6)

**********

<h3 id="1-5">1.5 Transcription</h3>

This menu handles various transcription functions.

Transcribe  
This is a manual action of transcription. If the user wants to start from fresh beginning to undo all previous modification, or after debugging problematic musicxml file, this will start a new transcription session. The [Transcription dialog](#2-1) will or will not appear according to settings in the dialog or [Settings dialog](#settings).

Format (submenu)  
Bar-over-bar (default)  
Line-over-line  
Section-by-section  
Brailleorch  
These 4 options will change the current format of score. The formatting will be done according to settings in [Settings dialog](#settings). We highly recommend users to set their preferred formats as default in the [Settings dialog](#settings), to reduce any messy formatting problems.  
All detailed options for these formats can be found and will be discussed in the [Settings Dialog](#settings) section.  
For single-staff instrument solo, the above will be unavailable, and settings for [single-line format](#3-3) will be applied. See corresponding settings in [Settings dialog](#settings) for details.

Format  
Format or reformat the braille score after manual editing and correction. Formatting layout will follow rules set in Score/Part/Text/Lyrics/Chords/Metronome/Percussion, Options and Page setup dialogs. Options changed after transcription process can also be applied.

Debugging mode  
A special mode used for checking errors and enhancing the software. See [Debugging Mode](#7-6) for details.

Output interval direction description  
A dialog appears, letting you to view the description. There are 2 kinds of description:  
1\. When all intervals are up/down, it will let you choose from two methods of descriptions:  
a. Literary: All intervals are read upwards/downwards;  
b. Notation: a C with second interval sign, space, two dots 35's, space, two notes with in-accord, either C-D or C-B.  
2\. When different intervals are used, it will show as:  
All intervals are read upwards/downwards, except blah blah, which is/are read downwards/upwards.

Output part list  
See this item in [Part management dialog](#2-4) for details.

Extract parts  
Extract parts for players/singers. A dialog appears, letting you check part(s) to extract. New .bor documents with only bmml sources for individual parts will be created. You can change the order of parts, or choose whether to extract parts as individual files or just one file shwing parts one by one. If "combine individual parts" is checked, the result file will generate a full score containing selected parts (this is useful for publishing choir-with-orchestra scores containing choir parts only).

Combine parts to score  
A reversed operation of part extraction. A dialog appears, letting you add files and adjust their order. But the files must be the whole parts of the same piece, otherwise BrailleOrch will refuse to go ahead. BrailleOrch will first check the coincidence of time signatures and measures among all parts, and shows a warning message telling which file(s) are unmatched. BrailleOrch will check coincidence according to the topmost file.

**********

<h3 id="1-6">1.6 Braille Music</h3>

This menu gives us several functions of editing and correcting braille music score. Some are very sophisticated functions.  
This menu will be modified and extended when we decide to develop braille music composing function.

Insert (submenu)  
Insert music (n)  
Enter notes/rests/voices, generally all music-related signs.  
Insert texts (x)  
Enter texts using standard input method. Untranslated unicode texts such as Chinese will be accepted, and can be edited later. All text-related adjustment can be done in [Text management dialog](#2-5).  
Insert braille file (shift+f)
Insert a .brf file, then the software saves all braille ASCII to braille dots inormation. This is useful when inserting long document in music, while the text is translated by software like Duxbury Braille Translator (commercial) or (free) BrailleBlaster. You can choose whether to maintain page information like form feeds. It's better to disable braille page numbers when translating texts in such softwares.  
Insert key signature (shift+k) (to solve conflict with braille key)  
Insert time signature (t)  
These two use braille input.  
Insert chord names and figured bass (c)  
Braille input of chord and figure symbols.  
Insert title page information (i)  
Insert title info at top of system. See [Score management dialog](#2-3) for details.  
There's a checkbox for inserting title information on a blank page. If checked, a blank page will be created.  
Insert footnotes (o)  
Add a line of dots 25's plus footnotes.  
Insert division signs (v)  
Centered 12 division characters. Choose from dots 25's and dot 5's.  
Insert new print page (shift+p)  
Insert new braille page (shift+b)  
These are for modification and/or reformatting, or when no print pages are available in musicxml 1.0. Also useful when developing braille music composing. Print page will be inserted at the beginning of the measure, while braille page will be inserted at the beginning of the current braille line.  
Insert splt point (shift+s)  
Put a split point under current location. The point must be at the beginning of a braille system or section, including measure number. If the current location is not suitable, the software will try to find a correct location and bring the cursor there for you to confirm. For splitting and merging function, please see [section 7.4](#7-4) for details.  
Set current measure number (m)  
Set number of current measure, overriding measure numbering in Musicxml. The consequent measure numbers will be changed accordingly, until Musicxml specifies a new sequence of measure numbers (e.g., starting a new movement from measure 1 or 0).  
Set current braille page (b)  
Set current braille page number. The extra choices for numbering are arabic, roman, lower-celled and (for title pages) none.  
Set current print page (p)  
Set current print page number, overriding Musicxml's settings. The extra choices are arabic, roman and none.

Other insertion of music objects may be implemented later. Other tags and properties can be marked using context menu directly on braille objects. Transcribers can also edit the score without using the above insert and context functions, but the result input will be marked as "other" in BMML, and can't be automatically reformatted correctly. They should be manually formatted.

Show/hide objects  
This dialog determines whether to show or hide hidden objects in Musicxml, or force some objects hidden in braille for other purposes. Hidden objects in Musicxml may be useful in braille. For example, a hidden note may be used to indicate the destination of a glissando line; a tuplet with both number and bracket set to "no" is often used in unmeasured music or a mathematically scaled passage where the time signature of some instruments may be different from others (e.g., in a 4/4 passage with staves in 12/8, the 12/8 parts have to be written as lots of tripllets of eighths with tullet numbers and brackets turned off). sometimes the hidden objects are only for layouting purpose, e.g., for placing a symbol, and unwanted in braille. So we can implement this option to show/hide such items contextually or globally.  
The dialog has two radio buttons for show (default) or hide, and a checkbox to set globally. Once an item is hidden, the "set globally" checkbox will be unchecked, unless you set all hidden globally, and vice versa. In the future, we should implement more sophisticated filtering capability to make show/hide function apply to certain kind of objects contextually or globally.  
Note that when showing hidden rests, accidentals, tuplets and texts, there must be a dot 5 before them. Normally hidden rests must be shown to fill the bar length, but sometimes they are also unnecessary.

Show/hide current part name  
This is a contextual version of show/hide part name function in [Part Management Dialog](#2-4). It only show/hide current part name througrout the music, unless you put the cursor right on the part name, which will be hidden only once.

Display images  
This menu is for extracting pictures contained in compressed Musicxml files (.mxl), which may be cover page images or special music symbols not being able to enter in notation programs. The listbox describes the details of every image (usually .svg files) as this:  
filename, part number, staff number, bar number, and beat position.  
Press View to read the image on screen, and press OK to bring the cursor to the location for transcribers to enter appropriate braille symbols. Press Define to define a symbol globally in this score. See [Define New Features](#7-7) for details.

Transpose  
This dialog will handle score/parts transposition. See [corresponding section](#2-2) for details.

Symbol conversion  
This dialog will be imllemented later. Sometimes the same text or symbol indications in different music cootext may have different meanings. For examlle, a Roman oukber may mean either string or position nukber, or a harmony indication; a plus sign may mean either horn stop or left hand pizzicato.  
The dialog may have two listboxes. The first Lists out parts, and the second lists out texts or symbols (determined by radio buttons above the boxes) in that part. To modify braille indication of an item, press F2 on it and input braille. The button below the boxes can set the current item globally to all parts. 

Score management  
A tool for managing various items such as page/measure numbering, movement divisions etc for the whole score or selected block. See [corresponding section](#2-3) for details.

Part management  
A very powerful tool for managing part names and grouping properties in the score. See [corresponding section](#2-4) for details.

Text management  
A very powerful tool for managing various text items in the score. See [corresponding section](#2-5) for details.

Lyrics management  
A tool for managing lyrics in the score. See [corresponding section](#2-6) for details.

Chords management  
A tool for modifying chord symbols. See [coresponding section](#2-7) for details.

Metronome management  
A tool to manage metronome marks in the score. See [corresponding section](#2-8) for details.

Defining percussion notes  
A tool for reprocessing percussion or drum staves. see [corresponding section](#2-9) for details.

**********

<h3 id="1-7">1.7 Playback</h3>

Play/stop (ctrl+l)  
Play current measure (shift+l)  
Play current part (ctrl+;)  
Play current voice (shift+;)  
Play metronome (default unchecked)  
Enter Play-along mode: ctrl+alt+l  
(See [Section 7.7](#7-8) for Play-along descriptions)

Choose Midi instruments  
List out all parts and their midi instruments. Assign button will bring up a dialog containing a 128-line list of GM instruments. By default, BrailleOrch will assign correct instruments according to settings in Musicxml.  
BrailleOrch should be able to use multiple instances of GM modules to handle more than 16 parts.

Play sounds when navigating (default checked)  
Whether to play MIDI sounds during cursor navigation. Default: checked.

Playback device  
Choose from available sound devices for Midi playback.

**********

<h3 id="1-8">1.8 Options</h3>

Settings  
Comprehensive settings dialog. Discussed in [separate chapter](#settings).

Announce modes (submenu)  
silent  
Braille only  
Objects only  
Braille and objects (default)  
Determine how the screen reader will read the score while navigating.  
Generally, Braille will announce things like "5, 1 4 5" etc, and Object will announce "fourth octave, C eighth" etc. Detailed indications for specified items may be discussed while developing.

**********

<h3 id="1-9">1.9 Window</h3>

Standard window menu, such as tile, cascade etc.

**********

<h3 id="1-10">1.10 Help</h3>

About  
User manual (F1)  
Software website  
Check for updates

**********

<h2 id="transcription">Chapter 2: Deeper View Of Transcription Functions</h2>

This is the core of the software, so please be careful to read it. For knowledge of braille music, please consult the [New International Manual Of Braille Music Notation (SBS, 1996)](http://www.rnib.org.uk/sites/default/files/New%20International%20Manual.doc) and [Music Braille Code 2015 (BANA)](http://www.brailleauthority.org/music/music.html). The latter contains more information about different formats used in braille music, and also some extra signs. For critical issues which must be considered during development, please chapters [5](#bmml) and [6](#braille).

The software will treat score with only one part with one staff as single-line format. It will automatically treat score with only one part with two to four staves as piano (or organ, chosen by the user) format. It will treat score with one single-line part above one multi-stave part as solo with keyboard accompaniment part, and add dots 5,345 prefix before the single-line part.

<h3 id="2-1">2.1 Transcription Dialog</h3>

Note: All dialogs in this software have "ok" and "cancel" buttons.

When importing a Musicxml file, the software brings up a dialog, giving the users options for adjusting transcription appearance. It can be turned off by checking "Don't show this dialog again" at the bottom of the dialog, or via [Settings dialog](#settings). The last settings will be stored, and users can override these options in [Settings dialog](#settings). The Transcription dialog also contains lots of buttons to bring up corresponding options in that dialog.

Presets  
This popup menu contains a list of default presets for commonly used transcription styles I prepared, e.g., North America, UK, Europe, Asia, etc. Users can also save their current settings as a custom preset for future use. The saved presets will automatically appear at the "user presets" submenu. There are of course commands for load (manually choose a preset file which is not located at the default place) and save (a save file dialog).

Transcribe without formatting  
This checkbox will generate a non-formatted braille score, disregarding all settings. This kind of bmml file only has musicxml-mirrored objects, no braille formatting indications are included. Users can edit the score and then use Format in [Transcription menu](#1-5).  
This must be reserved for future use when we develop the second phase of BMML.

Braille score format (radio button)  
bar-over-bar, line-over-line, section-by-section and BrailleOrch. Default is bar-over-bar.  
When one format is chosen, the corresponding option button will be shown, bringing user to corresponding items in [Settings dialog](#settings).

Page setup  
Brings up Page setup dialog in [File menu](#1-1).

Starting braille page  
Starting print page  
Starting measure number  
These 3 edit boxes let the user fill in specific numbers overriding musicxml's values and default braille transcription settings.

Score/Part/Text/Lyrics/Chords/metronome/Percussion management  
Bring up corresponding dialogs which are also available in [Braille Music menu](#1-6).

Transcription settings  
Bring up [Transcription settings](#3-2) in [Settings dialog](#settings).

Translation table  
Used for text translation. This can also be seen in Options and Score/Part/Text/Lyrics/Chords management dialogs.

Don't show this dialog (default unchecked)  
Disable this dialog, using options previously set.

**********

<h3 id="2-2">2.2 Transpose Dialog</h3>

Transpose (radio button)  
Display original transposition (default)  
Display in concert pitch  
Transpose the whole score (display a combo box for transposing the score in half steps, both plus and minus values are available. The max value is +/-24.)  
Transpose parts (display a list of all parts with checkboxes, and a combo box for transposition. The combo box will only take effect on checked parts.)

When transposed, the BMML must leave a record of the original key. So if we come back to the original key by selecting the first option, all parts can be rolled back to their original keys immediately, with correct enharmonics of pitch.

**********

<h3 id="2-3">2.3 Score Management Dialog</h3>

Description of the score  
This is a read-only text box, showing summary of the score. Available items are: general header, individual headers (headers with their starting print/braille pages), number of print/braille pages, number of measures and parts, page format, score format (single-line, bar-over-bar, line-over-line, section-by-section and BrailleOrch).

Running header: some countries have running headers at the top of page. A general header of the book can be set here. Some books use different header on different piece. This can be done by specifying individual headers using context menu within the score, and will override the general header.

Title/Subtitle/Composer/Lyricist/Copyright/Other  
These edit boxes will be automatically filled in if they can be retrieved from Musicxml source. Otherwise the user can enter them here, and the braille will be automatically generated and formatted. User can also insert them form Insert title page information dialog under Input submenu of Braille Music menu. If entered as braille manually, they can also be tagged later using context menu. The result braille can be copied/cut/pasted freely on the page.

Table of contents dialog  
This can be written in the braille window, but can also be done here. The difference is, the one set here can function like TOC items in MS Word, bringing the user to corresponding locations in the score.  
TOC title: Enter normal text, and the software can handle it correctly.  
The TOC format is title plus dashes or dots (dot 3's or 5's, or dots 36's) plus page number. There are 2 columns, one for title, one for braille pages. Indentation of the title's line break is automatic.  
Division patterns (radio button)  
dashes (dots 36's), dot 3's and dot 5's.  
Indentation: edit box. Default, by 2 cells.

Context menu for the above items should add "Translation table" to handle the braille manually.

Note:  
1\. Current untranslatabre texts such as Chinese characters can be manually translated via [Text management dialog](#2-5) in context menu.  
2\. If items in this dialog are removed completely, and no user-entered info are on title and TOC pages, the blank pages will always be removed automatically. Division signs will be removed even they are not deleted here.

**********

<h3 id="2-4">2.4 Part Management Dialog</h3>

Some Musicxml files have long part/abbreviation names, some have these names missing, some have group names and abbreviations for grouped staves, and some have instrument changes during the music. These are not able to be transcribed correctly. Here's a powerful tool for solving this problem.  
Part names and abbreviations will be automatically transcribed into braille, except Chinese, which can be edited in the Braille parts list table.  
All line breaks in the Musicxml part field will be shown as \n, and discarded in braille. Such kind of part names must be manually edited.

Print part list  
List all original items in "score-partlist" of Musicxml, plus part names caused by any instrument changes during the music.  
Items in this extensive table view can be navigated using up/down and left/right arrow keys, selected using shift+up/down, edited by pressing F2, and deleted using Del key. Its format is managed as the following grids from left to right:  
group name, group abbreviation, part ID, part name, and part abbreviation.  
If there are part names of instrument changes, these names and abbreviations will be marked as "instrument change".  
Any item will be left empty when none is found.  
Staves in a group will display group name and abbrev on all staves.  
When a multi-stave part is available, number or letter sequences will be added after the abbreviation names. Default is number.

Context menu items:  
Undo/Redo  
Common undo/redo function.  
Show/Hide  
Whether to show or hide certain part(s).  
Combine these staves  
Piano/harp/organ parts in some orchestral scores are not grouped correctly. Use this item to make selected staves into group.  
Treat as piano  
Change current group into piano format, thus adding hand signs before each staff. You can delete part names not belonging to the first staff.  
Treat as organ  
The same as piano, but treat the 3rd staff as organ pedal.  
Treat as multi-stave parts  
Some divisi parts have only two staves, and will be ocassionally transcribed as piano parts. Use this to turn them into common multi-stave parts. The individual names of the staves can be edited further.  
Use group name  
select if the part names in a group are missing or just arabic or roman numbers. E.g., some scores mark "Horns in F" as group name, and "I II" "III IV" as part names, no abbreviations, or abbreviations are the same as part names. But such modified abbreviations must still be edited for braille use.  
Use letter sequences for multi-stave part  
Choose if you want to use letters for current multi-stave part, e.g., vln1a, where numbers have already been used.  
Use number sequences for multi-stave part  
The opposite way of previous item.  
Assign hand  
A dialog for assigning initial hand signs. See [Section 7.3.1](7-3-1) for details.

Braille part list  
This table is used for editing braille part labels which can't be correctly transcribed. Braille input will be activated by pressing F2.

These two tables are linked, so scrolling one of them will also make the other scroll to the coresponding place.

Set interval direction dialog:  
Direction (combo box)  
According to clef  
All up
All down  
Keyboard
These 4 choices are for currently selected part(s). For clefs, treble and alto use descending intervals, while bass uses ascending intervals.  
Set globally (checkbox)  
Set current chosen interval direction to the whole score instead of selected part(s). Later operation on selected part(s) can override this setting.  
Include keyboard parts (checkbox)  
When checked, interval direction of keyboard instruments (including parts with piano property, such as organ and harp) will be changed regardless of common keyboard rules. This is useful in ensemble scores, in which all intervals should be in the same direction. In this case, the special hand signs should be used, i.e., 46,345,345 for treble reads upwards, etc.

Disregard instrument changes  
Will always use default part names and abbreviations.

**********

<h3 id="2-5">2.5 Text Management Dialog</h3>

A comprehensive dialog like [Part management dialog](#2-4). It lists out all texts items in the score. For dialog opened in this way, only words, credit words, DoletSibelius unrecognized system texts, rehearsal marks, instrument change texts and percussion instrument and beater pictograms are listed. When opened using context menu in the braille score, items such as title page and TOC info can be displayed.

Text list  
A same table as part list, but with different grids:  
measure, beat, part, voice, text, braille  
The list is sorted timewisely by default. Blank spaces at the beginning/end of text block will be automatically removed, and can be manually entered in braille if needed.  
One difference is, the Del key will remove the text from the score. So please use F2 to clear and re-edit it.

Context menu items:  
Undo/Redo  
Common undo/redo function.  
Translation table  
Choose one for current selected text(s). When using word signs, all uppercase signs will be ignored.  
Capitalization  
Toggle capitalization, overriding the default setting.  
Mark as dynamic  
Some special dynamic markings such as "sffzp" are not treated as dynamic in notation programs. This will tag the current text as dynamic mark.  
Mark as metronome mark  
This will change the property into metronome mark. Sometimes, special metronome marks are not assigned correctly in Musicxml. BMML must be re-designed to accept user-defined texts as metronome marks such as 4=ca120. Sibelius also exports notes to letters such as q=120, and the user must edit it accordingly.  
Put word signs before every word  
Mark as rehearsal mark  
Rehearsal mark will be parenthesized or word-sign enclosed, either within or above the system.  
Long text blocks (submenu)  
Use single word signs  
Use enclosed word signs  
Use parenthesis  
These are 3 different functions. The first adds dots 345 before every word in the text block; the second puts dots 345 before and after the whole block, and makes a space before (except fore after part name, hand sign, sign for begin of repetition and clef sign) and after (except for end of line) the block; and the last adds parenthesis to the block, with a space before (except for the same condition) and after (except for the same condition) it.  
Chinese texts  
This will add Chinese music parenthesis (dots 56,36 and dots 36,23) around the text. Once the Chinese translation is available, this option will be removed.  
Treat as texts as  
This dialog has the following: inside music, outside music (plain), outside music (with word sign), outside music (with parenthesis), and non-music texts.  
These choices will move current selected text items inside or outside the staff. By default, non-title/credit texts are inside the music. When texts are outside the music, it will be normal text without word signs, or single word with word sign, or multiple words surrounding by word signs, or words in parenthesis, placed on top of the staff it belongs to. Non-music texts are some long text blocks such as title or performace instructions (some musicmxl files have title information attached to score, or marked as Sibelius system texts), or top-system texts attached to the first staff. When the first staff is empty, this option will move the text out and remove the empty staff in cutoff mode. The format of such text can be freely edited.  
Combine selected texts  
Select at least two text items and choose this option. It brings up a dialog showing the result for you to edit, e.g., adding space etc. Sometimes special dynamics are entered this way, e.g.,, "sf-mf", entered as "sf" "-" and "mf", should be combined into one text item. Only items in the same voice, the same part and the same measure can be combined.  
Split text  
Split current text block into separate ones. A dialog appears, and you can press shift+enter at the position you want to split.  
Move text  
Move current text to different voice/part. A dialog will let you scroll through the part+voice to re-place the text. When the same beat position is not available due to note/rest value difference, the text will be shifted backwards to the nearest note/rest.  
Hyphenation  
Radio buttons. For long text blocks, hyphenation is required. The options are (English) End of line and (Chinese) Begin of line. Default is EOF, but we must finally recognize Chinese texts and switch to BOF for them automatically.

**********

<h3 id="2-6">2.6 Lyrics Management Dialog</h3>

A dialog showing table like [Text management](#2-5). The layout is:  
part, lyrics  
But since the lyrics are long blocks, they will not be displayed completely here. The beginning 5 words will be shown, and when pressing F2, a dialog containing multiple line editbox will appear for you to edit. In the dialog, there are radio buttons to switch between print and braille mode.

Context menu items:  
Undo/Redo  
Common undo/redo function.  
Translation table  
combo box. Choose a table for current selected lyrics part. Note that contracted braille and computer braille can't be used here, otherwise the output will be out of rules of braille music.

Chinese lyrics  
Checkbox. Chinese lyrics has different format from English one. This will be done later.

Use lyric sign (checkbox, default checked)  
Toggle lyric sign (dots 56,23) on/off. Some countries don't use lyric sign.

Lyrics position  
Radio button, put lyric line above/below music. Default is below.

Use repetition (checkbox, default checked)  
If same word(s) are repeated, use repeat signs (one or two dots 35's and one 35 around the block, or number plus dots 35 before and dots 35 alone after it, when repetition is more than 3 times).

Add prefix before lyrics  
Add a singer prefix (without word sign) according to the part this lyric line is associated to.

<h3 id="2-7">2.7 Chords Management</h3>
This dialog will deal with chord symbols and figured bass. We'll implement them later. Just extract chord symbols in the xml source and transcribe according corresponding rules.

**********

<h3 id="2-8">2.8 Metronome Dialog</h3>

This is a list of all metronome marks in the score. Press F2 to edit in either braille or common mode (e.g., 4=120, 4.=80).

**********

<h3 id="2-9">2.9 Percussion Dialog</h3>

This tool needs a [specific section](#7-4) to discuss.

**********

<h2 id="settings">Chapter 3: Settings Dialog</h2>

Ah, we come to the most detailed chapter, wholely dedicated to the most sophisticated part--Settings dialog! This is a multipage dialog, with several category pages dealing with almost all problems with braille music transcription. Settings in this dialog will apply globally to any newly imported Musicxml files, and also the current opened transcribed scores (we can also design to apply the changes with "reformat" process). The settings must be stored in both the BMML (individual preferences) and software .ini files (global preferences).

All of the following pages shouldhave a "save as default" and a "reset" buttons, letting users manage pages separately. The "Reset all" will revert all settings to factory mode, and load/save presets buttons can make custom presets containing all settings for future use or sharing purpose.

<h3 id="3-1">3.1 General Page</h3>

Default language (combo box)  
Currently English and Simplified Chinese only. More languages will be added later. You can even create your own language file by studying the .ini files in the "Lang" folder of the software's installation directory.

Show transcription dialog after importing (checkbox, default checked)  
Whether show [Transcription dialog](#2-1) before processing Musicxml file. If not, the transcription will be done according to previously defined settings.

Open debugging dialog when fatal error occurs (radio button)  
Yes  
No  
Ask me first (default)  
When serious xml errors are found, the software will automatically open the [Debugging mode](#7-6) if Yes. You can use find error function to navigate in all 3 windows. In most case, braille window will be empty, so please choose Transcribe in [Transcription menu](#1-5) after correction.

Workspace color (combo box)  
White screen black braille (default)  
Black screen white braille  
Black screen green braille  
Black screen blue braille

Page setup (button)  
Bring up Page setup dialog in [File menu](#1-1).

**********

<h3 id="3-2">3.2 Transcription Page</h3>

Translation table (combo box)  
List out all translation tables for literary braille.

capitalization (combo box)  
Default  
All  
None  
The Default will not capitalize expressions within the music. Title texts, tempo and expressions above score, and rehearsal marks are capitalized if they are. the All will add capital sign as long as the letter or word is capital, regardless where it is. The None will remove all capital signs (like in UK format).

UK metronome format (checkbox, default unchecked)  
Braille music produced in UK uses a different metronome expression. Instead of note-equals-number, it uses a sequence of stem sign, space, UK equal sign (dots 56,2356) and number.

Signs to be transcribed (button)  
A dialog list out some signs. Uncheck some of them when transcribing scores for beginners.  
The signs are: clefs, fingerings, articulations, ornaments, texts, lyrics, and chord symbols. All are checked by default.

Use ottava indications (checkbox)  
When checked, octave marks at the beginning and end of an 8va/15ma or 8vb/15mb passage will be transcribed according to rules specified in the code. Otherwise, they are treated as common octave marks, and shown only when needed.

Unison method (radio buttons)  
Interval (octave interval preceded by octave mark)  
Stem sign (a stem sign with the value of the written note)  
These two are for different conventions among countries. Sometimes stem signs are also specially used in music for bowed instruments to indicate two strings playing the same note.

Use doubling (checkbox, default checked)  
Apply doubling to articulations, bowings, tremolos etc.

Braille repeats (combo box)  
None  
Within measure  
Within and between measures (default)  
All  
Use braille repetition signs. All will use measure reference, e.g., 1-8. Since ensemble scores are too complicated, All should not be used.

Use repeats across system (checkbox, default checked)  
In keyboard and vocal scores, this should be checked. In ensemble scores, some countries use full-measure repetition sign when the first measure of the next braille system is the same as the previous measure in previous braille system; while other countries write the measure out verbatimly.

Supress phrasing slurs for vocal part (checkbox)  
When checked, the software will transcribe the part with lyrics using only common slur (dots 14).

Slur options (combo box)  
Standard  
Common only  
Common only except keyboard  
Phrasing only except vocal parts  
The Standard option is a hybrid mode, and will use phrasing slurs when the phrase is too long. See corresponding discussion in [section 6.4](#6-4) for details.  
Keyboard music is preferred to use a hybrid method, so I provide an option to opt it out and use common slurs in all other one-staff parts.

Phrasing slur length (note amount)  
An edit spinbox, default is 6, i.e., the software will apply phrasing slur to a phrase more than 5 notes.

Slur for grace notes (radio button)  
Common slur (dots 14)  
Grace slur (dots 56,14, default)
Some countries still use common slurs on grace notes.

Use "from" signs for crossing slurs and ties (checkbox)  
If this is turned on, any slurs/ties crossing voices/staves, besides the "to" sign, will have a "from" sign before the first applied note/chord of the destination voice/staff. This will show the way of the slur/tie clearly.

Add extra accidentals (combo box)  
None  
Voice only (default)  
Voice and measure  
For the same altered note in another voice, or a tied altered note in a new measure, add an extra accidental preceded by dot 5.

Add extra accidental to octave intervals (checkbox, default checked)  
When the above combo box is switched to Off, this checkbox will disappear.

Add extra tie to new system (checkbox, default unchecked)  
Some countries have such a custom, to add a reference tie when the tied measure starts at a new system in bar-over-bar/line-over-line formats, or a new section in section-by-section format.

Apply extended lines for non-text use (checkbox)  
If checked, temporary braille symbols will be applied for the user to change freely. In Musicxml, an extended line is usually marked as a dashed line. See discussion in [section 6.4](#6-4) for details.

Add hand change signs for selected passage  
This is for keyboard or harp music. See the same item in [section 7.2](#7-2) for details.

Harp pedalling format (combobox)  
Text  
USA  
The text format treats harp pedalling in common text format, converting the table into note names and accidentals. The USA new format (came out in the Music Braille Code 2015) will generate a set of symbols on top of the harp staves.

Output interval direction description (checkbox, default checked)  
See this item in [Transcription dialog](#2-1) for details.

Output part list (checkbox, default checked)  
This will usually generate new braille page(s) before the first music page. The list will show all parts and braille abbrev names listed and edited in the part tables in [Part management dialog](#2-4). 2-cell indentation for long names is automatic. New line can also be entered by pressing shift+enter in braille input mode in Braille part list table.

Output part list option (radio button)  
On new page (default)  
Just before music  
When only keyboard without part name is available, always don't use a new page, just say "keyboard". When there's an solo line above the keyboard, then "solo XX (instrument name) with keyboard accompaniment".

**********

<h3 id="3-3">3.3 Single-line Page</h3>

format (radio button)  
Continuous  
Line-based (default)  
These two radio buttons adjust format of the music. Some countries format it like section-by-section, according to measure amount of every staff in print version. When set to continuous mode, measure numbers will not be shown.

Section head (combo box)  
System number with prefix  
(Show system numbers before every section of music. The format is a parenthesised item with "l"+number with number sign.)  
System number without prefix  
(The same without "l".)  
Measure numbers with prefix  
(The same as system number, but with the prefix "b".)  
Measure numbers without prefix  
System and measure numbers (default)  
(Combine the above to into parenthesis, separated by a space.)  
System and measure numbers without prefixes

Combine full-measure rests (checkbox)  
If not checked, multiple full-measure rests will not be combined, leaving every empty bar separated by space.  
If checked, two or three full-measure rests will be combined without spaces, and more than three full-measure rests will be combined as a number with one whole rest.

Place extra key and time signatures at end of line (checkbox)  
When there's a key and/or time change at the beginning of the next braille line, some countries put a cautionary time/key at the end of the current line. Page turn sign is put before the change with a space between them. Note that when this is checked, any key cancellation natural signs (except the cancellation to C or "no key", where the natural sign(s) must be repeated) will be omitted for the key signature repeated at the beginning of new line.

**********

<h3 id="3-4">3.4 Bar-over-bar Page</h3>

For detailed rules of the formats discussed in the following sections, please consult Music Braille Code 2015. Some rules are not strictly obeyed by all countries, but their scores are fairly readable. So we have multiple options here.

Break page by (radio button)  
Measure number and part (default)  
Measure number  
Part  
Free  
the other three options are designed for music with extended parts which makes one parallel can't fit within one braille page.

Extra octave marks (radio button)  
None  
New line only  
All (default)  
Add octave marks in every measure of a line, no matter whether they are necessary. New line means adding an extra octave mark in the middle of a measure at the beginning of its new line. Different country uses different custom.

Indentation (radio button)  
From margin  
From the music  
When a single measure needs more than one line in a part, this controls how to indent after line break.

Indent by (spin box)  
default: 2 cells  
This will add additional cells after the set indentation point.

Ignore non-musical elements (checkbox, default unchecked)  
Some countries don't align the music by the first musical symbol. They just align the parallel with the first braille cell. So texts or dynamics are aligned with notes, articulations or measure repeats.

Keyboard measure number format (combo box)  
Don't show  
Left without number sign (default)  
Left with number sign  
Left with number sign for only first measure of a print system (a format used by ONCE, Spain, for both piano and ensemble scores)  
This includes piano, organ and solo with keyboard accompaniment.

Full score measure number format (combo box)  
Don't show  
Left without number sign  
Left with number sign  
Left with number sign for only first measure of a print system  
Above the system for the first measure (first measure of the braille system, default)  
Above system for all measures (all measures of the braille system)  
Above with measure range (for example, 48-49)

Show system number (checkbox, default checked)  
This will put a number (without number sign) before left hand sign (no space) of keyboard music, or put a parenthesized "l"+number item centered above measure number in ensemble score.

Rehearsal mark enclosure (combo box)   
Use word sign
Use parenthesis (default)

Rehearsal mark placement (combo box)  
After part prefix  
Before part prefix  
Above music and measure number (default)  
Above music and left of measure number  
When the last choice is set, Above system for all measures must be turned to first measure in case of unsufficient room in the line. 

Add guide dots (checkbox, default checked)  
When there are 7 and more spaces between two measures, or between part prefix and the first measure, guide dots (in NIM, they are called "tracking dots) (dot 3's) are added to ease navigation. Some countries (e.g., Spain), however, don't use them, so I put this as an option.

Multi-piano format (radio button)  
Piano style (default)  
Chamber style  
When transcribing a multi-piano score, there are two different formats. Piano style is to add a lower-celled number after dots 345 of hand signs (e.g. 46,345,2 and 456,345,2 for piano 1); chamber style will use the style like orchestral music, showing part prefixes.

Use parallel motion (checkbox, default unchecked)  
Use parallel motion sign for doubled parts.

Ensemble score cutoff (combo box)  
No  
Yes according to print (default)  
Yes for all silent instruments  
This is not applied to keyboard solo and solo with keyboard accompaniment scores. No will display all staves all the time, Yes according to print will hide silent staves according to settings in Musicxml, and Yes for all silent instruments will hide all silented (rest-only) instruments. If all instruments stop for one or more measures, staves of previously playing parts are shown, or show the ones according to Musicxml's setting.

Show all parts on first page (checkbox, default unchecked)  
Display full part names on first page (checkbox, default unchecked)  
These two are for ensemble scores.

Key signature placement (radio button)  
Before part prefix  
After part prefix (default)  
For scores with parts in different keys, or with transposing instruments with different key signatures. When at the left, all other part names must be shifted right. For scores with the same key in all parts, key signature will be automatically brailled above the system, below measure numbers.

Key signature display (combo box)  
All the time (default)  
Only once  
Appear at the beginning of a part or a key change. If Show all parts on first page is checked, they are present at the first page. If not, they will appear at the places where the paqt(s) appear for the first time.  
Reappear after silence  
The same as the second one, but will reappear after the instrument staves' cutoff.  
This option is again for score with transposing instruments.

Piano time signature placement (radio button)  
Above system if at first measure (default)  
After part prefixes  
After part prefixes without dot #c  
Some countries place time signatures after hand signs with a space instead of a dot 3 separator. Time signatures within a system are always placed within music surrounded by space.

Full score time signature placement (radio button)  
After part prefixes (default)  
Above system  
Two circumstances will override this setting, and print time signatures always within every part: 1. Different part has different time signature; 2. Time signature changes in the middle of a braille system.

Place extra key and time signatures at end of system (checkbox)  
When there's a key and/or time change at the beginning of the next system, some countries put a cautionary time/key at the end of the current system. Page turn sign is put before the change with a space between them.

Place blank line between keyboard systems (checkbox, default unchecked)  
Sometimes for easy reading purpose, keyboard and solo with keyboard accompaniment scores are formatted by separating systems using blank line.

Place blank line between ensemble systems (checkbox, default checked)  
Most of the ensemble scores using this custom.

Ignore page turnning (checkbox, default unchecked)  
The first part of a parallel will not be forced to put on a new page if checked. This is for long orchestral music to save paper.

Ignore new system (checkbox, default unchecked)  
By default, both bar-over-bar and line-over-line will start a new parallel when Musicxml starts a new system. Checking this will prevent BrailleOrch from starting a new parallel if there's room for the following measure(s) on next system. In this case, new system number will be moved to the next parallel in keyboard score, while shown above system right at the beginning of new system in ensemble score. If page turn is met, the turning page sign will be brailled at its right place.

**********

<h3 id="3-5">3.5 Line-over-line Page</h3>

The main difference of these two formats is whether to vertically align measures in all staves of the system. In line-over-line, all measures in a system are not aligned, and once there's a staff which doesn't come to line break, other staves can continue with several lines of music. The advantage of line-over-line is saving paper.

Most of the settings of bar-over-bar are the same, except the following:  
Extra octave marks: only None and Yes, Yes equals New line only.  
Measure number format: no Above system for all measures

No alignment options for texts  
No Add tracking dots

Add Combine full-measure rests checkbox

Ignore new system will turn off system number completely.

Extra time and key signatures will take effect to both new braille line and new system.

**********

<h3 id="3-6">3.6 Section-by-section Page</h3>

Section-by-section is used in many countries with varied layouts, and it's therefore much more flexible than bar-over-bar and line-over-line. Since it's not unified, I have to pick up some most essential features for the users. If anyone who wants a different layout, please contact us for implementation.

Break page by  
Free (default)  
Part  
Section  

Sectioned by (combo box)  
Systems (default)  
Custom (by user settings, see below)  
Specified measure amount (input a number below)

Customize sectioning (dialog)  
This dialog will open two lists. The upper one lists out all measures, and the lower one is waiting for the user to add section breaked measures.  
The dialog has "add", "save" and "cancel" buttons. Look at the original score, counting down measures, then scroll to the point where you want to create a new section (e.g., beginning of a music phrase or section), and press "add" to store a break point into the BMML file. If Sectioned by is set to Customize, the software will use these points to create sections. This will ease reading and memorize the music.

Indentation (radio button)  
First line indent (default)  
Following lines indent  
These are two main different indentation styles.

Indent by (spin box)
Default: 2 cells

Line-over-line style (checkbox, default unchecked)  
Only applicable to keyboard music. The layout is much like line-over-line, but line breaking is free for all staves.

Measure number placement for line-over-line style (radio button)  
Left of music (default)  
Above system

Section heading (radio button)  
Section only (section number)  
Measure only (measure number)  
Section and measure (default, plus number of first measure, no space and number sign. See next control)  
Section and measure range (section number, space, measure range)  
Complex (section number, space, measure range, space, page sign, page number, dot #c, staff number)  
These are 5 classical heading styles of section-by-section format. If more than one staff are indicated, staff ranges are separated by dots 36.

Section + measure format (radio button)  
Section uper-celled  
Measure upper-celled (default)

Section + measure range format (radio button)  
Section uper-celled (default)  
Measure range upper-celled

Put measure numbers within music (checkbox, default unchecked)  

If checked, measure numbers (without number sign) will be placed between measures, and every measure needs an octave sign.

Use system number as section number (checkbox, default unchecked)  
It uses system number on a print page for section number. So if a new page is here, the section number will return to 1.

Put system-change signs when not sectioned by systems (checkbox, default unchecked)  
The change system sign is dots 25,123.

Place blank line between sections (checkbox, default unchecked)

Key signature placement: no Before part prefix  
Other options of key and time signatures are the same as previous two formats.  
Braille page turn is ignored, but print system change can't. This ensures the sections to sync to systems in print.  
Other options are nearly the same as line-over-line, including the Combine full-measure rests.

Extra time and key signatures will take effect to both new braille line and new system.

**********

<h3 id="3-7">3.7 Brailleorch Format Page</h3>

When transcribing orchestral scores, I developed a special format, and now name it BrailleOrch, because these scores are solely for my braille music project.  
In such a format, the layout is between bar-over-bar and line-over-line, where all measures in all parts are not vertically aligned, while all parts shouldn't have line break unless there's only one measure.

The options are nearly the same as in the previous two referred formats, and I extract them out for my format to have a specific control. If one would like to have some line breaks, there's also a checkbox to allow line breaks in any part.

**********

# Part II: General References Of Important Points

The four sections below will be written on scratch, and only represent my own opinions. It is welcome if anyone feels it better to try different ways.

<h2 id="phases">Chapter 4: Development Phases</h2>

Only currently working or finished phase(s) are present, and they will be constantly supplemented and improved.

- Lines marked by a plus (+) sign are those need to be done.
- Lines marked by an equals (=) sign are those have been completed.
- Lines marked by a minus (-) sign are removed or abandoned points.
- Line marked by an exclamation mark (!) are important points or critical issues.

**********

<h3 id="4-1">4.1 First Phase</h3>

This phase is mainly focused on implementation of BMML, and basic build of the software. We can begin with the original BMML format, researching its DTD file and build braille equivalences according to excisting materials. Then we can enhance BMML to present more symbols. For how to deal with limited BMML materials and how to implement it, please read [the next chapter](#bmml).

\+ First, choose a suitable programming language or language bundle. The software should be at least completely accessible. Use [NVDA](http://www.nvaccess.org) to test the GUI.

\+ For line endings, I hope we use Windows format (cr-lf) to code the software and its format. It's easier to view the codes with Windows line endings in a plain text editor such as the common Notepad.

\+ The software should accept any size of Musicxml files. Many large-scaled musical works can generate more than 50mb of single XML file, and if it's in UTF-16 format, the size is doubled. We should find a way to load and parse XML data as fast and light as possible.

\+ The beta version of the software should convert Musicxml to braille which is fairly readable. Not all things are included, but the result must be suitable for further production.

\+ In the GUI, keys f, d, s and j, k, l should represent braille dots 1-6. Other keys are reserved for shortcuts, and I have implemented all single-key shortcuts which avoid these 6 keys. We can freely enter braille dots in the GUI to test. This is the very first GUI, and doesn't require file format. After this test, we can start to implement BMML reading and braille output.

\+ The structure of the installation folder can be defined as this:  
- Bin: all executable files
- Doc: Documentations, which can have subdirectories for different languages if HTML pages are used
- Include/Lib: Dependencies
- lang/Locale: Language files
- Modules: Either our own and third-party modules
- Tables: Liblouis raille tables  
The configuration files can be put either in the main directory or the user document (thus My Documents) directory. I prefer to use the latter, with a main directory BrailleOrch, which can contain additional data such as example files, user projects, templates, default and custom transcription presets etc.

\! **Important:** Put all music object descriptions, texts of menus, controls and plain description texts as well as warning and error messages into a separate file. This will make it possible to add multiple languages in the future. Every language uses one file. Store the files in a "Lang" folder, and make a unified extension (e.g., .ini) for the software to recognize. All items should be callable via variables.

\! **Important:** The components of Liblouis Braille Translator in the software directory should be able to be updated and replaced freely, so that the software can keep up with the latest improvements even if we can't maintain the software due to any unexpectable reason. The software should automatically detect new or modified language files and braille tables, picking up their names and rules.

TBC

**********

<h3 id="4-2">4.2 Second Phase</h3>

TODO

**********

<h3 id="4-3">4.3 Third Phase</h3>

TODO

**********

<h3 id="4-4">4.4 Fourth Phase</h3>

TODO

**********

<h3 id="4-5">4.5 Last Phase</h3>

TODO

**********

<h2 id="bmml">Chapter 5: BMML Enhancements</h2>

The current BMML is an incomplete implementation. There are lots of items not mapped from Musicxml, and the DTD is based on Musicxml 2.0.

<h3 id="5-1">5.1 Limited Learning Resources</h3>

Before doing many enhancements, we must get to know BMML as much as possible. There's not a formal document describing every element of BMML, but we can learn from some sources. There are three documents from two different sites. Each of them gives information fragments about BMML's definition together with other points regarding braille music transcription. Some of the source websites mentioned in these articles are obsolete and in fact of no use.

- [site 1 article 1](https://www.irit.fr/publis/SIG/2008_ICOMP_EJMR.pdf)
- [site 1 article 2](https://www.irit.fr/publis/SIG/2009_TOISJ_EJMRA.pdf)
- [site 2 article](http://bpfe.eclap.eu/eclap/axmedis/a/a79/00000-a7927300-b90e-45b9-957d-d450c03d177e/2/~saved-on-db-a7927300-b90e-45b9-957d-d450c03d177e.pdf)

There are also two websites containing similar resources. They are two ended projects which developed BMML. The websites contain libraries of braille music scores in this format, and we can open and read them using Braille Music Reader it provides  for download. BMR is a read-only version of Braille Music Editor 2.

- [contrapunctus (older)](http://www.contrapunctus.it)
- [Music4vip (newer, now still running but not developing)](http://www.music4vip.eu)

We can also download a demo of full Braille Music Editor 2 from [VEIA Progetti](http://www.veia.it) and enter various music objects to see how BMML is defined. Also, there's a Googlecode archive containing original Python scripts by VEIA, which converts Musicxml into BMML. It's an old tool, but we can learn from it and develop our own implements. The download is not available now, but I can provide the complete repository at the beginning of the development.

**********

<h3 id="5-2">5.2 Implementation Steps</h3>

To make enhancements of BMML, we should first map most elements of Musicxml 3.0 or 3.1 to BMML, no matter whether the items have corresponding braille signs. Because braille music code is always under development, and can be flexibly customized, with transcriber's notes for special symbols before the music. Layout information such as page/system/staff sizes and single object position can be ignored, because they are of no use in braille. But sometimes text positions can override the  sequence of their appearance in print, and this is sometimes needed in braille. Elements such as instrument changes and percussion symbols must be mapped as common texts, but with special indications to reserve future development of BMML to Musicxml back-translation.

Next, we need to create a conversion tool to generate braille according to the mapped elements, and place both elements of musicxml and braille into BMML source using braille music rules. Symbols not implemented in braille can be left empty for future development, or customizing using the [Defining New Features](#7-7) function. If the generated BMML doesn't contain braille formatting rules, it should not generate braille automatically, because it needs reposition of elements. On the other hand, if the initial formatting is changed after transcription, there may  be an additional implementation to store original position of elements to reserve correct reformatting. Or we can make an additional copy of BMML which contains the raw mappings to reserve these changes. Manually added, deleted or changed items should be marked to let the users choose whether to keep them during reformatting. these latter points can be implemented later.

An additional note: Musicxml is formatted as either Timewise or Partwise, and almost all softwares export it as partwise. But BMML use part tags to render a quasi Timewise format, because braille music is not Partwise. However, we can imitate Partwise in BMML, and insert line breaks or other intermediate objects at certain places, specific for braille use. This will also ease the future development of back-translation.

**********

<h3 id="5-3">5.3 Flows</h3>

Another thing we can consider is to implement BrailleOrch format as a container, which can contain multiple BMML workflows in one document, like the brand-new notation software Dorico does. A book may have preface, TOC and critical notes with music examples, and multiple pieces are in one book. Flow lets us manage individual pieces of music easily. We can first implement BrailleOrch to complete its function, and add this feature later. This feature is also useful when doing [split and merge](#7-4) functions. Mutiple MusicXML and BMML files are included in the archive, with a metadata sheet linking and ordering them together.

**********

<h2 id="braille">Chapter 6: Braille Transcription Specified Points</h2>

This chapter will be created and updated on scratch, but all of these points are critical for developing the software. General rules of braille music notation will not be repeated unless none of the current available softwares can handle them well.

**********

<h3 id="6-1">6.1 Braille Window</h3>

The GUI of BrailleOrch, including the advanced [Debugging](#7-6) windows, must be plain edit fields. The following points are all related to the braille music window.

Since different countries have different mapping tables for ASCII to braille, we use Unicode braille from U+2800 to U+283F. The braille entries are already stored in BMML source, so we just need to make the stored Unicode values displayed as braille. To benefit sighted users, we can marked correctly mapped braille with normal color, places containing errors marked as red, and manually entered unprocessed braille as yellow. Sighted user can choose to display more indications like placing vertical bars at bar lines, thin horizontal lines to separate parts (staves), and thick horizontal lines to separate systems (system means a whole group of staves).

**********

<h3 id="6-2">6.2 Navigation In The Score</h3>

When navigating in braille mode, just braille dots are reported, e.g., "1 4 5 6" for a C quarter.  
When navigating in object mode, we must have the following reported:

- For notes: Note name, value, octave;
- For rests: rest value;
- For octave sign: octave count;
- For articulations, ornaments and symbols: name;
- For key/time signatures, dynamics, texts and lyrics: attribute of the object, object information. E.g., key "three flats", "three-four time", text "Allegro", dynamic "ff", lyric "kyrie". We should let the user to have texts and lyrics spelled out using a shortcut. Or we can create a shortcut to read the whole item at once, and read cells one by one while navigation. When the cursor moves out of the object, it gives an announcement such as "end of text" or play a sound.

Space representing a bar kine should be announced as "bar line", otherwise it should be announced as "space".

Unmarked object (auto marked as "other") can just announce braille dots in any mode.

When navigating amoung bars, staves and systems, announce new bar number, new staff name and new system. Pressing corresponding key will tell the user where he/she is.

It's impossible to announce CJK texts cell by cell, so we can just announce using original text source.

**********

<h3 id="6-3">6.3 MusicXML Related</h3>

Although MusicXML is itself very complete, there shuld still be some attention to be paid when dealing with musicxml-to-braille process.

The XML based formats can commonly have two kinds of encoding, UTF-8 and UTF-16, with or without BOM prefixes. The software and its format should be based on UTF-8, but files in the other encoding can also be opened. Sibelius and Encore export Musicxml in UTF-16 format.

The software must allow some non-critical errors in Musicxml files which are exported from old-fashioned (such as Encore) or music recognition softwares (such as SharpEye and PDFtomusic Pro). Old softwares have incomplete support of Musicxml, and music recognition itself contains errors which need to be corrected in notation softwares. For example, there may be non-matched slurs, incomplete note description, wrong measure duration, and even wrong or missing values of elements. Unless there are extremely critical validation issues, the software should allow and process the file, giving some warnings such as at which line what error is found. In braille, the errors are also allowed, partially transcribed, letting the end-user to correct. Unsupported characters in text field are not transcribed, but the error finding function should take care of them.

**********

<h3 id="6-4">6.4 Transcription Related</h3>

The "movement-title" and "work" tags at the very beginning of the xml file are nearly the same. So we should treat them as the same thing.

The "credit" subtags have different properties. If both toplevel and credit title and composer fields are found, we can either give a warning message showing those two different places for comparison and choice, or simply apply the "credit" ones, which may contain additional text fields for title pages. Credit page numbers can be treated as print page numbers.

If there are texts at the pages other than page 1 in the credit section, it's better to include and put these texts at the beginning of each corresponding pages, below print page indications and above the first measure of the page. Of course, if the music starts from page 3 while there are texts on page 2, the texts will be placed as its pcorrect position on print page 2 before 3.

In the music, right below the "measure number", there are two kinds of statements controlling system and page breaks. "print new-page='yes'" means a new page turn. If there are also page numbers specified, we can use them as print page numbers. If not, simply do increment page numbering. "print new-system='yes'" is for systems within a page, and the first appearance of it should be treated as beginning of print system 2.

The "implicit" statement in "measure number" field means a pickup measure. When it's at the beginning  of a piece, this measure should be counted as 0. When is appears at the middle of music, it should be numbered according to the last numbered measure before it, and put a dot 3 before the measure number. When multiple implicit measures appear, they share the same measure number until the next numbered measure appears. In piano music whose measure numbers are put before hand sign, dot 3 replace space, thus no space is between measure number and hand sign.

Some metronome marks are not standard. For example, some metronome marks exported from Finale have the note values marked as "other", and the tempo speed is entered as texts, usually because there are text and number combined, e.g., quarter = ca 120. In Musicxml exported from Dolet for Sibelius, note values in a tempo + metronome combination are usually expressed as single letter, period (dot) or letter combination (e.g., Allegro q=120, Moderato q.=80, q=q, e=e, q.=q, etc). The software should convert such special combinations into correct braille indications, and there may no mistakes, thus there may be no plain text saying q=, h= etc, unless we are expressing mathematic formulas.  
(In Sibelius, note values are presented by letters using a special font: w = whole, h = half, q = quarter, e = 8th, x = 16th, and y = 32nd.)

The "accidental" and "accidental-mark" are two different tags. "Accidental" is used for notating an accidental of the current note; while the "accidental-mark" tag is used for other circumstances, such as an ornament with auxiliary note(s) containing accidental(s). The latter tag is placed under "notations". In braille, just put it  before any ornaments which is below it ("ornaments" is also put under "notations", one line below "accidental-mark").

Sometimes in contemporary scores, there are accidentals of triple sharps or flats. They are not implemented in braille, but we can simply transcribe them as three sharp or flat signs.

Some points on value distinction signs:  
1\. When the pickup (implicit) measure only contain a note or rest of 16th or shorter, the short value sign (dots 6,126,2) must be added;  
2\. When the first note of a measure is 16th or shorter, while the next note is an eighth, the long value sign (dots 45,126,2) must be added before the eighth;  
3\. If a long note is followed by a short note which has the same braille pattern (thus a half followed by a 32nd), the short value sign should be added before the short one;  
4\. If a group of short note is followed by a long note which have the same braille pattern (thus a group of 32nds followed by a half), the long value sign should be added before the long one;

When the note or chord after a tie doesn't contain any notes of the previous note or chord, we can ensure the tie is for a different purpose, thus letting the note ringing. The software should detect this, and replace the tie with a correct sign, dots 56,14. Also, there's a "let-ring" value in Musiixml 3.1, which will make the detection and implementation easier.

Transcription of parenthesized objects:  
Music parenthesis (thus for notes, accidentals, articulations and other musical objects) in braille is dots 6,3, placed before and after the object.  
If a note or an entire chord is parenthesized, the parenthesis  must enclose all its relative objects. It's not needed to terminate parenthesis within the chord unless there are unparenthesized notes.   
If a note in a chord is parenthesized, just place the sign around that note or interval sign.  
If an non-note object such as accidental, articulation or ornament is parenthesized, the sign is put around that symbol.

Interval direction in braille music means both the direction of intervals in the chord and the order of voices in a part. So, when altering interval direction, voice order must also be considered. For example, in piano music, right-hand part is usually read downwards, so the order of voices must be voice 1, 2, etc. The left-hand takes the opposite way, thus read upwards and the order of voices is 2, 1, etc. In orchestral music, we usually request for the same direction for all instruments, so left-hand part must be processed the same as right-hand part.

When a voice in a part has no rest but a "forward" command, we must add rest(s) according to the duration(s). Normally these rests are not shown in print, but in braille they are needed for reference. So we must add dot 5 before them to tell the readers they are "added". See below.

Tuplet implementation points:  
1\. A simple tuplet will just have a time-modification tag to determine the numberof tuplet, e.g., 3 against 2 for a triplet.  
2\. Sometimes there are nested tuplets, in which "tuplet number" is used. In this case, we must take this value instead of time-modification. E.g., in a group of 3 eighths (8th triplet), there's an eighth which consists of a 16th triplet (3 16ths). In this case, 9 against 4 is used for such 16ths, and we must take "tuplet number", otherwise we'll get these 16ths transcribed with incorrect tuplet indications.  
Note that in nested tuplets, the sign for non-toplevel triplet is dots 456,25,3.

There are two kinds of in-accord signs  for voice writing in braille--full measure and part measure in-accords. We should let the software to determine which one is needed. When there's a voice not occupy the whole measure, we should find a correct point to let the adjacent voice to use part-measure in-accord. For example, the upper voice has a half and two quarters, while the lower has just one quarter at beat 1, and the rest of the measure is "forwarded" by the "forward" command. Then we can break the measure by two halves, use part-measure in-accord at  the first  part, and add a quarter rest with dot 5 after the quarter note.

Points of braille line break:  
Break during the music within a bar must have a music hyphen (dot 5) at the end of the line, except there's a full-measure in-accord sign, division sign for part-measure in-accord, or it occurs between two words of a text block or after a long text block.  
When the break occurs during the music, it's better to split the line at the beginning of a beat. If it's impossible, for example, a dotted quarter note is here, simply break  after it. When there are grouped short notes (16th and below), the break should not interrupt the grouping, unless there's a long tuplet with large number of notes. In the latter case, grouping must be disabled. Also, we can consider subdivision of beams for breaks for very short notes (usually 32ndss and below).  
If the line breaks after a word in long text block, music hyphen is not needed. Although a text block is treated as one "words" element in Musicxml, we must allow the software to add line breaks smartly, or allow manual line breaks, while still keeping the whole block as one object in BMML. Then BMML must contain a line break command on the braille side.

There are two kinds of glissando lines in notation. One is a "gliss." with a sliding line, mainly placed during two notes, tagged as "glissando line" with start and stop values; the other is a sliding line which cross all notes it applies to, with no "gliss." indication, marked as "slide line" with start and stop values. In braille, both can be transcribed as dots 4,1. When two notes are applied, the sign is placed between two or three notes and after slur; when more than three notes are applied, place dots 4,1,3 after the first note (start) and dots 6,4,1 after the penultimate note.

The "dashed" line in Musicxml can be rendered as this: When it follows a text immediately, the end of the text should be marked as two dot 3's (begin of extended lines), and the end of line is marked as dots 345,3; When the line doesn't follow a text, it's up to the user. The latter can be set as whether to display dashed lines in the [General page](#3-2) of [Settings Dialog](#settings). If set, the beginning is marked as dots 345,3,3, which can be modified according to the context. For example, if a fingering is extended (in string music), the user can add appropriate symbol after the fingering. But since these are very uncertain circumstances, we currently only implement text for applying extended lines.

In vocal music, we usually use common slurs (dots 14) instead of phrasing slurs even in long phrases. If a part is detected with lyrics, the software must automatically supress phrasing slurs and use common slurs only.

Some notes about doublings:  
Doubling of intervals can include accidental in certain conditions, thus either the first or the last interval has an accidental. If both have accidentals, it's also ok as long as the total amount of chords is no less than 4.  
When applying doublings, we should skip any extra elements. For example, there are five staccato chords with 3rd interval, some have accent marks, some also have fifth interval, and there are even rests inserted. The doublings of staccato and 3rd interval should be kept till the end. Another thing is for octave interval. These intervals can be doubled even when there are accidentals, unless the two notes of the chord have different accidentals, thus an augmented or diminished octave.  
Doublings must be stopped if there are fingerings.  
When a series of different chords contain a similar interval (e.g., C-E-G, B-D-G, A-C-G, B-D-G), the same interval (in the above example, third) can be doubled.

The "other-dynamics" tag in Musicxml should be considered as standard dynamic marks. For other tags with "other" prefix (such as "other-articulation", "other-direction"), we should either make a smart detection and application engine, or let the users determine how to use them in the [Debugging Mode](#7-6).

There are no special indication for string and position numbers. They are written as Roman numbers in print, and the transcriber should determine which kind they belong to, and modify them manually. So we only need to allow string/position/fret signs (including doubling and extending line) to be accepted in BMML as braille music objects. Octave mark is needed after a position sign.

When dealing with MusicXML exported from Dolet plugin for Sibelius, the "Doletsibelius unknown symbol index" and other unrecognized items are very useful. For example, for symbols, we can read Sibelius' Manuscript Language Reference and get index numbers of all symbols listed in the Symbols gallery. When there are symbols unable to be exported, Dolet will give a line with symbol index. We can use this number to  convert the symbol into braille. When no braille equivalence is available, we can still give the English name of the symbol in the [feature defining function](#7-7) for users to create their own equivalence. We should store all the English symbol names in our software library, in case some non-English copies of Sibelius put other languages in the "other-direction" field below the index line. Many of these translations are not as accurate as their original English version, or even very weird.

According to rules in Music Braille Code 2015, metronome marks during the music may be enclosed in music parenthesis to avoid misreading. In ensemble music, we can move the mark above the braille system if it appears at the very beginning. This may be done manually using specified  context menu, and the parens will be removed automatically.

Here are two rules for tremolos: When the note is or longer than a 4th, one tremolo beam equals an 8th division, two equals 16th, and so on; When the note is or shorter than an 8th, the division of tremolo is based on the note value, thus one beam equals a half division (16th based on an 8th for example). Two-note alteration tremolos obey the same rules. We should let the software correctly detect and apply appropriate braille indications.

In Musicxml 3.1, tremolo-type has an "unmeasured" value. In braille, it can be transcribed as 32nd (quick music) or 64th tremolo (slow music). We should wait for the example to see what we can do.

In bar-over-bar, line-over-line and BrailleOrch formats, we must let the software smartly detect how many bars it can fit on one line according to the current page settings. Especially in bar-over-bar and BrailleOrch, the amount of bars is also determined by other parts in the same braille   system.

In bar-over-bar format, when adding tracking dots, make sure there are at least 7 blank spaces. The minimal number of the tracking dots is 5.

**********

<h2 id="advanced">Chapter 7: Braille Music Editing, Correction And Other Advanced Features</h2>

This chapter discusses braille music editing and correction related subjects.

<h3 id="7-1">7.1 GUI Specifications</h3>

The working area of BrailleOrch is an edit window like Windows notepad. Items entered and displayed here are all unicode braille. Untranslatable items such as Chinese characters are displayed as yellow question marks, and in braille output, a set of computer-braille question marks (dots 1456). Untagged items such as user-entered customized items are marked as "other" in bmml and displayed in gray. BrailleOrch can also ignore non-fatal musicxml errors, and displays such problematic items in red. Very serious error such as unmatched element tags will generate warnings, and store the xml into .bor file for debugging. Once debugging is finished, it can then be transcribed using Transcribe under [Transcription Menu](#1-5).

Items in the edit window must be announced via screen readers such as NVDA. The description should be as brief but clear as possible. Dots should also be announced. Settings of announcing modes are in Options Menu.

**********

<h3 id="7-2">7.2 Entering, Selecting And Marking Items, Transcription Related</h3>

The software should have wrapping function like MS Word. It's simple when entering literary texts, but  for music, we can implement it step by step. Generally speaking, it's better to put the break point at the beginning of a beat or half of a beat. For long tuplet or unmeasured music, breaks can be free according to note groupings (including subdivision of beams). Auto indentation follows rules and settings. We can also first ignore those issues, but display a warning message saying there are non-formatted lines which exceed line length when trying to save or print the document. Saving is certainly allowed, but the software will warn again when the file ii opened the next time, and we can find such unformatted items via find error function.

When correcting the music, for example, adding missing signs, moving words' position etc, please press letter n to start entering notes/rests/articulations. BrailleOrch will recognize them automatically. Unfinished enter will be tagged and announced as "other".  
(Note: make this complicated function later, now just tag all user-entered strings as "other". So reformatting of individual lines must be done manually, like manual transcription.)  
For moving words, please put cursor on any location within the word block, and right-click, choose "Cut", and paste it to new location. BrailleOrch always treats a word block as a single object.

When the cursor is on a part prefix, word block, lyric and chord symbol line, pressing F2 will bring up an edit window for simple modification, without opening corresponding dialogs. You can choose from normal and braille inputs via radio buttons.

Note: After editing a part prefix, a confirmation dialog will appear, asking you whether to change the prefix globally. This is useful when a part switches to another instrument or ensemble changes to solo. In notation programs, sighted engraver only hides part prefix and uses normal text to make such a change, but in braille, we must use corresponding prefix to make things clear.  
Note to BMML developers: In such case, the partlist will generate an extra sub-element to show a different prefix, from and to which measure. Or we can directly insert such tag within the score itself, like temporary midi instrument changes or part naming elements in Musicxml.

Selecting parts  
This function is copied from notation and sequencing softwares like Sibelius and Sonar. You can use ctrl+comma to select parts you want to delete, rename and move globally. For example, selecting parts 1 (piccolo) and 3 (oboes) and then select measure 5-12, then choose [Part management](#2-4), renaming the prefixes will ask you whether to rename them globally or just for selected measures. This will also ease modification for temporary divisi or instrument changes for multiple parts.

Selecting music  
Common selection may be done usinh shift plus arrows. Ctrl+shift+left/right will select bar(s). We can learn more selection functions by reading the Sibelius' reference manual.

Context menu for marking items  
Besides common edit context items, here are some special ones:  
Hide/Unhide  
This is an option for selected objects such as rests, to hide them in braille. For example, a harp glissando with 7 32nd notes to indicate string tuning, and then a gliss line to a note far from them. The intermediate rests can be hidden if the measure has no other notes after this series of notes. If unhide, the rests will be preceded by dot 5.  
The same thing is applicable for repeated texts which appear for more than one staves. For example, a tempo mark will appear on top of both piccolo and first violin parts, or even all parts.  
Tagging  
Change the property of current selected braille character(s). Available choices are text-music, text-non-music, text-title, text-subtitle, text-composer, text-lyricist, lyrics, chords, metronome marks, rehearsal marks, articulation and other.  
Property  
This dialog will define the property of current selected character(s). Choices are: isolate, before note and after note. When isolated, a line break can take place on either side of the object; before note will put line break only before it; and after note puts line break only after it.  
Part/Text/Lyrics/Chords/Metronome/Percussion management  
These are the same dialogs introduced before, but only display selected items on-the-fly. When on a specified item, dialogs of other properties will be unavailable.

Convert slur  
This option will convert slur in the current phrase, either from common (dots 14) to phrasing (dots 56,12 for open, and 45,23 for close) or vice versa. Normally, except vocal part, the software will apply phrasing slur when the phrase is very long, usually more than 5 notes. Or we can set the phrase length for detection. Note that this conversion is not applied to the music with nested slurs, since all slurs except the most inner one should always be phrasing slurs. Phasing slurs can be nested, while common slurs can not (because they have no open and close indications).

combining and split  
There must be a submenu of this. When in post production, sometimes a multipart braille system containing only one measure can be combined to another one, or a multimeasure braille system has to be splitted into two (after adding missing items) or more.  
Combine with  
Placing the cursor to the measure and choose it. This will let you choose whether to combine with previous or next measure. A confirmation prompt appears, answer Yes.  
When in bar-over-bar and BrailleOrch mode, a warning will appear if the result will make extra line break(s). In line-over-line format, a warning appears if all parts have new line breaks. Choose Cancel to abort.  
Make new braille system  
Will start a new braille system from the current measure. A confirmation prompt will appear. Answer Yes.

**********

<h3 id="7-3">7.3 Keyboard Style</h3>

We should dedicate a section to keyboard music. The following are all in the Keyboard Options submenu.

<h4 id="7-3-1">7.3.1 The Keyboard Options Dialog</h4>

The dialog will be shown automatically when a score contains multi-staff part(s), and the number of staves in one of the parts is no more than 4, and, we haven't dealt with them in the [Transcription Dialog](#2-1).

It will show all parts required for configuration. The options such as "Treat as" and "Assign hand signs" are the same as they were introduced before.

Details for Assign hand signs sub-dialog:  
The button brings up this dialog. Usually, upper staff or treble staves (except the last one) in a multi-staff part will get right-hand prefix(es), while lower staff or bass staves (except the first one) in a multi-staff part will get left-hand prefix(es). This dialog will override default judgement of the software.

Set for (radio buttons)  
Initial (default)
Current parallel  
From current to end  
From beginning to current  
These radio buttons are not visible in the same dialog in Settings, because that is for global controlling. The change will force interval direction of the affected passage. Objects such as fingering will go with the reordered notes/intervals.

**********

<h4 id="7-3-2">7.3.2 Other Contextual Options</h4>

Add hand changes for selected passage  
This is for piano or other keyboard music where some hand changes occur on one staff with direction change of stems. This dialog will let you choose which direction is for which hand, and add hand signs into the passage. Voice containing notes of another staff will always show appropriate hand changes.

Users can also select a passage and add hand signs manually, by entering braille directly or choosing approriate signs (rh, rh for lh, lh, and lh for rh) from the menu. It's adviceable to use special hand signs for passage containing intervals in music for alternated hands written in one part. But old standard is still possible. Anyway, interval direction is determined by the initial hand prefix.

Remove empty  
Remove all empty  
When one staff only contains "forward" instead of measure rest, we can either remove it or keep it filled with a measure rest preceded by dot 5. If choose to remove, and system numbers are shown, the first parallel of the system must keep completely, for we must have a staff for placing line numbers. But this is not used for chamber and orchestral music. The latter option is designed for this case.

**********

<h3 id="7-4">7.4 Percussion Problems</h3>

This is a really tricky topic. Percussion and drums are notated in various forms, from 1-line to 5-line staves, either pitched or unpitched. Here we are discussing implementation of managing unpitched percussion parts.

Although unpitched percussion instruments are unpitched, the notation softwares must require specific pitches to put them on staff line(s). Especially in drumkit part, the General Midi drumkit definition has lots of pitches to put different instruments and playing techniques on different positions. In braille, the rule is to transcribe them as bass clef instruments, or defining pitches which are convenient to read. For the latter, we can just leave the internal pitches unchanged. Now we'll deal with the former case.

When the [Percussion Dialog](#2-9) opens, there are two listboxes. The first lists out all unpitched percussion part(s) in the current score, and the second lists out available note pitch(es) in the part selected in the first list. Pitches are displayed as letters with octave number, e.g., B4 for B on the third line of a treble staff, and also a usual percussion pitch on a 1-line staff. Press Edit button to enter a new pitch such as C3, the common use of braille bass note (e.g., 456,13456). The pitches are also displayed in braille as whole notes, and there's also an edit field for braille input in the Edit dialog. Changing one of these will affect the other's display. So you needn't worry about not knowing how to choose correct note names and octaves.

Press "transcribe" button to apply new transcription to the part(s). The software will re-map all pitches to the defined ones in braille. If you need to retranscribe the braille as original pitches, just open the dialog and press "reset to original" and "transcribe" buttons.

So, for BMML, we must store both the original and modified pitches.

**********

<h3 id="7-5">7.5 Split And Merge</h3>

When a score is too large to fit in one braille volume, we can split it into two or more volumes. When we want multiple transcribers to work on a single volume score to speed up the work, we can first split, then merge the sections in the same project. This is why the split and merge functions are needed. In the [file menu](#1-1), we find these two options. Each opens a corresponding dialog, and they will be discussed below.

<h4 id="7-5-1">7.5.1 Split Dialog</h4>

Split point view  
This list will show split points the user set in [Braille music menu](#1-6). Every item has a checkbox. Choose the required point(s) and press Split button to finish. If none is found, we can't use automatic split function, and then set the split rules here.

Below the list there's a combo box for splitting rules. The first  is split points. If this is still chosen, the software will warn and ask you whether to return to the score and set points manually. If answering no, we can continue with other options.

The second option is print page, and the third option is braille page. These will display a edit spinbox for choosing page numbers. When print page is chosen, the new braille volume will create a new braille page if the print page begins at the middle of a braille page, unless the following checkbox "maintain braille pagination" is chosen. In such a case, the beginning of the new volume will contain an incomplete braille page for merging purpose.

The fourth option is measure and movement. This will display  a list of measures. When double or final barlines are found, the word "double", "dotted" or "final" will be added after the number. If there  are measure changes for multiple movement, an additional number will be added before measure numbers. E.g., 1 15, 2 30 double, etc. There's also an option for whether maintaining braille page.

Add title page to new volumes (checkbox)  
Whether to apply title page information. If every volume is checked for this, then volume numbers will be filled in the title page automatically, using the language and translation table set in the file.

Continuous braille page (checkbox)  
When unchecked, the new volumes will always begin with braille page 1.

Continuous measure numbers (checkbox)  
If unchecked, the new volume begins with measure 1.

Add volume (button)  
Add a split point according to the above rule. The user can add multiple volumes by continuing selecting pages or measures.

Split  
After adding volumes, we can finish with this button. The software will create separated files with the same name and a number after them. Each BMML file will store information such as file order, continuation of measures and pages, etc. An INI file is also created to list the files and various options, which are needed for merging.

**********

<h4 id="7-5-2">7.5.2 Merge Dialog</h4>

When the dialog is opened, we are first asked to upload the INI file created when splitting. If no we choose "skip", then please read [the next section](#7-4-3).

Once the INI file is loaded, the real option dialog appears. There's a list of all volumes found. You can navigate in the list and delete the unwanted item(s). However, non-adjacent volumes are not allowed. For example, for volumes 1-7, you can only merge volumes like 1, 2 and 3, 3, 4, 5 and 6, or 6 and 7, but not 1, 3 and 4. This option is provided for either combining transcribed parts, or a transcriber who wants to transcribe more volumes which are not finished by others.

Braille pagination (combo box)  
Keep original  
Create new page  
Keep original means you can combine incomplete braille pages between volumes. If either or both of the half are changed, the software will warn and give a choice for re-paging. Create new page takes no effect when the new volume begins at the top of the page.

Measure option (combo box)  
Keeporiginal  
Create double barline  
Create final barline  
Create new movement  
If there are already double or final barline or new movements at the beginning of new volume, just keep the original. Create new movement means the new volume begins at measure 1.

Merge (button)  
Merge the selected volumes and create the file. If all volumes are checked, the result file will replace volume numbers with "merge". If parts of the volumes are checked, the result file will add merged volume numbers, e.g., score_v1-2-3.

**********

<h4 id="7-5-3">7.5.3 Merge Non-splitted Files</h4>

There may be circumstance that we have to combine separate files which are not from split function into one book. For example, there are several pieces in a book engraved in separated files, or a symphony may have different instrument layout at different places, which has to use separate files to engrave. In such case, we have to skip the INI file and use alternative merging function specified for this situation. The merged files may have a combination of splitted files, but it's unable to use the INI file.

In the dialog, we must manually add files, and the order can be adjusted by pressing moving up/down buttons.

The other options may be as the same as the common merge function. Since every part may have different instrument definitions, the merged BMML file has to keep each part as individual portions, but not simple movements. However, if the instrument definitions are exactly the same, the software will try to make them into one with or without movements, chosen by the user. This can be discussed when enhancing BMML.

**********

<h3 id="7-6">7.6 Debugging Mode</h3>

This is a special tool for advanced users or developers to find errors in both Musicxml and BMML, or define new translation features when new version of Musicxml is released. Most of the errors are from incomplete musicxml, or some undeveloped features making BrailleOrch ill. The debugging mode will show errors and let you correct fatal errors on-the-fly. Newly defined features can be stored in the user definition file for future use. If I die one day, or if my team dismiss one day, future users can still keep my software new with the latest version of musicxml, as long as they know how to do it.

This mode will generate two extra windows linked to the main braille edit window (ctrl+1), one for Musicxml (ctrl+2) and the other BMML (ctrl+3) respectively. Ctrl+tab and shift+ctrl+tab can also cycle among these windows.

When navigating in one window, the other two will also be updated. For example, when navigated to a new note in braille, the other two will put the cursor to the first line of this entry.

Toolbar:  
find error (ctrl+F2)  
List all errors in a box to choose. The list shows errors layouted as part-measure-voice-beat. Press OK to jump there.  
Next error (Ctrl+F5)  
Previous error (ctrl+F3)  
Ignore (ctrl+)  
Mark such item as "other" quickly.

In the two xml windows, you can't do any copy/paste functions, but can still enter and delete, for example, correcting or deleting garbage codes (Finale often exports Chinese as garbage codes), and fix mismatched element entry. This way, copyrighted print materials will not be duplicated by end-users (unless he/she has enough time and patience to re-type thousands or millions of xml lines!).

For compressed Musicxml files (.mxl), some pieces may contain pictures for either cover pages or unusual music symbols or others. When images are available, there are two ways to access them visually on the screen:  
1\. Press Ctrl+I in the Musicxml window. If BrailleOrch finds any images, a list will appear, describing filename, part, staff and bar numbers. Choose one and press enter or OK, the picture can display on the screen, and the cursor will locate on the image link code.  
2\. On a line of image source link, press Ctrl+Alt+I to view this image.

**********

<h3 id="7-7">7.7 Defining New Features</h3>

Sometimes a musicxml file contains advanced symbols which are not available in braille, or there are unknown, unrecognized and unexported signs marked as certain tags, or there may contain dozens of images for symbols or lines not available in the notation software. Moreover, as musicxml version updates, more unexpected elements can be included, such as tons of glyphs from [SMUFL](http://www.smufl.org) fonts. So we must invent a tool to store our new definitions, without troubling the programmers to update the software too frequently. The defined rules and signs will be stored as a user configuration file in "My Document\BrailleOrch\User Config" folder, and can be shared and even included in future versions of the software.

In the Musicxml window, choose "Search for unknown" (ctrl+u), and the software will bring us to the first place it finds an unrecognized thing, including those marked as "other" except dynamic marks. Some of these are hidden in braille, with only symbol description, because there are no existing braille equivalent symbols. Press Ctrl+d to define. Or press ctrl+shift+u to list all unrecognized signs and images. In the list, press Enter to go to the place, or choose Define to begin the definition.

Definition dialog:  
Braille symbol  
Enter a braille symbol for the current selected item.  
Position (radio button)  
Before note, before articulation, after note  
After note includes fingering and harmonics which must be always placed right after a note.  
Doubling (checkbox)  
If checked, the sign can be doubled. Enter beginning and ending rules in the two  boxes below.  
Starting/Ending point (radio button)  
None, start, stop  
Some element has start and stop values, such as a line. We can first define a start sign, and then define a different stop sign. Please read the xml tag carefully before making this choice.  
Set globally (checkbox)  
Set for the whole score.  
Set as standard (checkbox)  
Store it to the user configuration file for future use. When BrailleOrch is launched the next time, the defined items will be automatically transcribed for all musicxml files.

You can create a branch on Github, and upload your definitions there. Or we can build a library where users share their definitions to help us update the software. This will benefit all future users.

**********

<h3 id="7-8">7.8 The Play-along Function</h3>

The brand-new Play-along function will make BrailleOrch like a common notation program, letting blind musicians read and play/sing the music along playback. the cursor and line will follow the playback. Since the current braille displays only has one line to display braille, the user must first choose an instrument (or hand of the piano) to follow.  
When pressing ctrl+alt+l, we enter the mode. A dialog will appear, asking you to choose which instrument and which measure it will follow. The default will be the current instrument and the current measure. By pressing Enter or OK button, the software comes back to the normal working area with a report of screen reader "play-along". Now, all editing functions will be disabled, and we enter the play-along mode. To exit this mode, choose Play-along from the Playback menu or press the shortcut again. The screen reader will say "play-allong off".

In this mode:  
pressing Space to start/stop playback;  
pressing shift+space to pause/play playback;  
Pressing "b" to play the current measure;  
Pressing "v" to play the current voice:  
Pressing "p" to play the current measure of the current part;  
Pressing shift+p to play the current part from the current location;  
Press "s" to solo current instrument when playing globally,press again to unsolo;  
Press "m" to mute current instrument when playing globally,press again to unmute;  
Pressing left+right arrow to jump backward/forward one measure;  
Pressing up/down arrow to jump to the previous/next instrument or hand;  
Pressing alt+up/down to cycle among voices on the staff.  
Press ctrl+up/down to make tempo faster/slower regardless the tempo setting in the original file;  
TBC: playback of other selections; navigation and playback etc.

**********

<h2 id="contact">Contact Information</h2>

If you have any questions about music, braille and this framework, or want to help me to make this framework to come true, please feel free to [write to me](mailto:hhpcomposer@gmail.com).

Thank you in advance!

**********

