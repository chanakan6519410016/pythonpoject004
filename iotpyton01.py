#Function 1 : No Parameter/No Return
def funcA( ) :
    print('Wow')
    print('woo')
    print('wee')
    print('Wea')
    funcB( )
    #ไม่มีคำสั่ง return
    
def funcB( ) :
    print('Hi')
    # funcA( ) ทำได้แต่ไม่ควรทำ
funcA( )
funcA( )
funcB( )
funcA( )
