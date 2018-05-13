class Choice(object):
    def __init__(self, user_submitted):
        self.user_choice = user_submitted
        
    def is_exit_code(self):
        if self.user_choice.lower() in ("stop", "exit", "end"):
            return True
        
    def is_NBA_year(self):
        if self.user_choice.isdigit() and int(self.user_choice) >= 1946:
            return self.user_choice.isdigit()
    
    def is_year_prior_NBA(self):
        if self.user_choice.isdigit() and int(self.user_choice) < 1946:
            return self.user_choice.isdigit()
        
    def is_name(self):
        if len(self.user_choice) > 0:
            return True