###Log into the application, navigate to the Fingerprint tab, retake the fingerprint, and then log out.
    def test_02_fingerprint(self):
        #Logging to the Application
        self.do_login("https://prezent-uatstaging.myprezent.com/signin", "engg_user.noreply@prezent.ai", "kiqjemkh")
        #Clicking on the Profile Icon
        self.wait_for_element("div[name='profile-icon']")
        print(f"Clicking on Profile Icon ")
        self.click("div[name='profile-icon']", timeout=15)
        #Clicking on Fingers Tab
        print(f"Clicking on fingerprints Tab ")
        self.click("#fingerprint-tab", timeout = 30)
        #Clicking on Re-Take Fingerprints
        print(f"Clicking on Re-take fingerprint Test ")
        self.click("div[class='btn-retake']", timeout=15)
        #Clicking on Discover My Fingerprint
        print(f"Clicking on Discover My fingerprint ")
        self.click("#discover", timeout=15)
        #Clicking on Slides
        self.wait_for_element("div[class='v-responsive__content']", timeout=15)
        for _ in range(1, 7):
            self.wait_for_element("div.v-responsive__content", timeout=15)
            self.click("div.v-responsive__content")
            self.wait(2)
        #Clicking on Label all charts Button
        self.wait_for_element("//span[text()=' Label all charts ']")
        self.click("//span[text()=' Label all charts ']", timeout = 15)
        #Clicking on next button
        self.wait_for_element("#show-fingerprint-for-btn--auto")
        self.click("#show-fingerprint-for-btn--auto", timeout = 15)
        #Clicking on Skip buttons
        self.wait_for_element("div[class='skip-button']", timeout=15)
        for _ in range(1,7):
            self.wait_for_element("div.skip-button", timeout = 15)
            self.click("div.skip-button")
            self.wait(2)
        #Clicking on Verify my Fingerprint
        self.wait_for_element("//span[text()=' View my fingerprint ']")
        self.click("//span[text()=' View my fingerprint ']", timeout = 100)
        self.wait(10)
        #Clicking on Back to Prezent
        self.wait_for_element("//span[text()=' Back to Prezent ']")
        self.click("//span[text()=' Back to Prezent ']", timeout = 15)
        #Clicking on Logout
        self.do_logout()
###Log into the application, select the third option from the suggestive dropdown, click on 'Generate', download the file, and then log out
    def test_03_autogenerate(self):
        #Logging to Application
        self.do_login("https://prezent-uatstaging.myprezent.com/signin", "engg_user.noreply@prezent.ai", "kiqjemkh")
        #Clicking on Auto generator
        self.wait_for_element("//div[text()='Auto Generator ']")
        print(f"Clicking on Auto Generator ")
        self.click("//div[text()='Auto Generator ']", timeout = 15)
        #Clicking on Text area for Dropdown
        self.wait_for_element("//textarea")
        print(f"Clicking on Dropdown ")
        self.click("//textarea", timeout = 15)
        #Selecting 3rd Suggested Dropdown
        self.wait_for_element("//p[@id='generate-suggested-2']")
        print(f"Clicking on 3rd Suggested Dropdown ")
        self.click("//p[@id='generate-suggested-2']", timeout = 15)
        #Clicking on Generate
        print(f"Clicking on Generate ")
        self.wait_for_element("//span[text()=' Generate ']")
        self.click("//span[text()=' Generate ']", timeout = 100)
        self.wait_for_element_present('div.v-spinner.loading-spinner')
        self.wait_for_element_absent('div.v-spinner.loading-spinner', timeout=300)
        #Clicking on Download
        print(f"Clicking on Download ")
        self.click("#download", timeout = 30)
        #Clicking on Download Button
        print(f"Clicking on Download Button")
        self.click("#download-btn", timeout = 30)
        #Clicking on Download as pptx
        print(f"Clicking on Download as PPTX")
        self.click("#download-btn-from-list", timeout = 60)
        self.wait(30)
        #Clicking on Logout
        self.do_logout()