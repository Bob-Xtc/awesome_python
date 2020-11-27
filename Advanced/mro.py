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
New-style class mro(python version >= 2.2)
    
'''
