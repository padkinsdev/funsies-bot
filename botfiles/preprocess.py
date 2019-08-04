import botfiles.bot_data as bd

gatekeeper = bd.gatekeeper

def update_activity(message):
  uptick(message.author.id, "activity")


def preprocess_list(message):
  update_activity(message)


def uptick(user_id, field_name):
  curVal = gatekeeper.userDB.get_field(user_id, field_name)
  if curVal:
    gatekeeper.userDB.write_field(user_id, field_name, curVal+1)
  else:
    gatekeeper.userDB.write_field(user_id, field_name, 1)
