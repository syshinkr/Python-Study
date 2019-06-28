class Diva:
    #클래스 변수
    version = "v4"

    #클래스 메소드
    def __init__(self, name="Diva"):
        #인스턴스 변수
        self.name = name

diva1 = Diva()
diva2 = Diva("Miku")
diva3 = Diva('hana')

def print_diva_info(diva):
    print("----")
    print("name : ", diva.name)
    print("version : ", diva.version)

print_diva_info(diva1)
print_diva_info(diva2)
print_diva_info(diva3)


diva2.version = "v2"
print_diva_info(diva1)