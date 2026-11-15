class Member:
  def __init__(self,name,visits,months):
    self.name = name
    self.visite= visits
    self.months= months

  def is_at_risk(self):
      return self.visite < 4 and self.months > 6

m1 = Member("สายฟ้า วิทยา", 2, 10)
m2 = Member("โชค", 2 , 10)
m3 = Member("พอส", 2 ,10)

print("ชื่อสมาชิก :", m1.name)
print("เสี่ยงเลิกใช้บริการ :", m1.is_at_risk())

# สำหรับ โชค
print("ชื่อสมาชิก :", m2.name)
print("เสี่ยงเลิกใช้บริการ :", m2.is_at_risk())

# สำหรับ พอส
print("ชื่อสมาชิก :", m3.name)
print("เสี่ยงเลิกใช้บริการ :", m3.is_at_risk())    