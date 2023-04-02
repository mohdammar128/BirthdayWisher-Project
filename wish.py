# 1->friend
# 2->jija
# 3->general
# 4->sister
# 5->brother

import smtplib
import pandas as pd
import datetime as dt

now = dt.datetime.now()
date = now.date().strftime(f"%Y-%m-%d")
date = date[5:]
time=now.hour

print(date)

my_email = "ammarsiddiqui1282003@gmail.com"
password = "idolvrojtegtzoan"

df = pd.read_csv("birthday.csv")

birthday_dob = df["dob"].tolist()
birthday_dob = [x[5:] for x in birthday_dob]

bithday_boy = df["name"].to_list()
birthdayboy_mail = df["email"].to_list()
birtdayboy_name = df["name"].to_list()
birthday_typ=df['typ'].to_list()
print(birthday_dob, birthdayboy_mail)

# --------------------------------------------------------------------------------------------------------------------
if date in birthday_dob :
    idx = birthday_dob.index(date)
    name_of_bb = birtdayboy_name[idx]
    mail_of_bb = birthdayboy_mail[idx]
    
    print((mail_of_bb))
    if birthday_typ[idx]=='friend':
       file_path=f"./Birthday letter/letter_1.txt"
    elif birthday_typ[idx]=='jija':
       file_path=f"./Birthday letter/letter_2.txt"
    elif birthday_typ[idx]=='general':
       file_path=f"./Birthday letter/letter_3.txt"
    elif birthday_typ[idx]=='sister':
       file_path=f"./Birthday letter/letter_4.txt"
    elif birthday_typ[idx]=='brother':
       file_path=f"./Birthday letter/letter_5.txt"
         
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        nt = text.replace("[name]", name_of_bb)
        nt=nt.replace("[regard]",'Mohd Ammar')
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=mail_of_bb,
            msg=f"Subject:Happy Birthday 🎂\n\n{nt}".encode('utf-8')
        )


