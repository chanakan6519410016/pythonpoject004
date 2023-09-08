#Function 2 : Have Parameter/No Return
#parameter คือ ตัวแปรประเภทหนึ่ง ขอบเขตการใช้พารามิเตอร์
# จะใช้ได้เฉพาะในฟังก์ชันนั้นๆ เท่านั้น

def funcA( x , y ) :
    print('Hi...')
    z = x + y 
    print(f'{x} + {y} = {z}')
    

def funcB( x ) :
    print(f"x is {x} 555...")
          
funcA(10, 20) #Argument อากิวเมนต์
funcA(5, 5)
funcB( 'SAU IoT')
