#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2 




form ="""
<div id="container">
    <h2> Ceasar</h2>
    <form method="post">
        <p><labe> Rotate by: <input class="rotinput" type="number" name="rot"> </label></p>
        <h3> Enter your text:</h3>
        <textarea class="txt" name="text" >%(text)s</textarea>
        <p style="color:red;"> %(error)s </p>
        <br>
        <input type="submit">
    </form>
</div>

<style>
    #container{
    padding-left: 30px;
    padding-top: 20px;
    width: 600px;
    height: 400px;
    margin: auto;
    }
    
    p, label{
    font-size:20px;
    }
    
    
    .rotinput{
    width: 60px;
    height: 22px;
    font-size: 15px;
    }
    
    .txt{
    height: 175px;
    width: 400px;
    font-size: 15px;
    }
    

</style>


"""
def alphabet_position(letter):
    uc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lc = 'abcdefghijklmnopqrstuvwxyz'

    for i in letter:
        if i in uc:
            char = uc.index(i)
            return char
        elif i in lc:
            char = lc.index(i)
            return int(char)

def rotate_character(mess, rot):
    uc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lc = 'abcdefghijklmnopqrstuvwxyz'
    rNum = rot

    position = alphabet_position(mess)
    encrypted = ''

    for i in mess:
        if i.isalpha():

            if i.isupper():
                position = uc.index(i) + rNum
                if position < 26:
                    encrypted = encrypted + uc[position]
                else:
                    encrypted += uc[position % 26]
                return encrypted
            if i.islower():
                position = lc.index(i) + rNum
                if position < 26:
                    encrypted = encrypted + lc[position]
                else:
                    encrypted += lc[position % 26]
                return encrypted

        else:
            encrypted += i
    return encrypted



def encrypt(text, rot):
    trans = ''

    for i in text:
        trans+= rotate_character(i, rot)
    return trans



        
        
class MainHandler(webapp2.RequestHandler):
    def write_form(self, error="", text=""):
        self.response.out.write(form % {"text":text,
                                       "error":error})
    
    def get(self):
        self.write_form()
    
    def post(self):
        error="You have to fill both fields!"
        rot = self.request.get("rot")
        text1 = self.request.get("text")
        if text1 and rot:
            rotate = encrypt(text1, int(rot))      
            self.write_form(text = rotate)
        else:
            self.write_form(error)
            
        


app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
