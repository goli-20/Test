###Log into the application, navigate to the Templates tab, locate the current template, print its name, and then log out
def test_01_profile(self):
        #Logging to the Application
        self.do_login("https://prezent-uatstaging.myprezent.com/signin","engg_user.noreply@prezent.ai","kiqjemkh")
        #Clicking on Profile Icon
        self.wait_for_element("div[name='profile-icon']")
        print(f"Clicking on Profile Icon ")
        self.click("div[name='profile-icon']", timeout=15)
        #Clicking on Templates Tab
        print(f"Clicking on Templates Tab ")
        self.click("#templates-tab")
        #Printing Current Template name
        self.wait_for_element('.pt-search__addmore.primary',timeout = 30)
        active_template_name = self.find_element("h4.pt-card__title").text
        print("The template '{}' is the current selected template.".format(active_template_name))
        tmpl_disp_names = [tmpl_el.text for tmpl_el in self.find_elements('.pt-card__details .pt-card__detailsleft')]
        print("Available templates names are : {}".format(tmpl_disp_names))
        #Clicking on Logout
        self.do_logout()