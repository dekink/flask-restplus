from marshmallow import Schema, fields, post_load


class UserData(object):
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return '{} , {}'.format(self.name, self.phone)


class UserSchema(Schema):
    name = fields.String()
    phone = fields.String()

    @post_load
    def creat_user(self, data):
        return UserData(**data)

input_dict = {}
input_dict['name'] = 'daeun'
input_dict['phone'] = '01022223333'

# user = UserData(input_dict['name'], input_dict['phone'])

schema = UserSchema()
# result = schema.dump(user)
result = schema.load(input_dict)
print(result.data)
# print(input_dict)