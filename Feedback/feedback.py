import webbrowser

class feedback:
    def feed_back(self):
        response = input("Do you wish to submit a feedback about this project('y' or 'n'): ").lower()
        if response in ['yes','y']:
            google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfhqMbLoG2CznP6AhBCPvnscfFFajPAKUFo9rNpZUM-pXVnQw/viewform?usp=sf_link"
            webbrowser.open(google_form_url)
            print("Opening feedback form...")
        else:
            print("Thank you! Have a great day!")



feed = feedback()
#feed.feed_back()

            


