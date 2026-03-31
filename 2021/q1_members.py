import csv
import os


class Member:
    """Task 1.1: Member class"""
    def __init__(self, member_id, name, membership_type, year_joined):
        self.member_id = member_id
        self.name = name
        self.membership_type = membership_type
        self.year_joined = year_joined
        self.fines = 0.0
    
    def __str__(self):
        return (f"ID: {self.member_id}, Name: {self.name}, "
                f"Type: {self.membership_type}, Year: {self.year_joined}, "
                f"Fines: £{self.fines:.2f}")


def LoadMembers(filename="members.csv"):
    """Task 1.1: Load members from CSV file"""
    members = {}
    
    if not os.path.exists(filename):
        print(f"Error: {filename} not found")
        return members
    
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        
        for row in reader:
            member_id = row[0]
            member = Member(row[0], row[1], row[2], row[3])
            if len(row) > 4 and row[4]:
                member.fines = float(row[4])
            members[member_id] = member
    
    print(f"Loaded {len(members)} members")
    return members


def DisplayMemberDetails(member_id, members):
    """Task 1.2: Display details for a specific member"""
    if member_id in members:
        print(members[member_id])
    else:
        print(f"Member {member_id} not found")


def DisplayMembersWithFines(members, min_fine=0):
    """Task 1.2: Display all members with fines above threshold"""
    found = False
    for member_id, member in members.items():
        if member.fines > min_fine:
            print(member)
            found = True
    
    if not found:
        print("No members found with fines above the threshold")


def CalculateTotalFines(members):
    """Task 1.2: Calculate total fines for all members"""
    total = sum(member.fines for member in members.values())
    print(f"Total fines: £{total:.2f}")
    return total


def UpdateMemberFine(member_id, new_fine, members):
    """Task 1.3: Update fine for a specific member"""
    if member_id in members:
        members[member_id].fines = new_fine
        print(f"Updated member {member_id} fine to £{new_fine:.2f}")
        return True
    else:
        print(f"Member {member_id} not found")
        return False


def AddNewMember(member_id, name, membership_type, year_joined, members):
    """Task 1.3: Add a new member"""
    if member_id in members:
        print(f"Member ID {member_id} already exists")
        return False
    
    members[member_id] = Member(member_id, name, membership_type, year_joined)
    print(f"Added new member: {name}")
    return True


def RemoveMember(member_id, members):
    """Task 1.3: Remove a member"""
    if member_id in members:
        removed = members.pop(member_id)
        print(f"Removed member: {removed.name}")
        return True
    else:
        print(f"Member {member_id} not found")
        return False


def SaveMembers(filename, members):
    """Task 1.4: Save all members to CSV"""
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["MemberID", "Name", "MembershipType", "YearJoined", "Fines"])
        
        for member in members.values():
            writer.writerow([member.member_id, member.name, member.membership_type,
                           member.year_joined, f"{member.fines:.2f}"])
    
    print(f"Saved {len(members)} members to {filename}")


def SearchByName(search_term, members):
    """Task 1.4: Search members by name (partial match)"""
    found = False
    search_lower = search_term.lower()
    
    for member in members.values():
        if search_lower in member.name.lower():
            print(member)
            found = True
    
    if not found:
        print("No matching members found")


def FilterByMembershipType(membership_type, members):
    """Task 1.4: Filter members by membership type"""
    count = 0
    for member in members.values():
        if member.membership_type == membership_type:
            print(member)
            count += 1
    
    print(f"Total {membership_type} members: {count}")
    return count


if __name__ == "__main__":
    members = LoadMembers("members.csv")
    
    print("\n" + "=" * 80)
    print("Task 1.2: Display members with fines > £5")
    print("=" * 80)
    DisplayMembersWithFines(members, 5)
    
    print("\n" + "=" * 80)
    print("Task 1.2: Calculate total fines")
    print("=" * 80)
    CalculateTotalFines(members)
