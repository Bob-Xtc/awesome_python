'''
Mix-in作为一种混入类，是python中一种约定俗成的技巧
使用方法类似“装饰器”，我们只是在Mixin类中规定了一些
属性，方便同一种类“们”添加这种属性

例如：
    交通工具有很多种，飞机、汽车和轮船等等，而客机和
直升机同有一种“飞行”的属性，但是其他有可能有不同的属
性，但是其他的交通工具不一定有这种飞行的属性，所以这
时我们不能将这个属性定义到父类（下例中父类为Vehicle）
中，但是fly属性又是很多交通工具共有的属性，如果每个类
中定义这个成员太过繁琐，所以我们定义一个PlaneMixin类
来告诉大家这是一个Mix-in混入类，不违反“is-a”继承规则

使用Mixin类实现多重继承要非常小心
    1、首先它必须表示某一种功能，而不是某个物品，如同Java中的Runnable，Callable等
    2、其次它必须责任单一，如果有多个功能，那就写多个Mixin类
    3、然后，它不依赖于子类的实现
    4、最后，子类即便没有继承这个Mixin类，也照样可以工作，就是缺少了某个功能
'''
class Vehicle:
    pass

class PlaneMixin(object):
    def fly():
	return "I can fly"

class Airplane(Vehicle, PlaneMixin):
    pass
	
	
