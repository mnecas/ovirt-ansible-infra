#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        'Define filters'
        return {
            'removepassword': self.removepassword,
        }

    def removepassword(self, data):
        """ If data contains password it will change to SECRETE """
        for i in range(len(data)):
            if 'password' in data[i]["item"]:
                data[i]["item"]['password'] = "SECRET"
        return data