# SourcePaste

SourcePaste is intended to make life easier for the average coder. Switching between the terminal and the browser GUI gets jarring at times; so why not keep it fully terminal! SourcePaste interacts with the PasteBin API to post your full source code (along with other options), all whilst staying in your Linux terminal.

## Setup

SourcePaste setup is *super* simple, all you need to do is install the requirements.txt:

---------------------------------------------------------------------------------
> sudo pip install -r requirements.txt
---------------------------------------------------------------------------------

Set the correct chmod permissions:

---------------------------------------------------------------------------------
> chmod +x sourcepaste
---------------------------------------------------------------------------------

And run setup.py with your PasteBin API devkey (https://pastebin.com/doc_api) as the first argument, your PasteBin username as the second, and your PasteBin password as the third:

---------------------------------------------------------------------------------   
> sudo python3 setup.py [DEVKEY] [USERNAME] [PASSWORD]
---------------------------------------------------------------------------------

That's it! Now you may run SourcePaste like so:

---------------------------------------------------------------------------------
> sourcepaste [OPTIONS DESCRIBED IN SOURCEPASTE HELP]
---------------------------------------------------------------------------------

Thanks for using SourcePaste!!!! :)
  
### Notes
  
There are 2 unfixable (unfixable as far as I am aware, reach out if you are aware of a fix) bugs to do with the handling of usernames/passwords in either the terminal or POST request to Pastebin when executing setup.py. This is due to username and password syntax (equals signs, ampersandes, crocodile symbols, etc) conflicting with terminal and POST request data and may cause "Bad API request, invalid login" errors or general weirdness in the terminal.
  
If you recieve either bug, the simplest fix is to simply quote out the password/username - like so:

---------------------------------------------------------------------------------
> python3 setup.py <DEVKEY> testuser "big&error>>"
---------------------------------------------------------------------------------
  
If you successfully do this and then run pastegrok, yet recieve a "Bad API request, invalid api_user_key" error - do the following: open up the sourcepaste file's code, find every mention of "api_user_key", then replace the data pertaining to "api_user_key" with your user key. Also, report the bug to me, as I have already released a patch for it and it should be working - though it might not be!
  
If these fixes STILL don't work, remove and reinstall pastegrok or message me on Discord :)
