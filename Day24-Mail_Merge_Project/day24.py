
def open_letter():
    with open("/Users/moniqueschukking/Desktop/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") \
            as file:
        return file.read()


def new_email(name):
    with open(f"/Users/moniqueschukking/Desktop/Mail Merge Project Start/Output/ReadyToSend/mail_for_{name}.txt",
              mode="w") as \
            mail:
        text = open_letter()
        new_text = text.replace("[name]", name)  
        mail.write(new_text)


name_list = open("/Users/moniqueschukking/Desktop/Mail Merge Project Start/Input/Names/invited_names.txt").readlines()

for n in range(len(name_list)):
    list_name = name_list[n - 1]
    stripped_name = list_name.strip("\n") 
    new_email(name=stripped_name)  
