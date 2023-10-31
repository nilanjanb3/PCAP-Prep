class A:
    def print_msg(self):
        print("Hello from A")


class B:
    def print_msg(self):
        print("Hello from B")

class C(B,A):
    pass

c = C()

c.print_msg()
