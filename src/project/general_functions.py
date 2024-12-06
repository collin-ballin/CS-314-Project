from lib.users import Member, Provider
from lib.services import Service

def add_member(name, id, address, city, state, zip):
    new_member = Member()
    new_member.name = name
    new_member.id = id
    new_member.address = address
    new_member.city = city
    new_member.state = state
    new_member.zip = zip

    return new_member

def edit_member(member_to_change, field_to_change, new_data):
    if field_to_change == 'name':
        member_to_change.name = new_data
    elif field_to_change == 'address':
        member_to_change.address = new_data
    elif field_to_change == 'city':
        member_to_change.city = new_data
    elif field_to_change == 'state':
        member_to_change.state = new_data
    elif field_to_change == 'zip':
        member_to_change.zip = new_data
    else:
        print("no changes were made")
        
    return member_to_change

    

def add_provider():
    new_provider = Provider()

def edit_provider():
    pass

def add_service():
    new_service = Service()

def edit_service():
    pass
