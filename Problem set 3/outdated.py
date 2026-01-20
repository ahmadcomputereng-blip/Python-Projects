my_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while (True):
    try:
        date = input("Date: ").strip()
        if "/" in date:
            year = date.split("/")[2]
            day = int(date.split("/")[1])
            month = int(date.split("/")[0])
            if 0 <= day <= 31 and 0 <= month <= 12:
                print(f"{year}-{month:02}-{day:02}")
                break
            else:
                raise ValueError
        elif "," in date:
            year = date.split(" ")[2]
            day = int(date.split(" ")[1].replace("," , ""))
            month = date.split(" ")[0].title()
            if month in my_list:
                month = my_list.index(month)+1
            if 0 <= day <= 31 and 0 <= month <= 12:
                print(f"{year}-{month:02}-{day:02}")
                break
            else:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        continue
