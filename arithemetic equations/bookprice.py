""" 
wholesale cost for 60 copies
Author = Karan
"""

book_cover_price = 24.95
discount = 40 # in percentage %
copies = 60

book_discount_price = book_cover_price * discount / 100
unit_price = book_cover_price - book_discount_price # book price after discount

total = unit_price * copies                         
# shipping  cost
shipping = 3 + 0.75* (copies - 1)
grand_total = total + shipping
print("total wholesale cost for 60 copies is $", grand_total,sep="")                        