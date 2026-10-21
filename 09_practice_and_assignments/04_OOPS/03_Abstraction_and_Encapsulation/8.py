# Problem 3: Fitness Club Rewards System

class Member:
    def calculateRewardsPoints(self, hours):
        return hours * 2

class PremiumMember(Member):
    def calculateRewardsPoints(self, hours):
        return hours * 4

if __name__ == "__main__":
    hours = int(input())
    premium = input().strip().lower()
    
    if premium == "yes":
        member = PremiumMember()
    else:
        member = Member()
        
    print(member.calculateRewardsPoints(hours))
