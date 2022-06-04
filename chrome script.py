## export all urls from active chome window to user specified file
## or open all urls from user specified file

import subprocess

import_export = raw_input('For open from file type \'open\' \n For export to file type \'export\':\n')

if import_export == 'export':
    command_string = 'osascript -e\'set text item delimiters to linefeed\' -e\'tell app \"google chrome\" to url of tabs of window 1 as text\' > '
    newname = raw_input('type output filename [ex: test.txt]\n')
    command_string += newname
    subprocess.Popen(command_string, shell="True")

if import_export == 'open':
    test_variable = raw_input('filename?\n')
    with open(test_variable,'r') as f:
        for line in f:
            subprocess.call(['open', '-na', 'Google Chrome', '--args', '--incognito', line])

