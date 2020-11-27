'''
1、Classical mro(python version < 2.2):
        Classical mro use a kind of simple method:DFS from left to right
    Take [diamond inheritance](菱形继承) as an example,The search order is
    [D, B, A, C, A], The result that keep the first item of the duplicate 
    class is [D, B, A, C]. But we use the method of "show()" in C, not A(
    c.show() is a more specific), so this classical mro is not a kind of 
    great method.
'''
import inspect
class A:
    def show(self):
        print "A.show()"
        
class B(A): pass

class C(A):
    def show(self):
        print "C.show()"

class D(B, C): pass

inspect.getmro(D)
'''
  (<class __main__.D at 0x105f0a6d0>, 
   <class __main__.B at 0x105f0a600>, 
   <class __main__.A at 0x105f0a668>, 
   <class __main__.C at 0x105f0a738>)
'''





'''
New-style class mro(Python version = 2.2)
        In order to solve the problem of classical mro, Python 2.2 proposes 
    a new mro calculation method for new-style class.
        New-style class mro is similar to classical mro: It still use DFS left 
    to right, but if it duplicate classes occur, only the last one is retained.
    [D, B, A, C, A] ——> [D, B, C, A]
    
        But if it's a little more complicated example:
            >>> class X(object): pass
            >>> class Y(object): pass
            >>> class A(X, Y): pass
            >>> class B(Y, X): pass
            >>> class C(A, B): pass
        Then, only the last of the repeating elements is kept, and the result is 
    [C, A, B, Y, X, object]. Python 2.2 adjusts the method to respect the sequence 
    of classes in the base class. The actual result is [C, A, B, X, Y, object].
        Is this a reasonable result? First, let's look at the method parsing sequence 
    in each class. For A, the search sequence is [A, X, Y, object]. For B, the search 
    sequence is [B, Y, X, object]. For C, the search order is [C, A, B, X, Y, object]. 
    We'll find that B and C have the opposite search order of X and Y! That is, when B 
    is inherited, its own behavior has changed, which can easily lead to undetectable 
    errors. In addition, even swapping the X and Y in the C search order does not solve 
    the problem, and it will conflict with the A search order.
        In fact, problems may arise not only in these particular cases, but in other cases. 
    The reason is that the inheritance relationship violates the linearized "monotoneity 
    principle"(单调性原则): Subclasses cannot change the method search order of base classes.
        The MRO algorithm of Python 2.2 does not guarantee this monotonicity. It does not 
    prevent the programmer from writing the ambiguous inheritance relationship. Therefore, 
    it may be the root cause of the error. In addition to monotonicity, the MRO of Python 
    2.2 and classic classes may violate the inherited "local precedence"(局部优先级). For details, 
    see the official document. A better MRO approach is imperative.
'''
class A:
    def show(self):
        print "A.show()"
        
class B(A): pass

class C(A):
    def show(self):
        print "C.show()"

class D(B, C): pass

D.__mro__
'''
    (<class '__main__.D'>,
     <class '__main__.B'>,
     <class '__main__.C'>,
     <class '__main__.A'>,
     <type 'object'>,
    )
'''




'''
C3 mro(Python version > 2.2):
        To solve the problem of MRO in Python 2.2, Python 2.3 and later use the C3 algorithm to 
    determine the method parsing sequence. If you enter the preceding code in a version later than 
    Python 2.3, an exception is generated, prohibiting creating ambiguous inheritance relationships.
        If this occurs in the preceding example, an error is reported:
                >>> TypeError: Cannot create a consistent method resolution
                ... order (MRO) for bases X, Y
                
        For details about C3 algorithm parsing, see: https://blog.csdn.net/u011467553/article/details/81437780
'''


