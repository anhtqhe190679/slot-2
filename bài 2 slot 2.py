
while True:
    try:
        x = float(input('Nhập điểm trung bình của bạn: '))
        if 0.0 >= x <= 10.0:
            break
        else:
            print:('Vui lòng nhập lại')
            break
                
    except ValueError:
        print('Vui lòng nhập lại')
        
        break
def quy_doi_diem():
    if x < 4.0:
        print('Điểm hệ số 4 của bạn là: 0')
        print('Điểm chữ của bạn là: F')
    elif x >= 4.0 and x <= 5.4:
        print('Điểm hệ số 4 của bạn là: 1')
        print('Điểm chữ của bạn là: D')
    elif x >= 5.5 and x <= 6.9:
        print('Điểm hệ số 4 của bạn là: 2')
        print('Điểm chữ của bạn là: C')
    elif x >= 7.0 and x <= 8.4:
        print('Điểm hệ số 4 của bạn là: 3')
        print('Điểm chữ của bạn là: B')
    else:
        print('Điểm hệ số 4 của bạn là: 4')
        print('Điểm chữ của bạn là: A')

while True:
    quy_doi_diem()
    break
    
    


        