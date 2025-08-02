#! python3
# mclip.py - a multi-clipboard prm

'''You want to be able to run this program with a command line argument
that is a short key phrase—for instance, agree or busy. The message associated
with that key phrase will be copied to the clipboard so that the user
can paste it into an email. This way, the user can have long, detailed messages
without having to retype them.'''

text = {
    'agree' : 'Yes I agree, that sounds fine to me! ',
    'busy': 'Sorry, Can we do this later this week or next week? ',
    'upsell': 'Would you like to consider making this a monthly donation? '
}

import sys,pyperclip

if len(sys.argv) < 2:
    print('Enter atleast 1 arguments')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print('Text corresponding to ' + keyphrase + ' has been copied to clipboard')
else:
    print(keyphrase + ': no corresponding message exists')




#print(f'Script name {sys.argv[0]}')
#print(f"{sys.argv[1]}")

