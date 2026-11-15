name = "ณรงชัย "
visits = 10
month = 10

#ฟังชั้นสำหรับครวจความเสี่ยง
def is_at_risk(visits,month):
  return visits < 4 and month > 6
#แสดงผลลัพธ
print("ชื่อสมาชิก :", name)
print("จำนวนครั้งที่ใช้งาน :", visits)
print("อายุสามชิก :", month,"เดือน")
print("เสี่ยงเลิกใช้บริการ :", is_at_risk(visits,month))