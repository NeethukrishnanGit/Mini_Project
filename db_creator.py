import datetime

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["employee_asset_management"]

Instrument_Collection = mydb["Instruments"]

instruments_dict = {"Instruments": [
    {
        "name": "Prober",
        "type": "A",
        "description": "This is used to test wafer ",
        "availability": True,
        "check_in": datetime.datetime(2022, 11, 16, 00, 00, 00),
        "check_out": datetime.datetime(2022, 11, 16, 00, 00, 00)
    },
    {
        "name": "Handler",
        "type": "A",
        "description": "This used to test packaged device and place the component for testing",
        "availability": True,
        "check_in": datetime.datetime(2022, 11, 16, 00, 00, 00),
        "check_out": datetime.datetime(2022, 11, 16, 00, 00, 00)
    },
    {
        "name": "Manipulator",
        "type": "C",
        "description": "This is used to support and tilt the test head",
        "availability": True,
        "check_in": datetime.datetime(2022, 11, 16, 00, 00, 00),
        "Check_out": datetime.datetime(2022, 11, 16, 00, 00, 00)
    },
    {
        "name": "Test Head",
        "type": "B",
        "description": "This carries some critical sensitive devices",
        "availability": False,
        "check_in": datetime.datetime(2022, 11, 16, 00, 00, 00),
        "check_out": datetime.datetime(2022, 11, 16, 00, 00, 00)
    },
    {
        "name": "Tester Rack",
        "type": "COMBINED",
        "description": "This contains of bulky instruments",
        "availability": True,
        "check_in": datetime.datetime(2022, 11, 16, 00, 00, 00),
        "check_out": datetime.datetime(2022, 11, 16, 00, 00, 00)
    },
    {
        "name": "Device Interface",
        "type": "COMBINED",
        "description": "This sits on top of the TEST HEAD",
        "availability": True,
        "check_in": datetime.datetime(2022, 11, 16, 00, 00, 00),
        "check_out": datetime.datetime(2022, 11, 16, 00, 00, 00)
    },
    {
        "name": "Instrument Cards",
        "type": "COMBINED",
        "description": "This is Fixed inside the TEST HEAD",
        "availability": False,
        "check_in": datetime.datetime(2022, 11, 16, 00, 00, 00),
        "check_out": datetime.datetime(2022, 11, 16, 00, 00, 00)
    }
]
}

instrument_ids = Instrument_Collection.insert_many(instruments_dict["Instruments"])

user_Collection = mydb["users"]
user_dict = {"users": [
    {
        "user_name": "Mithileash",
        "role": "EMPLOYEE"
    },
    {
        "user_name": "Naveen",
        "role": "CUSTOMER"
    },
    {
        "user_name": "Roshan",
        "role": "PARTNER"
    },
    {
        "user_name": "nivedha",
        "role": "EMPLOYEE"
    },
    {
        "user_name": "Pugazhi",
        "role": "CUSTOMER"
    }
]
}
user_ids = user_Collection.insert_many(user_dict["users"])

Audit_Collection = mydb["Audit Data"]
audit_dict = {"02/11/2022": [
    {
        "user_id": user_ids[0],
        "instrument_id": instrument_ids[0],
        "event type": "check_out",
        "time": datetime.datetime(2022, 11, 2, 00, 00, 00)
    },
    {
        "user_id": user_ids[1],
        "instrument_id": instrument_ids[0],
        "event type": "check_out",
        "time": datetime.datetime(2022, 11, 2, 00, 00, 00)
    },
    {
        "user_id": user_ids[0],
        "instrument_id": instrument_ids[2],
        "event type": "check_out",
        "time": datetime.datetime(2022, 11, 2, 00, 00, 00)
    },
    {
        "user_id": user_ids[1],
        "instrument_id": instrument_ids[2],
        "event type": "check_out",
        "time": datetime.datetime(2022, 11, 2, 00, 00, 00)
    }
]}

audit_data = Audit_Collection.insert_many(audit_dict["02/11/2022"])
