import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["employee_asset_management"]


Instrument_Collection = mydb["Instruments"]

instruments_dict = {"Instruments": [
    {
        "name": "Prober",
        "type": "A",
        "description": "This is used to test wafer ",
        "Available": True,
        "Check_IN": "12:00 AM",
        "Check_OUT": "11:00 AM"
    },
    {
        "name": "Handler",
        "type": "A",
        "description": "This used to test packaged device and place the component for testing",
        "Availability": True,
        "Check_IN": "08:24 AM",
        "Check_OUT": "10:00 AM"
     },
    {
        "name": "Manipulator",
        "type": "C",
        "description": "This is used to support and tilt the test head",
        "Availability": True,
        "Check_IN": "12:00 AM",
        "Check_OUT": "03:30 PM"
    },
    {
        "name": "Test Head",
        "type": "B",
        "description": "This carries some critical sensitive devices",
        "Availability": False,
        "Check_IN": "01:30 PM",
        "Check_OUT": "04:00 PM"
     },
    {
        "name": "Tester Rack",
        "type": "COMBINED",
        "description": "This contains of bulky instruments",
        "Availability": True,
        "Check_IN": "10:00 AM",
        "Check_OUT": "11:30 AM"
     },
    {
        "name": "Device Interface",
        "type": "COMBINED",
        "description": "This sits on top of the TEST HEAD",
        "Availability": True,
        "Check_IN": "03:00 PM",
        "Check_OUT": "05:00 PM"
     },
    {
        "name": "Instrument Cards",
        "type": "COMBINED",
        "description": "This is Fixed inside the TEST HEAD",
        "Availability": False,
        "Check_IN": "02:00 PM",
        "Check_OUT": "04:00 PM"
    }
]
}

Instrument_Collection.insert_many(instruments_dict["Instruments"])

Audit_Collection = mydb["Audit Data"]
audit_data = {"01/01/2023": [{"Instrument_ID": "I-21",
                        "Event Type": "Check_Out",
                        "Time": "11:00 AM"
                        },
                       {"Instrument_ID": "I-24",
                        "Event Type": "Check_In",
                        "Time": "11:30 AM"
                        },
                       {
                        "Instrument_Id": "I-44",
                        "Event Type": "Check_Out",
                        "Time": "03:00 PM"
                        },
                       {
                        "Instrument_Id": "I-04",
                        "Event Type": "Check_Out",
                        "Time": "03:00 PM"
                        }
                       ]}

Audit_Collection.insert_many(audit_data["01/01/2023"])


user_Collection = mydb["users"]
user_dict = {"users": [
    {
        "User_Name": "Mithileash",
        "Role": "Automation"
    },
    {
        "User_Name": "Naveen",
        "Role": "DFT"
    },
    {
        "User_Name": "Roshan",
        "Role": "ATE"
    },
    {
        "User_Name": "nivedha",
        "Role": "Automation"
    },
    {
        "User_Name": "Pugazhi",
        "Role": "ATE"
    }
]
}
user_Collection.insert_many(user_dict["users"])