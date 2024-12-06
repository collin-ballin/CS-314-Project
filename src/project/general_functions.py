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

def add_provider(name, id, address, city, state, zip):
    new_provider = Provider()
    new_provider.name = name
    new_provider.id = id
    new_provider.address = address
    new_provider.city = city
    new_provider.state = state
    new_provider.zip = zip

    return new_provider

# names, IDs, dos, dor, comments only need to be added when making changes to the service
# and when they're added to member/provider records
def add_service(name, id, fee):
    new_service = Service()
    new_service.name = name
    new_service.id = id
    new_service.fee = fee

    return new_service

def edit_object(obj_to_change, field_to_change, new_data):
    if hasattr(obj_to_change, field_to_change):
        setattr(obj_to_change, field_to_change, new_data)
    else:
        print("No changes were made: Invalid field name.")
    return obj_to_change
