import requests as re
import pandas as pd
import json

pd.options.display.max_columns = None
#pd.options.display.max_rows = None

class web_scrap:

    #connect_to_url
    def get_random_users(n):
        response = re.get("https://randomuser.me/api/?results={}".format(n))
        data = response.json()
        return data["results"]

    #get_data
    users = get_random_users(1000)

    #create_schema_dataframe
    df = pd.DataFrame(users, columns=["login", "name", "gender","dob", "location", "email", "phone", "picture"])

    #drop_some_columns
    df = pd.concat([df.drop(["login"], axis=1), df["login"].apply(pd.Series)], axis=1)
    df = pd.concat([df.drop(["name"], axis=1), df["name"].apply(pd.Series)], axis=1)
    df = pd.concat([df.drop(["location"], axis=1), df["location"].apply(pd.Series)], axis=1)
    df = pd.concat([df.drop(["dob"], axis=1), df["dob"].apply(pd.Series)], axis=1)
    df = pd.concat([df.drop(["picture"], axis=1), df["picture"].apply(pd.Series)], axis=1)

    #build_data
    df = df[["uuid",
            "first",
            "last",
            "gender",
            "age",
            "state", 
            "city", 
            "country", 
            "postcode",
            "email",
            "phone",
            "large"
            ]]
    
    #join_column
    df["full_name"] = df[["first", "last"]].apply(lambda x: " ".join(x), axis=1)

    #setting_position_column
    df = df[["uuid", "full_name", "gender", "age", "state", "city", "country", "postcode", "email", "phone", "large"]]

    #change_name_columns
    column_names = {"uuid": "id_user",
                    "full_name": "nama",  
                    "gender": "jenis_kelamin",
                    "age": "umur",
                    "state": "kecamatan", 
                    "city": "kota", 
                    "country": "negara", 
                    "postcode": "kode_pos",
                    "email": "email",
                    "phone": "No.HP",
                    "large": "url_photo"}

    df.rename(columns=column_names, inplace=True)

    #output
    print(df.head(10))

    #save_to_csv
    try :

        data_to_csv = df.to_csv("User.csv", index=False)

        print("Data user success to save")
    
    except :

        print("Data user unsuccess to save")