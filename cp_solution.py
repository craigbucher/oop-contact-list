class ContactList(object):
    def __init__(self, name, contacts):
        self.name = name
        self.contacts = contacts
        self.contacts.sort(key=get_name)  # Use lambda equation?

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.contacts.sort(key=get_name)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.remove(contact)

    def find_shared_contacts(self, other_contact_list):
        shared_contacts = ContactList(f'{self.name} & {other_contact_list.name} shared contacts', []) #name for new list
        for contact in self.contacts:
            for other_contact in other_contact_list.contacts:
                if contact['name'] == other_contact['name'] and contact['number'] == other_contact['number']:
                    shared_contacts.add_contact(contact)
        return shared_contacts


######## Driver Code #########
def get_name(item):
    return item['name']

alice = {
    'name': 'alice',
    'number' : '867-5309'
}
bob = {
    'name': 'bob',
    'number' : '555-5555'
}
carol = {
    'name': 'carol',
    'number' : '123-4567'
}
dan = {
    'name': 'dan',
    'number' : '987-6543'
}
eve = {
    'name': 'eve',
    'number' : '711-2022'
}

friends_list = ContactList('my friends', [alice, bob, dan, carol])
# print(friends_list.name)
# print(friends_list.contacts)
# friends_list.add_contact(eve)
# print(friends_list.contacts)
# friends_list.remove_contact('alice')
# print(friends_list.contacts)
work_friends = ContactList('my coworkers', [alice, bob, dan, eve])
shared_contacts = work_friends.find_shared_contacts(friends_list)
print(shared_contacts.name)
print(shared_contacts.contacts)
