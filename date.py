from datetime import datetime


now = datetime.now()


formatted_datetime = now.strftime("%b %d, %Y %I:%M:%S %p")


print(formatted_datetime)

