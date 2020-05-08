import os, platform

def notify(title, text):
    
    osType = platform.system()
    if osType == 'Darwin':	# macOS
	    os.system("""
	        osascript -e 'display notification "{}" with title "{}"'
	        """.format(text, title))

    else:	# windows
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast(title, text)
    
    # no linux support figure it out yourself if you wanna be that special
        
notify('We live in a ...', 'SOCIETY')
