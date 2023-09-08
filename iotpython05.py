# หาพื้นที่สี่เหลี่ยม และสามเหลี่ยม โดยรับกว้าง ยาว/ฐาน สูง ทางแป้นพิมพ์ และแสดงผลทางหน้าจอ
# feature การทำงานอะไรบ้าง
# 1. รับค่า กว้างยาว 2. รับค่า ฐาน สูง 
# 3. คำนวณพท.สี่เหลี่ยม และแสดงพท.สี่เหลี่ยม  4. คำนวณพท.สามเหลี่ยม และแสดงพท.สามเหลี่ยม
def inputWitdhLong( ) :
    wi = float(input('ป้อนกว้าง : '))
    lo = float(input('ป้อนยาว : '))
    return wi,lo

def inputBaseHigh( ) :
    be = float(input('ป้อนฐาน : '))
    hi = float(input('ป้อนสูง : '))
    return be,hi

def calAndShowAreaSquare( wi, lo ) :
    area = wi * lo
    print(f'สี่เหลี่ยมกว้าง {wi} ยาว {lo} มีพื้นที่ {area}')

def calAndShowAreaTrianble( ba, hi ) :
    area = ba * hi / 2
    print(f'สามเหลี่ยมฐาน {ba} สูง {hi} มีพื้นที่ {area}')
    
wi, lo = inputWitdhLong()
calAndShowAreaSquare(wi, lo)
print('-------------------------------')
ba, hi = inputBaseHigh( )
calAndShowAreaTrianble(ba, hi)
