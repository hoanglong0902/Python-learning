#TÌM LỖI
def dem_loi():
    mo_file=open("security.log","r")
    so_loi=0
    for loi in mo_file:
        if "ERROR" in loi:
            so_loi+=1
    mo_file.close()
    print(f"Tổng số lỗi : {so_loi}")

#TÌM TỪ KHOÁ
def tim_tu_khoa(tu_khoa):
    mo_file=open("security.log","r")                        #Khi mà người dùng nhập số 2 thì sẽ cho người dùng nhập từ khoá
    print(f"Kết quả tìm kiếm từ khoá : {tu_khoa}")          #Sau đó từ khoá đó sẽ xuất hiện và chúng ta gọi hàm def tim_tu_khoa(từ khoá mà ta đã nhập)
    tim_thay_tu_can_tim=False
    for tu_can_kiem in mo_file:                             #Sau đó nó liền chạy lên hàm def và bắt đầu mở file ròi in từ tìm được
        if tu_khoa in tu_can_kiem:                          #Rồi chạy vào vòng lặp ròi tạo ra mục lớn là tu_can_kiem
            print(tu_can_kiem.strip())                      #Khi đó từ cái từ khoá mà khách chọn sẽ đối chiếu vs từ cần kiếm và lọc ra đoạn từ khoá
            tim_thay_tu_can_tim=True
    mo_file.close()
    if tim_thay_tu_can_tim==False:
        print("Từ này không có trong từ điển!!!")
        print("Hãy nhập lại")

#TÌM IP ĐỘC
def quet_ip_doc(ip_can_tim):                                #ip_can_tim: Là 1 đoạn chuỗi ngắn1
    mo_file=open("security.log","r")                        #mo_file : là 1 đoạn chuỗi dài
    so_lan_xh=0
    for ip_can_kiem in mo_file:                             #ip_can_kiem : Nó đang nằm trong mo_file , mà mo_file là đoạn chuỗi dài => ip_can_kiem cũng là đoạn chuỗi dài
        if ip_can_tim in ip_can_kiem:                       #Thế nên ip_can_tim phải nằm trong ip_can_kiem
            so_lan_xh+=1
    mo_file.close()
    if so_lan_xh>=1:
        print(f"CẢNH BÁO MỨC ĐỘ CAO NHẤT!!!:IP {ip_can_tim} xuất hiện {so_lan_xh} lần , vượt quá số lần xuất hiện")
    else:
        print("AN TOÀN!!!",f"IP {ip_can_tim} xuất hiện {so_lan_xh} lần trong file",end="\n")

#CHỌN ĐIỀU BẠN MUỐN
while True:
    print("  ---HỆ THỐNG PHÂN TÍCH SECURITY LOG---  ")
    print("1. Đếm tổng số chữ ERROR")
    print("2. Tìm kiếm từ khóa bất kỳ")
    print("3. Kiểm tra IP độc hại (192.168.1.100)")
    print("4. Thoát chương trình")
    chon_so=input("Hãy chọn số mà bạn muốn : ")
    if chon_so=="1":
        dem_loi()
    elif chon_so=="2":
        tu_khoa_can_tim=input("Hãy nhập từ khoá bạn muốn tìm : ")
        tim_tu_khoa(tu_khoa_can_tim)
    elif chon_so=="3":
        quet_ip_doc("192.168.1.100")
    elif chon_so=="4":
        print("Đang đóng hệ thống!!!")
        break
    else:
        print("Lỗi ký tự xin hãy nhập lại!!!")
