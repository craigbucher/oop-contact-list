class ContactList():
    contacts = []
    def __init__(self, list_name, list_item):
        self.list_name = list_name
        self.list_item = list_item
        ContactList.contacts.append([list_name, list_item])

    # def __str__(self):
    #     return(f'{self.list_item}')

    def add_contact(self, contact_add):
        self.list_item.append(contact_add)
        self.list_item = sorted(self.list_item, key=lambda x: x['name'])
        print(self.list_item)

    def remove_contact(self, contact_remove):
        for i in range(0, len(self.list_name)):
            if self.list_name[i][0] == contact_remove:
                del self.list_name[i]

friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]
my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)

new_contact = {'name': 'Craig', 'number': '739-8994'}
my_friends_list = my_friends_list.add_contact(new_contact)
my_friends_list = my_friends_list.remove_contact('Craig')

print(ContactList.contacts)