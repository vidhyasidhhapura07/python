# check is given year is leep year or not

year = int(input("enter any year"))

def a(year):
    if (year % 4 == 0):
        print(f"yes, {year}  is leep year")
    else:
        print(f"no..! {year} is not leep year")
a(year)
