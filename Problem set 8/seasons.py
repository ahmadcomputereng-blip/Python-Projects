from datetime import date
import sys
import inflect

def main():
    print(text_date(input("Date of Birth: ")))

def text_date(birth):
    try:
        year, month , day = birth.split("-")
        d1 = date(int(year) , int(month) , int(day))
        d2 = date.today()
        diff = d2 - d1
        minutes = diff.days * 24 * 60
        interval = f"{inflect.engine().number_to_words(minutes)} minutes"
        if "and" in interval:
            interval = interval.replace("and ", "")
        return (interval[0].upper() + interval[1:])
    except:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
