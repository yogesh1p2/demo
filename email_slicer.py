#email_slicer
email = input("What is the email address: ").strip()
user = email[0:email.index("@")]
domain = email[email.index("@")+1:]
print("Your email is {} and your username is {} and domain is {}".format(email,user,domain))