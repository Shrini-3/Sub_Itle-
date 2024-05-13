## SUBTITLE SERVICES FOR YOUTUBE SHORTS

# Problem Statement:
Developing an efficient and user-friendly subtitle service tailored specifically for YouTube Shorts to enhance accessibility and engagement for a diverse audience.

# Abstract:
Recently, with the development of Speech to Text, which converts voice to text, and machine translation,technologies for simultaneously translating the captions of video into other languages have been developed. Using this, YouTube, a video-sharing site, provides captions in many languages.Currently, the automatic caption system extracts voice data when uploading a video and provides asubtitle ﬁle converted into text. This method creates subtitles suitable for the running time. Since the generated subtitles are separated by time units rather than sentence units, and are translated, it is very diﬃcult to understand the translation result as a whole.So as the solution for this we will be creating a model which extracts subtitle from vedio uploaded simultaneously.In addition, we expect that language barriers in online education will be more easily broken by achieving more accurate translations of numerous video lectures in English.

## Background Study:
1.User Experience and Preferences-
50% of Americans turn on subtitles “most of the time.” That number jumps all the way up to 80% for Gen Z.

And it’s not just personal preference. Data shows that subtitles and captions matter for viewer retention and engagement.

# Facts about subtitles
80% of viewers are more likely to finish a video with subtitles
85% of all videos on Facebook are watched with the sound off
80% of viewers respond negatively to video ads that auto-play sound
37% of viewers said video subtitles encourage them to turn the sound on
One company saw an 7.32% total increase in YouTube views after adding subtitles
61% of people who localize their video content translate their subtitles

# 2.Quality Control and Editing Tools-
Quality assurance in subtitling includes checking:
 Audio Synchronization
 Timing and Duration
 Text Formatting
 Platform and Device Compatibility
 Language Accuracy
 Consistency and Style
 Synchronization
 Line breaks

# 3.Integration with Video Platform-
  VEED.IO-
  VEED.IO offers video subtitling in three main ways: 
  a)Manual typing, 
  b)Automatic subtitle generating,
  c)Uploading a text file (it supports the formats of SRT, VTT, TXT, ASS, SSA). Irrespective of how you wish to subtitle the video, you can decide the text’s fonts, colors, size, and timings.
  Rev
  Rev’s services to add subtitles to video makes your video appealing, boosts your SEO, and helps you cater to a larger audience. 
  It works with almost any format, from MP4, MOV, and VOB to AVI and OGG.
  AmberScript
  You have both with AmberScript — man and the machine for subtitling and transcribing.
  While their AI engine can subtitle in 39 languages, their experts can do it in eleven languages.
  They have pre-paid and subscription-based plans for automatic subtitling. And the manual service is time-based and also offers translated subtitling.
  SubtitleBee
  SubtitleBee is an AI-powered video subtitle generator. 
  You can add closed captions and change the head title in different styles, fonts, and colors to make your video attractive. 
  You can also customize the auto-captioning settings to enhance creativity.

# 4.Cost Consideration-
 Captioning prices can differ from vendor to vendor. Ultimately, pricing will come down to video duration, service, features, and quality.
 Most vendors charge per minute. Captioning rates can range from $1 per minute to $15 per minute. Some vendors round up per minute, which can add up quickly if you have many short files.
 Some vendors also charge fees. For example, vendors might charge extra for multiple speakers, caption formats, resubmissions, or video platform integrations.
 Using automatic speech recognition (ASR) is cheap and fast but often painfully inaccurate. 
 YouTube, for example, offers free automatic captioning, but accuracy rates can range from 60% to 70%. 
 Thus, you end up spending more time fixing your ASR captions.
5.File formats-
 SubRipper (.srt)
 The SubRipper format, commonly known as SRT, is widely supported by subtitle converters and players. 
 It features a concise and easily understandable structure. 
 When opened with a text editor, an SRT file displays the time when the text appears and the corresponding subtitles. 
 This format is widely compatible and can be edited without difficulty.
 MicroDVD (.sub)
 SUB subtitles are like the reliable Swiss Army knife of subtitles. 
 They are named after MicroDVD, the software that popularized this format. 
 What sets SUB apart is its straightforwardness and effectiveness.
 WebVTT (.vtt)
 The WebVTT format, often referred to as VTT, holds a prominent place in the world of subtitles. 
 It’s recognized as a W3C standard, making it a dependable choice for web-based content. 
 VTT subtitles are prized for their simplicity and compatibility, ensuring accessibility across various platforms.
 STL (Spruce Subtitle File)
 STL (Spruce Subtitle File) is a widely used binary subtitle format primarily employed in the broadcasting and video production industries. 
 STL files contain graphical representations of subtitles in the form of bitmaps, allowing for precise styling, positioning, and timing.
# 6.WCAG for accesibility standards and compilance inclusivity-
 What is required in the WCAG standard at Level A, AA, and AAA. (WCAG is introduced in the Planning page of this resource.)
 What is needed to meet user needs, beyond WCAG. If there are no “A”s, then it is not required in WCAG.
 Audio-only (e.g., podcast):
 For pre-recorded:
 Captions are useful for people who are hard of hearing to get the richness of listening to the audio and fill in what they don’t hear well by reading the captions.
 Captions are not required to meet WCAG. (Transcripts are at Level A.)
 For live:
 Captions are useful for people who are hard of hearing to get the richness of listening to the audio and fill in what they don’t hear well by reading the captions.
 Live text stream or accurate script of the audio available when live is in WCAG at Level AAA.
 Video-only (no audio content):
 For pre-recorded and live:
 Captions are not needed because there is no audio information.
 Video with audio content:
 Does the video have audio information that is needed to understand what the video is communicating?
 If no (for example, it is just background music):
 Captions are not needed because there is no important audio content. Consider informing users.
 If yes:
 For pre-recorded:
 Captions are needed to provide the audio content to people who are Deaf or hard of hearing.
 Captions are required in WCAG at Level A.
 For live:
 Captions are needed to provide the audio content to people who are Deaf or hard of hearing.
 Captions are required in WCAG at Level AA.
# Flow Chart:
![OE](https://github.com/Shrini-3/OE-Project/assets/119584214/8e114c4a-9952-47eb-8a7e-b70c8976b5de)




# Proposed Solution:
Creating an interactive website which gives you the accurate subtitle for Youtube shorts by integarting youtube API's for video processing and subtitle generation. 

# WorkFLow Of the Project:
Workflow of the project is being described as:

Front End with Flask:
Python Flask is used to create a web application that handles user authentication and serves HTML and CSS files to the client (web browser).
Flask provides routes (URL endpoints) that respond to HTTP requests from the client, such as requests for login, registration, and accessing protected pages.


Website (HTML and CSS):
HTML (Hypertext Markup Language) is used to structure the content of web pages.
CSS (Cascading Style Sheets) is used to style the HTML elements, controlling their appearance and layout.
Together, HTML and CSS are used to create the visual presentation of the website, including its layout, colors, fonts, and other stylistic elements.


Video to Text Transition with MoviePy:
MoviePy is a Python library used for video editing and manipulation.
In this project, MoviePy is used specifically for converting video content into text subtitles.
The process typically involves the following steps:
a)Extracting Audio: The video's audio track is extracted using MoviePy.

b)Speech Recognition: The extracted audio is then processed using a speech recognition library (e.g., Google's Speech Recognition API or CMU Sphinx) to transcribe spoken words into text.

c)Subtitle Generation: The transcribed text is formatted into subtitle text format, typically with timestamps indicating when each subtitle should appear on the screen.

d)Overlaying Subtitles: The generated subtitles are overlaid onto the video frames using MoviePy, creating a new video file with embedded subtitles.
This process allows users to watch the video with accompanying text subtitles, enhancing accessibility and usability.

# Outline of the Project Implemented:
1.Set up a Flask web application with routes for user authentication, login, and protected pages.

2.Create HTML templates for the website's pages, including login and protected content pages, and style them with CSS.

3.Implement the video-to-text transition functionality using MoviePy:

4.Install MoviePy and any necessary dependencies.

5.Write Python code to extract audio from videos, perform speech recognition, generate subtitles, and overlay them onto the video frames.

6.Integrate this functionality into your Flask application, allowing users to upload videos and receive subtitles in return.

7.Test the application to ensure that users can authenticate, upload videos, and view them with subtitles.

8.Deploy the Flask application to a web server so that users can access it online.
