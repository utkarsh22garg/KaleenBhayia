# Welcome to KALEEN_BHAYIA bot!
## Team Kaleen Bhayia ke Ladke in HACK36

## **Kaleen_Bhayia-Bot** is a zulip chatbot 

# Instructions to run locally:
1. [Create a Zulip Realm](https://zulip.com/create_realm/)
2. Goto to settings and create a new generic bot named 'Kaleen_Bhayia'. (Settings can be found in dropdown of gear icon present in top right corner of zulip realm)
3. Download the zuliprc file for your bot and place it in your home directory as '.zuliprc'.  
4. Install all the requirements using ``` pip install -r requirements.txt ```
5. In ``` kaleen_bhayia.py ``` , change site in ``` self.client = zulip.Client(site="https://kaleen_bhayia.zulipchat.com/api/") ``` to url of your created zulip realm.Do the same for ``` BOT_MAIL ``` variable.  
6. Run ``` kaleen_bhayia.py ``` using python 3. ``` python3 bot.py ```
7. Head over to your created zulip realm and start using the bot.


# Libraries and Packages to be installed:
## For text-to-speech (used in joke.py file) , *install following packages* :-
* pip  install gTTS
* sudo apt-get install mpg321
* pip install --upgrade requests

## For web Scrapping
* pip install beautifulsoup4 (may you get error in virtualenv, so try to run  this command outside of virtualenv)
* for Proxy type
* * proxy
* * proxy working
* for College notice Type
* * college_notice

## For Online Music
* sudo apt-get install youtube-dl (If getting signature error then try below command)
* pip install --upgrade youtube-dl
* sudo apt-get install ffmpeg
* * type play (song_name)
## for run bot
* zulip-run-bot kaleen_bhayia --config-file (path_of_zuliprc)

## for merging python and firebase
* pip install pyrebase

## for cloud messaging
* pip install pyfcm

## for http-client
* pip install ndg-httpsclient

## for translator
*  pip install googletrans

# Features

Kaleen Bhayia bot can :-
>* Also Works on voice commands (Run botInterface.py file explicitly for this)
>* Translate any Language
>* Get top Cricket News
>* Check PNR Status
>* Crack a Joke
>* List all the working Proxies (with Area Specification)
>* Find your Phone
>* Search any Friend's or your phone Location
>* Get meanings of english vocablury, so that you don't stop while discussing
>* Allows you to save your meetings
>* Diagnose about any Disease or pain
>* List all the College notices
>* Find latest jobs available with location
>* Play any song
>* Show nearby places like Hospitals,Parks,etc
>* Send message using mobile phone 
>* Updates you with Upcoming Coding Contests
>* Lets you run above faetures with command of your preferences 

## Technology Stack Used
1. Zulip Platform (using Zulip API)
2. Languages -: Python3, JAVA (for APP)
3. IDE Utilities :- Android Studio, Sublime TextEditor
4. Wit.ai -: Easily create text or voice based bots that humans can chat with on their preferred messaging platform (NLP).

## Contributors
* [Aniket Kumar](https://github.com/Aniket468)  
* [Shivam Kumar](https://github.com/shivam4035)  
* [Utkarsh Garg](https://github.com/utkarsh22garg)  
* [Ankit Kumar Maurya](https://github.com/mauryaankitsh)
