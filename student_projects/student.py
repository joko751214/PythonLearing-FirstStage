
class Student:
    count = 0  # 此类变量用来记录学生的个数

    def __init__(self, n, a, s=0):
        self.__name = n
        self.__age = a
        self.__score = s
        Student.count += 1  # 让对象个数加1
    def __del__(self):
        Student.count -= 1  # 对象销毁时count减1

    def get_age(self):
        return self.__age

    def get_score(self):
        return self.__score

    def set_score(self, score):
        '''此方法用於制定設置成績時的規則'''
        if 0 <= score <= 100:
            self.__score = score
            return
        raise ValueError('不合法的成績信息:'+ str(score))


    def get_infos(self):
        return (self.__name, self.__age, self.__score)

    def is_name(self, n):
        '''判斷n是否和self的名字相同'''
        return self.__name == n

    def write_to_file(self, file):
        file.write(self.__name)
        file.write(',')
        file.write(str(self.__age))
        file.write(',')
        file.write(str(self.__score))
        file.write('\n')

    @classmethod
    def getTotalCount(cls):
        '''此方法用來得到學生對象的個數'''
        return cls.count


def test():
    L = []  # 1班的學生
    L.append(Student('小張', 20, 100))
    L.append(Student('小王', 18, 97))
    L.append(Student('小李', 19, 98))
    print('此时學生對象的個數是:',
          Student.getTotalCount())

    L2 = []  # 2班學生
    L2.append(Student('小趙', 18, 99))
    print(Student.getTotalCount())  # 4
    # 删除L中的一个学生
    L.pop(1)
    print("此時學生個數為:", Student.getTotalCount())

    all_student = L + L2
    scores = 0  # 用此變量來記錄所有學生的成績總和
    for s in all_student:
        # scores += s.score  # 累加所有學生的成績
        scores += s.get_score()

    print("平均成績是:", scores/len(all_student))


if __name__ == '__main__':
    test()

