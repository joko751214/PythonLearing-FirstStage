
from menu import show_menu
from student_info import *

# 定義一個主函數，用來獲取鍵盤操作，實現選擇的功能
def main():
    docs = []  # 此列表用來存储所有學生的信息的字典
    while True:
        show_menu()
        s = input("請選擇: ")
        if s == '1':
            docs += input_student()
        elif s == '2':
            output_student(docs)
        elif s == '3':  # 修改學生成績
            modify_student_info(docs)
        elif s == '4':  # 刪除學生成績
            delete_student_info(docs)
        elif s == '5':
            print_by_score_desc(docs)
        elif s == '6':
            print_by_score_asc(docs)
        elif s == '7':
            print_by_age_desc(docs)
        elif s == '8':
            print_by_age_asc(docs)
        elif s == '9':
            # 保存
            save_to_file(docs)
        elif s == '10':
            # 讀取
            docs = read_from_file()
        elif s == 'q':
            return  # 結束此函數執行，直接退出

main()
