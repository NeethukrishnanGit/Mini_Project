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
        "Available": True,
        "Check_IN": "08:24 AM",
        "Check_OUT": "10:00 AM"
     },
    {
        "name": "Manipulator",
        "type": "C",
        "description": "This is used to support and tilt the test head",
        "Available": True,
        "Check_IN": "12:00 AM",
        "Check_OUT": "03:30 PM"
    },
    {
        "name": "Test Head",
        "type": "B",
        "description": "This carries some critical sensitive devices",
        "Available": False,
        "Check_IN": "01:30 PM",
        "Check_OUT": "04:00 PM"
     },
    {
        "name": "Tester Rack",
        "type": "COMBINED",
        "description": "This contains of bulky instruments",
        "Available": True,
        "Check_IN": "10:00 AM",
        "Check_OUT": "11:30 AM"
     },
    {
        "name": "Device Interface",
        "type": "COMBINED",
        "description": "This sits on top of the TEST HEAD",
        "Available": True,
        "Check_IN": "03:00 PM",
        "Check_OUT": "05:00 PM"
     },
    {
        "name": "Instrument Cards",
        "type": "COMBINED",
        "description": "This is Fixed inside the TEST HEAD",
        "Available": False,
        "Check_IN": "02:00 PM",
        "Check_OUT": "04:00 PM"
    }
]
}

Instrument_Collection.insert_many(instruments_dict["Instruments"])


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

