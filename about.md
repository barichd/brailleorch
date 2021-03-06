# BrailleOrch Project

## Introduction

BrailleOrch is a two-branched project for providing advanced braille music scores and enhancing braille music transcription. The main goal is to fill the gap between the need of braille music and the shortage of braille music scores available, with the help of both current and future software technologies, giving the blind musicians possibility of reading, studying and playing music as convenient as sighted people, letting blind musicians much more acknowledged by the public. Currently, there are many basic and a number of intermediate levelled music scores already available in braille, especially piano music, so this project is to fill the blank of intermediate and advanced braille music, including instrumental, vocal and symphonic literature. The website of the project will contain our products - a library of free braille music scores, a braille music transcription software and other resources for obtaining braille music scores from various organizations around the world.

The project is divided into two parts: BrailleOrch and Open Braille Music. BrailleOrch is mainly for software development, and will be introduced later in this document. The current work is the latter, Open Braille Music, braille music transcription. When there are a certain amount of scores available, the software development side will be launched. Alternatively, we can also go with two legs, but pay more attention to the current one first.

## A. Open Braille Music

The Open Braille Music branch is based on current software techniques, transcribing music scores into braille efficiently. The overall workflow is as follows:

- 1\. Select printed music scores (either hardcopy or scanned pdf images) and have them engraved into Sibelius. Or get existing engraved music source files (in formats such as Finale, Sibelius, Musescore etc.) from individuals or organizations. If the file is not perfectly engraved (thus done by non-professional engraver), we'll have it checked and corrected. These source files will be used for braille music transcription only, and we will never redistribute any music materials which can be reproduced for sighted people.
- 2\. I will convert these notation files into MusicXML, and then convert into braille using BrailleMuse, an online free braille music translation system developed by Gotoh Toshiyuki from Yokohama University of Japan <http://gotoh-lab.jks.ynu.ac.jp/braille_music_score/en/index.html>.
- 3\. The result of braille will be edited mainly by me, and will sometimes need sight assistance if there are symbols which can't be converted into either MusicXML or braille. Other materials before and/or after the music will also be transcribed using literary braille translation software such as BrailleBlaster.
- 4\. The final braille music scores will be published on our website for free download. The files can be read using braille displays, or embossed using standard braille embossers.

Currently, the division of this branch is as this: I mainly design the whole project and make braille music transcriptions; Chen Jing, a blind friend, mainly manage collected funds for engraving and build the website. Our website is now under authorization, and will be online soon. The engraving services can be both in China and other countries such as Russia. We are mainly working with a cheap and good service in China.

Currently, I have transcribed over 50 scores into braille. Most of them are orchestral, and there are also small chamber and piano ones. The source files are mainly from other people, and there are 10 works from engraving services. For me, the transcription speed can be very fast, 3-4 days for a 60-100-page orchestral music, according to its complexity.  If it takes 1 month to have such a score engraved, I can then transcribe over 1000 pages of print music into braille per year. And in fact, I have done about 2500 pages last year!

The collected funds of this branch is used mainly for music engraving and braille transcription, and a small amount of it will be used for the website. In the service we are engaging, the price is: around 20 yuan per page for piano and other solo music, 25 yuan for chamber music, and 35 or above for symphonic music (according to the complexity of the score). If large work such as an opera will be done, we'll ask for a quick service in Russia, where $4 is for small ensemble and $8 for large scaled scores. We'll now have some music scores most need by standard composition students and music producers engraved, and then will go for more advanced ones. According to my speed, there will be about 50000-60000 yuan need for a year's outcoming, including engraving and my transcription. I'd prefer to make annual installment, because there may be changes for the project, or some other unexpectable event. If we will begin to develop the software, the funding arrangement can also be estimated again.

## B. BrailleOrch

The BrailleOrch branch is for enhancing current braille music transcription to a higher level. If this software is out, there will be a burst in this field, and we blind musicians can obtain as many music scores as sighted people, as long as the score is notated in standard way. The current softwares, including Goodfeel, Braille Music Editor and BrailleMuse are good for basic and intermediated scores, but none of them are so smart for advanced complex music and perfect formatting functions. So the official transcribers seldom use them, and still prefer manual transcription, which is very slow and expensive. Moreover, since the software need too many manual adjustment in both original file and braille result, we can't use the source files held by most composers and mainstream publishers such as Schott. If my software come out, the source holders can just make ready-to-format braille scores with less effort and loss of data, then the transcribers just do the braille side by viewing the original scores they have, without making large number of adjustments and corrections. After years' of learning and testing, I summed all problems I have met and make out a plan for the software. Last year, I wrote a detailed framework and put it on Github (https://github.com/barichd/brailleorch). But since I'm not a programmer, I can't write the software. So I hope anyone who is willing to help us to join in. The overall plan and progress of making this software has been written in the framework.

The software team can be divided into 3 parts: the designer, mainly me, sometimes other blind musicians who have additional suggestions; the development side, containing people who know programming and (optional but important) music; and the testing side, blind musicians around the world, including me. The requirements for developing this software were also written in the framework, but can be changed if better possibilities are available.

Currently, the GUI of the software can be bilingual--English first and then Chinese. When the software is complete enough for standard production, we can consider adding more languages with the help of people from different countries.

After the software's out, we can cooperate with mainstream music publishers and organizations for the blind, letting them use our free software to produce braille music. This way, we will spend much less money on score engraving, and pay more attentiong on braille music production. We can even give online training for transcribers to help them to produce high quality braille music using the software.

## C. The Final Results

The final results of the BrailleOrch Project will be:

- 1\. A growing library of braille scores;
- 2\. A sophisticated braille music transcription software with comprehensive user guide;
- 3\. A collection of links to other sources where blind musicians can obtain braille music;
- 4\. A small team for further development and updates, going the same step with MusicXML's development.
- and 5. A user group from individual blind musicians to organizations for the blind and music publishers.

The above are simply my current ideas of the whole project. We welcome all people who want to help me, either on funds and techniques. Thank you all in advance!

  Hu Haipeng

