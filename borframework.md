# Borframework - BrailleOrch Software Development Framework

By Hu Haipeng

Date: Jan 31, 2016  
First draft: Feb 26, 2016  
Last updated: Sep 22, 2017  

Project holder: [Daniel Barich](mailto:barichd@kenyon.edu)  
Project designer: [Hu Haipeng](mailto:hhpcomposer@gmail.com)  
Project development website: <https://github.com/barichd/brailleorch>

Copyright (C) 2017 By Hu Haipeng and Daniel Barich.

**********

BrailleOrch is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

BrailleOrch is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with BrailleOrch. If not, see <http://www.gnu.org/licenses/>.

**********

# Contents

Preliminary Materials

- [A. Purpose](#purpose)
- [B. About This Framework](#framework)
- [C. About BrailleOrch And BMML Formats](#formats)
- [D. Braille Music Notation Codebooks Used In This Development](#codebooks)
- [E. Capabilities The Software Must Reach](#capability)
- [F. Development Requirements](#requirements)
- [G. Working Progress](#progress)

Part I: General Overview Of The Software

- [Chapter 1: Menus Overview](#overview)
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
- [Chapter 2: Deeper view of transcription functions](#transcription)
- [2.1 Transcription Dialog](#2-1)
- [2.2 Transpose Dialog](#2-2)
- [2.3 Score Management Dialog](#2-3)
- [2.4 Part Management Dialog](#2-4)
- [2.5 Text Management Dialog](#2-5)
- [2.6 Lyrics Management Dialog](#2-6)
- [2.7 Chords Dialog](#2-7)
- [2.8 Metronome Dialog](#2-8)
- [Chapter 3: Settings Dialog](#settings)
- [3.1 General Page](#3-1)
- [3.2 Transcription Page](#3-2)
- [3.3 Single-line Page](#3-3)
- [3.4 Bar-over-bar Page](#3-4)
- [3.5 Line-over-line Page](#3-5)
- [3.6 Section-by-section Page](#3-6)
- [3.7 BrailleOrch Format Page](#3-7)

Part II: General References Of Points During Development

- [Chapter 4: BMML Enhancements](#bmml)
- [4.1 Limited Learning Resources](4-1)
- [4.2 Implementation Steps](#4-2)
- [Chapter 5: Braille Specified Points](#braille)
- [5.1 Braille Window](#5-1)
- [5.2 Navigation In The Score](#5-2)
- [5.3 Transcription related](#5-3)
- [Chapter 6: Braille Music Editing And Debugging Related Points](#editing)
- [6.1 GUI specifications](#6-1)
- [6.2 Entering And Marking Items, Transcription Related](#6-2)
- [6.3 Debugging Mode](#6-3)
- [6.4 Define New Features](#6-4)
- [Chapter 7: Play-along Function Overview](#playalong)
- [Contact Information](#contact)

**********

# Preliminary Materials

<h2 id="purpose">A. Purpose</h2>

This is a detailed framework of BrailleOrch, braille music transcription software for advanced formatting and publishing purpose. The final software will convert Musicxml files, or via a separate plugin, Sibelius files, into our extended Braille Music Markup Language (BMML) format (originally created, developed and copyrighted by [Veia Progetti s.r.l.](http://www.veia.it), Italy, as free software. See copyright information in the BMML package for details), which can be flexibly edited and modified, to fulfill most of the requirements of braille music publishment.

Since this software is free, and under GPL and Veia free software licenses, anyone who are willing to help us can join in to develop and enhance it. We welcome people around the world to do anything making convenience to braille music production for blind musicians.

**********

<h2 id="framework">B. About This Framework</h2>

This comprehensive document will describe all menus and functions of BrailleOrch. People who wants to develop/enhance the software must read it carefully. The first three chapters give a general overview of the software's menus and functions, and the remaining four chapters give detailed development points on improving BMML and Musicxml-to-braille transcription, and advanced braille editing, debugging and playing functions. More in-depth issues will be discussed in a future mailinglist or forum during the development process. Only critical issues needed to be done are shown here. For detailed rules of braille and braille music, please always consult the [codebooks](#codebooks) mentioned below.

**********

<h2 id="formats">C. About BrailleOrch And BMML Formats</h2>

BrailleOrch (.bor) format is a compressed file. It contains original musicxml (if transcribed from musicxml) and bmml sources, and additional debugging information such as error records. When the final editing and correction has been finished, the musicxml source and most debugging information can be removed to save file size. People can still edit and reformat braille output, though. See Make final document in File Menu.

For BMML format, I think we should design two stages.  
The one is the current format, and we can just extend it to include more signs and functions. This kind of BMML file contains both musical and braille information.  
The second one is a BMML file which is just a mapped format from Musicxml, and is ready for braille transcription. Music publishers can first generate such an intermediate file for transcribers or end users, and the braille users can check and format music with their own preferences. This format can be developed later, since it needs very smart on-the-fly formatting. and previewing functions of the software. This format is inspired by Sunshine professional, a Chinese braille translation software made by China Braille Publishing House. The wording, hyphening and formatting are constantly changed while the user is editing the file, like MS Word, and this interface is very friendly and smart.  

**********

<h2 id="codebooks">D. Braille Music Notation Codebooks Used In This Development</h2>

The braille music code used to manage the transcription work is based on New International Manual Of Braille Music Notation published in 1996 in Switzerland. You can download a MS Word version [here](http://www.rnib.org.uk/sites/default/files/New%20International%20Manual.doc).  
Also, some additional features and symbols may be taken from the newer codebook Music Braille Code 2015 published in The US. Since this book is mainly used by American countries, the New International Manual will always be the first reference. You can download the 2015 American code as both PDF and Braille formats [here](http://www.brailleauthority.org/music/music.html).  
In future development, we can implement both codebooks to output both formats via the users' choice.

**********

<h2 id="capability">E. Capabilities The Software Must Reach</h2>

- Convert Musicxml files directly into well-formatted braille music scorres, leaving few post-editing effort to the users
- Transcribe all kinds of music from instrumental and vocal solo to complicated symphonic and dramatic works
- Brief and clear description of music objects via screen readers while navigating
- Flexible playback functions, including a smart play-along mode, to enhance the learning speed for blind musicians
- Powerful and flexible editing and formatting ability for both blind users and sighted transcribers
- Support bar-over-bar, line-over-line, section-by-section and customized BrailleOrch formats, to fit most countries' braille music publishing standards
- Support transposition, part extraction etc, producing various editions from one document
- Support multiple language braille output with the help of Liblouis translation tables
- Smart copy protection mechanism for music publishers to work with braille music transcribers
- Two-sided xml integration for developers
- Powerful xml debugging mode for dealing with Musicxml with problems or new features
- Support user-defined new symbols and features, to let the software keep up with the latest music and Musicxml techniques

**********

<h2 id="require">F. Development Requirements</h2>

An experienced C++ or Python skill plus XML knowledge is required for developing this software. C++ can process large XML files fast, but Python or other advanced languages can make programing easier. We have to decide what programing language or language combination should be used. A basic Git knowledge is required for committing changes. Knowledge of music, musicxml, braille and/or braille music is recommended, which will largely enhance the efficiency and quality of development. Sibelius Manuscript Language is required if anyone who wants to make a BrailleOrch export plugin for Sibelius (see the fifth phase in [the next section](#progress)). Some items in Sibelius can't be correctly exported into musicxml via its internal export function and/or Dolet For Sibelius plugin.

Besides general components for software development, we also need the following:

- A screen reader like Jaws (commercial) or NVDA (free) for accessibility test  
- [Liblouis](http://www.liblouis.org) for multilingual braille translation  
- Plenty of Musicxml and braille music sources, which I can provide during the development

The software will run under any Microsoft Windows systems, from Windows 2000/XP to Windows 10, both 32 and 64 bits. A screen reader such as NVDA is required for announcing unicode braille objects. Music publishers and sighted braille transcribers are not asked for this option.

**********

<h2 id="progress">G. Working Progress</h2>

Since this is an extensive project for a highly sophisticated software, we have to divide the development session into several phases.

The first phase is to build up a general GUI, containing basic menus and functions. Use original BMML source and extend it. Map most Musicxml elements except visual layout to BMML, create coresponding braille symbol elements, and define rules for transcription. Basic functions in Page setup, Score/Part/Text/Lyrics/Chords/Metronome management and Transcription options dialogs should be done. Bar-over-bar and line-over-line formats are firstly considered, also my special BrailleOrch format is OK. The result braille music score can represent at least 95% information of print version. The  score can be manually edited, but not reformatted and retagged automatically, since this requires deeper research of BMML and further development of the software. The user-edited strings are gray-colored, and simply marked as "other" in BMML, and can be tagged in future versions of the software.

The second phase is to enhance transcription quality. Items in Musicxml 3.1 or later should be added, and the formatting function must be more flexible. Add [Define New Features](#6-4) function. Add section-by-section format. Enhance translation table to add support to Chinese Mandarin braille (Cantonese and Taiwanese Chinese braille have already been done in Liblouis).

The third phase is to enhance the reformatting function. The software can recognize most user-entered strings as music signs, texts etc, and can correctly break lines when reformatted.

The fourth phase is to develop the Play-along function described in the last chapter. This will ease braille music reading, and enhance the learning progress and quality for blind musicians.

The fifth phase is to develop a Sibelius plug-in, directly exporting .bor files from Sibelius. Musicxml exported from Sibelius has some information missing, because there are special user items. We can use Manuscript Language to make the braille version more close to the original score. Unspecified items can also be exported and tagged for manual editing. BMML exported from this plugin is not correctly formatted, so this tool has to be delayed to the time BrailleOrch is powerful and flexible enough.

The last phase is to develop the braille music composing function. Since the software can already recognize common braille music signs entered, the main focus is on advanced signs, creating parts and groups, writing chord symbols, handling visual appearance, Midi functions etc.

**********

# Part I: General Overview Of The Software

<h2 id="overview">Chapter 1: Menus Overview</h2>

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

Set copy protection  
This is a special function for protecting music pubisher's copyright. After they convert their scores into musicxml and import into BrailleOrch, they can immediately set this option. The braille score can still be edited, reformatted and embossed, but can't be exported into musicxml for back-translation. The file is also encrypted, so it also can't be saved as bmml format. Any debugging process upon the xml source and bmml score can, however, be done using the internal [debugging](#6-3) interface.  
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
Show page turn: checkbox, visible when Print page numbers is checked. Page turn includes dots 5 2-5 with (or without) new page number.  
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
Format or reformat the braille score after manual editing and correction. Formatting layout will follow rules set in Score/Part/Text/Lyrics/Chords/Metronome, Options and Page setup dialogs. Options changed after transcription process can also be applied.

Debugging mode  
A special mode used for checking errors and enhancing the software. See [Debugging Mode](#6-3) for details.

Output interval direction description  
A dialog appears, letting you to view the description. There are 2 kinds of description:  
1\. When all intervals are up/down, it will let you choose from two methods of descriptions:  
a. Literary: All intervals are read upwards/downwards;  
b. Notation: a C with second interval sign, space, two dots 3-5's, space, two notes with in-accord, either C-D or C-B.  
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

Input (submenu)  
Insert notes (n)  
Enter notes/rests/voices, generally all music-related signs.  
Insert texts (x)  
Enter texts using standard input method. Untranslated unicode texts such as Chinese will be accepted, and can be edited later. All text-related adjustment can be done in [Text management dialog](#2-5).  
Insert key signature (shift+k) (to solve conflict with braille key)  
Insert time signature (t)  
These two use braille input.  
Insert chord names and figured bass (c)  
Braille input of chord and figure symbols.  
Insert title page information (i)  
Insert title info at top of system. See [Score management dialog](#2-3) for details.  
There's a checkbox for inserting title information on a blank page. If checked, a blank page will be created.  
Insert footnotes (o)  
Add a line of dots 2-5's plus footnotes.  
Insert division signs (v)  
Centered 12 division characters. Choose from dots 2-5's and dot 5's.  
Insert new print page (shift+p)  
Insert new braille page (shift+b)  
These are for modification and/or reformatting, or when no print pages are available in musicxml 1.0. Also useful when developing braille music composing. Print page will be inserted at the beginning of the measure, while braille page will be inserted at the beginning of the current braille line.  
Set current measure number (m)  
Set number of current measure, overriding measure numbering in Musicxml. The consequent measure numbers will be changed accordingly, until Musicxml specifies a new sequence of measure numbers (e.g., starting a new movement from measure 1 or 0).  
Set current braille page (b)  
Set current braille page number. The extra choices for numbering are arabic, roman, lower-celled and (for title pages) none.  
Set current print page (p)  
Set current print page number, overriding Musicxml's settings. The extra choices are arabic, roman and none.

Other tags and properties can be marked using context menu directly on braille objects. Transcribers can also edit the score without using the above insert and context functions, but the result input will be marked as "other" in BMML, and can't be automatically reformatted correctly. They should be manually formatted.

Display images  
This menu is for extracting pictures contained in compressed Musicxml files (.mxl), which may be cover page images or special music symbols not being able to enter in notation programs. The listbox describes the details of every image file as this:  
filename, part number, staff number, bar number, and beat position.  
Press View to read the image on screen, and press OK to bring the cursor to the location for transcribers to enter appropriate braille symbols. Press Define to define a symbol globally in this score. See [Define New Features](#6-4) for details.

Transpose  
This dialog will handle score/parts transposition. See [corresponding section](#2-2) for details.

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

**********

<h3 id="1-7">1.7 Playback</h3>

Play/stop (ctrl+l)  
Play current measure (shift+l)  
Play current part (ctrl+;)  
Play current voice (shift+;)  
Play metronome (default unchecked)  
Enter Play-along mode: ctrl+alt+l  
See the [last chapter](#playalong) for Play-along descriptions.

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
Generally, Braille will announce things like "dot 5, dots 1 4 5", and Object will announce "fourth octave, C eighth". Detailed indications for specified items may be discussed while developing.

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

The software will treat score with only one part with one staff as single-line format. It will automatically treat score with only one part with two to four staves as piano (or organ, chosen by the user) format. It will treat score with one single-line part above one multi-stave part as solo with keyboard accompaniment part, and add dots 5 3-4-5 prefix before the single-line part.

<h3 id="2-1">2.1 Transcription Dialog</h3>

Note: All dialogs in this software have "ok" and "cancel" buttons.

When importing a Musicxml file, the software brings up a dialog, giving the users options for adjusting transcription appearance. It can be turned off by checking "Don't show this dialog again" at the bottom of the dialog, or via [Settings dialog](#settings). The last settings will be stored, and users can override these options in [Settings dialog](#settings). The Transcription dialog also contains lots of buttons to bring up corresponding options in that dialog.

Transcribe without formatting  
This checkbox will generate a non-formatted braille score, disregarding layout settings. This kind of bmml file only has musicxml-mirrored objects, no braille layout indications are included. Users can edit the score and then use Format in Transcription menu.  
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

Score/Part/Text/Lyrics/Chords/metronome management  
Bring up corresponding dialogs which are also available in [Braille Music menu](#1-6).

Transcription settings  
Bring up [Transcription settings](#3-2) in [Settings dialog](#settings).

Translation table  
Used for text translation. This can also be seen in Options and Score/Part/Text/Lyrics/Chords management dialogs.

Add hand change signs for selected passage  
This is for piano or other 2-staff music. See the same item in [section 7.2](#6-2) for details.

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
The TOC format is title plus dashes or dots (dot 3's or 5's, or dots 3-6's) plus page number. There are 2 columns, one for title, one for braille pages. Indentation of the title's line break is automatic.  
Division patterns (radio button)  
dashes (dots 3-6's), dot 3's and dot 5's.  
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
List all original items in <score-partlist> of Musicxml, plus part names caused by any instrument changes during the music.  
Items in this extensive table view can be navigated using up/down and left/right arrow keys, selected using shift+up/down, edited by pressing F2, and deleted using Del key. Its format is managed as the following grids from left to right:  
group name, group abbreviation, part ID, part name, and part abbreviation.  
If there are part names of instrument changes, these names and abbreviations will be marked as "instrument change".  
Any item will be left empty when none is found.  
Staves in a group will display group name and abbrev on all staves.  
When a multi-stave part is available, number or letter sequences will be added after the abbreviation names. Default is number.

Context menu items:  
Undo/Redo  
Common undo/redo function.  
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

Braille part list  
This table is used for editing braille part labels which can't be correctly transcribed. Braille input will be activated by pressing F2.

These two tables are linked, so scrolling one of them will also make the other scroll to the coresponding place.

Set interval direction dialog:  
Direction (combo box)  
According to clef  
Up/Down  
Keyboard
These 4 choices are for currently selected part(s). For clefs, treble and alto use descending intervals, while bass uses ascending intervals.  
Set globally (checkbox)  
Set current chosen interval direction to the whole score instead of selected part(s). Later operation on selected part(s) can override this setting.  
Include keyboard parts (checkbox)  
When checked, interval direction of keyboard instruments (including parts with piano property, such as organ and harp) will be changed regardless of common keyboard rules. This is useful in ensemble scores, in which all intervals should be in the same direction. In this case, the special hand signs should be used, i.e., 4-6 3-4-5 3-4-5 for treble reads upwards, etc.

Disregard instrument changes  
Will always use default part names and abbreviations.

**********

<h3 id="2-5">2.5 Text Management Dialog</h3>

A comprehensive dialog like [Part management dialog](#2-4). It lists out all texts items in the score. For dialog opened in this way, only words, credit items, rehearsal marks, instrument change texts, percussion beaters and DoletSibelius unrecognized system texts are listed. When opened using context menu in the braille score, items such as title page and TOC info can be displayed.

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
Mark as dynamic  
Some special dynamic markings such as "sffzp" are not treated as dynamic in notation programs. This will tag the current text as dynamic mark.  
Mark as metronome mark  
This will change the property into metronome mark. Sometimes, special metronome marks are not assigned correctly in Musicxml. BMML must be re-designed to accept user-defined texts as metronome marks such as 4=ca120. Sibelius also exports notes to letters such as q=120, and the user must edit it accordingly.  
Put word signs before every word  
Mark as rehearsal mark  
Rehearsal mark will be parenthesized, either within or above system.  
Long text blocks  
Use parenthesis  
These are 3 different functions. The first adds dots 3-4-5 before every word in the text block; the second puts dots 3-4-5 around the whole block, and makes a space before (except fore after part name, hand sign, sign for begin of repetition and clef sign) and after (except for end of line) the block; and the last adds parenthesis to the block, with a space before (except for the same condition) and after (except for the same condition) it.  
Chinese texts  
This will add Chinese music parenthesis (dots 5-6 3-6 and dots 3-6 2-3) around the text. Once the Chinese translation is available, this option will be removed.  
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
Toggle lyric sign (dots 5-6 2-3) on/off. Some countries don't use lyric sign.

Lyrics position  
Radio button, put lyric line above/below music. Default is below.

Use repetition (checkbox, default checked)  
If same word(s) are repeated, use repeat signs (one or two dots 3-5's and one 3-5 around the block, or number plus dots 3-5 before and dots 3-5 alone after it, when repetition is more than 3 times).

Add prefix before lyrics  
Add a singer prefix (without word sign) according to the part this lyric line is associated to.

<h3 id="2-7">2.7 Chords Management</h3>
This dialog will deal with chord symbols and figured bass. We'll implement them later. Just extract chord symbols in the xml source and transcribe according corresponding rules.

**********

<h3 id="2-8">2.8 Metronome Dialog</h3>

This is a list of all metronome marks in the score. Press F2 to edit in either braille or common mode (e.g., 4=120, 4.=80).

**********

<h2 id="settings">Chapter 3: Settings Dialog</h2>

Ah, we come to the most detailed chapter, wholely dedicated to the most sophisticated part--Settings dialog! This is a multipage dialog, with several category pages dealing with almost all problems with braille music transcription. Settings in this dialog will apply globally to any imported Musicxml files.

<h3 id="3-1">3.1 General Page</h3>

Default language (combo box)  
Current English only. More languages will be added later. You can even create your own language file.

Show transcription dialog after importing (checkbox, default checked)  
Whether show [Transcription dialog](#2-1) before processing Musicxml file. If not, the transcription will be done according to previously defined settings.

Open debugging dialog when fatal error occurs (radio button)  
Yes  
No  
Ask me first (default)  
When serious xml errors are found, the software will automatically open the [Debugging mode](#6-3) if Yes. You can use find error function to navigate in all 3 windows. In most case, braille window will be empty, so please choose Transcribe in [Transcription menu](#1-5) after correction.

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

Show capital signs (checkbox, default checked)  
Some countries don't show capital signs. Note that capital signs will always be removed when texts are using word sign prefix (dots 3-4-5).

UK metronome format (checkbox, default unchecked)  
Braille music produced in UK uses a different metronome expression. Instead of note-equals-number, it uses a sequence of stem sign, space, UK equal sign (dots 5-6 2-3-5-6) and number.

Signs to be transcribed (button)  
A dialog list out some signs. Uncheck some of them when transcribing scores for beginners.  
The signs are: clefs, fingerings, articulations, ornaments, lyrics, and chords. All are checked by default.

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

Add extra accidentals (combo box)  
None  
Voice only (default)  
Voice and measure  
For the same altered note in another voice, or a tied altered note in a new measure, add an extra accidental preceded by dot 5.

Add extra accidental to octave intervals (checkbox, default checked)  
When the above combo box is switched to Off, this checkbox will disappear.

Add extra tie to new system (checkbox, default unchecked)  
Some countries have such a custom, to add a reference tie when the tied measure starts at a new system in bar-over-bar/line-over-line formats, or a new section in section-by-section format.

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

Section prefix (combo box)  
System number only  
Show system numbers before every section of music. The format is a parenthesised item with "l"+number with number sign.  
Measure numbers only  
The same as system number, but with the prefix "b".  
System and measure numbers (default)  
Combine the above to into parenthesis, separated by a space.

Combine full-measure rests (checkbox)  
If not checked, multiple full-measure rests will not be combined, leaving every empty bar separated by space.  
If checked, two or three full-measure rests will be combined without spaces, and more than three full-measure rests will be combined as a number with one whole rest.

**********

<h3 id="3-4">3.4 Bar-over-bar Page</h3>

Extra octave marks (radio button)  
None  
New line only  
All (default)  
Add octave marks in every measure of a line, no matter whether they are necessary. New line means adding an extra octave mark in the middle of a measure at the beginning of its new line. Different country uses different custom.

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

Rehearsal mark placement (combo box)  
After part prefix  
Before part prefix  
Above music and measure number (default)  
Above music and left of measure number  
When the last choice is set, Above system for all measures must be turned to first measure in case of unsufficient room in the line. 

Add tracking dots (checkbox, default checked)  
When a line contains 7 and more spaces, tracking dots (dot 3) are added to ease navigation. Some countries don't use them.

Multi-piano format (radio button)  
Piano style (default)  
Chamber style  
When transcribing a multi-piano score, there are two different formats. Piano style is to add a lower-celled number after dots 3-4-5 of hand signs (e.g. 4-6 3-4-5 2 and 4-5-6 3-4-5 2 for second piano); chamber style will use the style like orchestral music, showing part prefixes.

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
After part prefixes  
Above system (default)  

Full score time signature placement (radio button)  
After part prefixes (default)  
Above system  
Two circumstances will override this setting, and print time signatures always within every part: 1. Different part has different time signature; 2. Time signature changes in the middle of a braille system.

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

No Add tracking dots

Add Combine full-measure rests checkbox

Ignore new system will turn off system number completely.

**********

<h3 id="3-6">3.6 Section-by-section Page</h3>

Section-by-section is used in many countries with varied layouts. Here, I choose some classical features for the users. If anyone who wants a different layout, please contact Daniel Barich for implementation.

Indentation (radio button)  
First line indent (default)  
Following lines indent  
These are two main different indentation styles.

Line-over-line style (checkbox, default unchecked)  
Only applicable to keyboard music. The layout is much like line-over-line, but line breaking is free for all staves.

Measure number placement for line-over-line style (radio button)  
Left of music (default)  
Above system

Section head format (radio button)  
Section only (section number)  
Measure only (measure number)  
Section and measure (default, plus number of first measure, no space and number sign. See next control)  
Section and measure range (section number, space, measure range)  
These are 4 classical head styles of a section.

Section+measure format (radio button)  
Section uper-celled  
Measure upper-celled (default)  
Section+measure range format (radio button)  
Section uper-celled (default)  
Measure upper-celled  
These two numbers are often in different type, one upper-celled while the other lower-celled.

Use system number as section number (checkbox, default unchecked)  
It uses system number on a print page for section number. So if a new page is here, the section number will return to 1.

Place blank line between sections (checkbox, default unchecked)  
See previous explanation.

Key signature placement: no Before part prefix  
Other options of key and time signatures are the same as previous two formats.  
Braille page turn is ignored, but print system change can't. This ensures the sections to sync to systems in print.  
Other options are nearly the same as line-over-line, including the Combine full-measure rests.

**********

<h3 id="3-7">3.7 Brailleorch Format Page</h3>

When transcribing orchestral scores, I developed a special format, and now name it BrailleOrch, because these scores are solely for my braille music project.  
In such a format, the layout is between bar-over-bar and line-over-line, where all measures in all parts are not vertically aligned, while all parts shouldn't have line break unless there's only one measure.

The options are nearly the same as in the previous two referred formats, and I extract them out for my format to have a specific control. If one would like to have some line breaks, there's also a checkbox to allow line breaks in any part.

**********

# Part II: General References Of Points During Development

<h2 id="bmml">Chapter 4: BMML Enhancements</h2>

The current BMML is an incomplete implementation. There are lots of items not mapped from Musicxml, and the DTD is based on Musicxml 2.0.

<h3 id="4-1">4.1 Limited Learning Resources</h3>

Before doing many enhancements, we must get to know BMML as much as possible. There's not a formal document describing every element of BMML, but we can learn from some sources. There are three documents from two different sites. Each of them gives information fragments about BMML's definition together with other points regarding braille music transcription. Some of the source websites mentioned in these articles are obsolete and in fact of no use.

- [site 1 article 1](https://www.irit.fr/publis/SIG/2008_ICOMP_EJMR.pdf)
- [site 1 article 2](https://www.irit.fr/publis/SIG/2009_TOISJ_EJMRA.pdf)
- [site 2 article](http://bpfe.eclap.eu/eclap/axmedis/a/a79/00000-a7927300-b90e-45b9-957d-d450c03d177e/2/~saved-on-db-a7927300-b90e-45b9-957d-d450c03d177e.pdf)

There are also two websites containing similar resources. They are two ended projects which developed BMML. The websites contain libraries of braille music scores in this format, and we can open and read them using Braille Music Reader it provides  for download. BMR is a read-only version of Braille Music Editor 2.

- [contrapunctus (older)](http://www.contrapunctus.it)
- [Music4vip (newer, now still running but not developing)](http://www.music4vip.eu)

Also, there's a Googlecode archive containing original Python scripts which converts Musicxml into BMML. It's also an old tool, but we can learn from it and develop our own implements. The download is not available now, but I can provide the complete repository at the beginning of the development.

**********

<h3 id="4-2">4.2 Implementation Steps</h3>

To make enhancements of BMML, we should first map most elements of Musicxml 3.0 or 3.1 to BMML, no matter whether the item has corresponding braille presentation, because braille music code is always under development, and can be flexibly customized. Layout information such as page/system/staff sizes and single object position can be ignored, because they are of no use in braille. Elements such as instrument changes and percussion beaters must be mapped as common texts but with special indications to reserve future development of BMML to Musicxml conversion.

Next, we need to create a convertion tool to generate braille according to the elements, and place both elements of musicxml and braille into BMML source using braille music rules. Symbols not implemented in braille can be left empty for future development or customizing using the Definition feature under Debugging Mode of the GUI. If the generated BMML doesn't contain formatting rules, it should not generate braille, because it needs reposition of elements. On the other hand, if initial formatting is changed after transcription, there may  be an additional implementation to store original position of elements to reserve correct reformatting. Or we can make an additional copy of BMML which contains the raw mappings to reserve these changes. Manually added, deleted or changed items should be marked to let the users choose whether to keep them during reformatting.

An additional note: Musicxml is formatted as either time-wise or part-wise, and almost all softwares export it as partwise. But BMML use part tags to render a quasi time-wise format, because braille music is not part-wise. However, we can imitate part-wise in BMML, and insert line breaks or other intermediate objects at certain places. This will ease future development of back-translation.

**********

<h2 id="braille">Chapter 5: Braille Specified Points</h2>

This chapter will be created and updated on scratch, but all of these points are critical for developing the software. General rules of braille music notation will not be repeated unless none of the current available softwares can do.

**********

<h3 id="5-1">5.1 Braille Window</h3>

The GUI of BrailleOrch, including the advanced [Debugging](#6-3) windows, must be plain edit fields. The following points are all related to the braille music window.

Since different countries have different mapping tables for ASCII to braille, we use Unicode braille from U+2800 to U+283F. The braille entries are already stored in BMML source, so we just need to make the stored Unicode values displayed as braille. To benefit sighted users, we can marked correctly mapped braille with normal color, places containing errors marked as red, and manually entered unprocessed braille as yellow. Sighted user can choose to display more indications like placing vertical bars at bar lines, thin horizontal lines to separate parts (staves), and thick horizontal lines to separate systems (system means a whole group of staves).

**********

<h3 id="5-2">5.2 Navigation In The Score</h3>

When navigating in braille mode, just braille dots are reported.  
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

<h3 id="5-3">5.3 Transcription related</h3>

In bar-over-bar, line-over-line and BrailleOrch formats, we must let the software smartly detect how many bars it can fit on one line according to the current page settings. Especially in bar-over-bar and BrailleOrch, the amount of bars is also determined by other parts in the same braille   system.

Line break during the music within a bar must have a music hyphen (dot 5) at the end of the line. If the line breaks after a word in long text block, music hyphen is not needed. Although a text block is treated as one "words" element in Musicxml, we must allow the software to add line breaks smartly, or allow manual line breaks, while still keeping the whole block as one object in BMML. Then BMML must contain a line break command on the braille side.

**********

<h2 id="editing">Chapter 6: Braille Music Editing And Debugging Related Points</h2>

This chapter discusses braille music editing and correction related subjects.

<h3 id="6-1">6.1 GUI Specifications</h3>

The working area of BrailleOrch is an edit window like Windows notepad. Items entered and displayed here are all unicode braille. Untranslatable items such as Chinese characters are displayed as yellow question marks, and in braille output, a set of computer-braille question marks (dots 1-4-5-6). Untagged items such as user-entered customized items are marked as "other" in bmml and displayed in gray. BrailleOrch can also ignore non-fatal musicxml errors, and displays such problematic items in red. Very serious error such as unmatched element tags will generate warnings, and store the xml into .bor file for debugging. Once debugging is finished, it can then be transcribed using Transcribe under [Transcription Menu](#1-5).

Items in the edit window must be announced via screen readers such as NVDA. The description should be as brief but clear as possible. Dots should also be announced. Settings of announcing modes are in Options Menu.

**********

<h3 id="6-2">6.2 Entering, Selecting And Marking Items, Transcription Related</h3>

When correcting the music, for example, adding missing signs, moving words' position etc, please press letter n to start entering notes/rests/articulations. BrailleOrch will recognize them automatically. Unfinished enter will be tagged and announced as "other".  
(Note: make this complicated function later, now just tag all user-entered strings as "other". So reformatting of individual lines must be done manually, like manual transcription.)  
For moving words, please put cursor on any location within the word block, and right-click, choose "Cut", and paste it to new location. BrailleOrch always treats a word block as a single object.

When the cursor is on a part prefix, word block, lyric and chord symbol line, pressing F2 will bring up an edit window for simple modification, without opening corresponding dialogs. You can choose from normal and braille inputs via radio buttons.

Note: After editing a part prefix, a confirmation dialog will appear, asking you whether to change the prefix globally. This is useful when a part switches to another instrument or ensemble changes to solo. In notation programs, sighted engraver only hides part prefix and uses normal text to make such a change, but in braille, we must use corresponding prefix to make things clear.  
Note to BMML developers: In such case, the partlist will generate an extra sub-element to show a different prefix, from and to which measure. Or we can directly insert such tag within the score itself, like temporary midi instrument changes or part naming elements in Musicxml.

Selecting parts  
This function is copied from notation and sequencing softwares like Sibelius and Sonar. You can use ctrl+comma to select parts you want to delete, rename and move globally. For example, selecting parts 1 (piccolo) and 3 (oboes) and then select measure 5-12, then choose [Part management](#2-4), renaming the prefixes will ask you whether to rename them globally or just for selected measures. This will also ease modification for temporary divisi or instrument changes for multiple parts.

Context menu for marking items  
Besides common edit context items, here are some special ones:  
Hide/Unhide  
This is an option for selected objects such as rests, to hide them in braille. For example, a harp glissando with 7 32nd notes to indicate string tuning, and then a gliss line to a note far from them. The intermediate rests can be hidden if the measure has no other notes after this series of notes. If unhide, the rests will be preceded by dot 5.  
The same thing is applicable for repeated texts which appear for more than one staves. For example, a tempo mark will appear on top of both piccolo and first violin parts, or even all parts.  
Tagging  
Change the property of current selected braille character(s). Available choices are text-music, text-non-music, text-title, text-subtitle, text-composer, text-lyricist, lyrics, chords, metronome marks, rehearsal marks, articulation and other.  
Property  
This dialog will define the property of current selected character(s). Choices are: isolate, before note and after note. When isolated, a line break can take place on either side of the object; before note will put line break only before it; and after note puts line break only after it.  
Part/Text/Lyrics/Chords/Metronome management  
These are the same dialogs introduced before, but only display selected items on-the-fly. When on a specified item, dialogs of other properties will be unavailable.

Add hand change signs for selected passage  
This is for piano or other 2-staff music where some hand changes occur on one staff with direction change of stems. This dialog will let you choose which direction is for which hand, and add hand signs into the passage.

combining and split  
There must be a submenu of this. When in post production, sometimes a multipart braille system containing only one measure can be combined to another one, or a multimeasure braille system has to be splitted into two (after adding missing items) or more.  
Combine with  
Placing the cursor to the measure and choose it. This will let you choose whether to combine with previous or next measure. A confirmation prompt appears, answer Yes.  
When in bar-over-bar and BrailleOrch mode, a warning will appear if the result will make extra line break(s). In line-over-line format, a warning appears if all parts have new line breaks. Choose Cancel to abort.  
Make new braille system  
Will start a new braille system from the current measure. A confirmation prompt will appear. Answer Yes.

**********

<h3 id="6-3">6.3 Debugging Mode</h3>

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

<h3 id="6-4">6.4 Defining New Features</h3>

Sometimes a musicxml file contains advanced symbols which are not available in braille, or there are unexported signs marked as certain tags, or there may contain dozens of images. Moreover, as musicxml version updates, more unknown elements can be included. So we must invent a tool to store our new definitions, without troubling the programmers to update the software too frequently. The defined rules and signs will be stored as a user configuration file in "My Document\BrailleOrch\User Config" folder, and can be shared and even included in future versions of the software.

In the Musicxml window, choose "Search for unknown" (ctrl+u), and the software will bring us to the first place it finds an unrecognized thing. Press Ctrl+d to define. Or press ctrl+shift+u to list all unrecognized signs and images. In the list, press Enter to go to the place, or choose Define to begin the definition.

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

<h2 id="playalong">Chapter 7: Play-along Function Overview</h2>

The Play-along function will make BrailleOrch like a common notation program, letting blind musicians read music along playing. the cursor and line will follow the playback. Since the current braille displays only has one line to display braille, the user must first choose an instrument or hand of the piano to follow.  
When pressing ctrl+alt+l, we enter the mode. A dialog will appear, asking you to choose which instrument and which measure it will follow. The default will be the current instrument and cthe current measure. By pressing Enter or OK button, the software comes back to normal working area. But now, all editing functions will be disabled, and we enter the play-along mode. To exit this mode, choose Play-along from the Playback menu or press the shortcut again.

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

If you are willing to help us, or want to join in the projecet, please write to [Daniel](mailto:barichd@kenyon.edu) for requesting of adding colleagues into Github, and/or for questions about software development.

If you have any questions about music, braille and braille music, please write to [me](mailto:hhpcomposer@gmail.com).

Thank you in advance!

**********

