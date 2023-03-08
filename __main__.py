#!/usr/bin/env python3

from revChatGPT.V3 import Chatbot
import json
import subprocess
import os
import sys

class ChatGPT:
    def __init__(self):
        self.safe_mode = True
        # chatgpt prompt to create env for interaction
        with open("./system_prompt.txt", 'r') as h:
            system_prompt = h.read()
        # connect to the openAI API using your API key
        api_key = os.environ['CHATGPT_KEY']
        self.chatbot = Chatbot(api_key=api_key, system_prompt=system_prompt)

    def run_system_cmd(self):
        p = subprocess.Popen(command, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, shell=True)
        output, err = p.communicate()
        exit_code = p.wait()
        api_res = chatbot.ask('Backend: {"STDOUT":"%s", "EXITCODE":"%s"}' % (output, exit_code))
        return api_res

    def bootstrap(self):
        try:
            while True:
                prompt = input("[ChatGPT]$ ")
                if prompt.lower().strip() in ['exit', 'quit', 'q']:
                    return 0
                api_res = self.chatbot.ask("Human: " + prompt)
                while True:
                    if "@Backend" in api_res:
                        chat_res = api_res.split("@Backend")[1]
                        json_str = json.loads(res)
                        cmd = json_str['command']
                        if self.safe_mode:
                            conf = input(f"[!] Run command :: {cmd}\n [Y/n]")
                            if prompt.lower().strip()[0] == "y":
                                api_res = run_system_cmd(cmd)
                            else:
                                break
                        else:
                            api_res = run_system_cmd(cmd)
                    elif "@Human" in api_res:
                        reply = "[+] Response :: " + api_res.split("@Human")[1]
                        print(reply)
                        break
                    else:
                        print(f"[x] Error :: {api_res}")
                        break
        except KeyboardInterrupt:
            return 0

def main():
    chatbot=ChatGPT()
    return chatbot.bootstrap()

if __name__ == '__main__':
    sys.exit(main())
