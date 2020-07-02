# whatsapp_py

Send whatsapp messages to people using python script.

## Requirements-

1. python
2. Chrome Driver-

#### Installing chrome driver-

Download from the official page (preferred, though chromedriver is available in the repo)-
1] Visit ```https://sites.google.com/a/chromium.org/chromedriver/downloads```
2] Download and extract (e.g. to ```~/bin/``` or ```/usr/local/share/```)
3] Remember to ```sudo chmod +x chromedriver```.

###### Chromedriver must be available in your path. You can add ```~/bin``` to your path like this:

1. COPY this at end of .bshrc file present in home->
    ```export PATH="$PATH:/home/abhisri/Bin"```
    
## Running the script-

1. Open whatsapp.py in your favourite text editor.
2. Write your message to be send against variable ```message_text```.
3. Mention the no. of times message is to be sent to each user against variable ```no_of_messages```.
4. Write all the phone nos. against python array ```mobile_no_list``` in the format ```919871111111```.
5. Run the script as ```python whatsapp.py```.
