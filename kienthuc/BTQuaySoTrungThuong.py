# khai báo thunng2 phiếu
import random

thungPhieu = set()
while True:
    print("Vui lòng chọn chức năng")
    print("1.Thêm một số điện thoại vào thùng phiếu dự thưởng")
    print("2.Xóa một số điện thoại vào thùng phiếu dự thưởng")
    print("3.Quay một số ngủ nhiên điện thoại lấy ra từ thùng phiếu dự thưởng")
    print("4.kết thúc")
    print("Thùng Phieếu hiên tại: ", thungPhieu)
    luaChon = int(input("Lựa chọn: "))
    if luaChon == 1:
        soDienThoai = input("Nhập số điện thoại để thêm vào dể dự thưởng:")
        thungPhieu.add( soDienThoai)
    elif luaChon == 2:
        soDienThoai = input("Nhập số điện thoại để cần xóa: ")
        thungPhieu.discard(soDienThoai)
    elif luaChon == 3:
        index = random.randint(0, len(thungPhieu) - 1)
        print("vị trí trúng thưởng: " + str(index))
        i = 0
        for x in thungPhieu:
            if i == index:
                
                break
            print("chúc mừng SDT: " + x + "ĐÃ TRÚNG THƯỠNG")
            i += 1
            thungPhieu.discard(x)
    else:
        break
    print("Nhập phím bất kỳ để thực hiên chúc năng tiếp theo")
