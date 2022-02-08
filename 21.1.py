def vat(price):
    v = price*(7/100)
    return v

def disc(price):
    d = price*(10/100)
    return d

def total(price,vat,disc):
    t = price+vat-disc
    return t

price = int(input("ราคาสินค้า:"))
price("ภาษีมูลค่าเพิ่ม", vat(price))
price("ส่วนลด", disc(price))
price("ราคารวม", total(price,vat(price),disc(price)))
    