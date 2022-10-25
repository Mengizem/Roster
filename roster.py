"""Implements Team Roster Operations"""

class Roster(object):
    """Implements Team Roster Operations"""
    def _init_(self):
        self.newRoster = {}
        pass

    def new_roster(self):
        rosterFile = open("/data/team_roster.json")
        txt = rosterFile.read()
        rosterData = json.loads(txt)
        rosterFile.close()

        print("Enter Roster Type :- ")
        type = input()
        print("Enter Roster Date :- ")
        date = input()
        print("Enter Roster Sport :- ")
        sport = input()
        print("Enter Roster Country :- ")
        country = input()
        print("Enter Roster member name :- ")
        memberName = input()
        print("Enter Roster member age:- ")
        age = input()

        rosterData.append({
            "type": type,
            "date": date,
            "sport": sport,
            "country": country,
            "members": [
                {
                    "name": memberName,
                    "age": age
                }
            ]
        })

        js = json.dumps(rosterData)
        roster = open("/data/team_roster.json")
        roster.write(js)
        roster.close()

    def load_roster(self):
        rosterFile = open("/data/team_roster.json")
        txt = rosterFile.read()
        rosterData = json.loads(txt)
        print(rosterData)
        rosterData

    def print_roster(self):
        rosterData = self.load_roster()
        for roster in rosterData:
            print(roster)

    def add_members(self):
        rosterFile = open("/data/team_roster.json")
        txt = rosterFile.read()
        rosterData = json.loads(txt)
        rosterFile.close()

        print("Enter Roster member name :- ")
        memberName = input()
        print("Enter Roster member age:- ")
        age = input()

        members = rosterData[0]["members"]
        members.append({"name": memberName, "age": age})

        rosterData[0]["members"] = members

        js = json.dumps(rosterData)
        roster = open("/data/team_roster.json")
        roster.write(js)
        roster.close()


    def save_roster(self):
        rosterFile = open("/data/team_roster.json")
        txt = rosterFile.read()
        rosterData = json.loads(txt)
        rosterFile.close()

        js = json.dumps(rosterData)
        roster = open("/data/team_roster.json")
        roster.write(js)
        roster.close()