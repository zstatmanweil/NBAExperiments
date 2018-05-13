class Player(object):
    
    def __init__(self, first_name, last_name, draft_year, draft_pick, draft_round):
            self.first_name = first_name
            self.last_name = last_name
            self.draft_year = draft_year
            self.draft_pick = draft_pick
            self.draft_round = draft_round
            
#creates a full name of a player
    def full_name(self):
        return self.first_name + " " + self.last_name
    
#creates a name that can be easily compared to the user's input
    def search_name(self):
        return self.full_name().lower().strip()

#transforms round number so it can be properly used in a sentence
    def round(self):
        if self.draft_round == "1":
            return "1st"
        elif self.draft_round == "2":
            return "2nd"
    
#rovides a draft summary of an individual player
    def draft_info(self):
        if self.draft_year != '':
            return """\n%s was drafted number %s in the %s \
round in %s""" % (
                self.full_name(),
                self.draft_pick,
                self.round(),
                self.draft_year
                )
        elif self.draft_year == '':
            return "\nThere is no draft data for %s. He may not have been drafted." % self.full_name()
            