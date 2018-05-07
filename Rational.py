class Rational:
    """
    1 参数列表第一个参数表示实际使用时的调用对象， self 作为参数时 ，表示的时实例方法；
    
    2 在一个类里 通常都会定义一个初始化方法，用来构造本类的新对象。
      创建实例对象采用函数调用的描述形式，以类名作为函数名。

    3 程序里不需要说明对象有哪些属性，赋值就会创建
     
    4 非实例方法 静态方法： 本质上说就是类里面定义的普通函数，也是该类的局部函数 ；
      描述时 需要在函数定义的头部行之前加上修饰符 @staticmethod,参数表中不应该有self参数
		
    5 类定义可以写在程序的任何地方，但通常把类定义写在模块最外层，这样定义的类类型可以在
      整个模块里都可以用，而且允许其它模块通过import 语句导入和使用
     
    6 类的实例方法, 通过 x.method(...)的形式调用方法函数method时， 对象x将被作为method的第一个实参，
      约束到方法函数的第一个形参self

    7 类方法 :定义的形式是在def行前 加修饰符@classmethod。 这种方法必须有一个表示其调用类的参数，习惯
      用cls作为参数名， 在类方法执行时，调用他的的类将自动约束到方法的cls参数

    8 作用域： 函数定义，其中局部名字的作用域自动延伸到内部嵌套的作用域；
      类定义，则不同，在类里定义的名字，不会自动延伸到内部嵌套的作用域。
      因此需要在类中的函数定 义里引用这个类的属性，一定要采用基于  类名的属性引用方式。

    9 静态约束或静态绑定， 在python中不是这样的， 基于方法调用时 self所表示的那个实例对象的类型确定。
      在程序设计领域，这种通过动态约束确定调用关系的函数称为虚寒数。
      


 	
    """

    counter = 0;

    @staticmethod
    def _gcd(m, n):
        # print("int n = %d; m = %d" % (n, m))
        if n == 0:
            m, n = n, m
            # print("n = %d; m = %d" %(n,m))
        while m != 0:
            # 下一轮：分母是上一轮的分子 分子是 上一轮分母取模分子 ，直到分子为0结束
            m, n = n % m, m
            # print("n = %d; m = %d" % (n, m))

        # print("max n = %d" %(n));
        return n

    @classmethod
    def get_count(cls):
        # print("countter= %d  " %Rational.counter)
        return Rational.counter

    def __init__(self, num, den=1):
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError

        sign = 1

        if num < 0:
            num, sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign

        g = Rational._gcd(num, den)

        # // 取整除 返回商的整数部分
        self._num = sign * (num // g)
        self._den = den // g
        self.den = den
        Rational.counter += 1
        print("n = %d; m = %d" % (self._num, self._den))

    def num(self):
        return self._num

    def den(self):
        return self._den

    def plus(self, another):
        den = self._den * another._den
        num = (self._num * another._den + self._den * another._num)
        return Rational(num, den)

    def prints(self):
        # print("max n = %d " %(Rational._gcd(self.num,self.den)))

        # Rational._gcd(2,100)
        # Rational._gcd(50,100)
        # Rational._gcd(50,0)

        print(str(self._num) + "/" + str(self._den))

    def __str__(self):
        return str(self._num) + "/" + str(self._den)


# r1 = Rational(3, "asd")
# r1 = Rational(3, 0)
r1 = Rational(3, 6)
r2 = r1.plus(Rational(2, 11))
r2.prints()
print(Rational.get_count())

print(r2)
