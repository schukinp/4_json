# Prettify JSON

Script prints to console JSON file data in readable format

# Quickstart

* Put your JSON file into script folder
* Run pprint_json.py --file `filename.json`

Example of script launch on Linux, Python 3.5:
```
$ python pprint_json.py --file alco_shops.json
{
    "geometry": {
        "coordinates": [
            37.52306063236498,
            55.603784102617695
        ],
        "type": "Point"
    },
    "properties": {
        "Attributes": {
            "Address": "Вильнюсская улица, дом 5",
            "AdmArea": "Юго-Западный административный округ",
            "ClarificationOfWorkingHours": null,
            "District": "район Ясенево",
            "IsNetObject": "нет",
            "Name": "СТУДИЯ-ЛюМиСон",
            "OperatingCompany": null,
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 423-31-51"
                }
            ],
            "TypeService": "реализация продовольственных товаров",
            "WorkingHours": [
                {
                    "DayOfWeek": "понедельник",
                    "Hours": "09:00-22:00"
                },
                {
                    "DayOfWeek": "вторник",
                    "Hours": "09:00-22:00"
                },
                {
                    "DayOfWeek": "среда",
                    "Hours": "09:00-22:00"
                },
                {
                    "DayOfWeek": "четверг",
                    "Hours": "09:00-22:00"
                },
                {
                    "DayOfWeek": "пятница",
                    "Hours": "09:00-22:00"
                },
                {
                    "DayOfWeek": "суббота",
                    "Hours": "09:00-22:00"
                },
                {
                    "DayOfWeek": "воскресенье",
                    "Hours": "09:00-22:00"
                }
            ],
            "global_id": 58943804
        },
        "DatasetId": 1854,
        "ReleaseNumber": 2,
        "RowId": "262b6a0b-3479-4540-b0cc-2ffb84142ce9",
        "VersionNumber": 1
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
