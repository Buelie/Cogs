import Math.area
import Math.volume

if __name__ == '__main__':
    while True:
        command = input("Debugging\\\\User\\\\root>>>")
        if command == "$Math":
            print("数学函数调试:")
            print("正方形的面积(10*10)=" + str(Math.area.Area(10).square()))
            print("长方形的面积(10*10)=" + str(Math.area.Area(10).rectangle(10)))
            print("平行四边形的面积(10*10)=" + str(Math.area.Area(10).parallelogram(10)))
            print("梯形的面积((5+5)*10)=" + str(Math.area.Area(10).trapezium(5, 5)))
            print("园的面积(2²*3.14)=" + str(Math.area.Area(0).round(2)))
            print("长方体的表面积(h:10,w:10,l:1)=" + str(Math.area.Area(10).cuboid(1, 10)))
            print("正方体的表面积(10*10*6)=" + str(Math.area.Area(10).cube()))
            print("圆柱的表面积(r:2,h:10)="+str(Math.area.Area(10).cylinder(2)))
            print("")
            print("长方体的体积(l:10,w:10,h:10)="+str(Math.volume.Volume(10).cuboid(10,10)))
            print("正方体的体积(l:10)="+str(Math.volume.Volume(10).cube()))
            print("圆柱的体积(r:10,h:1)="+str(Math.volume.Volume(1).cylinder(10)))
            print("")
        elif command == "$HELP" or command == "$Help":
            print("= = = = = = HELP | 帮助 = = = = = =")
            print("|$Math                  数学函数调试|")
            print("|$Help                  获取所有帮助|")
            print("= = = = = = = = = = = = = = = = = =")
