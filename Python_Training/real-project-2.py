import csv
import json
import mysql.connector
from cryptography.fernet import Fernet

csvpath = r"C:\Users\User\PycharmProjects\pythonProject3\mycsvfile.csv"
linux_jsonfile = r"C:\Users\User\PycharmProjects\pythonProject3\mylinux.json"

with open(linux_jsonfile) as jf:
    print("We are fetching MySQL password with encryption and decryption......")
    my_dict = json.load(jf)
    username_mysql = my_dict["username"]
    password_mysql = my_dict["password"]
    message = password_mysql.encode("utf-8")
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message)
    decrypted_message = f.decrypt(encrypted_message)
    passwd_mysql = decrypted_message.decode("utf-8")
    print(passwd_mysql)

    mydb = mysql.connector.connect(
        host="192.168.0.150",
        user="mysql_user",
        passwd=passwd_mysql,
        database="alnafi"
    )
    print("CSV file reading and storing into MySQL database")

    with open(csvpath) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        all_values = []

        # Skip the header row if it exists
        headers = next(readCSV, None)
        print(f"Headers found: {headers}")

        for row_num, row in enumerate(readCSV, start=2):
            if len(row) == 9:
                try:
                    # Clean the usage percentage - remove '%' and convert to integer
                    usage_percent = row[4].replace('%', '').strip()
                    if usage_percent.isdigit():
                        usage_value = int(usage_percent)
                    else:
                        usage_value = 0  # Default value if not a number
                        print(f"Warning: Row {row_num} - Invalid usage value '{row[4]}', using 0")

                    value = (row[0], row[1], row[2], row[3], usage_value, row[5], row[6], row[7], row[8])
                    all_values.append(value)

                except Exception as e:
                    print(f"Error processing row {row_num}: {row} - {e}")
            else:
                print(f"Skipping row {row_num} with incorrect column count: {row}")

    if all_values:
        query = "INSERT INTO my_df_data (filesystem, size, used, avail, usage_with_per, mounted_on, datetime, ip_address, hostname) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        mycursor = mydb.cursor()

        try:
            mycursor.executemany(query, all_values)
            mydb.commit()
            print(f"Successfully inserted {mycursor.rowcount} rows into database")
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
        finally:
            mycursor.close()
    else:
        print("No valid data to insert")

    mydb.close()