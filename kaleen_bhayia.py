from typing import Any, Dict
from calculate import Calculator
from coding_contest import Coding
from Dictionary import Dictionary
from joke import Joke
from dean import Dean
from cricknews import Cricket
from proxy import Proxy
from music import Music
from send_message import Send_message
from Meeting import Meeting
from pnr import Pnr
import sys
import threading
import os
import signal
from subprocess import check_output
#from song_mood import Mood
from sympton import Sympton
class Kaleen_bhayia(object):
    def usage(self) -> str:
        return
    t2="";
    def handle_message(self, message: Dict[str, Any], bot_handler: Any) -> None:
        string =message['content'].split()
        content="something went wrong"
        check=string[0].lower()
        
        if check=="calculate":
            content=Calculator.calculate(string)
        elif check=="coding_contest":
        	content=Coding().getList();
        elif check.lower()=='define':
            dictword=string[1]
            content=Dictionary.words(dictword)
        elif check.lower()=='telljoke':
            content=Joke.tellJoke()
        elif check == "cricknews":
        	content = Cricket().news()
        elif check=="proxy":
            if len(string) > 1:
                if string[1].lower()=="working":
                    content=Proxy.getWorkingProxy();
                    content="Working Proxies in Your Area \n\n"+content
                elif string[1].lower()=="help":
                    content=Proxy.getHelpList();
                else:
                    content="try proxy help"
            else:         
                content=Proxy.getProxyStatus();
                content="Proxies Status--->\n\n"+content;
        elif check.lower()=="play":
            try:
                pid=check_output(["pidof"],"mpg321");
                os.kill(int(pid),signal.SIGKILL)
                os.remove("hello.mp3");
                content=Music.main(string[1:])
            except:
                content=Music.main(string[1:])
            bot_handler.send_reply(message,"playing song ")
        elif check=="stop":
            pid=check_output(["pidof","mpg321"])
            #print(int(pid))
            os.kill(int(pid),signal.SIGKILL)
            content="Bye........:)"
            bot_handler.send_reply(message,content)      
        elif check=="college_notice":
            content=Dean.getNotice();
        elif check=="add" and string[1]=="meeting":
            content="Enter <Date> as <dd/mm/yyyy> <Time> as <hrs:min> and am/pm and purpose(one word)"
            
        elif len(string[0].split('/'))==3:
            res=Meeting.AddMeeting(string)
            if res.lower()=="ok":
                content="New Meeting successfully Added "
            else:
                content=res
        elif check=="show" and string[1].lower()=="meetings":
            content=Meeting.ShowMeeting()
        elif check=="pnr" and string[1].lower()=="status":
            content=Pnr.getpnr(string[2])     
        elif check=="message" or check=="find" or check=="where":
            content=Send_message.sendMessage(string);
        # elif check=="mood":
        #     Mood.capture();
        elif check=="symptom":
            string_1=" ";
            gender=string[1];
            dob=string[2];
            st=string[3:];
            string_1=string_1.join(st);
            content=Sympton.getExactSympton(string_1)
            try:
                content="Please Tell me clearly\n"+content;
            except:
                p=int(content)
                content=Sympton.getIssueId(str(p),gender,dob)
        bot_handler.send_reply(message, content)
handler_class = Kaleen_bhayia
