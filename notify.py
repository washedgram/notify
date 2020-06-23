import os, platform, requests, json, time
# people running this on Windows will need to install win10toast, see below

webhook = "https://hooks.slack.com/services/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"

def notify(title, message):
    
    osType = platform.system()
    if osType == 'Darwin':	# macOS
	    os.system("""osascript -e 'display notification "{}" with title "{}"'""".format(message, title))

    elif osType == 'Windows':	# windows
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast(title, message)
    
    else:   # linux
        currentTime = time.time()
        slack_data = {
            "attachments": [{
                    "title": title,
                    "text": message,
                    "color": "#36a64f",
                    "ts": str(currentTime),
                    "footer": "Example Slack Webhook Embed"
                }]
            }
        response = requests.post(webhook, json = slack_data)
        if response.status_code != 200:
            raise ValueError('Request failed ... got response %s' % (response.text))

        
#notify('We live in a ...', 'SOCIETY')
