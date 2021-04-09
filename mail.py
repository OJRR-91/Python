"""gusers=["Oscar Rodriguez","Jeus Martinez","Carlos Martinez"]
ousers=["Peter Parker","Tony Stark", "Steve Rogers","Bruce Banner"]
yusers=["Clark Kent", "Luisa Lane", "Bruce Wane","Barry allen"]"""
emails={"yahoo":["Clark Kent", "Luisa Lane", "Bruce Wane","Barry allen"],
    "gmail":["Oscar Rodriguez","Jesus Martinez","Carlos Martinez"],
    "outlook":["Peter Parker","Tony Stark", "Steve Rogers","Bruce Banner"]}
emailServer=emails.keys()
for server in emailServer:
    for usr in emails[server]:
        usuario=usr.replace(" ",".")
        print("{}@{}.com".format(usuario,server)) 