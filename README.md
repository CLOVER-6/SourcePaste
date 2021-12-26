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
> sudo python3 setup.py <DEVKEY> <USERNAME> <PASSWORD>
---------------------------------------------------------------------------------

That's it! Now you may run SourcePaste like so:

---------------------------------------------------------------------------------
> sourcepaste [OPTIONS DESCRIBED IN SOURCEPASTE HELP]
---------------------------------------------------------------------------------

Thanks for using SourcePaste!!!! :)
