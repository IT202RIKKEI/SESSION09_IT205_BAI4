order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]


# order_list = []


while True:
    try:
        user_choice = int(input("""
===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
1. Hiển thị danh sách đơn hàng
2. Thêm đơn hàng mới
3. Xóa đơn hàng theo mã
4. Thoát chương trình
Mời bạn nhập vào lựa chọn: """))
        
        # ko được để trống
        if not user_choice:
            print("không được để trống!")
            continue
        
        match user_choice:
            case 1:
                if len(order_list) == 0:
                    print("Danh sách đơn hàng hiện đang trống.")
                else:
                    for position, order in enumerate(order_list, start=1):
                        print(f"{position}. {order}")
            case 2:
                
                # menu con
                
                sub_choice = int(input("""
----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----
1. Thêm đơn hàng mới
2. Sửa đơn hàng theo vị trí
3. Xóa đơn hàng theo vị trí
4. Quay lại menu chính
Mời nhập vào lựa chọn: """))
                                
                match sub_choice:
                    case 1:
                        # 2.1. Thêm đơn hàng mới
                        
                        new_product_id = input("Mời bạn nhập vào mã đơn hàng: ").strip().upper()
                        new_product_status = input("Mời bạn nhập vào trạng thái (PENDING, DELIVERING, COMPLETED, CANCELLED): ")
                        
                        format_new_product = f"{new_product_id} - {new_product_status}"
                        
                        # thêm vào cuối list
                        order_list.append(format_new_product)
                        print("Thêm sản phẩm thành công")
                    case 2:
                        # 2.2. Sửa đơn hàng theo vị trí
                        edit_position = int(input("Mời người dùng nhập vào vị trí cần sửa: "))
                        
                        real_position = edit_position - 1
                        
                        # kiểm tra tính hợp lệ
                        if real_position < 0 or real_position >= len(order_list):
                            print(f"Vị trí hợp lệ nên là: 1 - {len(order_list)}")
                        else:
                            new_product_id = input("Mời bạn nhập vào mã đơn hàng: ").strip().upper()
                            new_product_status = input("Mời bạn nhập vào trạng thái (PENDING, DELIVERING, COMPLETED, CANCELLED): ").strip().upper()
                            
                            format_new_product = f"{new_product_id} - {new_product_status}"
                            
                            order_list[real_position] = format_new_product
                            print("Đã cập nhật thành công")
                    case 3:
                        # 2.3. Xóa đơn hàng theo vị trí
                        delete_index = int(input("Mời bạn nhập vào vị trí cần xóa (bắt đầu từ 0):"))
                        
                        if delete_index < 0 or delete_index > len(order_list):
                            print("KHÔNG TỒN TẠI VỊ TRÍ NÀY ĐỂ XÓA")
                        else:
                            deleted_product = order_list.pop(delete_index)
                            
                            print(f"Đã xóa thành công đơn hàng: {deleted_product}")
                    case 4:
                        break
                
            case 3:
                # THỐNG KÊ SỐ LƯỢNG ĐƠN HÀNG
                count_pending_status = 0
                count_delivering_status = 0
                count_completed_status = 0
                count_cancelled_status = 0
                
                for order in order_list:
                    if "PENDING" in order:
                        count_pending_status += 1

                    elif "DELIVERING" in order:
                        count_delivering_status += 1

                    elif "COMPLETED" in order:
                        count_completed_status += 1

                    elif "CANCELLED" in order:
                        count_cancelled_status += 1
                
                print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
                print(f"PENDING    : {count_pending_status}")
                print(f"DELIVERING : {count_delivering_status}")
                print(f"COMPLETED  : {count_completed_status}")
                print(f"CANCELLED  : {count_cancelled_status}")
                print(f"Tổng số đơn hàng {len(order_list)}")
            case 4:
                print("ĐÃ THOÁT CHƯƠNG TRÌNH")
                break
            case _:
                print("nhập sai!")
        
    except ValueError:
        print("Không được nhập vào cái khác nha")